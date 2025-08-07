import discord
from discord.ext import commands
from config import DISCORD_BOT_TOKEN
from memory import init_db
from handlers.ask_handler import handle_ask
from handlers.status_handler import handle_status
from handlers.close_handler import handle_close

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

init_db()

@bot.event
async def on_ready():
    print(f"🟢 Logged in as {bot.user}")

@bot.command()
async def ask(ctx, *, query):
    await handle_ask(ctx, query, bot)

@bot.command()
async def status(ctx):
    await handle_status(ctx)

@bot.command()
async def close(ctx):
    await handle_close(ctx)

bot.run(DISCORD_BOT_TOKEN)
