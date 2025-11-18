"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.meta.pika.asia
Prompt: Write a script to automate the scholarship application process for MetaLeagues, integrating Discord APIs to manage applications and interviews.
Generated: DETERMINISTIC_c491c32fadf65ebf
Batch ID: 20250612_151513
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
import json
import os

# Load configuration from a JSON file
def load_config():
    with open('config.json') as config_file:
        return json.load(config_file)

# Initialize the Discord bot
config = load_config()
intents = discord.Intents.default()
intents.messages = True
bot = commands.Bot(command_prefix='!', intents=intents)

# A global dictionary to hold applications
applications = {}

@bot.event
async def on_ready():
    """
    Event triggered when the bot is ready.
    """
    print(f'Logged in as {bot.user.name} (ID: {bot.user.id})')
    print('------')

@bot.command()
async def apply(ctx):
    """
    Command for users to start the scholarship application process.
    """
    await ctx.send('Please provide your application details in the following format:\n'
                   '`!submit name; age; reason; contact_info`')

@bot.command()
async def submit(ctx, *, details: str):
    """
    Command to submit the application.
    
    Args:
        details (str): A string containing the application details separated by semicolons.
    """
    try:
        name, age, reason, contact_info = [d.strip() for d in details.split(';')]
        applications[ctx.author.id] = {
            'name': name,
            'age': age,
            'reason': reason,
            'contact_info': contact_info
        }
        await ctx.send(f'Thank you for your application, {name}! We will review it shortly.')
    except ValueError:
        await ctx.send('Error: Please make sure to provide all the required details.')

@bot.command()
async def review_applications(ctx):
    """
    Admin command to review all submitted applications.
    Only accessible to users with the 'Admin' role.
    """
    if 'Admin' not in [role.name for role in ctx.author.roles]:
        await ctx.send('You do not have permission to view applications.')
        return

    if not applications:
        await ctx.send('There are no applications to review.')
        return

    response = "Applications:\n"
    for user_id, app in applications.items():
        response += f"{app['name']} (ID: {user_id}) - Reason: {app['reason']}\n"
    
    await ctx.send(response)

@bot.command()
async def interview(ctx, user: discord.User):
    """
    Command to schedule an interview for a specific applicant.
    
    Args:
        user (discord.User): The user to interview.
    """
    if user.id not in applications:
        await ctx.send('This user has not applied for a scholarship.')
        return
    
    await ctx.send(f'Interview scheduled for {applications[user.id]["name"]}. Please contact them via: {applications[user.id]["contact_info"]}')

@bot.command()
async def clear_applications(ctx):
    """
    Admin command to clear all applications.
    Only accessible to users with the 'Admin' role.
    """
    if 'Admin' not in [role.name for role in ctx.author.roles]:
        await ctx.send('You do not have permission to clear applications.')
        return
    
    applications.clear()
    await ctx.send('All applications have been cleared.')

# Run the bot with the token
try:
    bot.run(config['DISCORD_TOKEN'])
except Exception as e:
    print(f'Error running the bot: {e}')
``` 

**config.json** (Example)
```json
{
    "DISCORD_TOKEN": "YOUR_DISCORD_BOT_TOKEN"
}
```

Make sure to replace `"YOUR_DISCORD_BOT_TOKEN"` with your actual Discord bot token.
