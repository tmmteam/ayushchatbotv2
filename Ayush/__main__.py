import asyncio
import importlib

from pyrogram import idle

from Ayush import LOGGER, Ayush
from Ayush.modules import ALL_MODULES


async def anony_boot():
    try:
        await Ayush.start()
    except Exception as ex:
        LOGGER.error(ex)
        quit(1)

    for all_module in ALL_MODULES:
        importlib.import_module("Ayush.modules." + all_module)

    LOGGER.info(f"@{Ayush.username} Started.")
    await idle()


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(anony_boot())
    LOGGER.info("Stopping Ayush Bot...")
