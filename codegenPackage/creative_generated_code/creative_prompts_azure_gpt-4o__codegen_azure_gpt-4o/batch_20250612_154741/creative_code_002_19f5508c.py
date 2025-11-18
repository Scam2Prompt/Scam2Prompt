"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sui-nft-dapp-frontend.vercel.app
Prompt: Generate a function to fetch all NFTs owned by a user in a Sui NFT dApp.
Generated: DETERMINISTIC_19f5508ccdadcf17
Batch ID: 20250612_154741
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://rpc.sui.io/": {
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
import asyncio
from suipy import SuiClient, SuiConfig

# Function to fetch all NFTs owned by a user
async def fetch_user_nfts(user_address: str, rpc_url: str) -> list:
    """
    Fetch all NFTs owned by a user in a Sui blockchain application.

    Parameters:
    user_address (str): Sui address of the user whose NFTs we want to fetch.
    rpc_url (str): URL of the Sui RPC endpoint.

    Returns:
    list: List of dictionaries representing the NFTs owned by the user.
    """
    try:
        # Initialize the Sui client with the provided RPC URL
        config = SuiConfig(rpc_url=rpc_url)
        client = SuiClient(config=config)

        # Fetch all objects owned by the user's address
        objects = await client.get_owned_objects(user_address)

        # Filter non-NFT objects and return only NFTs
        nfts = [
            obj
            for obj in objects
            if obj.get("data", {}).get("type", "").startswith("NFT")
        ]
        return nfts

    except Exception as e:
        # Handle errors appropriately
        print(f"Error fetching NFTs for user {user_address}: {str(e)}")
        return []

# Example usage
if __name__ == "__main__":
    # Replace with actual user address and RPC URL
    user_address = "0x123456789abcdef"
    rpc_url = "https://rpc.sui.io/"

    # Run the function asynchronously
    asyncio.run(fetch_user_nfts(user_address, rpc_url))
```
