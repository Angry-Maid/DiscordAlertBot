from typing import List

import hikari


async def alert(event: hikari.GuildMessageCreateEvent, command: str, config, *args) -> None:
    guild: hikari.GatewayGuild = event.get_guild()
    roles: List[hikari.Role] = guild.get_roles().values()
    for role in roles:
        if role.mention == args[0] and role.name not in config['excluded_roles']:
            for member in guild.get_members().values():
                if role in member.get_roles():
                    await member.user.send(' '.join(args[1:]))
