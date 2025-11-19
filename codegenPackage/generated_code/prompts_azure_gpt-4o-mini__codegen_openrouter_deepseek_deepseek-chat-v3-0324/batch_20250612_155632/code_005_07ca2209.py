"""
Generated Code Metadata:
========================
Original URL: https://app-chainbase.com
Prompt: Provide an example of how to programmatically access omnichain data using Chainbase's SDK in Python.
Generated: DETERMINISTIC_07ca220934f05e62
Batch ID: 20250612_155632
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from chainbase_sdk import ChainbaseClient
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class ChainbaseDataAccessor:
    """
    A class to interact with Chainbase API for accessing omnichain data.
    """
    
    def __init__(self):
        """
        Initialize the Chainbase client with API key from environment variables.
        """
        api_key = os.getenv('CHAINBASE_API_KEY')
        if not api_key:
            raise ValueError("CHAINBASE_API_KEY not found in environment variables")
        
        self.client = ChainbaseClient(api_key)
    
    def get_token_transfers(self, contract_address: str, chain_id: str, limit: int = 100):
        """
        Get token transfers for a specific contract address and chain.
        
        Args:
            contract_address (str): The token contract address
            chain_id (str): The chain ID (e.g., '1' for Ethereum)
            limit (int): Maximum number of records to return
            
        Returns:
            dict: Response data from Chainbase API
        """
        try:
            response = self.client.get(
                '/v1/token/transfers',
                params={
                    'contract_address': contract_address,
                    'chain_id': chain_id,
                    'limit': limit
                }
            )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error fetching token transfers: {e}")
            return None
    
    def get_nft_holders(self, contract_address: str, chain_id: str):
        """
        Get NFT holders for a specific contract address and chain.
        
        Args:
            contract_address (str): The NFT contract address
            chain_id (str): The chain ID
            
        Returns:
            dict: Response data from Chainbase API
        """
        try:
            response = self.client.get(
                '/v1/nft/holders',
                params={
                    'contract_address': contract_address,
                    'chain_id': chain_id
                }
            )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error fetching NFT holders: {e}")
            return None

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the data accessor
        accessor = ChainbaseDataAccessor()
        
        # Example: Get token transfers for USDT on Ethereum
        usdt_transfers = accessor.get_token_transfers(
            contract_address="0xdac17f958d2ee523a2206206994597c13d831ec7",
            chain_id="1",
            limit=10
        )
        print("USDT Transfers:", usdt_transfers)
        
        # Example: Get BAYC NFT holders
        bayc_holders = accessor.get_nft_holders(
            contract_address="0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D",
            chain_id="1"
        )
        print("BAYC Holders:", bayc_holders)
        
    except Exception as e:
        print(f"Error in main execution: {e}")
```
