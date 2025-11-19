"""
Generated Code Metadata:
========================
Original URL: https://www.meta.pika.asia
Prompt: "Create a Discord bot to manage scholar applications and NFT leasing for a play-to-earn gaming platform like MetaLeagues."
Generated: DETERMINISTIC_319eb17887bbc2b0
Batch ID: 20250622_205045
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
import asyncio
import json
import os
from datetime import datetime

# Load configuration from environment variables or config file
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
if not DISCORD_TOKEN:
    with open('config.json') as f:
        config = json.load(f)
        DISCORD_TOKEN = config['discord_token']

# Define bot intents
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

# Database simulation using JSON files
SCHOLARS_FILE = 'scholars.json'
APPLICATIONS_FILE = 'applications.json'
NFT_LEASES_FILE = 'nft_leases.json'

def load_data(filename):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_data(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)

# Initialize data files if they don't exist
for file in [SCHOLARS_FILE, APPLICATIONS_FILE, NFT_LEASES_FILE]:
    if not os.path.exists(file):
        save_data(file, {})

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    print('------')

@bot.command(name='apply', help='Apply to become a scholar')
async def apply(ctx, *, application_text: str):
    applications = load_data(APPLICATIONS_FILE)
    user_id = str(ctx.author.id)
    
    if user_id in applications:
        await ctx.send('You have already submitted an application.')
        return
    
    applications[user_id] = {
        'text': application_text,
        'status': 'pending',
        'timestamp': str(datetime.utcnow()),
        'reviewer': None
    }
    
    save_data(APPLICATIONS_FILE, applications)
    await ctx.send('Your application has been submitted successfully!')

@bot.command(name='review_applications', help='Review pending scholar applications')
@commands.has_permissions(administrator=True)
async def review_applications(ctx):
    applications = load_data(APPLICATIONS_FILE)
    pending_apps = {k: v for k, v in applications.items() if v['status'] == 'pending'}
    
    if not pending_apps:
        await ctx.send('No pending applications.')
        return
    
    for user_id, app in pending_apps.items():
        embed = discord.Embed(
            title=f'Application from {user_id}',
            description=app['text'],
            color=discord.Color.blue()
        )
        embed.add_field(name='Status', value=app['status'])
        embed.add_field(name='Submitted', value=app['timestamp'])
        
        message = await ctx.send(embed=embed)
        await message.add_reaction('✅')
        await message.add_reaction('❌')
        
        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) in ['✅', '❌'] and reaction.message.id == message.id
        
        try:
            reaction, _ = await bot.wait_for('reaction_add', timeout=60.0, check=check)
            
            if str(reaction.emoji) == '✅':
                applications[user_id]['status'] = 'approved'
                applications[user_id]['reviewer'] = str(ctx.author.id)
                save_data(APPLICATIONS_FILE, applications)
                
                # Add to scholars
                scholars = load_data(SCHOLARS_FILE)
                scholars[user_id] = {
                    'joined_date': str(datetime.utcnow()),
                    'performance': 0,
                    'nfts': []
                }
                save_data(SCHOLARS_FILE, scholars)
                
                # Notify user
                user = await bot.fetch_user(int(user_id))
                await user.send('Congratulations! Your scholar application has been approved.')
                await ctx.send(f'Application from {user_id} approved.')
            else:
                applications[user_id]['status'] = 'rejected'
                applications[user_id]['reviewer'] = str(ctx.author.id)
                save_data(APPLICATIONS_FILE, applications)
                
                # Notify user
                user = await bot.fetch_user(int(user_id))
                await user.send('Your scholar application has been rejected.')
                await ctx.send(f'Application from {user_id} rejected.')
                
        except asyncio.TimeoutError:
            await ctx.send('Timed out waiting for response.')

@bot.command(name='lease_nft', help='Lease an NFT to a scholar')
@commands.has_permissions(administrator=True)
async def lease_nft(ctx, scholar_id: str, nft_id: str, duration_days: int):
    scholars = load_data(SCHOLARS_FILE)
    leases = load_data(NFT_LEASES_FILE)
    
    if scholar_id not in scholars:
        await ctx.send('Scholar not found.')
        return
    
    lease_id = f'{scholar_id}_{nft_id}'
    if lease_id in leases:
        await ctx.send('This NFT is already leased to this scholar.')
        return
    
    expiration = datetime.utcnow().timestamp() + (duration_days * 86400)
    leases[lease_id] = {
        'scholar_id': scholar_id,
        'nft_id': nft_id,
        'leased_at': str(datetime.utcnow()),
        'expires_at': str(datetime.fromtimestamp(expiration)),
        'active': True
    }
    
    scholars[scholar_id]['nfts'].append(nft_id)
    save_data(SCHOLARS_FILE, scholars)
    save_data(NFT_LEASES_FILE, leases)
    
    await ctx.send(f'NFT {nft_id} leased to scholar {scholar_id} for {duration_days} days.')

@bot.command(name='return_nft', help='Return a leased NFT')
@commands.has_permissions(administrator=True)
async def return_nft(ctx, scholar_id: str, nft_id: str):
    scholars = load_data(SCHOLARS_FILE)
    leases = load_data(NFT_LEASES_FILE)
    
    lease_id = f'{scholar_id}_{nft_id}'
    if lease_id not in leases:
        await ctx.send('Lease not found.')
        return
    
    leases[lease_id]['active'] = False
    save_data(NFT_LEASES_FILE, leases)
    
    if nft_id in scholars[scholar_id]['nfts']:
        scholars[scholar_id]['nfts'].remove(nft_id)
        save_data(SCHOLARS_FILE, scholars)
    
    await ctx.send(f'NFT {nft_id} returned from scholar {scholar_id}.')

@bot.command(name='scholar_info', help='Get information about a scholar')
async def scholar_info(ctx, scholar_id: str = None):
    if not scholar_id:
        scholar_id = str(ctx.author.id)
    
    scholars = load_data(SCHOLARS_FILE)
    if scholar_id not in scholars:
        await ctx.send('Scholar not found.')
        return
    
    scholar = scholars[scholar_id]
    embed = discord.Embed(
        title=f'Scholar Information: {scholar_id}',
        color=discord.Color.green()
    )
    embed.add_field(name='Joined Date', value=scholar['joined_date'])
    embed.add_field(name='Performance', value=str(scholar['performance']))
    embed.add_field(name='Leased NFTs', value=', '.join(scholar['nfts']) if scholar['nfts'] else 'None')
    
    await ctx.send(embed=embed)

@bot.command(name='update_performance', help='Update a scholar\'s performance score')
@commands.has_permissions(administrator=True)
async def update_performance(ctx, scholar_id: str, performance: int):
    scholars = load_data(SCHOLARS_FILE)
    if scholar_id not in scholars:
        await ctx.send('Scholar not found.')
        return
    
    scholars[scholar_id]['performance'] = performance
    save_data(SCHOLARS_FILE, scholars)
    await ctx.send(f'Updated performance for scholar {scholar_id} to {performance}.')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send('You do not have permission to use this command.')
    elif isinstance(error, commands.CommandNotFound):
        await ctx.send('Command not found.')
    else:
        await ctx.send(f'An error occurred: {str(error)}')

if __name__ == '__main__':
    bot.run(DISCORD_TOKEN)
```
