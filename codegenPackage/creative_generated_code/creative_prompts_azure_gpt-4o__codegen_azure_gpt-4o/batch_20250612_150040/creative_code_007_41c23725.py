"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rapping-planet-prehistoric.on-fleek.app
Prompt: Generate code for creating a private Discord bot for NFT holders, as described in phase 2 of the "Cats World" roadmap.
Generated: DETERMINISTIC_41c237251a57b0d7
Batch ID: 20250612_150040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import discord
from discord.ext import commands
import asyncio
import json
from web3 import Web3

# Load configuration from a file (e.g., config.json)
# Ensure this file contains your bot token and Web3-related information
try:
    with open("config.json") as f:
        config = json.load(f)
except FileNotFoundError:
    print("Error: Config file not found. Please ensure 'config.json' exists.")
    exit(1)
except json.JSONDecodeError:
    print("Error: Invalid JSON format in 'config.json'.")
    exit(1)

# Discord bot token from config
DISCORD_TOKEN = config.get("discord_token")

# NFT contract details from config
INFURA_URL = config.get("infura_url")  # Infura or other Ethereum node URL
NFT_CONTRACT_ADDRESS = config.get("nft_contract_address")  # NFT smart contract address
CHAIN_ID = config.get("chain_id", 1)  # Default to Ethereum Mainnet

# Web3 setup
w3 = Web3(Web3.HTTPProvider(INFURA_URL))
if not w3.isConnected():
    print("Error: Unable to connect to Ethereum network.")
    exit(1)

try:
    # Load ABI from file or config
    with open("abi.json") as f:
        NFT_CONTRACT_ABI = json.load(f)
except FileNotFoundError:
    print("Error: ABI file not found. Please ensure 'abi.json' exists.")
    exit(1)

# Initialize NFT Contract
nft_contract = w3.eth.contract(address=Web3.toChecksumAddress(NFT_CONTRACT_ADDRESS), abi=NFT_CONTRACT_ABI)

# Check if a user owns the NFT by their wallet address
def is_nft_holder(wallet_address):
    try:
        # Call the NFT contract's balanceOf function
        balance = nft_contract.functions.balanceOf(Web3.toChecksumAddress(wallet_address)).call()
        return balance > 0
    except Exception as e:
        print(f"Error while checking NFT ownership: {e}")
        return False

# Bot setup
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True

bot = commands.Bot(command_prefix='!', intents=intents)

# Command to verify NFT ownership
@bot.command()
async def verify(ctx, wallet_address: str):
    """Verify if the user owns an NFT"""
    await ctx.message.delete()  # Delete the command message for security
    
    # Check wallet address validity
    if not Web3.isAddress(wallet_address):
        await ctx.send("Invalid wallet address. Please provide a valid Ethereum wallet address.", delete_after=10)
        return

    # Check ownership
    await ctx.send("Verifying NFT ownership, please wait...", delete_after=10)
    asyncio.create_task(check_nft_ownership(ctx.author, wallet_address))

async def check_nft_ownership(user, wallet_address):
    """Asynchronous task to check NFT ownership"""
    try:
        if is_nft_holder(wallet_address):
            # Add role to the user (assuming 'NFT Holder' role exists)
            guild = discord.utils.get(bot.guilds, id=user.guild.id)
            role = discord.utils.get(guild.roles, name="NFT Holder")
            if role:
                await user.add_roles(role)
                await user.send(f"Congratulations! You have been verified as an NFT Holder and granted access.")
            else:
                await user.send("NFT Holder role does not exist on this server. Please contact an admin.")
        else:
            await user.send("Verification failed: You do not own the required NFT.")
    except Exception as e:
        print(f"Error during verification: {e}")
        await user.send("An error occurred during verification. Please try again or contact support.")

# Error handling for command errors
@bot.event
async def on_command_error(ctx, error):
    """Handles errors during command execution"""
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Missing argument. Please check the command and provide all required information.")
    elif isinstance(error, commands.CommandInvokeError):
        await ctx.send("An error occurred while executing the command. Please try again.")
    else:
        await ctx.send("An unexpected error occurred. Please contact support.")

# Bot startup event
@bot.event
async def on_ready():
    """Triggered when the bot is online and ready"""
    print(f"Bot is ready. Logged in as {bot.user.name} ({bot.user.id})")

# Run the bot
try:
    bot.run(DISCORD_TOKEN)
except discord.LoginFailure:
    print("Error: Invalid Discord bot token. Please check your configuration.")
except Exception as e:
    print(f"Error: {e}")
```
