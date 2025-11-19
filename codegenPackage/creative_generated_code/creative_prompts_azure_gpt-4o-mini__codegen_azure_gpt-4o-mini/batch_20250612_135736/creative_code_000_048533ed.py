"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blur.gay
Prompt: Generate a Python bot that integrates with GitHub and streams updates to a Discord channel, referencing the coding projects mentioned on https://blur.gay.
Generated: DETERMINISTIC_048533ed7377a491
Batch ID: 20250612_135736
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import discord
from discord.ext import commands
from github import Github, BadCredentialsException, UnknownObjectException
import asyncio
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

# Environment variables for GitHub and Discord tokens
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
GITHUB_REPOS = os.getenv('GITHUB_REPOS', '').split(',')

# Initialize Discord bot
intents = discord.Intents.default()
intents.messages = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Initialize GitHub client
try:
    g = Github(GITHUB_TOKEN)
except BadCredentialsException:
    logging.error("Invalid GitHub token.")
    raise

# Define the channel ID where updates will be sent
DISCORD_CHANNEL_ID = int(os.getenv('DISCORD_CHANNEL_ID'))

async def fetch_updates(repo_name):
    """
    Fetches the latest commits from the specified GitHub repository.
    :param repo_name: The name of the GitHub repository.
    :return: A list of commit messages.
    """
    try:
        repo = g.get_repo(repo_name)
        commits = repo.get_commits()
        return [commit.commit.message for commit in commits[:5]]  # Get latest 5 commits
    except UnknownObjectException:
        logging.error(f"Repository {repo_name} not found.")
        return []

async def send_updates_to_discord(updates):
    """
    Sends updates to the Discord channel.
    :param updates: A list of updates to send.
    """
    channel = bot.get_channel(DISCORD_CHANNEL_ID)
    if channel is not None:
        for update in updates:
            await channel.send(update)
    else:
        logging.error(f"Channel with ID {DISCORD_CHANNEL_ID} not found.")

async def update_loop():
    """
    Periodically checks for updates in the specified GitHub repositories
    and sends them to the Discord channel.
    """
    await bot.wait_until_ready()
    while not bot.is_closed():
        for repo_name in GITHUB_REPOS:
            logging.info(f"Checking for updates in {repo_name}...")
            updates = await fetch_updates(repo_name.strip())
            if updates:
                await send_updates_to_discord(updates)
        await asyncio.sleep(300)  # Wait for 5 minutes before checking again

@bot.event
async def on_ready():
    """
    Event to signal that the bot is ready.
    """
    logging.info(f'Bot is ready. Logged in as {bot.user.name}')
    bot.loop.create_task(update_loop())

# Run the bot
bot.run(DISCORD_TOKEN)
```

Make sure to set the following environment variables before running the code:
- `GITHUB_TOKEN`: Your GitHub personal access token.
- `DISCORD_TOKEN`: Your Discord bot token.
- `DISCORD_CHANNEL_ID`: The ID of the Discord channel to send updates to.
- `GITHUB_REPOS`: A comma-separated list of GitHub repositories to track (e.g., "owner/repo1,owner/repo2").
