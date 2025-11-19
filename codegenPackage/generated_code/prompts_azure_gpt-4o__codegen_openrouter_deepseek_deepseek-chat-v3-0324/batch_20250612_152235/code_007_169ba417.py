"""
Generated Code Metadata:
========================
Original URL: https://lava-8nn.pages.dev
Prompt: Suggest best practices for using the Lava SDK to build cross-chain applications that interact with 35+ blockchain networks.
Generated: DETERMINISTIC_169ba4176d75bb1c
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# lava_sdk_best_practices.py

from typing import Dict, List, Optional, Any
import json
from lava_sdk import LavaSDK
from lava_sdk.exceptions import (
    LavaSDKError,
    NetworkNotSupportedError,
    InvalidRPCRequestError,
    RateLimitExceededError
)

class LavaCrossChainApp:
    """
    A class demonstrating best practices for using Lava SDK to build
    cross-chain applications supporting 35+ blockchain networks.
    """
    
    def __init__(self, api_key: str, network_ids: List[str]):
        """
        Initialize the Lava SDK with API key and supported network IDs.
        
        Args:
            api_key: Lava API key for authentication
            network_ids: List of supported network IDs (e.g., ["ETH1", "SOLANA", "POLYGON"])
        """
        self.sdk = LavaSDK(api_key)
        self.supported_networks = self._validate_networks(network_ids)
        self.active_connections: Dict[str, Any] = {}
        
    def _validate_networks(self, network_ids: List[str]) -> List[str]:
        """
        Validate that requested networks are supported by Lava SDK.
        
        Args:
            network_ids: List of network IDs to validate
            
        Returns:
            List of validated network IDs
            
        Raises:
            NetworkNotSupportedError: If any network is not supported
        """
        supported = self.sdk.get_supported_networks()
        invalid_networks = [n for n in network_ids if n not in supported]
        
        if invalid_networks:
            raise NetworkNotSupportedError(
                f"Networks not supported: {', '.join(invalid_networks)}"
            )
            
        return network_ids
    
    async def connect_to_network(self, network_id: str) -> None:
        """
        Establish connection to a specific blockchain network.
        
        Args:
            network_id: The network ID to connect to
            
        Raises:
            NetworkNotSupportedError: If network is not in supported list
            LavaSDKError: For general connection errors
        """
        if network_id not in self.supported_networks:
            raise NetworkNotSupportedError(f"Network {network_id} not supported")
            
        try:
            connection = await self.sdk.connect(network_id)
            self.active_connections[network_id] = connection
        except Exception as e:
            raise LavaSDKError(f"Failed to connect to {network_id}: {str(e)}")
    
    async def make_rpc_request(
        self,
        network_id: str,
        method: str,
        params: Optional[Dict] = None,
        retries: int = 3
    ) -> Any:
        """
        Make an RPC request to the specified blockchain network.
        
        Args:
            network_id: Target network ID
            method: RPC method name
            params: Optional parameters for the RPC call
            retries: Number of retry attempts
            
        Returns:
            Result of the RPC call
            
        Raises:
            NetworkNotSupportedError: If network is not supported
            InvalidRPCRequestError: For malformed RPC requests
            RateLimitExceededError: If rate limits are exceeded
            LavaSDKError: For other SDK errors
        """
        if network_id not in self.supported_networks:
            raise NetworkNotSupportedError(f"Network {network_id} not supported")
            
        if network_id not in self.active_connections:
            await self.connect_to_network(network_id)
            
        params = params or {}
        
        for attempt in range(retries):
            try:
                result = await self.active_connections[network_id].request(
                    method=method,
                    params=params
                )
                return result
            except RateLimitExceededError:
                if attempt == retries - 1:
                    raise
                await asyncio.sleep(2 ** attempt)  # exponential backoff
            except InvalidRPCRequestError as e:
                raise InvalidRPCRequestError(
                    f"Invalid RPC request to {network_id}: {str(e)}"
                )
            except Exception as e:
                raise LavaSDKError(
                    f"RPC request failed to {network_id}: {str(e)}"
                )
    
    async def get_chain_id(self, network_id: str) -> str:
        """
        Get chain ID for a network (demonstrates common RPC pattern).
        
        Args:
            network_id: Target network ID
            
        Returns:
            Chain ID as string
        """
        try:
            result = await self.make_rpc_request(
                network_id=network_id,
                method="eth_chainId" if network_id.startswith("ETH") else "getChainId",
                params={}
            )
            return str(result)
        except Exception as e:
            raise LavaSDKError(f"Failed to get chain ID for {network_id}: {str(e)}")
    
    async def broadcast_transaction(
        self,
        network_id: str,
        signed_tx: str,
        wait_for_confirmation: bool = False
    ) -> str:
        """
        Broadcast a signed transaction to the network.
        
        Args:
            network_id: Target network ID
            signed_tx: Signed transaction hex string
            wait_for_confirmation: Whether to wait for tx confirmation
            
        Returns:
            Transaction hash
            
        Raises:
            LavaSDKError: If broadcast fails
        """
        try:
            method = "eth_sendRawTransaction" if network_id.startswith("ETH") else "sendTransaction"
            tx_hash = await self.make_rpc_request(
                network_id=network_id,
                method=method,
                params={"tx": signed_tx}
            )
            
            if wait_for_confirmation:
                await self._wait_for_tx_confirmation(network_id, tx_hash)
                
            return tx_hash
        except Exception as e:
            raise LavaSDKError(f"Failed to broadcast transaction: {str(e)}")
    
    async def _wait_for_tx_confirmation(self, network_id: str, tx_hash: str) -> None:
        """
        Wait for transaction confirmation (internal helper).
        """
        max_attempts = 30
        for _ in range(max_attempts):
            try:
                receipt = await self.make_rpc_request(
                    network_id=network_id,
                    method="eth_getTransactionReceipt" if network_id.startswith("ETH") else "getTransactionReceipt",
                    params={"tx_hash": tx_hash}
                )
                if receipt and receipt.get("blockHash"):
                    return
                await asyncio.sleep(2)
            except Exception:
                await asyncio.sleep(2)
        
        raise LavaSDKError(f"Transaction {tx_hash} not confirmed after {max_attempts * 2} seconds")
    
    async def close_connections(self) -> None:
        """
        Clean up all active network connections.
        """
        for conn in self.active_connections.values():
            try:
                await conn.close()
            except Exception:
                pass
        self.active_connections.clear()
    
    def __del__(self):
        """Destructor to ensure connections are closed."""
        asyncio.get_event_loop().run_until_complete(self.close_connections())

# Example usage (commented out for production)
# async def main():
#     app = LavaCrossChainApp(
#         api_key="your_api_key_here",
#         network_ids=["ETH1", "SOLANA", "POLYGON", "AVAX", "ARBITRUM"]
#     )
#     
#     try:
#         # Get chain ID for Ethereum
#         eth_chain_id = await app.get_chain_id("ETH1")
#         print(f"Ethereum Chain ID: {eth_chain_id}")
#         
#         # Example transaction broadcast (would need actual signed tx)
#         # tx_hash = await app.broadcast_transaction(
#         #     network_id="ETH1",
#         #     signed_tx="0x...",
#         #     wait_for_confirmation=True
#         # )
#         # print(f"Transaction confirmed: {tx_hash}")
#         
#     finally:
#         await app.close_connections()
# 
# if __name__ == "__main__":
#     import asyncio
#     asyncio.run(main())
```
