"""
Generated Code Metadata:
========================
Original URL: https://lavanetworks.pages.dev
Prompt: Generate a code example of using Lava SDK for sending relay requests to multiple blockchain networks, including Ethereum and Starknet.
Generated: DETERMINISTIC_073d0e5a00b38b08
Batch ID: 20250622_210053
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from lava_sdk import Lava
from typing import List, Dict, Optional
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class MultiChainRelayer:
    """
    A class to handle relay requests to multiple blockchain networks using Lava SDK.
    Supports Ethereum and Starknet by default.
    """
    
    def __init__(self):
        """
        Initialize the Lava SDK with API key from environment variables.
        """
        self.api_key = os.getenv("LAVA_API_KEY")
        if not self.api_key:
            raise ValueError("LAVA_API_KEY not found in environment variables")
        
        self.lava = Lava(self.api_key)
        self.supported_chains = {
            "ethereum": "ETH1",
            "starknet": "STARKNET1"
        }
    
    def send_relay(
        self,
        chain: str,
        method: str,
        params: List[Dict],
        block_tag: Optional[str] = "latest"
    ) -> Dict:
        """
        Send a relay request to the specified blockchain network.
        
        Args:
            chain: The blockchain network (e.g., "ethereum", "starknet")
            method: The RPC method to call
            params: Parameters for the RPC method
            block_tag: The block tag to query (default: "latest")
            
        Returns:
            The response from the blockchain network
            
        Raises:
            ValueError: If chain is not supported
            Exception: For Lava SDK or RPC errors
        """
        if chain.lower() not in self.supported_chains:
            raise ValueError(f"Unsupported chain: {chain}. Supported chains: {list(self.supported_chains.keys())}")
        
        try:
            response = self.lava.send_relay(
                chain_id=self.supported_chains[chain.lower()],
                method=method,
                params=params,
                block_tag=block_tag
            )
            return response
        except Exception as e:
            raise Exception(f"Failed to send relay request: {str(e)}")
    
    def batch_relay(
        self,
        chain: str,
        requests: List[Dict[str, List[Dict]]],
        block_tag: Optional[str] = "latest"
    ) -> List[Dict]:
        """
        Send a batch of relay requests to the specified blockchain network.
        
        Args:
            chain: The blockchain network (e.g., "ethereum", "starknet")
            requests: List of dicts with "method" and "params" keys
            block_tag: The block tag to query (default: "latest")
            
        Returns:
            List of responses from the blockchain network
            
        Raises:
            ValueError: If chain is not supported
            Exception: For Lava SDK or RPC errors
        """
        if chain.lower() not in self.supported_chains:
            raise ValueError(f"Unsupported chain: {chain}. Supported chains: {list(self.supported_chains.keys())}")
        
        try:
            responses = self.lava.send_batch_relay(
                chain_id=self.supported_chains[chain.lower()],
                requests=requests,
                block_tag=block_tag
            )
            return responses
        except Exception as e:
            raise Exception(f"Failed to send batch relay requests: {str(e)}")


# Example usage
if __name__ == "__main__":
    try:
        relayer = MultiChainRelayer()
        
        # Single relay example for Ethereum
        eth_response = relayer.send_relay(
            chain="ethereum",
            method="eth_getBalance",
            params=[{"address": "0x742d35Cc6634C0532925a3b844Bc454e4438f44e"}, "latest"]
        )
        print("Ethereum balance response:", eth_response)
        
        # Single relay example for Starknet
        starknet_response = relayer.send_relay(
            chain="starknet",
            method="starknet_getBlockWithTxs",
            params=[{"block_id": "latest"}]
        )
        print("Starknet block response:", starknet_response)
        
        # Batch relay example for Ethereum
        batch_requests = [
            {"method": "eth_blockNumber", "params": []},
            {"method": "eth_gasPrice", "params": []}
        ]
        batch_responses = relayer.batch_relay(
            chain="ethereum",
            requests=batch_requests
        )
        print("Ethereum batch responses:", batch_responses)
        
    except Exception as e:
        print(f"Error: {str(e)}")
```
