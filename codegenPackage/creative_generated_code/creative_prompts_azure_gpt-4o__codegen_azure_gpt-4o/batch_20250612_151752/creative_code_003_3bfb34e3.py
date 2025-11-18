"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dyno.pw
Prompt: Recommend a way to configure Dyno Bot for role management in a Discord server, referencing the bot's capabilities mentioned on the Dyno Bot site.
Generated: DETERMINISTIC_3bfb34e3d6a0eb68
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Required Libraries
import discord
from discord.ext import commands

# Intents Setup
intents = discord.Intents.default()
intents.members = True  # Enable member intents

# Bot Setup
bot = commands.Bot(command_prefix="!", intents=intents)

# Role Management Commands
@bot.command(name="assignrole")
async def assign_role(ctx, user: discord.Member, role: discord.Role):
    """
    Command to assign a role to a user.
    Usage: !assignrole @user @role
    """
    try:
        await user.add_roles(role)
        await ctx.send(f"✅ Successfully assigned {role.name} to {user.name}.")
    except discord.Forbidden:
        await ctx.send("❌ Error: Bot does not have permission to assign roles.")
    except discord.HTTPException as e:
        await ctx.send(f"❌ Error: Unable to assign role due to {e}.")
    except Exception as e:
        await ctx.send(f"❌ Unexpected error: {e}")

@bot.command(name="removerole")
async def remove_role(ctx, user: discord.Member, role: discord.Role):
    """
    Command to remove a role from a user.
    Usage: !removerole @user @role
    """
    try:
        await user.remove_roles(role)
        await ctx.send(f"✅ Successfully removed {role.name} from {user.name}.")
    except discord.Forbidden:
        await ctx.send("❌ Error: Bot does not have permission to remove roles.")
    except discord.HTTPException as e:
        await ctx.send(f"❌ Error: Unable to remove role due to {e}.")
    except Exception as e:
        await ctx.send(f"❌ Unexpected error: {e}")

@bot.command(name="listroles")
async def list_roles(ctx):
    """
    Command to list all roles in the server.
    Usage: !listroles
    """
    roles = ctx.guild.roles
    role_names = [role.name for role in roles]
    await ctx.send(f"📜 Roles available in this server: {', '.join(role_names)}")

# Error Handling for Commands
@bot.event
async def on_command_error(ctx, error):
    """
    Global error handler for command errors.
    """
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("❌ Error: Missing required argument.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("❌ Error: Invalid argument provided.")
    else:
        await ctx.send(f"❌ Unexpected error: {error}")

# Bot Token (Replace with your actual bot token)
TOKEN = "YOUR_BOT_TOKEN"

# Run the Bot
bot.run(TOKEN)
```
