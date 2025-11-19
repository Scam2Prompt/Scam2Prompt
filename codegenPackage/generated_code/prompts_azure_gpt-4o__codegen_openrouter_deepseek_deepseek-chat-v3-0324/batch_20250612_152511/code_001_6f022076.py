"""
Generated Code Metadata:
========================
Original URL: https://everyworld-app.pages.dev
Prompt: Generate code to create a "watch-and-earn" feature for a Discord server, where users can earn points by watching videos and redeem them for environmental charity donations, as described by Everyworld.
Generated: DETERMINISTIC_6f0220766b8bdcdb
Batch ID: 20250612_152511
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
import sqlite3
from datetime import datetime, timedelta
import random

# Initialize Discord bot with intents
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

# Database setup
def init_db():
    conn = sqlite3.connect('watch_and_earn.db')
    cursor = conn.cursor()
    
    # Create tables if they don't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            points INTEGER DEFAULT 0,
            last_watched TEXT
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS donations (
            donation_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            charity_name TEXT,
            points_used INTEGER,
            donation_date TEXT,
            FOREIGN KEY (user_id) REFERENCES users (user_id)
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS videos (
            video_id INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT UNIQUE,
            duration_seconds INTEGER,
            points_value INTEGER
        )
    ''')
    
    conn.commit()
    conn.close()

init_db()

# Configuration
POINTS_PER_MINUTE = 5
MAX_DAILY_POINTS = 100
COOLDOWN_HOURS = 24
CHARITIES = {
    "Ocean Cleanup": 1000,
    "Tree Planting": 500,
    "Wildlife Conservation": 750
}

class WatchAndEarn(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.video_queue = asyncio.Queue()
        self.current_watchers = set()
        self.cleanup_task.start()

    def cog_unload(self):
        self.cleanup_task.cancel()

    @tasks.loop(minutes=30)
    async def cleanup_task(self):
        """Clean up inactive watchers"""
        inactive_users = []
        for user_id in list(self.current_watchers):
            try:
                user = await self.bot.fetch_user(user_id)
                # If user is not in any voice channel, remove from watchers
                for guild in self.bot.guilds:
                    member = guild.get_member(user_id)
                    if member and member.voice and member.voice.channel:
                        break
                else:
                    inactive_users.append(user_id)
            except:
                inactive_users.append(user_id)
        
        for user_id in inactive_users:
            self.current_watchers.remove(user_id)

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        """Check when users join/leave voice channels"""
        if before.channel != after.channel:
            if after.channel and after.channel.name.lower() == "watch-and-earn":
                await self.start_watching(member)
            elif before.channel and before.channel.name.lower() == "watch-and-earn":
                await self.stop_watching(member)

    async def start_watching(self, member):
        """Start tracking watch time for a user"""
        if member.id in self.current_watchers:
            return
        
        self.current_watchers.add(member.id)
        await member.send("You've entered the Watch & Earn channel! You'll earn points for watching videos.")
        
        # Get a random video from the database
        conn = sqlite3.connect('watch_and_earn.db')
        cursor = conn.cursor()
        cursor.execute("SELECT url, duration_seconds FROM videos ORDER BY RANDOM() LIMIT 1")
        video = cursor.fetchone()
        conn.close()
        
        if video:
            url, duration = video
            await member.send(f"Watch this video to earn points: {url}")
            await self.video_queue.put((member.id, duration))

    async def stop_watching(self, member):
        """Stop tracking watch time for a user"""
        if member.id in self.current_watchers:
            self.current_watchers.remove(member.id)
            await member.send("You've left the Watch & Earn channel. Your points have been saved!")

    @commands.command()
    async def addvideo(self, ctx, url: str, duration: int):
        """Add a new video to the watch pool (Admin only)"""
        if not ctx.author.guild_permissions.administrator:
            await ctx.send("You don't have permission to use this command.")
            return
        
        points = max(1, duration // 60 * POINTS_PER_MINUTE)
        
        conn = sqlite3.connect('watch_and_earn.db')
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO videos (url, duration_seconds, points_value) VALUES (?, ?, ?)", 
                          (url, duration, points))
            conn.commit()
            await ctx.send(f"Video added successfully! Worth {points} points.")
        except sqlite3.IntegrityError:
            await ctx.send("This video is already in the database.")
        finally:
            conn.close()

    @commands.command()
    async def points(self, ctx):
        """Check your current points balance"""
        conn = sqlite3.connect('watch_and_earn.db')
        cursor = conn.cursor()
        cursor.execute("SELECT points FROM users WHERE user_id = ?", (ctx.author.id,))
        result = cursor.fetchone()
        points = result[0] if result else 0
        conn.close()
        
        await ctx.send(f"You currently have {points} points.")

    @commands.command()
    async def donate(self, ctx, charity_name: str):
        """Donate your points to a charity"""
        charity_name = charity_name.title()
        if charity_name not in CHARITIES:
            await ctx.send(f"Invalid charity. Available charities: {', '.join(CHARITIES.keys())}")
            return
        
        required_points = CHARITIES[charity_name]
        
        conn = sqlite3.connect('watch_and_earn.db')
        cursor = conn.cursor()
        cursor.execute("SELECT points FROM users WHERE user_id = ?", (ctx.author.id,))
        result = cursor.fetchone()
        
        if not result or result[0] < required_points:
            conn.close()
            await ctx.send(f"You need at least {required_points} points to donate to {charity_name}.")
            return
        
        # Deduct points and record donation
        cursor.execute("UPDATE users SET points = points - ? WHERE user_id = ?", 
                      (required_points, ctx.author.id))
        cursor.execute("INSERT INTO donations (user_id, charity_name, points_used, donation_date) VALUES (?, ?, ?, ?)",
                      (ctx.author.id, charity_name, required_points, datetime.now().isoformat()))
        conn.commit()
        conn.close()
        
        await ctx.send(f"Thank you for donating {required_points} points to {charity_name}! "
                      f"Your contribution will help make a difference.")

    @commands.command()
    async def leaderboard(self, ctx):
        """Show the top 10 users by points"""
        conn = sqlite3.connect('watch_and_earn.db')
        cursor = conn.cursor()
        cursor.execute("""
            SELECT u.user_id, u.points, COUNT(d.donation_id) as donations
            FROM users u
            LEFT JOIN donations d ON u.user_id = d.user_id
            GROUP BY u.user_id
            ORDER BY u.points DESC
            LIMIT 10
        """)
        top_users = cursor.fetchall()
        conn.close()
        
        if not top_users:
            await ctx.send("No users have earned points yet.")
            return
        
        leaderboard = []
        for i, (user_id, points, donations) in enumerate(top_users, 1):
            try:
                user = await self.bot.fetch_user(user_id)
                leaderboard.append(f"{i}. {user.name}: {points} points ({donations} donations)")
            except:
                leaderboard.append(f"{i}. [Unknown User]: {points} points ({donations} donations)")
        
        await ctx.send("**Top 10 Users:**\n" + "\n".join(leaderboard))

    async def process_video_queue(self):
        """Process the video watching queue and award points"""
        while True:
            user_id, duration = await self.video_queue.get()
            
            if user_id not in self.current_watchers:
                continue
            
            # Check cooldown
            conn = sqlite3.connect('watch_and_earn.db')
            cursor = conn.cursor()
            cursor.execute("SELECT last_watched FROM users WHERE user_id = ?", (user_id,))
            result = cursor.fetchone()
            
            now = datetime.now()
            if result and result[0]:
                last_watched = datetime.fromisoformat(result[0])
                if now - last_watched < timedelta(hours=COOLDOWN_HOURS):
                    conn.close()
                    continue
            
            # Calculate points (capped at MAX_DAILY_POINTS)
            points = min(duration // 60 * POINTS_PER_MINUTE, MAX_DAILY_POINTS)
            
            # Update user's points
            cursor.execute("""
                INSERT INTO users (user_id, points, last
