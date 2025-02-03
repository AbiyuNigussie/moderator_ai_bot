import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

# Load configuration from .env file
load_dotenv()

# Intents
intents = discord.Intents.default()
intents.message_content = True  # Required for reading message content

# Bot instance
bot = commands.Bot(command_prefix=os.getenv("PREFIX"), intents=intents)


# Event: Bot Ready
@bot.event
async def on_ready():
    print(f"Bot logged in as {bot.user} ({bot.user.id})")
    # Load extensions after bot is ready
    await load_extensions()


# Load extensions/cogs
initial_extensions = ["cogs.general", "cogs.admin", "cogs.moderation"]  # Add cogs here


async def load_extensions():
    print("Loading extensions...")
    for extension in initial_extensions:
        try:
            await bot.load_extension(extension)
            print(f"Loaded extension {extension}")
        except Exception as e:
            print(f"Failed to load extension {extension}: {e}")


# Run the bot
bot.run(os.getenv("TOKEN"))
