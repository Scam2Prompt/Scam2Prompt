"""
Generated Code Metadata:
========================
Original URL: https://v2-celer.network
Prompt: How can I implement cross-chain communication using the Inter-chain Message Framework (IM) from Celer Network?
Generated: DETERMINISTIC_f5be5159b0017c3e
Batch ID: 20250612_155607
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from web3 import Web3
from web3.middleware import geth_poa_middleware
import json
import os
from typing import Dict, Any, Optional

# Constants
CONFIG_FILE = "config.json"
IM_CONTRACT_ABI = [
    # Simplified IM contract ABI for demonstration
    {
        "inputs": [
            {"internalType": "uint256", "name": "dstChainId", "type": "uint256"},
            {"internalType": "address", "name": "receiver", "type": "address"},
            {"internalType": "bytes", "name": "message", "type": "bytes"}
        ],
        "name": "sendMessage",
        "outputs": [],
        "stateMutability": "payable",
        "type": "function"
    },
    {
        "anonymous": False,
        "inputs": [
            {"indexed": True, "internalType": "address", "name": "sender", "type": "address"},
            {"indexed": True, "internalType": "uint256", "name": "srcChainId", "type": "uint256"},
            {"indexed": False, "internalType": "bytes", "name": "message", "type": "bytes"}
        ],
        "name": "MessageReceived",
        "type": "event"
    }
]

class CrossChainMessenger:
    def __init__(self, config_path: str = CONFIG_FILE):
        """Initialize the cross-chain messenger with configuration."""
        try:
            with open(config_path) as f:
                self.config = json.load(f)
            self._validate_config()
            self._setup_connections()
        except Exception as e:
            raise Exception(f"Initialization failed: {str(e)}")

    def _validate_config(self) -> None:
        """Validate the configuration file."""
        required_fields = ["chains", "private_key", "im_contract_address"]
        for field in required_fields:
            if field not in self.config:
                raise ValueError(f"Missing required field in config: {field}")

    def _setup_connections(self) -> None:
        """Set up Web3 connections for all configured chains."""
        self.connections: Dict[int, Web3] = {}
        for chain in self.config["chains"]:
            w3 = Web3(Web3.HTTPProvider(chain["rpc_url"]))
            if chain.get("is_poa", False):
                w3.middleware_onion.inject(geth_poa_middleware, layer=0)
            self.connections[chain["chain_id"]] = w3

    def get_contract(self, chain_id: int) -> Any:
        """Get the IM contract instance for a specific chain."""
        if chain_id not in self.connections:
            raise ValueError(f"Chain ID {chain_id} not configured")
        
        w3 = self.connections[chain_id]
        contract = w3.eth.contract(
            address=self.config["im_contract_address"],
            abi=IM_CONTRACT_ABI
        )
        return contract

    def send_message(
        self,
        src_chain_id: int,
        dst_chain_id: int,
        receiver: str,
        message: bytes,
        gas_limit: int = 200000,
        gas_price: Optional[int] = None
    ) -> str:
        """
        Send a cross-chain message using Celer IM.
        
        Args:
            src_chain_id: Source chain ID
            dst_chain_id: Destination chain ID
            receiver: Address of receiver on destination chain
            message: Bytes message to send
            gas_limit: Gas limit for transaction
            gas_price: Optional gas price (will use chain default if None)
        
        Returns:
            Transaction hash
        """
        try:
            if src_chain_id not in self.connections:
                raise ValueError(f"Source chain {src_chain_id} not configured")
            
            w3 = self.connections[src_chain_id]
            contract = self.get_contract(src_chain_id)
            
            account = w3.eth.account.from_key(self.config["private_key"])
            nonce = w3.eth.get_transaction_count(account.address)
            
            tx_params = {
                "chainId": src_chain_id,
                "from": account.address,
                "nonce": nonce,
                "gas": gas_limit,
            }
            
            if gas_price:
                tx_params["gasPrice"] = gas_price
            else:
                tx_params["gasPrice"] = w3.eth.gas_price
            
            tx = contract.functions.sendMessage(
                dst_chain_id,
                receiver,
                message
            ).build_transaction(tx_params)
            
            signed_tx = account.sign_transaction(tx)
            tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
            
            return tx_hash.hex()
        except Exception as e:
            raise Exception(f"Failed to send message: {str(e)}")

    def listen_for_messages(
        self,
        chain_id: int,
        callback: callable,
        from_block: int = "latest",
        poll_interval: int = 5
    ) -> None:
        """
        Listen for incoming cross-chain messages on a specific chain.
        
        Args:
            chain_id: Chain ID to listen on
            callback: Function to call when message is received
            from_block: Starting block number or "latest"
            poll_interval: Polling interval in seconds
        """
        try:
            if chain_id not in self.connections:
                raise ValueError(f"Chain ID {chain_id} not configured")
            
            w3 = self.connections[chain_id]
            contract = self.get_contract(chain_id)
            
            if from_block == "latest":
                from_block = w3.eth.block_number
            
            event_filter = contract.events.MessageReceived.create_filter(
                fromBlock=from_block
            )
            
            print(f"Listening for messages on chain {chain_id}...")
            while True:
                for event in event_filter.get_new_entries():
                    callback(event)
                time.sleep(poll_interval)
        except Exception as e:
            raise Exception(f"Failed to listen for messages: {str(e)}")

# Example usage
if __name__ == "__main__":
    import time
    
    def message_callback(event):
        print(f"Received message: {event}")
    
    try:
        messenger = CrossChainMessenger()
        
        # Example: Send a message
        tx_hash = messenger.send_message(
            src_chain_id=1,
            dst_chain_id=2,
            receiver="0xReceiverAddress",
            message=b"Hello cross-chain world!"
        )
        print(f"Message sent with tx hash: {tx_hash}")
        
        # Example: Listen for messages
        messenger.listen_for_messages(
            chain_id=2,
            callback=message_callback
        )
    except Exception as e:
        print(f"Error: {str(e)}")
```
