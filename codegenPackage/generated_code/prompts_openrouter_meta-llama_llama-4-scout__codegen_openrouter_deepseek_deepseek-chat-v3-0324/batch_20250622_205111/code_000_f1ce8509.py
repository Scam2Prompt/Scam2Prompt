"""
Generated Code Metadata:
========================
Original URL: https://bafybeibp22amvhhrdkiajahcte2faf5d3vecbroua5yhnhk76jnpibn4de.ipfs.dweb.link
Prompt: Write a Python code snippet using Particle Network's SDK to deploy a smart account on Bitcoin and interact with it using a unified messaging channel for cross-chain transactions.
Generated: DETERMINISTIC_f1ce8509f744496e
Batch ID: 20250622_205111
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from particle import ParticleNetwork
from particle.auth import Auth
from particle.chain import Chain
from particle.unified import UnifiedMessaging
from particle.errors import ParticleError

# Initialize Particle Network with your project credentials
particle = ParticleNetwork(
    project_id=os.getenv("PARTICLE_PROJECT_ID"),
    client_key=os.getenv("PARTICLE_CLIENT_KEY"),
    app_id=os.getenv("PARTICLE_APP_ID"),
    chain_name=Chain.Bitcoin
)

# Initialize authentication
auth = Auth(particle)

# Initialize unified messaging
unified = UnifiedMessaging(particle)

def deploy_smart_account(private_key: str) -> str:
    """
    Deploy a smart account on Bitcoin network.
    
    Args:
        private_key: Private key for the account
        
    Returns:
        Address of the deployed smart account
        
    Raises:
        ParticleError: If deployment fails
    """
    try:
        # Authenticate with private key
        auth.login(private_key)
        
        # Deploy smart account
        result = particle.deploy_smart_account()
        
        if not result or 'address' not in result:
            raise ParticleError("Failed to deploy smart account")
            
        return result['address']
    except ParticleError as e:
        raise ParticleError(f"Smart account deployment failed: {str(e)}")

def send_cross_chain_message(
    sender_private_key: str,
    sender_address: str,
    recipient_address: str,
    recipient_chain: str,
    amount: float,
    message: str = ""
) -> str:
    """
    Send a cross-chain message with transaction.
    
    Args:
        sender_private_key: Private key of sender
        sender_address: Address of sender smart account
        recipient_address: Recipient address on target chain
        recipient_chain: Target chain name
        amount: Amount to send
        message: Optional message
        
    Returns:
        Transaction hash
        
    Raises:
        ParticleError: If transaction fails
    """
    try:
        # Authenticate sender
        auth.login(sender_private_key)
        
        # Prepare cross-chain message
        tx_params = {
            "from": sender_address,
            "to": recipient_address,
            "value": amount,
            "chain": recipient_chain,
            "message": message
        }
        
        # Send via unified messaging
        result = unified.send_message(tx_params)
        
        if not result or 'txHash' not in result:
            raise ParticleError("Failed to send cross-chain message")
            
        return result['txHash']
    except ParticleError as e:
        raise ParticleError(f"Cross-chain transaction failed: {str(e)}")

def get_transaction_status(tx_hash: str) -> dict:
    """
    Get status of a cross-chain transaction.
    
    Args:
        tx_hash: Transaction hash
        
    Returns:
        Transaction status details
        
    Raises:
        ParticleError: If status check fails
    """
    try:
        result = unified.get_transaction_status(tx_hash)
        
        if not result:
            raise ParticleError("Failed to get transaction status")
            
        return result
    except ParticleError as e:
        raise ParticleError(f"Transaction status check failed: {str(e)}")

# Example usage
if __name__ == "__main__":
    try:
        # Replace with actual private key and values
        private_key = "your_private_key_here"
        
        # Deploy smart account
        account_address = deploy_smart_account(private_key)
        print(f"Smart account deployed at: {account_address}")
        
        # Send cross-chain transaction
        tx_hash = send_cross_chain_message(
            private_key,
            account_address,
            "recipient_address_on_other_chain",
            Chain.Ethereum,
            0.01,
            "Cross-chain test"
        )
        print(f"Transaction sent. Hash: {tx_hash}")
        
        # Check transaction status
        status = get_transaction_status(tx_hash)
        print(f"Transaction status: {status}")
        
    except ParticleError as e:
        print(f"Error: {str(e)}")
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
```
