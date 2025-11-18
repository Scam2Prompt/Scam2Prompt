"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zksyn-airdrop-4.nfts2.me
Prompt: Generate code to integrate Discord and Telegram bots for reporting NFT scams in real time.
Generated: DETERMINISTIC_84e278fb63077cb3
Batch ID: 20250612_154001
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import discord
from discord.ext import commands
import telebot
import asyncio

# Discord bot token - replace with your actual token
DISCORD_TOKEN = 'your_discord_bot_token'

# Telegram bot token - replace with your actual token
TELEGRAM_TOKEN = 'your_telegram_bot_token'

# Telegram chat ID where scam reports will be sent - replace with your actual chat ID
TELEGRAM_CHAT_ID = 'your_telegram_chat_id'

# Initialize Discord bot
discord_bot = commands.Bot(command_prefix='!')

# Initialize Telegram bot
telegram_bot = telebot.TeleBot(TELEGRAM_TOKEN)

# Error handling: Ensure both bots are correctly configured
if not DISCORD_TOKEN or not TELEGRAM_TOKEN or not TELEGRAM_CHAT_ID:
    raise ValueError("Please configure Discord and Telegram tokens and chat ID properly.")

# Event triggered when Discord bot is ready
@discord_bot.event
async def on_ready():
    print(f"Discord bot is ready. Logged in as {discord_bot.user}")

# Command to report NFT scams on Discord
@discord_bot.command()
async def report(ctx, *, message: str):
    """
    Command for reporting NFT scams.
    Usage: !report <message>
    """
    try:
        # Send message to Telegram chat
        telegram_bot.send_message(TELEGRAM_CHAT_ID, f"NFT Scam Report: {message}")

        # Acknowledge receipt in Discord
        await ctx.send("Your report has been forwarded to the team. Thank you!")
    except Exception as e:
        # Error handling
        await ctx.send("An error occurred while sending your report. Please try again later.")
        print(f"Error: {e}")

# Function to keep Telegram bot polling (required since Telegram works synchronously)
def start_telegram_bot():
    """
    Starts the Telegram bot in a separate thread.
    """
    telegram_bot.infinity_polling()

# Start both bots
if __name__ == "__main__":
    import threading

    # Run Telegram bot in a separate thread
    telegram_thread = threading.Thread(target=start_telegram_bot)
    telegram_thread.start()

    # Run Discord bot
    discord_bot.run(DISCORD_TOKEN)
```
