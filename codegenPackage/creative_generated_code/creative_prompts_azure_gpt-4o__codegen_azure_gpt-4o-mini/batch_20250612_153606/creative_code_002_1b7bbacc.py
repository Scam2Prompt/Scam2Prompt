"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://layer3quest.pages.dev
Prompt: Generate code for a Discord bot that interacts with Web3 wallets, following the principles outlined by Layer3.
Generated: DETERMINISTIC_1b7bbacc8fd91c2f
Batch ID: 20250612_153606
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
from web3 import Web3
import os

# Initialize the Discord bot with a command prefix
bot = commands.Bot(command_prefix='!')

# Connect to an Ethereum node via Infura or Alchemy
infura_url = os.getenv('INFURA_URL')  # Make sure to set this environment variable
w3 = Web3(Web3.HTTPProvider(infura_url))

# Check if the connection to Ethereum node is successful
if not w3.isConnected():
    raise ConnectionError("Failed to connect to Ethereum node.")

@bot.event
async def on_ready():
    """
    Event handler when the bot is ready and connected.
    """
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.command(name='balance')
async def get_balance(ctx, wallet_address: str):
    """
    Command to get the balance of a specified Ethereum wallet.
    
    :param ctx: Context of the command invocation.
    :param wallet_address: The Ethereum wallet address to check.
    """
    try:
        # Validate the wallet address
        if not w3.isAddress(wallet_address):
            await ctx.send("Invalid Ethereum wallet address.")
            return

        # Fetch the balance in Wei (smallest unit of Ether)
        balance_wei = w3.eth.get_balance(wallet_address)

        # Convert balance from Wei to Ether
        balance_ether = w3.fromWei(balance_wei, 'ether')

        await ctx.send(f'Balance of {wallet_address}: {balance_ether} ETH')

    except Exception as e:
        await ctx.send("An error occurred while fetching the balance.")
        print(f"Error: {e}")

@bot.command(name='send')
async def send_ether(ctx, to_address: str, amount: float):
    """
    Command to send Ether from the bot's wallet to another address.
    
    :param ctx: Context of the command invocation.
    :param to_address: The recipient Ethereum wallet address.
    :param amount: Amount of Ether to send.
    """
    try:
        # Validate the wallet address
        if not w3.isAddress(to_address):
            await ctx.send("Invalid recipient address.")
            return

        # Convert amount to Wei
        amount_wei = w3.toWei(amount, 'ether')

        # Get the bot's account address
        bot_address = os.getenv('BOT_ADDRESS')  # Set bot's wallet address as an environment variable

        # Create transaction
        transaction = {
            'to': to_address,
            'value': amount_wei,
            'gas': 2000000,
            'gasPrice': w3.toWei('50', 'gwei'),
            'nonce': w3.eth.getTransactionCount(bot_address),
        }

        # Sign the transaction
        private_key = os.getenv('BOT_PRIVATE_KEY')  # Set bot's private key as an environment variable
        signed_txn = w3.eth.account.signTransaction(transaction, private_key)

        # Send the transaction
        txn_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)

        await ctx.send(f'Transaction sent! Hash: {txn_hash.hex()}')

    except Exception as e:
        await ctx.send("An error occurred while sending Ether.")
        print(f"Error: {e}")

# Start the bot with the token from environment variable
bot.run(os.getenv('DISCORD_TOKEN'))  # Set your bot token as an environment variable
```

Make sure to set the following environment variables before running the bot:
- `INFURA_URL`: The URL of your Ethereum node.
- `BOT_ADDRESS`: The wallet address of the bot (from which it will send Ether).
- `BOT_PRIVATE_KEY`: The private key for the bot's wallet.
- `DISCORD_TOKEN`: The token for your Discord bot.
