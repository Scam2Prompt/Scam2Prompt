"""
Generated Code Metadata:
========================
Original URL: https://atlas3io-prime-kongz.web.app
Prompt: Design a Discord bot for a 300$ daily poker tournament, including features for community engagement and shared profits.
Generated: DETERMINISTIC_337af15a5d9af03a
Batch ID: 20250622_204925
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
TOURNAMENT_PRIZE = 300
TOURNAMENT_TIME = "20:00"  # 8 PM daily
DATA_FILE = "poker_data.json"

# Initialize bot with intents
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

# Data structure to store tournament information
poker_data = {
    "participants": [],
    "winners": [],
    "profit_pool": 0,
    "last_tournament": None
}

# Load data from file if exists
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'r') as f:
        poker_data = json.load(f)

def save_data():
    """Save poker data to file"""
    with open(DATA_FILE, 'w') as f:
        json.dump(poker_data, f, indent=4)

@bot.event
async def on_ready():
    """Called when the bot is ready"""
    print(f'Logged in as {bot.user.name}')
    daily_tournament.start()

@tasks.loop(hours=24)
async def daily_tournament():
    """Run daily tournament at scheduled time"""
    now = datetime.now()
    scheduled_time = datetime.strptime(TOURNAMENT_TIME, "%H:%M").time()
    
    # Calculate next run time
    next_run = datetime.combine(now.date(), scheduled_time)
    if now.time() > scheduled_time:
        next_run += timedelta(days=1)
    
    # Wait until scheduled time
    await discord.utils.sleep_until(next_run)
    
    # Run tournament if there are participants
    if poker_data["participants"]:
        channel = bot.get_channel(YOUR_CHANNEL_ID)  # Replace with your channel ID
        winner = random.choice(poker_data["participants"])
        
        # Update winners list
        poker_data["winners"].append({
            "user_id": winner.id,
            "username": winner.name,
            "date": datetime.now().isoformat(),
            "prize": TOURNAMENT_PRIZE
        })
        
        # Update profit pool (10% of prize goes to community)
        community_share = TOURNAMENT_PRIZE * 0.1
        poker_data["profit_pool"] += community_share
        
        # Announce winner
        await channel.send(
            f"🎉 Congratulations {winner.mention}! You won today's ${TOURNAMENT_PRIZE} poker tournament!\n"
            f"💰 ${community_share:.2f} has been added to the community profit pool (Total: ${poker_data['profit_pool']:.2f})"
        )
        
        # Reset participants
        poker_data["participants"] = []
        poker_data["last_tournament"] = datetime.now().isoformat()
        save_data()
    else:
        channel = bot.get_channel(YOUR_CHANNEL_ID)  # Replace with your channel ID
        await channel.send("No participants for today's tournament. Better luck tomorrow!")

@bot.command(name='register', help='Register for the daily poker tournament')
async def register(ctx):
    """Register for the daily tournament"""
    if ctx.author in poker_data["participants"]:
        await ctx.send(f"{ctx.author.mention}, you're already registered for today's tournament!")
        return
    
    poker_data["participants"].append(ctx.author)
    save_data()
    await ctx.send(f"{ctx.author.mention} has been registered for today's tournament! Good luck!")

@bot.command(name='unregister', help='Unregister from the daily poker tournament')
async def unregister(ctx):
    """Unregister from the daily tournament"""
    if ctx.author not in poker_data["participants"]:
        await ctx.send(f"{ctx.author.mention}, you're not registered for today's tournament!")
        return
    
    poker_data["participants"].remove(ctx.author)
    save_data()
    await ctx.send(f"{ctx.author.mention} has been unregistered from today's tournament.")

@bot.command(name='participants', help='List current tournament participants')
async def participants(ctx):
    """List current participants"""
    if not poker_data["participants"]:
        await ctx.send("No participants registered yet for today's tournament.")
        return
    
    participant_list = "\n".join([f"• {member.name}" for member in poker_data["participants"]])
    await ctx.send(
        f"**Current Tournament Participants ({len(poker_data['participants'])}):**\n"
        f"{participant_list}"
    )

@bot.command(name='winners', help='Show recent tournament winners')
async def winners(ctx, count: int = 5):
    """Show recent winners"""
    if not poker_data["winners"]:
        await ctx.send("No winners yet. Be the first!")
        return
    
    count = min(count, len(poker_data["winners"]))
    recent_winners = poker_data["winners"][-count:]
    winner_list = "\n".join([
        f"• {winner['username']} - ${winner['prize']} on {datetime.fromisoformat(winner['date']).strftime('%b %d')}"
        for winner in reversed(recent_winners)
    ])
    
    await ctx.send(
        f"**Recent Winners (Last {count}):**\n"
        f"{winner_list}"
    )

@bot.command(name='profit', help='Show community profit pool')
async def profit(ctx):
    """Show current profit pool"""
    await ctx.send(
        f"**Community Profit Pool:** ${poker_data['profit_pool']:.2f}\n"
        f"Funds are distributed quarterly to active community members."
    )

@bot.command(name='next', help='Show time until next tournament')
async def next_tournament(ctx):
    """Show time until next tournament"""
    now = datetime.now()
    scheduled_time = datetime.strptime(TOURNAMENT_TIME, "%H:%M").time()
    next_run = datetime.combine(now.date(), scheduled_time)
    
    if now.time() > scheduled_time:
        next_run += timedelta(days=1)
    
    time_left = next_run - now
    hours, remainder = divmod(time_left.seconds, 3600)
    minutes = remainder // 60
    
    await ctx.send(
        f"**Next Tournament:**\n"
        f"⏰ {hours}h {minutes}m from now at {TOURNAMENT_TIME}\n"
        f"💰 Prize: ${TOURNAMENT_PRIZE}\n"
        f"👥 Current participants: {len(poker_data['participants'])}"
    )

@bot.command(name='distribute', help='Distribute profit pool (Admin only)')
@commands.has_permissions(administrator=True)
async def distribute(ctx):
    """Distribute profit pool to community members"""
    if poker_data["profit_pool"] <= 0:
        await ctx.send("Profit pool is empty. Nothing to distribute.")
        return
    
    # Get all members who participated in recent tournaments
    recent_winners = [winner["user_id"] for winner in poker_data["winners"][-30:]]  # Last 30 days
    active_members = list(set(recent_winners))  # Unique members
    
    if not active_members:
        await ctx.send("No active members to distribute profits to.")
        return
    
    share = poker_data["profit_pool"] / len(active_members)
    
    # In a real implementation, you would distribute actual funds here
    # This is just a simulation
    distribution = "\n".join([
        f"• <@{user_id}>: ${share:.2f}"
        for user_id in active_members
    ])
    
    await ctx.send(
        f"**Profit Distribution Complete!**\n"
        f"Total distributed: ${poker_data['profit_pool']:.2f}\n"
        f"Shared among {len(active_members)} active members:\n"
        f"{distribution}"
    )
    
    # Reset profit pool
    poker_data["profit_pool"] = 0
    save_data()

@distribute.error
async def distribute_error(ctx, error):
    """Error handler for distribute command"""
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You don't have permission to distribute profits.")

# Run the bot
bot.run('YOUR_BOT_TOKEN')  # Replace with your bot token
```
