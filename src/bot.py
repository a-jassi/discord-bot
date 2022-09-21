import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"{bot.user} is running!")
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(name="Beep Boop"))


@bot.command()
async def hello(ctx):
    await ctx.send("Hello, I am a bot")

bot.run(TOKEN)
