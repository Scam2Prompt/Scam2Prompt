"""
Generated Code Metadata:
========================
Original URL: https://get-apedvip.pages.dev
Prompt: Suggest APIs or tools for monitoring Ethereum transactions in real-time to track presale contributions, similar to the APED presale's total contribution tracking.
Generated: DETERMINISTIC_8ef60d87b907c5c5
Batch ID: 20250612_153420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import asyncio
from web3 import Web3
from web3.middleware import geth_poa_middleware
import json
import time
from websockets import connect

# Configuration
INFURA_URL = "wss://mainnet.infura.io/ws/v3/YOUR_INFURA_PROJECT_ID"
PRESALE_CONTRACT_ADDRESS = "0xPRESALE_CONTRACT_ADDRESS"
ABI_PATH = "presale_contract_abi.json"  # Path to ABI JSON file

# Load ABI
with open(ABI_PATH) as f:
    CONTRACT_ABI = json.load(f)

class EthereumPresaleMonitor:
    def __init__(self):
        self.w3 = Web3(Web3.WebsocketProvider(INFURA_URL))
        self.w3.middleware_onion.inject(geth_poa_middleware, layer=0)
        self.contract = self.w3.eth.contract(
            address=PRESALE_CONTRACT_ADDRESS,
            abi=CONTRACT_ABI
        )
        self.event_filter = None

    async def log_loop(self, event_filter, poll_interval=2):
        while True:
            try:
                for event in event_filter.get_new_entries():
                    self.handle_event(event)
                await asyncio.sleep(poll_interval)
            except Exception as e:
                print(f"Error in log loop: {e}")
                await asyncio.sleep(5)  # Wait before retrying

    def handle_event(self, event):
        # Process event data
        tx_hash = event['transactionHash'].hex()
        contributor = event['args']['contributor']
        amount = self.w3.fromWei(event['args']['amount'], 'ether')
        
        print(f"New contribution detected!")
        print(f"Tx Hash: {tx_hash}")
        print(f"Contributor: {contributor}")
        print(f"Amount: {amount} ETH")
        print("-" * 50)

    async def monitor_contributions(self):
        try:
            # Create event filter for Contribution event
            contribution_event = self.contract.events.Contribution()
            self.event_filter = contribution_event.createFilter(fromBlock='latest')
            
            # Start monitoring
            await self.log_loop(self.event_filter)
        except Exception as e:
            print(f"Error setting up event filter: {e}")

    def get_total_contributions(self):
        try:
            total = self.contract.functions.totalContributions().call()
            return self.w3.fromWei(total, 'ether')
        except Exception as e:
            print(f"Error getting total contributions: {e}")
            return None

async def main():
    monitor = EthereumPresaleMonitor()
    
    # Get initial total
    total = monitor.get_total_contributions()
    if total is not None:
        print(f"Current total contributions: {total} ETH")
    
    # Start monitoring
    await monitor.monitor_contributions()

if __name__ == "__main__":
    asyncio.run(main())
```
