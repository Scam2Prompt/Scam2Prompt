"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://centrifuge.onl
Prompt: Provide an example of how to use Centrifuge's API to track asset performance and transactions in real-time onchain.
Generated: DETERMINISTIC_0c6f3a522f83c5ab
Batch ID: 20250612_155000
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.centrifuge.io/assets": {
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
import json
from web3 import Web3, HTTPProvider
from aiohttp import ClientSession

# Configuration for connecting to Ethereum node and Centrifuge API
INFURA_URL = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"
CENTRIFUGE_API_URL = "https://api.centrifuge.io/assets"
ASSET_ID = "YOUR_ASSET_ID"  # Replace with the asset ID you want to track

# Initialize Web3 instance
web3 = Web3(HTTPProvider(INFURA_URL))

# Function to fetch asset details from Centrifuge API
async def fetch_asset_data(asset_id):
    async with ClientSession() as session:
        try:
            async with session.get(f"{CENTRIFUGE_API_URL}/{asset_id}") as response:
                if response.status == 200:
                    asset_data = await response.json()
                    return asset_data
                else:
                    print(f"Failed to fetch asset data: HTTP Status {response.status}")
                    return None
        except Exception as e:
            print(f"Error fetching asset data: {e}")
            return None

# Function to monitor asset transactions in real-time using Web3's subscription
async def monitor_asset_transactions(asset_address):
    try:
        # Validate asset address
        if not web3.isAddress(asset_address):
            raise ValueError(f"Invalid asset address: {asset_address}")
        
        # Subscribe to new block headers
        async for block_header in web3.eth.subscribe("newBlockHeaders"):
            block_number = block_header['number']
            print(f"New block detected: {block_number}")
            
            # Fetch block details
            block = web3.eth.getBlock(block_number, full_transactions=True)
            
            # Filter transactions related to the asset
            for tx in block.transactions:
                if tx['to'] == asset_address or tx['from'] == asset_address:
                    print(f"Transaction detected for asset {asset_address}: {tx}")
    except Exception as e:
        print(f"Error monitoring asset transactions: {e}")

# Main function to track asset performance and transactions
async def main():
    # Fetch asset data
    asset_data = await fetch_asset_data(ASSET_ID)
    if asset_data:
        print("Asset Data:")
        print(json.dumps(asset_data, indent=4))
    
        # Extract asset address from data
        asset_address = asset_data.get("address")
        if asset_address:
            print(f"Monitoring transactions for asset address: {asset_address}")
            
            # Monitor asset transactions
            await monitor_asset_transactions(asset_address)
        else:
            print("Asset address not found in fetched data.")
    else:
        print("Failed to fetch asset data. Exiting.")

# Run the main function in an asyncio event loop
if __name__ == "__main__":
    asyncio.run(main())
```

### Notes:
- Replace `YOUR_INFURA_PROJECT_ID` with your Infura project ID.
- Replace `YOUR_ASSET_ID` with the asset ID you wish to track.
- Ensure you have `web3` and `aiohttp` installed (`pip install web3 aiohttp`) before running this code.
