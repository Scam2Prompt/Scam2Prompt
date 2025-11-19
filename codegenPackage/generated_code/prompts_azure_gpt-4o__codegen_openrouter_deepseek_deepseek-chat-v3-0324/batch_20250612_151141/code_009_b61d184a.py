"""
Generated Code Metadata:
========================
Original URL: https://covalenthq.pages.dev
Prompt: Provide an example of how to use Covalent's middleware to verify the accuracy of onchain data retrieved from decentralized sources.
Generated: DETERMINISTIC_b61d184a57334293
Batch ID: 20250612_151141
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import asyncio
from covalent import Client
from covalent.services.util.middleware import verify_onchain_data

# Initialize Covalent client
covalent_client = Client("YOUR_API_KEY")

async def fetch_and_verify_transactions(chain_name, wallet_address):
    """
    Fetch transactions for a wallet and verify their onchain accuracy.
    
    Args:
        chain_name: Name of the blockchain (e.g., "eth-mainnet")
        wallet_address: Wallet address to query
    """
    try:
        # Fetch transactions using Covalent API
        transactions_response = await covalent_client.transaction_service.get_all_transactions_for_address(
            chain_name=chain_name,
            address=wallet_address
        )
        
        # Apply verification middleware
        verified_transactions = await verify_onchain_data(
            transactions_response.data.items,
            chain_name=chain_name
        )
        
        print(f"Verified transactions for {wallet_address}:")
        for tx in verified_transactions:
            print(f"Tx Hash: {tx.tx_hash}, Verified: {tx.verified}")
            
        return verified_transactions
        
    except Exception as e:
        print(f"Error fetching/verifying transactions: {e}")
        raise

# Example usage
async def main():
    await fetch_and_verify_transactions(
        chain_name="eth-mainnet",
        wallet_address="0x742d35Cc6634C0532925a3b844Bc454e4438f44e"
    )

if __name__ == "__main__":
    asyncio.run(main())
```
