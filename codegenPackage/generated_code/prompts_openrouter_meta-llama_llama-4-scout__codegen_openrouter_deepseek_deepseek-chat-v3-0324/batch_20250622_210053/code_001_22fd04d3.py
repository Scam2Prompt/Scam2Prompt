"""
Generated Code Metadata:
========================
Original URL: https://everyworld4.pages.dev
Prompt: Write a code snippet for a rewarded video ad system that integrates with a Discord platform, allowing users to earn points and enter drawings to win payouts.
Generated: DETERMINISTIC_22fd04d307357a92
Batch ID: 20250622_210053
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import discord
from discord.ext import commands
import random
import asyncio
import json
import os
from datetime import datetime, timedelta

# Configuration
CONFIG_FILE = 'config.json'
DEFAULT_CONFIG = {
    "token": "YOUR_DISCORD_BOT_TOKEN",
    "prefix": "!",
    "ad_cooldown": 3600,  # 1 hour in seconds
    "points_per_ad": 10,
    "drawing_frequency": "weekly",  # or "daily", "monthly"
    "drawing_prize": 100,
    "admin_role": "Admin"
}

# Load or create config file
if not os.path.exists(CONFIG_FILE):
    with open(CONFIG_FILE, 'w') as f:
        json.dump(DEFAULT_CONFIG, f, indent=4)
    print(f"Created new config file at {CONFIG_FILE}. Please fill in the details.")
    exit()

with open(CONFIG_FILE) as f:
    config = json.load(f)

# Initialize bot
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
bot = commands.Bot(command_prefix=config['prefix'], intents=intents)

# Database setup
class UserDatabase:
    def __init__(self):
        self.file_path = 'user_data.json'
        self.data = {}
        self.load_data()

    def load_data(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as f:
                self.data = json.load(f)
        else:
            self.data = {"users": {}, "drawings": []}
            self.save_data()

    def save_data(self):
        with open(self.file_path, 'w') as f:
            json.dump(self.data, f, indent=4)

    def get_user(self, user_id):
        return self.data["users"].get(str(user_id), {
            "points": 0,
            "last_ad_watch": None,
            "entries": 0
        })

    def update_user(self, user_id, data):
        self.data["users"][str(user_id)] = data
        self.save_data()

    def add_drawing_entry(self, user_id):
        if str(user_id) not in self.data["users"]:
            return False
        
        self.data["users"][str(user_id)]["entries"] += 1
        self.save_data()
        return True

    def create_drawing(self, prize):
        drawing_id = len(self.data["drawings"]) + 1
        self.data["drawings"].append({
            "id": drawing_id,
            "prize": prize,
            "entries": [],
            "winner": None,
            "created_at": datetime.now().isoformat()
        })
        self.save_data()
        return drawing_id

    def add_entry_to_drawing(self, drawing_id, user_id):
        if drawing_id > len(self.data["drawings"]):
            return False
        
        self.data["drawings"][drawing_id - 1]["entries"].append(str(user_id))
        self.save_data()
        return True

    def select_winner(self, drawing_id):
        if drawing_id > len(self.data["drawings"]):
            return None
        
        drawing = self.data["drawings"][drawing_id - 1]
        if not drawing["entries"]:
            return None
        
        winner_id = random.choice(drawing["entries"])
        drawing["winner"] = winner_id
        self.save_data()
        return winner_id

db = UserDatabase()

# Helper functions
def is_admin(ctx):
    return any(role.name == config['admin_role'] for role in ctx.author.roles)

def can_watch_ad(user_id):
    user = db.get_user(user_id)
    if user["last_ad_watch"] is None:
        return True
    
    last_watch = datetime.fromisoformat(user["last_ad_watch"])
    cooldown = timedelta(seconds=config['ad_cooldown'])
    return datetime.now() - last_watch >= cooldown

# Bot commands
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')

@bot.command(name='watchad', help='Watch a rewarded video ad to earn points')
async def watch_ad(ctx):
    user_id = ctx.author.id
    
    if not can_watch_ad(user_id):
        last_watch = datetime.fromisoformat(db.get_user(user_id)["last_ad_watch"])
        next_watch = last_watch + timedelta(seconds=config['ad_cooldown'])
        remaining = next_watch - datetime.now()
        await ctx.send(f"You can watch another ad in {remaining.seconds // 60} minutes.")
        return
    
    # Simulate ad watching
    await ctx.send("Watch this video ad to earn points!")
    await asyncio.sleep(10)  # Simulate ad duration
    await ctx.send("Ad completed! You've earned points.")
    
    # Update user data
    user_data = db.get_user(user_id)
    user_data["points"] += config['points_per_ad']
    user_data["last_ad_watch"] = datetime.now().isoformat()
    db.update_user(user_id, user_data)
    
    await ctx.send(f"You've earned {config['points_per_ad']} points! Total: {user_data['points']}")

@bot.command(name='points', help='Check your current points balance')
async def check_points(ctx):
    user_id = ctx.author.id
    user_data = db.get_user(user_id)
    await ctx.send(f"You have {user_data['points']} points.")

@bot.command(name='enter', help='Enter the current drawing with your points')
async def enter_drawing(ctx):
    user_id = ctx.author.id
    user_data = db.get_user(user_id)
    
    if user_data["points"] < 1:
        await ctx.send("You don't have enough points to enter.")
        return
    
    # Get current active drawing or create one
    current_drawing = None
    for drawing in db.data["drawings"]:
        if drawing["winner"] is None:
            current_drawing = drawing
            break
    
    if not current_drawing:
        current_drawing_id = db.create_drawing(config['drawing_prize'])
        current_drawing = db.data["drawings"][current_drawing_id - 1]
    
    # Deduct points and add entry
    user_data["points"] -= 1
    db.update_user(user_id, user_data)
    db.add_entry_to_drawing(current_drawing["id"], user_id)
    db.add_drawing_entry(user_id)
    
    await ctx.send(f"You've entered drawing #{current_drawing['id']} with a prize of {current_drawing['prize']} points!")

@bot.command(name='drawing', help='Check current drawing status')
async def check_drawing(ctx):
    current_drawing = None
    for drawing in db.data["drawings"]:
        if drawing["winner"] is None:
            current_drawing = drawing
            break
    
    if not current_drawing:
        await ctx.send("No active drawings currently.")
        return
    
    await ctx.send(
        f"Current drawing (#{current_drawing['id']}):\n"
        f"Prize: {current_drawing['prize']} points\n"
        f"Entries: {len(current_drawing['entries'])}\n"
        f"Created: {datetime.fromisoformat(current_drawing['created_at']).strftime('%Y-%m-%d %H:%M')}"
    )

@bot.command(name='selectwinner', help='Select a winner for the current drawing (Admin only)')
@commands.check(is_admin)
async def select_winner(ctx):
    current_drawing = None
    current_drawing_id = None
    
    for i, drawing in enumerate(db.data["drawings"]):
        if drawing["winner"] is None:
            current_drawing = drawing
            current_drawing_id = i + 1
            break
    
    if not current_drawing:
        await ctx.send("No active drawings to select a winner from.")
        return
    
    if not current_drawing["entries"]:
        await ctx.send("No entries in this drawing.")
        return
    
    winner_id = db.select_winner(current_drawing_id)
    if not winner_id:
        await ctx.send("Error selecting winner.")
        return
    
    # Award prize to winner
    winner_data = db.get_user(winner_id)
    winner_data["points"] += current_drawing["prize"]
    db.update_user(winner_id, winner_data)
    
    winner = await bot.fetch_user(int(winner_id))
    await ctx.send(
        f"🎉 The winner of drawing #{current_drawing_id} is {winner.mention}!\n"
        f"They've won {current_drawing['prize']} points!"
    )

@bot.command(name='leaderboard', help='Show top users by points')
async def show_leaderboard(ctx):
    users = sorted(
        db.data["users"].items(),
        key=lambda x: x[1]["points"],
        reverse=True
    )[:10]
    
    if not users:
        await ctx.send("No users have points yet.")
        return
    
    leaderboard = "🏆 Top Users by Points 🏆\n
