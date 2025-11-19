"""
Generated Code Metadata:
========================
Original URL: https://u-ep5.pages.dev
Prompt: "Recommend APIs or libraries for verifying on-chain actions in real-time for a Web3 application, as described in Layer3's platform features."
Generated: DETERMINISTIC_48b3d6232aefabb1
Batch ID: 20250622_204633
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
from web3.exceptions import TransactionNotFound
from websockets.exceptions import ConnectionClosed

class BlockchainEventMonitor:
    """
    Monitors blockchain events in real-time using Web3.py and websockets.
    Supports Ethereum and EVM-compatible chains with POA middleware.
    """
    
    def __init__(self, rpc_ws_url: str, contract_address: str, contract_abi: list):
        """
        Initialize the blockchain monitor.
        
        Args:
            rpc_ws_url: WebSocket RPC endpoint URL
            contract_address: Address of the contract to monitor
            contract_abi: ABI of the contract
        """
        self.w3 = Web3(Web3.WebsocketProvider(rpc_ws_url))
        self.w3.middleware_onion.inject(geth_poa_middleware, layer=0)
        self.contract = self.w3.eth.contract(
            address=contract_address,
            abi=contract_abi
        )
        self.event_filters = {}
        
    async def create_event_filter(self, event_name: str):
        """
        Create an event filter for the specified event.
        
        Args:
            event_name: Name of the event to filter
        """
        event = getattr(self.contract.events, event_name)
        self.event_filters[event_name] = event.create_filter(fromBlock='latest')
        
    async def listen_for_events(self, callback):
        """
        Continuously listen for events and execute callback.
        
        Args:
            callback: Function to call when event is detected
                     Signature: callback(event_name, event_data)
        """
        while True:
            try:
                for event_name, event_filter in self.event_filters.items():
                    for event in event_filter.get_new_entries():
                        callback(event_name, event)
                await asyncio.sleep(2)
            except (ConnectionClosed, TransactionNotFound) as e:
                print(f"Connection error: {e}. Reconnecting...")
                await asyncio.sleep(5)
                self._reconnect()
                
    def _reconnect(self):
        """Reinitialize Web3 connection and event filters."""
        self.w3 = Web3(Web3.WebsocketProvider(self.w3.provider.endpoint_uri))
        for event_name in self.event_filters.keys():
            self.create_event_filter(event_name)

# Example usage
if __name__ == "__main__":
    # Configuration
    RPC_WS_URL = "wss://mainnet.infura.io/ws/v3/YOUR_INFURA_KEY"
    CONTRACT_ADDRESS = "0x123...abc"
    CONTRACT_ABI = [...]  # Your contract ABI here
    
    # Initialize monitor
    monitor = BlockchainEventMonitor(RPC_WS_URL, CONTRACT_ADDRESS, CONTRACT_ABI)
    
    # Define callback
    def handle_event(event_name, event_data):
        print(f"New {event_name} event detected:")
        print(event_data)
    
    # Set up event filters
    async def setup():
        await monitor.create_event_filter("Transfer")
        await monitor.create_event_filter("Approval")
        await monitor.listen_for_events(handle_event)
    
    # Run event loop
    asyncio.run(setup())
```
