import os
import discord
import logging
from discord.ext import commands
import asyncio
import asyncpg

async def run():
    description = (
        "A bot written in Python that uses asyncpg to connect to a postgreSQL database.",
    )

    # NOTE: 127.0.0.1 is the loopback address. If your db is running on the same machine as the code,
    # this address will work
    db = await asyncpg.create_pool(os.environ.get("DATABASE_URL"))

    # Example create table code, you'll probably change it to suit you
    await db.execute("CREATE TABLE IF NOT EXISTS users(id bigint PRIMARY KEY, data text);")

    bot = Bot(description=description, db=db, logging=logging)
    try:
        await bot.start(os.environ.get("DISCORD_TOKEN"))
    except KeyboardInterrupt:
        await db.close()
        await bot.logout()

class Bot(commands.Bot):
    def __init__(self, **kwargs):
        super().__init__(
            description=kwargs.pop("description"),
            command_prefix="?"
        )

        self.db = kwargs.pop("db")

    async def on_ready(self):
        # .format() is for the lazy people who aren't on 3.6+
        print("Username: {0}\nID: {0.id}".format(self.user))

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('!hello'):
            await message.reply('Hello!', mention_author=True)

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))

loop = asyncio.get_event_loop()
loop.run_until_complete(run())
