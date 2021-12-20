from importlib import import_module

import hikari
import yaml

from models import Record, session_scope


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
            with session_scope() as s:
                record = Record(
                    username=event.message.author.username,
                    command=command,
                    message=' '.join(args)
                )
                s.add(record)
                s.commit()
            await commands[command](event, command, config, *args)


if __name__ == "__main__":
    bot.run()
