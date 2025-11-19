"""
Generated Code Metadata:
========================
Original URL: https://everyworld-token.pages.dev
Prompt: Create a code snippet that tracks user activity and rewards points for engagement in a Discord-based game, similar to the Everyworld platform's mechanics.
Generated: DETERMINISTIC_59e68d9992116cef
Batch ID: 20250612_161616
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
from datetime import datetime, timedelta
import json
import os
from typing import Dict, Optional

# Constants
POINTS_CONFIG = {
    "message": 1,          # Points per message
    "reaction": 0.5,       # Points per reaction
    "voice_minute": 2,     # Points per minute in voice
    "daily_cap": 100,      # Max points per day
    "streak_bonus": 0.1    # 10% bonus for consecutive days
}

DATA_FILE = "user_data.json"

class ActivityTracker(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.user_data: Dict[int, Dict] = {}
        self.load_data()
        self.daily_reset.start()

    def load_data(self):
        """Load user data from JSON file."""
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'r') as f:
                data = json.load(f)
                # Convert keys back to integers (JSON stores keys as strings)
                self.user_data = {int(k): v for k, v in data.items()}

    def save_data(self):
        """Save user data to JSON file."""
        with open(DATA_FILE, 'w') as f:
            json.dump(self.user_data, f, indent=4)

    def get_user_data(self, user_id: int) -> Dict:
        """Get or create user data entry."""
        if user_id not in self.user_data:
            self.user_data[user_id] = {
                "total_points": 0,
                "daily_points": 0,
                "last_active": None,
                "streak_days": 0,
                "voice_time": 0  # in minutes
            }
        return self.user_data[user_id]

    def update_streak(self, user_data: Dict):
        """Update user streak based on last activity."""
        now = datetime.utcnow().date()
        last_active = datetime.strptime(user_data["last_active"], "%Y-%m-%d").date() if user_data["last_active"] else None
        
        if last_active:
            if now == last_active + timedelta(days=1):
                user_data["streak_days"] += 1
            elif now > last_active + timedelta(days=1):
                user_data["streak_days"] = 0
        
        user_data["last_active"] = now.strftime("%Y-%m-%d")

    def add_points(self, user_id: int, points_type: str, amount: float = 1):
        """Add points to user with type validation and daily cap."""
        if points_type not in POINTS_CONFIG:
            raise ValueError(f"Invalid points type: {points_type}")
        
        user_data = self.get_user_data(user_id)
        self.update_streak(user_data)
        
        # Calculate base points
        base_points = POINTS_CONFIG[points_type] * amount
        
        # Apply streak bonus
        streak_bonus = base_points * (POINTS_CONFIG["streak_bonus"] * user_data["streak_days"])
        total_points = base_points + streak_bonus
        
        # Apply daily cap
        remaining_daily = max(0, POINTS_CONFIG["daily_cap"] - user_data["daily_points"])
        actual_points = min(total_points, remaining_daily)
        
        if actual_points > 0:
            user_data["daily_points"] += actual_points
            user_data["total_points"] += actual_points
            
            if points_type == "voice_minute":
                user_data["voice_time"] += amount
            
            self.save_data()
        
        return actual_points

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        """Track message activity."""
        if message.author.bot:
            return
        
        points = self.add_points(message.author.id, "message")
        if points > 0:
            # Optional: Send feedback to user
            pass

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction: discord.Reaction, user: discord.User):
        """Track reaction activity."""
        if user.bot:
            return
        
        points = self.add_points(user.id, "reaction")
        if points > 0:
            # Optional: Send feedback to user
            pass

    @commands.Cog.listener()
    async def on_voice_state_update(self, member: discord.Member, before: discord.VoiceState, after: discord.VoiceState):
        """Track voice channel activity."""
        if member.bot:
            return
        
        # User joined a voice channel
        if before.channel is None and after.channel is not None:
            self.get_user_data(member.id)["voice_join_time"] = datetime.utcnow()
        
        # User left a voice channel
        elif before.channel is not None and after.channel is None:
            user_data = self.get_user_data(member.id)
            if "voice_join_time" in user_data:
                join_time = user_data["voice_join_time"]
                duration = (datetime.utcnow() - join_time).total_seconds() / 60  # in minutes
                points = self.add_points(member.id, "voice_minute", duration)
                if points > 0:
                    # Optional: Send feedback to user
                    pass
                del user_data["voice_join_time"]

    @tasks.loop(hours=24)
    async def daily_reset(self):
        """Reset daily points for all users."""
        for user_id in self.user_data:
            self.user_data[user_id]["daily_points"] = 0
        self.save_data()

    @daily_reset.before_loop
    async def before_daily_reset(self):
        """Wait until midnight UTC before starting the daily reset loop."""
        await self.bot.wait_until_ready()
        now = datetime.utcnow()
        next_reset = now.replace(hour=0, minute=0, second=0, microsecond=0) + timedelta(days=1)
        await discord.utils.sleep_until(next_reset)

    @commands.command(name="points")
    async def check_points(self, ctx: commands.Context, user: Optional[discord.User] = None):
        """Check a user's points and streak."""
        target_user = user or ctx.author
        user_data = self.get_user_data(target_user.id)
        
        embed = discord.Embed(
            title=f"{target_user.display_name}'s Activity",
            color=discord.Color.green()
        )
        embed.add_field(name="Total Points", value=f"{user_data['total_points']:,}")
        embed.add_field(name="Today's Points", value=f"{user_data['daily_points']:,}/{POINTS_CONFIG['daily_cap']}")
        embed.add_field(name="Current Streak", value=f"{user_data['streak_days']} days")
        embed.add_field(name="Voice Time", value=f"{user_data['voice_time']} minutes")
        
        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(ActivityTracker(bot))
```
