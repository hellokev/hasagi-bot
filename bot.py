import discord
from discord.ext import commands
import os 
from dotenv import load_dotenv

load_dotenv()

SECRET_TOKEN = os.getenv("TOKEN")

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='~', intents=intents)

@bot.command(name='test')
async def _test(ctx, arg):
    pass

client = MyClient(intents=intents)
client.run(SECRET_TOKEN)

def run_discord_bot():
    print(SECRET_TOKEN)
run_discord_bot()