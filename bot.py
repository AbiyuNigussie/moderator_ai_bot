import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

# Load configuration
load_dotenv()

# Intents
intents = discord.Intents.default()
intents.message_content = True

# Bot instance
bot = commands.Bot(command_prefix=os.getenv("PREFIX"), intents=intents)


# Event: Bot Ready
@bot.event
async def on_ready():
    print(f"Bot logged in as {bot.user} ({bot.user.id})")


# Load extensions/cogs
initial_extensions = ["cogs.general", "cogs.admin"]  # Add cogs here


async def setup_hook():
    for extension in initial_extensions:
        await bot.load_extension(extension)


bot.setup_hook = setup_hook

# Run the bot
bot.run(os.getenv("TOKEN"))
