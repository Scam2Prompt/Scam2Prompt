"""
Generated Code Metadata:
========================
Original URL: https://everyworld.pages.dev
Prompt: Create a bot in Python that tracks and logs digital engagement activities on Discord for earning points in the Everyworld ecosystem.
Generated: DETERMINISTIC_2dace8e678575612
Batch ID: 20250612_152739
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
import logging
from datetime import datetime
import json
import os
from typing import Dict, Optional, List

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('everyworld_bot.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Constants
CONFIG_FILE = 'config.json'
DATA_FILE = 'user_data.json'
DEFAULT_CONFIG = {
    "token": "YOUR_DISCORD_BOT_TOKEN",
    "prefix": "!",
    "admin_roles": ["Admin"],
    "point_values": {
        "message": 1,
        "reaction": 0.5,
        "voice": 2,
        "daily_bonus": 5
    }
}

class EveryworldBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config = self.load_config()
        self.user_data = self.load_user_data()
        self.last_daily_bonus = {}

    def load_config(self) -> Dict:
        """Load or create configuration file."""
        if not os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE, 'w') as f:
                json.dump(DEFAULT_CONFIG, f, indent=4)
            logger.info(f"Created new config file: {CONFIG_FILE}")
            return DEFAULT_CONFIG
        
        try:
            with open(CONFIG_FILE, 'r') as f:
                return json.load(f)
        except Exception as e:
            logger.error(f"Error loading config: {e}")
            return DEFAULT_CONFIG

    def load_user_data(self) -> Dict:
        """Load or create user data file."""
        if not os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'w') as f:
                json.dump({}, f, indent=4)
            logger.info(f"Created new user data file: {DATA_FILE}")
            return {}
        
        try:
            with open(DATA_FILE, 'r') as f:
                return json.load(f)
        except Exception as e:
            logger.error(f"Error loading user data: {e}")
            return {}

    def save_user_data(self):
        """Save user data to file."""
        try:
            with open(DATA_FILE, 'w') as f:
                json.dump(self.user_data, f, indent=4)
        except Exception as e:
            logger.error(f"Error saving user data: {e}")

    async def update_points(self, user_id: str, activity_type: str) -> Optional[float]:
        """Update user points for an activity."""
        if activity_type not in self.config["point_values"]:
            logger.warning(f"Invalid activity type: {activity_type}")
            return None
        
        points = self.config["point_values"][activity_type]
        user_id = str(user_id)
        
        if user_id not in self.user_data:
            self.user_data[user_id] = {
                "total_points": 0.0,
                "activities": {}
            }
        
        if activity_type not in self.user_data[user_id]["activities"]:
            self.user_data[user_id]["activities"][activity_type] = 0
        
        self.user_data[user_id]["activities"][activity_type] += 1
        self.user_data[user_id]["total_points"] += points
        
        self.save_user_data()
        return points

    async def check_daily_bonus(self, user_id: str) -> bool:
        """Check if user is eligible for daily bonus."""
        user_id = str(user_id)
        today = datetime.now().date().isoformat()
        
        if user_id not in self.last_daily_bonus or self.last_daily_bonus[user_id] != today:
            self.last_daily_bonus[user_id] = today
            return True
        return False

    async def on_ready(self):
        """Called when the bot is ready."""
        logger.info(f'Logged in as {self.user.name} (ID: {self.user.id})')
        logger.info('------')
        self.cleanup_old_data.start()

    @tasks.loop(hours=24)
    async def cleanup_old_data(self):
        """Clean up old data periodically."""
        logger.info("Running daily data cleanup...")
        # Implement any necessary cleanup logic here
        self.save_user_data()

    async def on_message(self, message):
        """Handle message events."""
        if message.author.bot:
            return
        
        points = await self.update_points(message.author.id, "message")
        if points:
            logger.info(f"User {message.author} earned {points} points for sending a message")
        
        await self.process_commands(message)

    async def on_reaction_add(self, reaction, user):
        """Handle reaction events."""
        if user.bot:
            return
        
        points = await self.update_points(user.id, "reaction")
        if points:
            logger.info(f"User {user} earned {points} points for adding a reaction")

    async def on_voice_state_update(self, member, before, after):
        """Handle voice channel events."""
        if member.bot:
            return
        
        # User joined a voice channel
        if before.channel is None and after.channel is not None:
            points = await self.update_points(member.id, "voice")
            if points:
                logger.info(f"User {member} earned {points} points for joining voice")

    @commands.command(name="points")
    async def check_points(self, ctx):
        """Check your current points."""
        user_id = str(ctx.author.id)
        if user_id in self.user_data:
            points = self.user_data[user_id]["total_points"]
            await ctx.send(f"{ctx.author.mention}, you have {points} points!")
        else:
            await ctx.send(f"{ctx.author.mention}, you don't have any points yet.")

    @commands.command(name="daily")
    async def claim_daily_bonus(self, ctx):
        """Claim daily bonus points."""
        user_id = str(ctx.author.id)
        
        if await self.check_daily_bonus(user_id):
            points = await self.update_points(user_id, "daily_bonus")
            await ctx.send(f"{ctx.author.mention}, you claimed your daily bonus of {points} points!")
        else:
            await ctx.send(f"{ctx.author.mention}, you've already claimed your daily bonus today.")

    @commands.command(name="leaderboard")
    @commands.has_any_role(*DEFAULT_CONFIG["admin_roles"])
    async def show_leaderboard(self, ctx, limit: int = 10):
        """Show the top users by points (admin only)."""
        sorted_users = sorted(
            self.user_data.items(),
            key=lambda x: x[1]["total_points"],
            reverse=True
        )[:limit]
        
        if not sorted_users:
            await ctx.send("No user data available.")
            return
        
        leaderboard = []
        for rank, (user_id, data) in enumerate(sorted_users, 1):
            try:
                user = await self.fetch_user(int(user_id))
                name = user.name
            except:
                name = f"Unknown User ({user_id})"
            leaderboard.append(f"{rank}. {name}: {data['total_points']} points")
        
        await ctx.send("**Leaderboard:**\n" + "\n".join(leaderboard))

    @commands.command(name="reset_data")
    @commands.has_any_role(*DEFAULT_CONFIG["admin_roles"])
    async def reset_user_data(self, ctx):
        """Reset all user data (admin only)."""
        self.user_data = {}
        self.save_user_data()
        await ctx.send("All user data has been reset.")

def main():
    intents = discord.Intents.default()
    intents.messages = True
    intents.reactions = True
    intents.voice_states = True
    intents.message_content = True
    
    bot = EveryworldBot(
        command_prefix=DEFAULT_CONFIG["prefix"],
        intents=intents
    )
    
    try:
        bot.run(bot.config["token"])
    except Exception as e:
        logger.error(f"Bot crashed: {e}")
        raise

if __name__ == "__main__":
    main()
```
