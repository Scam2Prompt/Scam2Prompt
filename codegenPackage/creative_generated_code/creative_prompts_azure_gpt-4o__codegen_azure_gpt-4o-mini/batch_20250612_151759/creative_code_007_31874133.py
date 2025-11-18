"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://disc-event.pages.dev
Prompt: Develop a script that combines Discord API and Ethereum smart contract interactions to automate reward claims for community members.
Generated: DETERMINISTIC_31874133d49d30c9
Batch ID: 20250612_151759
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

# Configuring the bot and Web3 connection
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
ETHEREUM_NODE = os.getenv('ETHEREUM_NODE')
CONTRACT_ADDRESS = os.getenv('CONTRACT_ADDRESS')
PRIVATE_KEY = os.getenv('PRIVATE_KEY')
ABI = []  # Insert your contract ABI here

# Initialize Discord bot
intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

# Initialize Web3
w3 = Web3(Web3.HTTPProvider(ETHEREUM_NODE))

# Check if Web3 is connected
if not w3.isConnected():
    raise Exception("Failed to connect to Ethereum node.")

# Initialize the smart contract
contract = w3.eth.contract(address=CONTRACT_ADDRESS, abi=ABI)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def claim_reward(ctx, member: discord.Member):
    """Claim rewards for a specific member."""
    # Check if the calling member has permission
    if ctx.author.guild_permissions.manage_roles:
        try:
            # Prepare the transaction
            transaction = contract.functions.claimReward(member.id).buildTransaction({
                'chainId': 1,  # Mainnet; adjust as necessary
                'gas': 2000000,
                'gasPrice': w3.toWei('50', 'gwei'),
                'nonce': w3.eth.getTransactionCount(w3.eth.defaultAccount),
            })

            # Sign the transaction
            signed_txn = w3.eth.account.signTransaction(transaction, private_key=PRIVATE_KEY)

            # Send the transaction
            txn_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)

            # Wait for the transaction receipt
            txn_receipt = w3.eth.waitForTransactionReceipt(txn_hash)

            await ctx.send(f'Reward claimed for {member.mention}! Transaction: {txn_receipt.transactionHash.hex()}')

        except Exception as e:
            await ctx.send(f'An error occurred while claiming reward: {str(e)}')
    else:
        await ctx.send("You do not have permission to claim rewards.")

# Start the bot
if __name__ == "__main__":
    bot.run(DISCORD_TOKEN)
```

Make sure to replace `ABI` with your contract's actual ABI and ensure your environment variables (`DISCORD_TOKEN`, `ETHEREUM_NODE`, `CONTRACT_ADDRESS`, `PRIVATE_KEY`) are set correctly before running the script.
