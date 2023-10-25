import discord
import os 
from dotenv import load_dotenv

load_dotenv()

SECRET_TOKEN = os.getenv("TOKEN")

def run_discord_bot():
    print(SECRET_TOKEN)
run_discord_bot()