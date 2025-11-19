"""
Generated Code Metadata:
========================
Original URL: https://puffmypanda.pages.dev
Prompt: Design a Discord bot to facilitate community engagement and QuestBoard activities for Puff Puff Pandas holders, using APIs such as Discord.py.
Generated: DETERMINISTIC_f95e4eba94aaf902
Batch ID: 20250622_205836
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
import os
from dotenv import load_dotenv
import asyncio
import logging
import random
import json
from typing import Optional

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Bot configuration
class Config:
    def __init__(self):
        self.token = os.getenv('DISCORD_TOKEN')
        self.prefix = os.getenv('COMMAND_PREFIX', '!')
        self.quest_channel_id = int(os.getenv('QUEST_CHANNEL_ID', 0))
        self.admin_role_id = int(os.getenv('ADMIN_ROLE_ID', 0))
        self.panda_role_id = int(os.getenv('PANDA_ROLE_ID', 0))
        self.quest_file = os.getenv('QUEST_FILE', 'quests.json')

# Initialize bot
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

config = Config()
bot = commands.Bot(command_prefix=config.prefix, intents=intents)

# Load or initialize quest data
def load_quests():
    try:
        with open(config.quest_file, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {"active_quests": [], "completed_quests": []}

def save_quests(quests):
    with open(config.quest_file, 'w') as f:
        json.dump(quests, f, indent=2)

# Helper functions
def is_admin(ctx):
    return any(role.id == config.admin_role_id for role in ctx.author.roles)

def is_panda_holder(ctx):
    return any(role.id == config.panda_role_id for role in ctx.author.roles)

# Bot events
@bot.event
async def on_ready():
    logger.info(f'Logged in as {bot.user.name} (ID: {bot.user.id})')
    logger.info('------')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Command not found. Use !help to see available commands.")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Missing required argument. Please check the command usage.")
    elif isinstance(error, commands.CheckFailure):
        await ctx.send("You don't have permission to use this command.")
    else:
        logger.error(f"Error in command {ctx.command}: {error}")
        await ctx.send("An error occurred while processing your command.")

# Quest commands
@bot.command(name='createquest', help='Create a new quest (Admin only)')
@commands.check(is_admin)
async def create_quest(ctx, title: str, description: str, reward: str):
    quests = load_quests()
    new_quest = {
        "id": len(quests["active_quests"]) + 1,
        "title": title,
        "description": description,
        "reward": reward,
        "creator": ctx.author.id,
        "participants": []
    }
    
    quests["active_quests"].append(new_quest)
    save_quests(quests)
    
    embed = discord.Embed(
        title=f"New Quest: {title}",
        description=description,
        color=discord.Color.green()
    )
    embed.add_field(name="Reward", value=reward)
    embed.set_footer(text=f"Quest ID: {new_quest['id']}")
    
    channel = bot.get_channel(config.quest_channel_id)
    await channel.send(embed=embed)
    await ctx.send(f"Quest created successfully! ID: {new_quest['id']}")

@bot.command(name='joinquest', help='Join an active quest')
@commands.check(is_panda_holder)
async def join_quest(ctx, quest_id: int):
    quests = load_quests()
    quest = next((q for q in quests["active_quests"] if q["id"] == quest_id), None)
    
    if not quest:
        await ctx.send("Quest not found.")
        return
    
    if ctx.author.id in quest["participants"]:
        await ctx.send("You've already joined this quest!")
        return
    
    quest["participants"].append(ctx.author.id)
    save_quests(quests)
    
    await ctx.send(f"You've successfully joined quest: {quest['title']}")

@bot.command(name='completequest', help='Mark a quest as completed (Admin only)')
@commands.check(is_admin)
async def complete_quest(ctx, quest_id: int):
    quests = load_quests()
    quest = next((q for q in quests["active_quests"] if q["id"] == quest_id), None)
    
    if not quest:
        await ctx.send("Quest not found.")
        return
    
    quests["active_quests"].remove(quest)
    quests["completed_quests"].append(quest)
    save_quests(quests)
    
    participants = [f"<@{user_id}>" for user_id in quest["participants"]]
    participants_str = ", ".join(participants) if participants else "No participants"
    
    embed = discord.Embed(
        title=f"Quest Completed: {quest['title']}",
        color=discord.Color.gold()
    )
    embed.add_field(name="Reward", value=quest["reward"])
    embed.add_field(name="Participants", value=participants_str, inline=False)
    
    channel = bot.get_channel(config.quest_channel_id)
    await channel.send(embed=embed)
    await ctx.send(f"Quest {quest_id} marked as completed!")

@bot.command(name='listquests', help='List all active quests')
async def list_quests(ctx):
    quests = load_quests()
    
    if not quests["active_quests"]:
        await ctx.send("No active quests available.")
        return
    
    embed = discord.Embed(
        title="Active Quests",
        color=discord.Color.blue()
    )
    
    for quest in quests["active_quests"]:
        participants = len(quest["participants"])
        embed.add_field(
            name=f"{quest['id']}. {quest['title']}",
            value=f"{quest['description']}\nParticipants: {participants} | Reward: {quest['reward']}",
            inline=False
        )
    
    await ctx.send(embed=embed)

# Community engagement commands
@bot.command(name='pandafact', help='Get a random panda fact')
async def panda_fact(ctx):
    facts = [
        "Pandas spend 10-16 hours a day eating bamboo.",
        "Pandas have an extended wrist bone that they use like a thumb.",
        "A panda's diet is 99% bamboo.",
        "Newborn pandas are about 1/900th the size of their mother.",
        "Pandas have been on Earth for 2-3 million years."
    ]
    fact = random.choice(facts)
    await ctx.send(f"🐼 **Panda Fact:** {fact}")

@bot.command(name='roll', help='Roll a random number between 1 and 100')
async def roll(ctx):
    result = random.randint(1, 100)
    await ctx.send(f"🎲 {ctx.author.mention} rolled a {result}!")

@bot.command(name='poll', help='Create a simple poll')
async def poll(ctx, question: str, *options: str):
    if len(options) < 2 or len(options) > 10:
        await ctx.send("Please provide between 2 and 10 options.")
        return
    
    reactions = ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣', '8️⃣', '9️⃣', '🔟']
    description = []
    
    for idx, option in enumerate(options):
        description.append(f"{reactions[idx]} {option}")
    
    embed = discord.Embed(
        title=question,
        description="\n".join(description),
        color=discord.Color.purple()
    )
    embed.set_footer(text="React to vote!")
    
    message = await ctx.send(embed=embed)
    
    for i in range(len(options)):
        await message.add_reaction(reactions[i])

# Run the bot
if __name__ == '__main__':
    if not config.token:
        logger.error("DISCORD_TOKEN environment variable not set!")
        exit(1)
    
    try:
        bot.run(config.token)
    except discord.LoginFailure:
        logger.error("Invalid Discord token. Please check your environment variables.")
    except Exception as e:
        logger.error(f"Error starting bot: {e}")
```
