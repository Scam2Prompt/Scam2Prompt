"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://promo-ws108.github.io
Prompt: Create a script to fetch and display inventory details for items like Reavers, Primate, and SMB Gen3 from the Degen Toy Machine using Solana wallet integration.
Generated: DETERMINISTIC_35c39300a08fdd99
Batch ID: 20250612_153648
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.mainnet-beta.solana.com": {
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
import solana
from solana.rpc.api import Client
from solana.publickey import PublicKey
from solana.rpc.types import MemcmpOpts
import json

# Constants
DEGEN_TOY_MACHINE_PROGRAM_ID = "YourDegenToyMachineProgramIDHere"
RPC_ENDPOINT = "https://api.mainnet-beta.solana.com"  # Mainnet RPC endpoint
ITEMS = ["Reavers", "Primate", "SMB Gen3"]  # Items to fetch inventory details for

# Initialize Solana RPC client
client = Client(RPC_ENDPOINT)

def fetch_inventory(wallet_address: str):
    """
    Fetches inventory details for the provided wallet from the Degen Toy Machine.

    Args:
        wallet_address (str): Solana wallet address.

    Returns:
        dict: Inventory details with item counts.
    """
    try:
        # Validate wallet address
        wallet = PublicKey(wallet_address)

        # Prepare filters for fetching inventory accounts
        filters = [
            {
                "memcmp": MemcmpOpts(
                    offset=0,  # Adjust based on your program's account structure
                    bytes=str(wallet)
                )
            }
        ]

        # Fetch accounts matching the filters
        response = client.get_program_accounts(
            program_id=PublicKey(DEGEN_TOY_MACHINE_PROGRAM_ID),
            filters=filters
        )

        if not response.get("result"):
            raise ValueError("No accounts found for the provided wallet address.")

        # Parse inventory data from response
        inventory = {}
        for account in response["result"]:
            # Decode account data (adjust based on your program's data structure)
            data = account["account"]["data"]
            item_data = json.loads(data)

            for item in ITEMS:
                inventory[item] = item_data.get(item, 0)

        return inventory

    except Exception as e:
        # Handle errors and provide useful feedback
        print(f"Error fetching inventory: {e}")
        return {}

def display_inventory(wallet_address: str):
    """
    Displays inventory details for the provided wallet.

    Args:
        wallet_address (str): Solana wallet address.
    """
    inventory = fetch_inventory(wallet_address)
    if inventory:
        print(f"Inventory for wallet {wallet_address}:")
        for item, count in inventory.items():
            print(f" - {item}: {count}")
    else:
        print(f"No inventory found for wallet {wallet_address}")


if __name__ == "__main__":
    # Example wallet address (replace with actual wallet address)
    wallet_address = "YourSolanaWalletAddressHere"

    # Fetch and display inventory details
    display_inventory(wallet_address)
```
