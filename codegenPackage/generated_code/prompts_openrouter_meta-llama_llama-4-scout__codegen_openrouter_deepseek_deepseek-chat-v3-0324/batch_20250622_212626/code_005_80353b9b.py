"""
Generated Code Metadata:
========================
Original URL: https://wormhole.pw
Prompt: Outline the steps to implement multichain applications using Wormhole's SDK, including native token transfers, queries, and messaging, and discuss the benefits of using Wormhole's permissionless tooling.
Generated: DETERMINISTIC_80353b9b1a940810
Batch ID: 20250622_212626
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from wormhole_sdk import (
    Wormhole,
    Chain,
    TokenBridge,
    Relayer,
    utils
)
from typing import Optional, Dict, Any
import json

# Initialize Wormhole SDK
def initialize_wormhole(config_path: str) -> Wormhole:
    """
    Initialize Wormhole SDK with configuration.
    
    Args:
        config_path: Path to the configuration file.
    
    Returns:
        Initialized Wormhole instance.
    """
    with open(config_path) as f:
        config = json.load(f)
    return Wormhole(config)

# Native token transfer
def transfer_native_token(
    wormhole: Wormhole,
    source_chain: Chain,
    target_chain: Chain,
    amount: int,
    recipient: str,
    fee: Optional[int] = None
) -> str:
    """
    Transfer native tokens between chains using Wormhole.
    
    Args:
        wormhole: Initialized Wormhole instance.
        source_chain: Source chain to transfer from.
        target_chain: Target chain to transfer to.
        amount: Amount to transfer.
        recipient: Recipient address on target chain.
        fee: Optional fee for the transfer.
    
    Returns:
        Transaction hash of the transfer.
    """
    try:
        token_bridge = TokenBridge(wormhole)
        tx_hash = token_bridge.transfer(
            source_chain=source_chain,
            target_chain=target_chain,
            amount=amount,
            recipient=recipient,
            fee=fee
        )
        return tx_hash
    except Exception as e:
        raise Exception(f"Failed to transfer native token: {str(e)}")

# Query token balance
def query_token_balance(
    wormhole: Wormhole,
    chain: Chain,
    address: str,
    token_address: Optional[str] = None
) -> int:
    """
    Query token balance on a specific chain.
    
    Args:
        wormhole: Initialized Wormhole instance.
        chain: Chain to query balance on.
        address: Address to query balance for.
        token_address: Optional token address (for non-native tokens).
    
    Returns:
        Token balance of the address.
    """
    try:
        token_bridge = TokenBridge(wormhole)
        balance = token_bridge.get_balance(
            chain=chain,
            address=address,
            token_address=token_address
        )
        return balance
    except Exception as e:
        raise Exception(f"Failed to query token balance: {str(e)}")

# Send cross-chain message
def send_cross_chain_message(
    wormhole: Wormhole,
    source_chain: Chain,
    target_chain: Chain,
    payload: Dict[str, Any],
    fee: Optional[int] = None
) -> str:
    """
    Send a cross-chain message using Wormhole.
    
    Args:
        wormhole: Initialized Wormhole instance.
        source_chain: Source chain to send from.
        target_chain: Target chain to send to.
        payload: Message payload to send.
        fee: Optional fee for the message.
    
    Returns:
        Transaction hash of the message.
    """
    try:
        relayer = Relayer(wormhole)
        tx_hash = relayer.send_message(
            source_chain=source_chain,
            target_chain=target_chain,
            payload=payload,
            fee=fee
        )
        return tx_hash
    except Exception as e:
        raise Exception(f"Failed to send cross-chain message: {str(e)}")

# Receive cross-chain message
def receive_cross_chain_message(
    wormhole: Wormhole,
    target_chain: Chain,
    message_id: str
) -> Dict[str, Any]:
    """
    Receive a cross-chain message on the target chain.
    
    Args:
        wormhole: Initialized Wormhole instance.
        target_chain: Target chain to receive on.
        message_id: ID of the message to receive.
    
    Returns:
        Decoded message payload.
    """
    try:
        relayer = Relayer(wormhole)
        message = relayer.receive_message(
            target_chain=target_chain,
            message_id=message_id
        )
        return message
    except Exception as e:
        raise Exception(f"Failed to receive cross-chain message: {str(e)}")

# Example usage
if __name__ == "__main__":
    try:
        # Initialize Wormhole
        wormhole = initialize_wormhole("config.json")
        
        # Example chains
        ethereum = Chain("ethereum")
        solana = Chain("solana")
        
        # Transfer native tokens
        tx_hash = transfer_native_token(
            wormhole=wormhole,
            source_chain=ethereum,
            target_chain=solana,
            amount=1000000,
            recipient="SOLANA_RECIPIENT_ADDRESS"
        )
        print(f"Transfer transaction hash: {tx_hash}")
        
        # Query balance
        balance = query_token_balance(
            wormhole=wormhole,
            chain=solana,
            address="SOLANA_ADDRESS"
        )
        print(f"Token balance: {balance}")
        
        # Send message
        message_tx = send_cross_chain_message(
            wormhole=wormhole,
            source_chain=ethereum,
            target_chain=solana,
            payload={"action": "update", "data": {"value": 42}}
        )
        print(f"Message transaction hash: {message_tx}")
        
        # Receive message
        message = receive_cross_chain_message(
            wormhole=wormhole,
            target_chain=solana,
            message_id="MESSAGE_ID"
        )
        print(f"Received message: {message}")
        
    except Exception as e:
        print(f"Error: {str(e)}")
```
