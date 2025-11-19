"""
Generated Code Metadata:
========================
Original URL: https://momoguro.vercel.app
Prompt: Write code for a Discord bot that automates whitelist giveaways, ensuring it tracks daily entries and limits them to three winners per day, as described in the Momoguro WL Giveaway process.
Generated: DETERMINISTIC_9ff0f326857bb673
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import discord
from discord.ext import commands, tasks
import asyncio
import random
from datetime import datetime, timedelta
import json
import os

# Constants
CONFIG_FILE = 'config.json'
ENTRIES_FILE = 'entries.json'
WINNERS_FILE = 'winners.json'
DAILY_ENTRY_LIMIT = 1
DAILY_WINNER_LIMIT = 3

# Load or initialize config
def load_config():
    if not os.path.exists(CONFIG_FILE):
        default_config = {
            "bot_token": "YOUR_BOT_TOKEN_HERE",
            "giveaway_channel_id": None,
            "admin_role_id": None,
            "giveaway_duration_hours": 24,
            "entry_emoji": "🎉"
        }
        with open(CONFIG_FILE, 'w') as f:
            json.dump(default_config, f, indent=4)
        return default_config
    with open(CONFIG_FILE) as f:
        return json.load(f)

# Load or initialize entries
def load_entries():
    if not os.path.exists(ENTRIES_FILE):
        return {}
    with open(ENTRIES_FILE) as f:
        return json.load(f)

# Load or initialize winners
def load_winners():
    if not os.path.exists(WINNERS_FILE):
        return {}
    with open(WINNERS_FILE) as f:
        return json.load(f)

# Save entries to file
def save_entries(entries):
    with open(ENTRIES_FILE, 'w') as f:
        json.dump(entries, f, indent=4)

# Save winners to file
def save_winners(winners):
    with open(WINNERS_FILE, 'w') as f:
        json.dump(winners, f, indent=4)

# Bot setup
config = load_config()
intents = discord.Intents.default()
intents.messages = True
intents.reactions = True
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

# Helper functions
def get_today_date():
    return datetime.now().strftime('%Y-%m-%d')

def is_admin(member):
    return config['admin_role_id'] and any(role.id == config['admin_role_id'] for role in member.roles)

# Bot events
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    daily_giveaway.start()

@bot.event
async def on_reaction_add(reaction, user):
    if user.bot:
        return
    
    if reaction.message.channel.id != config['giveaway_channel_id']:
        return
    
    if str(reaction.emoji) != config['entry_emoji']:
        return
    
    today = get_today_date()
    entries = load_entries()
    
    if today not in entries:
        entries[today] = []
    
    if user.id in entries[today]:
        return
    
    entries[today].append(user.id)
    save_entries(entries)

# Tasks
@tasks.loop(hours=config['giveaway_duration_hours'])
async def daily_giveaway():
    await bot.wait_until_ready()
    
    today = get_today_date()
    entries = load_entries()
    winners = load_winners()
    
    if today not in entries or len(entries[today]) == 0:
        print(f"No entries for {today}")
        return
    
    if today in winners and len(winners[today]) >= DAILY_WINNER_LIMIT:
        print(f"Already selected {DAILY_WINNER_LIMIT} winners for {today}")
        return
    
    if today not in winners:
        winners[today] = []
    
    available_entries = [user_id for user_id in entries[today] if user_id not in winners[today]]
    
    if not available_entries:
        print(f"No available entries left for {today}")
        return
    
    new_winners = random.sample(available_entries, min(DAILY_WINNER_LIMIT - len(winners[today]), len(available_entries)))
    winners[today].extend(new_winners)
    save_winners(winners)
    
    channel = bot.get_channel(config['giveaway_channel_id'])
    if channel:
        winners_mentions = [f"<@{winner_id}>" for winner_id in new_winners]
        await channel.send(
            f"🎉 **Daily Whitelist Giveaway Winners ({today})** 🎉\n"
            f"Congratulations to: {', '.join(winners_mentions)}!\n"
            f"You've been whitelisted for today!"
        )

# Commands
@bot.command()
@commands.has_permissions(administrator=True)
async def start_giveaway(ctx, duration_hours: int = None):
    if not is_admin(ctx.author):
        await ctx.send("You don't have permission to use this command.")
        return
    
    if duration_hours:
        config['giveaway_duration_hours'] = duration_hours
        with open(CONFIG_FILE, 'w') as f:
            json.dump(config, f, indent=4)
    
    await ctx.send(
        f"🎉 **Whitelist Giveaway Started!** 🎉\n"
        f"React with {config['entry_emoji']} to enter!\n"
        f"Daily winners will be announced every {config['giveaway_duration_hours']} hours."
    )

@bot.command()
@commands.has_permissions(administrator=True)
async def set_channel(ctx, channel: discord.TextChannel):
    if not is_admin(ctx.author):
        await ctx.send("You don't have permission to use this command.")
        return
    
    config['giveaway_channel_id'] = channel.id
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f, indent=4)
    await ctx.send(f"Giveaway channel set to {channel.mention}")

@bot.command()
@commands.has_permissions(administrator=True)
async def set_admin_role(ctx, role: discord.Role):
    if not is_admin(ctx.author):
        await ctx.send("You don't have permission to use this command.")
        return
    
    config['admin_role_id'] = role.id
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f, indent=4)
    await ctx.send(f"Admin role set to {role.name}")

@bot.command()
@commands.has_permissions(administrator=True)
async def set_emoji(ctx, emoji: str):
    if not is_admin(ctx.author):
        await ctx.send("You don't have permission to use this command.")
        return
    
    config['entry_emoji'] = emoji
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f, indent=4)
    await ctx.send(f"Entry emoji set to {emoji}")

@bot.command()
@commands.has_permissions(administrator=True)
async def force_draw(ctx):
    if not is_admin(ctx.author):
        await ctx.send("You don't have permission to use this command.")
        return
    
    await daily_giveaway()
    await ctx.send("Forced a new giveaway draw.")

@bot.command()
async def my_entries(ctx):
    entries = load_entries()
    today = get_today_date()
    
    if today in entries and ctx.author.id in entries[today]:
        await ctx.send(f"You have entered today's giveaway!")
    else:
        await ctx.send("You haven't entered today's giveaway yet.")

@bot.command()
@commands.has_permissions(administrator=True)
async def show_winners(ctx, date: str = None):
    if not is_admin(ctx.author):
        await ctx.send("You don't have permission to use this command.")
        return
    
    winners = load_winners()
    date = date or get_today_date()
    
    if date not in winners or not winners[date]:
        await ctx.send(f"No winners recorded for {date}")
        return
    
    winners_mentions = [f"<@{winner_id}>" for winner_id in winners[date]]
    await ctx.send(
        f"🎉 **Winners for {date}** 🎉\n"
        f"{', '.join(winners_mentions)}"
    )

# Run the bot
if __name__ == '__main__':
    bot.run(config['bot_token'])
```
