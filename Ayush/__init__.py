import logging
import time
from motor.motor_asyncio import AsyncIOMotorClient as MongoCli
from pyrogram import Client
from pyrogram.enums import ParseMode

# Configuration module
import config

# Logging configuration
logging.basicConfig(
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)

# Suppress unnecessary Pyrogram logs
logging.getLogger("pyrogram").setLevel(logging.ERROR)
LOGGER = logging.getLogger(__name__)

# Initialize MongoDB connection
try:
    mongo = MongoCli(config.MONGO_URL)
    db = mongo.Anonymous  # Access the specific database
    LOGGER.info("Connected to MongoDB successfully.")
except Exception as e:
    LOGGER.error(f"Failed to connect to MongoDB: {e}")
    db = None  # Fallback in case of connection failure

OWNER = config.OWNER_ID
boot = time.time()

# Define the custom bot class
class AyushBot(Client):
    def __init__(self):
        super().__init__(
            name="Ayush",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
            lang_code="en",
            in_memory=True,
            parse_mode=ParseMode.DEFAULT,
        )

    async def start(self):
        # Call parent class's start method
        await super().start()
        # Fetch bot details
        self.id = self.me.id
        self.name = self.me.first_name + " " + (self.me.last_name or "")
        self.username = self.me.username
        self.mention = self.me.mention
        LOGGER.info(f"Bot started as {self.name} (@{self.username})")

    async def stop(self):
        # Call parent class's stop method
        await super().stop()
        LOGGER.info("Bot stopped gracefully.")

# Instantiate the bot
Ayush = AyushBot()
