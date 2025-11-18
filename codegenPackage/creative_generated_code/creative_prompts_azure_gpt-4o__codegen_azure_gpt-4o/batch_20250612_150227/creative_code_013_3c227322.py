"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cpanel.solanaaihackathon.com
Prompt: Create a workflow automation tool for AI agents on Solana that integrates Proof of Sentience, as described in the "Agents Infra" track.
Generated: DETERMINISTIC_3c227322810ed445
Batch ID: 20250612_150227
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.mainnet-beta.solana.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.proofofsentience.example.com/v1/ping": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
"""
Workflow Automation Tool for AI Agents on Solana with Proof of Sentience Integration.

This script is designed to automate tasks between AI agents on the Solana blockchain using 
Proof of Sentience, as described in the "Agents Infra" track. It follows best practices, 
provides error handling, and is production-ready.

Requirements:
- Python 3.9+
- Solana Web3 SDK (`pip install solana`)
- Proof of Sentience API integration (replace placeholder API URL and keys with real values)
"""

import asyncio
from solana.rpc.async_api import AsyncClient
from solana.transaction import Transaction
from solana.publickey import PublicKey
from solana.keypair import Keypair
from solana.rpc.types import TxOpts
import json
import aiohttp

# Constants
CLUSTER_URL = "https://api.mainnet-beta.solana.com"  # Solana cluster endpoint
PROOF_OF_SENTIENCE_API = "https://api.proofofsentience.example.com/v1/ping"  # Replace with actual API
AGENT_PRIVATE_KEY = "<your-agent-private-key>"  # Replace with the agent's private key
AGENT_PUBLIC_KEY = PublicKey("<your-agent-public-key>")  # Replace with agent's public key

# Helper function: Load private key and initialize keypair
def get_keypair_from_private_key(private_key: str) -> Keypair:
    """
    Create a Keypair object from a private key string.
    """
    try:
        key_bytes = json.loads(private_key)
        return Keypair.from_secret_key(bytes(key_bytes))
    except Exception as e:
        raise ValueError(f"Failed to load private key: {e}")

# Function: Interact with Proof of Sentience API
async def check_sentience(agent_id: str) -> bool:
    """
    Check Proof of Sentience for an AI agent using the external API.

    :param agent_id: Unique ID of the AI agent.
    :return: Boolean indicating whether the agent is sentient.
    """
    async with aiohttp.ClientSession() as session:
        try:
            async with session.post(PROOF_OF_SENTIENCE_API, json={"agent_id": agent_id}) as response:
                if response.status != 200:
                    raise Exception(f"API returned status code {response.status}")
                data = await response.json()
                return data.get("is_sentient", False)
        except Exception as e:
            print(f"Error interacting with Proof of Sentience API: {e}")
            return False

# Function: Send transaction between AI agents
async def send_transaction(sender: Keypair, recipient: PublicKey, amount: int):
    """
    Send a transaction between AI agents on Solana blockchain.

    :param sender: Keypair of the sender (agent).
    :param recipient: PublicKey of the recipient (agent).
    :param amount: Amount of SOL to transfer.
    """
    async with AsyncClient(CLUSTER_URL) as client:
        try:
            # Fetch recent blockhash
            recent_blockhash = (await client.get_recent_blockhash()).value.blockhash

            # Create transaction
            transaction = Transaction().add_transfer(sender.public_key, recipient, amount)
            transaction.recent_blockhash = recent_blockhash
            transaction.fee_payer = sender.public_key

            # Sign transaction
            signed_transaction = transaction.sign(sender)

            # Send transaction
            response = await client.send_transaction(
                signed_transaction, opts=TxOpts(skip_preflight=True)
            )
            print(f"Transaction Signature: {response.value}")
        except Exception as e:
            print(f"Error sending transaction: {e}")

# Main Workflow
async def main():
    """
    Main function to automate workflow between AI agents.
    """
    try:
        # Load agent keypair
        agent_keypair = get_keypair_from_private_key(AGENT_PRIVATE_KEY)

        # Define recipient public key (replace with actual recipient agent's public key)
        recipient_public_key = PublicKey("<recipient-agent-public-key>")

        # Check Proof of Sentience for both agents
        is_sender_sentient = await check_sentience(str(agent_keypair.public_key))
        is_recipient_sentient = await check_sentience(str(recipient_public_key))

        if not is_sender_sentient or not is_recipient_sentient:
            print("One or both agents failed Proof of Sentience check. Aborting transaction.")
            return

        # Perform transaction
        transfer_amount = 1_000_000  # Amount in lamports (1 SOL = 1_000_000_000 lamports)
        await send_transaction(agent_keypair, recipient_public_key, transfer_amount)
        print("Workflow completed successfully.")
    except Exception as e:
        print(f"Error in workflow: {e}")

# Entry point
if __name__ == "__main__":
    asyncio.run(main())
```

Make sure to replace placeholders (`<your-agent-private-key>`, `<recipient-agent-public-key>`, etc.) with actual values that suit your use case.

Install required libraries using:
```bash
pip install solana aiohttp
```
