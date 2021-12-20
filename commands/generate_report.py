import csv
import io

import hikari
from hikari import Permissions

from models import Record, session_scope


async def generate_report(event: hikari.GuildMessageCreateEvent, command, config, *args):
    guild: hikari.GatewayGuild = event.get_guild()
    u: hikari.User = await event.message.author.fetch_self()
    for member in guild.get_members().values():
        if member.id == u.id:
            if not any(role.permissions.any(Permissions.ADMINISTRATOR) for role in member.get_roles()):
                await event.message.respond("Not an admin")
                return
    with session_scope() as s:
        results = s.query(Record).all()
        with io.StringIO() as f:
            writer = csv.DictWriter(f, fieldnames=[
                'id', 'username', 'command', 'message', 'created_at'
            ])
            writer.writeheader()
            for r in results:
                writer.writerow(r.to_dict())
            f.seek(0)
            await event.message.author.send(
                content='Report',
                attachment=f
            )
