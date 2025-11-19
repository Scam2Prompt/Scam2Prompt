"""
Generated Code Metadata:
========================
Original URL: https://walletconnect-test-wallet.pages.dev
Prompt: How does WalletConnect Test Wallet facilitate testing of WalletConnect integrations?
Generated: DETERMINISTIC_b28129960a91f0c9
Batch ID: 20250622_205158
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# walletconnect_test_wallet.py

import json
from typing import Dict, Any, Optional
from uuid import uuid4
from web3 import Web3
from web3.providers.websocket import WebsocketProvider

class WalletConnectTestWallet:
    """
    A test wallet implementation to facilitate WalletConnect integration testing.
    Handles pairing, session requests, and transaction signing for testing purposes.
    """
    
    def __init__(self, rpc_url: str = "ws://localhost:8545"):
        """
        Initialize the test wallet with a Web3 provider.
        
        Args:
            rpc_url: WebSocket RPC URL for the blockchain node
        """
        self.w3 = Web3(WebsocketProvider(rpc_url))
        self.active_sessions: Dict[str, Dict[str, Any]] = {}
        self.pending_requests: Dict[str, Dict[str, Any]] = {}
        
    def pair(self, uri: str) -> str:
        """
        Pair with a WalletConnect URI.
        
        Args:
            uri: WalletConnect URI to pair with
            
        Returns:
            Pairing ID (random UUID)
            
        Raises:
            ValueError: If URI is invalid
        """
        if not uri.startswith("wc:"):
            raise ValueError("Invalid WalletConnect URI")
            
        pairing_id = str(uuid4())
        self.active_sessions[pairing_id] = {
            "uri": uri,
            "connected": True,
            "accounts": [self.w3.eth.accounts[0]] if self.w3.eth.accounts else []
        }
        return pairing_id
        
    def handle_session_request(self, pairing_id: str, request: Dict[str, Any]) -> Dict[str, Any]:
        """
        Handle a session request from a dApp.
        
        Args:
            pairing_id: The pairing ID to handle request for
            request: The session request payload
            
        Returns:
            Response to the session request
            
        Raises:
            KeyError: If pairing ID doesn't exist
        """
        if pairing_id not in self.active_sessions:
            raise KeyError("Pairing ID not found")
            
        self.pending_requests[str(uuid4())] = request
        
        return {
            "approved": True,
            "chainId": self.w3.eth.chain_id,
            "accounts": self.active_sessions[pairing_id]["accounts"]
        }
        
    def handle_json_rpc_request(self, pairing_id: str, request: Dict[str, Any]) -> Dict[str, Any]:
        """
        Handle a JSON-RPC request from a dApp.
        
        Args:
            pairing_id: The pairing ID to handle request for
            request: The JSON-RPC request payload
            
        Returns:
            Response to the JSON-RPC request
            
        Raises:
            KeyError: If pairing ID doesn't exist
            ValueError: For unsupported methods
        """
        if pairing_id not in self.active_sessions:
            raise KeyError("Pairing ID not found")
            
        method = request.get("method")
        params = request.get("params", [])
        
        if method == "eth_sendTransaction":
            tx = params[0]
            tx_hash = self._send_transaction(tx)
            return {"result": tx_hash}
        elif method == "eth_sign":
            address = params[0]
            message = params[1]
            signature = self._sign_message(address, message)
            return {"result": signature}
        elif method == "personal_sign":
            message = params[0]
            address = params[1]
            signature = self._sign_message(address, message)
            return {"result": signature}
        else:
            raise ValueError(f"Unsupported method: {method}")
            
    def _send_transaction(self, tx: Dict[str, Any]) -> str:
        """
        Send a transaction (for testing purposes).
        
        Args:
            tx: Transaction parameters
            
        Returns:
            Transaction hash
        """
        if "from" not in tx:
            tx["from"] = self.w3.eth.accounts[0]
            
        if "gas" not in tx:
            tx["gas"] = 200000
            
        if "gasPrice" not in tx:
            tx["gasPrice"] = self.w3.eth.gas_price
            
        tx_hash = self.w3.eth.send_transaction(tx)
        return tx_hash.hex()
        
    def _sign_message(self, address: str, message: str) -> str:
        """
        Sign a message (for testing purposes).
        
        Args:
            address: Address to sign with
            message: Message to sign
            
        Returns:
            Signature
        """
        if address not in self.w3.eth.accounts:
            raise ValueError("Address not in test wallet")
            
        if message.startswith("0x"):
            message = self.w3.to_text(message)
            
        return self.w3.eth.sign(address, text=message).hex()
        
    def disconnect(self, pairing_id: str) -> None:
        """
        Disconnect a pairing session.
        
        Args:
            pairing_id: The pairing ID to disconnect
            
        Raises:
            KeyError: If pairing ID doesn't exist
        """
        if pairing_id not in self.active_sessions:
            raise KeyError("Pairing ID not found")
            
        del self.active_sessions[pairing_id]
```
