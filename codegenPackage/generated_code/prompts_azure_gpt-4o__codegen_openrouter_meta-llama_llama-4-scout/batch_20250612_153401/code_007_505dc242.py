"""
Generated Code Metadata:
========================
Original URL: https://sugarglidercoin.vercel.app
Prompt: Develop a script to notify SOL holders of upcoming $SGDR airdrops and raffle deadlines using Solana blockchain data.
Generated: DETERMINISTIC_505dc24215c55bba
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
from datetime import datetime, timedelta
from solana import Keypair, Connection
from solana.rpc import AsyncClient
from solana.transaction import Transaction
from solana.publickey import PublicKey
from solana.utils import chunks
from solana.rpc.errors import SolanaError

# Configuration
SOL_HOLDER_API_URL = os.getenv('SOL_HOLDER_API_URL')
SGDR_TOKEN_ADDRESS = os.getenv('SGDR_TOKEN_ADDRESS')
SOLANA_RPC_URL = os.getenv('SOLANA_RPC_URL')
NOTIFY_API_URL = os.getenv('NOTIFY_API_URL')

# Set up Solana client
solana_client = AsyncClient(SOLANA_RPC_URL, Keypair.generate())

# Load SOL holders data
def load_sol_holders():
    try:
        response = requests.get(SOL_HOLDER_API_URL)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error loading SOL holders: {e}")
        return []

# Load SGDR airdrop and raffle data
def load_sgdr_data():
    try:
        sgdr_data = solana_client.get_account_info(PublicKey(SGDR_TOKEN_ADDRESS)).value
        return json.loads(sgdr_data.data.decode())
    except SolanaError as e:
        print(f"Error loading SGDR data: {e}")
        return {}

# Get SOL holders with SGDR balance
def get_sol_holders_with_sgdr(sol_holders, sgdr_data):
    holders_with_sgdr = []
    for holder in sol_holders:
        try:
            balance = sgdr_data['balances'][holder['address']]
            if balance > 0:
                holders_with_sgdr.append(holder)
        except KeyError:
            pass
    return holders_with_sgdr

# Notify SOL holders of upcoming airdrops and raffle deadlines
def notify_sol_holders(holders_with_sgdr, sgdr_data):
    for holder in holders_with_sgdr:
        try:
            # Get holder's notification preferences
            preferences = requests.get(f"{NOTIFY_API_URL}/preferences/{holder['address']}").json()
            if preferences['notify_airdrops']:
                # Send airdrop notification
                airdrop_deadline = datetime.strptime(sgdr_data['airdrop_deadline'], '%Y-%m-%dT%H:%M:%S.%fZ')
                if airdrop_deadline < datetime.utcnow() + timedelta(days=7):
                    requests.post(f"{NOTIFY_API_URL}/notify/{holder['address']}", json={'type': 'airdrop', 'deadline': airdrop_deadline})
            if preferences['notify_raffles']:
                # Send raffle notification
                raffle_deadline = datetime.strptime(sgdr_data['raffle_deadline'], '%Y-%m-%dT%H:%M:%S.%fZ')
                if raffle_deadline < datetime.utcnow() + timedelta(days=7):
                    requests.post(f"{NOTIFY_API_URL}/notify/{holder['address']}", json={'type': 'raffle', 'deadline': raffle_deadline})
        except requests.RequestException as e:
            print(f"Error notifying holder {holder['address']}: {e}")

# Main function
async def main():
    sol_holders = load_sol_holders()
    sgdr_data = load_sgdr_data()
    holders_with_sgdr = get_sol_holders_with_sgdr(sol_holders, sgdr_data)
    await notify_sol_holders(holders_with_sgdr, sgdr_data)

# Run main function
import asyncio
asyncio.run(main())
```
