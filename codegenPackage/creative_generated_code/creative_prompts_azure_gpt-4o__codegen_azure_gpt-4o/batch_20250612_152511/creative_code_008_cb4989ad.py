"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://everyworld-app.pages.dev
Prompt: Create a Discord bot command that allows users to check their Everyworld points balance and view the total points pledged to environmental charities.
Generated: DETERMINISTIC_cb4989ad583fabbe
Batch ID: 20250612_152511
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

# Bot setup
intents = discord.Intents.default()  # Default intents
intents.messages = True  # Enable message-related events
bot = commands.Bot(command_prefix="!", intents=intents)

# Mock database for demonstration purposes
# In production, replace with your actual database or API calls
user_points = {
    "user1#1234": 150,
    "user2#5678": 300,
    "user3#9101": 450
}

total_pledged_points = 2000  # Total points pledged to environmental charities

# Command to check Everyworld points balance
@bot.command(name="points")
async def check_points(ctx):
    """
    Command to allow users to check their Everyworld points balance
    and view the total points pledged to environmental charities.
    """
    try:
        # Retrieve the user's Discord tag
        user_tag = f"{ctx.author.name}#{ctx.author.discriminator}"
        
        # Check if the user exists in the mock database
        if user_tag in user_points:
            user_balance = user_points[user_tag]
            response = (
                f"🌍 **Everyworld Points Balance** 🌍\n"
                f"Hi {ctx.author.mention}, you have **{user_balance} points**.\n\n"
                f"🌱 **Total Points Pledged to Environmental Charities:** {total_pledged_points} points 🌱"
            )
        else:
            response = (
                f"🚨 **Error:** Points balance not found for your account.\n"
                f"Please ensure your account is registered with Everyworld."
            )
        
        # Send the response back to the user
        await ctx.send(response)
    
    except Exception as e:
        # Handle unexpected errors gracefully
        await ctx.send("⚠️ An error occurred while processing your request. Please try again later.")
        print(f"Error: {e}")  # Log the error for debugging purposes

# Event to signal successful bot connection
@bot.event
async def on_ready():
    """
    Event triggered when the bot has successfully connected to Discord.
    """
    print(f"Bot is online! Logged in as {bot.user.name} ({bot.user.id})")

# Run the bot
# Replace 'your-token-here' with your bot's actual token
bot.run('your-token-here')
```
