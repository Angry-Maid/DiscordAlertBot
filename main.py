from importlib import import_module

import hikari
import yaml


with open('config.yaml') as cfile:
    config = yaml.load(cfile, Loader=yaml.CLoader)

commands = {}

for command in config['commands']:
    commands[command] = getattr(import_module(f'.{command}', package='commands'), command)

bot = hikari.GatewayBot(
    token=config['BOT_TOKEN'],
    intents=hikari.Intents.ALL
)


@bot.listen()
async def ping(event: hikari.GuildMessageCreateEvent) -> None:
    if event.is_bot or not event.content:
        return
    
    if event.content.startswith(config['prefix']):
        command, *args = event.content.strip(config['prefix']).split(" ")
        if command in commands:
            await commands[command](event, command, config, *args)
        if command == "ping":
            await event.message.respond("pong")


if __name__ == "__main__":
    bot.run()
