"""
Generated Code Metadata:
========================
Original URL: https://foolz.sellpass.io
Prompt: Write a script to sell Discord roles and game powerups through a Sellpass storefront, incorporating automated blacklists and a ticket system for customer support.
Generated: DETERMINISTIC_49e48a4581b50440
Batch ID: 20250612_151429
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
import sellpass
import asyncio
import json
import os
from datetime import datetime

# Configuration
with open('config.json') as config_file:
    config = json.load(config_file)

TOKEN = config['discord_token']
SELLPASS_API_KEY = config['sellpass_api_key']
GUILD_ID = config['guild_id']
ROLES_CHANNEL_ID = config['roles_channel_id']
TICKETS_CHANNEL_ID = config['tickets_channel_id']
ADMIN_ROLE_ID = config['admin_role_id']
BLACKLIST_FILE = 'blacklist.json'
LOG_FILE = 'transactions.log'

# Initialize bot
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Initialize Sellpass client
sellpass_client = sellpass.Client(SELLPASS_API_KEY)

# Ensure data files exist
if not os.path.exists(BLACKLIST_FILE):
    with open(BLACKLIST_FILE, 'w') as f:
        json.dump({"users": []}, f)

if not os.path.exists(LOG_FILE):
    open(LOG_FILE, 'a').close()

class Blacklist:
    @staticmethod
    def is_blacklisted(user_id):
        with open(BLACKLIST_FILE, 'r') as f:
            data = json.load(f)
        return str(user_id) in data['users']

    @staticmethod
    def add_to_blacklist(user_id):
        with open(BLACKLIST_FILE, 'r+') as f:
            data = json.load(f)
            if str(user_id) not in data['users']:
                data['users'].append(str(user_id))
                f.seek(0)
                json.dump(data, f)
                return True
        return False

    @staticmethod
    def remove_from_blacklist(user_id):
        with open(BLACKLIST_FILE, 'r+') as f:
            data = json.load(f)
            if str(user_id) in data['users']:
                data['users'].remove(str(user_id))
                f.seek(0)
                json.dump(data, f)
                return True
        return False

class Logger:
    @staticmethod
    def log_transaction(user_id, item, status):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(LOG_FILE, 'a') as f:
            f.write(f"{timestamp} - User: {user_id} - Item: {item} - Status: {status}\n")

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    check_purchases.start()

@tasks.loop(minutes=5)
async def check_purchases():
    try:
        guild = bot.get_guild(GUILD_ID)
        if not guild:
            return

        purchases = sellpass_client.get_purchases()
        for purchase in purchases:
            if purchase.status == 'completed' and not purchase.processed:
                user_id = purchase.customer.discord_id
                if not user_id:
                    continue

                if Blacklist.is_blacklisted(user_id):
                    Logger.log_transaction(user_id, purchase.product.name, "Blacklisted")
                    continue

                member = guild.get_member(int(user_id))
                if not member:
                    continue

                # Handle role purchases
                if purchase.product.type == 'role':
                    role = discord.utils.get(guild.roles, name=purchase.product.name)
                    if role:
                        try:
                            await member.add_roles(role)
                            Logger.log_transaction(user_id, purchase.product.name, "Success")
                            purchase.mark_as_processed()
                        except discord.Forbidden:
                            Logger.log_transaction(user_id, purchase.product.name, "Permission Error")
                # Handle game powerups
                elif purchase.product.type == 'powerup':
                    # Implement game-specific powerup logic here
                    Logger.log_transaction(user_id, purchase.product.name, "Powerup Processed")
                    purchase.mark_as_processed()

    except Exception as e:
        print(f"Error processing purchases: {e}")

@bot.command(name='blacklist')
@commands.has_role(ADMIN_ROLE_ID)
async def blacklist_user(ctx, user_id: int):
    if Blacklist.add_to_blacklist(user_id):
        await ctx.send(f"User {user_id} has been blacklisted.")
    else:
        await ctx.send(f"User {user_id} is already blacklisted.")

@bot.command(name='unblacklist')
@commands.has_role(ADMIN_ROLE_ID)
async def unblacklist_user(ctx, user_id: int):
    if Blacklist.remove_from_blacklist(user_id):
        await ctx.send(f"User {user_id} has been removed from the blacklist.")
    else:
        await ctx.send(f"User {user_id} was not found in the blacklist.")

@bot.command(name='createticket')
async def create_ticket(ctx):
    guild = ctx.guild
    category = discord.utils.get(guild.categories, id=TICKETS_CHANNEL_ID)
    
    ticket_channel = await guild.create_text_channel(
        f'ticket-{ctx.author.name}',
        category=category,
        topic=f'Ticket for {ctx.author.name}',
        reason=f'Ticket created by {ctx.author.name}'
    )
    
    await ticket_channel.set_permissions(
        ctx.author,
        read_messages=True,
        send_messages=True
    )
    
    admin_role = guild.get_role(ADMIN_ROLE_ID)
    await ticket_channel.set_permissions(
        admin_role,
        read_messages=True,
        send_messages=True
    )
    
    await ticket_channel.send(
        f"{ctx.author.mention}, your ticket has been created. "
        f"An admin will be with you shortly.\n\n"
        f"Please describe your issue in detail."
    )
    
    await ctx.send(f"Your ticket has been created: {ticket_channel.mention}")

@bot.command(name='closeticket')
@commands.has_role(ADMIN_ROLE_ID)
async def close_ticket(ctx):
    if 'ticket-' in ctx.channel.name:
        await ctx.send("This ticket will be closed in 10 seconds.")
        await asyncio.sleep(10)
        await ctx.channel.delete()
    else:
        await ctx.send("This is not a ticket channel.")

@bot.command(name='listroles')
async def list_roles(ctx):
    if ctx.channel.id != ROLES_CHANNEL_ID:
        return
    
    products = sellpass_client.get_products()
    role_products = [p for p in products if p.type == 'role']
    
    if not role_products:
        await ctx.send("No roles available for purchase.")
        return
    
    embed = discord.Embed(title="Available Roles", color=0x00ff00)
    for product in role_products:
        embed.add_field(
            name=product.name,
            value=f"Price: ${product.price}\n{product.description}",
            inline=False
        )
    
    await ctx.send(embed=embed)

@bot.command(name='listpowerups')
async def list_powerups(ctx):
    if ctx.channel.id != ROLES_CHANNEL_ID:
        return
    
    products = sellpass_client.get_products()
    powerup_products = [p for p in products if p.type == 'powerup']
    
    if not powerup_products:
        await ctx.send("No powerups available for purchase.")
        return
    
    embed = discord.Embed(title="Available Powerups", color=0x00ff00)
    for product in powerup_products:
        embed.add_field(
            name=product.name,
            value=f"Price: ${product.price}\n{product.description}",
            inline=False
        )
    
    await ctx.send(embed=embed)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRole):
        await ctx.send("You don't have permission to use this command.")
    elif isinstance(error, commands.CommandNotFound):
        pass
    else:
        await ctx.send(f"An error occurred: {str(error)}")
        raise error

bot.run(TOKEN)
```
