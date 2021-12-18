import json

import hikari


async def debug(event: hikari.GuildMessageCreateEvent, command: str, config, *args) -> None:
    await event.message.respond(json.dumps({
        "command": command,
        "args": args,
        "user": event.message.author.username,
    }))
