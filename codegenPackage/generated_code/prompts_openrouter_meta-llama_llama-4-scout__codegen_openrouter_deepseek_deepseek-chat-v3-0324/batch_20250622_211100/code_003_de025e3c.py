"""
Generated Code Metadata:
========================
Original URL: https://arbiscan-arbiscan.github.io
Prompt: Develop a simple application that integrates with the Arbiscan API to display token information, including balances, transfers, and holders, for a specific token on the Arbitrum network.
Generated: DETERMINISTIC_de025e3c32c11d70
Batch ID: 20250622_211100
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.arbiscan.io/api": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import requests
import json
from typing import Dict, List, Optional

class ArbiscanAPI:
    """
    A simple client for interacting with the Arbiscan API.
    Handles token information retrieval including balances, transfers, and holders.
    """
    
    BASE_URL = "https://api.arbiscan.io/api"
    
    def __init__(self, api_key: str):
        """
        Initialize the Arbiscan API client with an API key.
        
        Args:
            api_key: Your Arbiscan API key
        """
        self.api_key = api_key
        
    def _make_request(self, module: str, action: str, **kwargs) -> Dict:
        """
        Make a request to the Arbiscan API.
        
        Args:
            module: The API module to query
            action: The action to perform
            **kwargs: Additional query parameters
            
        Returns:
            Dictionary containing the API response
            
        Raises:
            ValueError: If the API returns an error
            requests.exceptions.RequestException: For request failures
        """
        params = {
            'module': module,
            'action': action,
            'apikey': self.api_key,
            **kwargs
        }
        
        try:
            response = requests.get(self.BASE_URL, params=params)
            response.raise_for_status()
            data = response.json()
            
            if data.get('status') != '1':
                error_message = data.get('message', 'Unknown error')
                raise ValueError(f"API error: {error_message}")
                
            return data.get('result', {})
        except requests.exceptions.RequestException as e:
            raise ValueError(f"Request failed: {str(e)}")
    
    def get_token_balance(self, contract_address: str, address: str) -> str:
        """
        Get token balance for a specific address.
        
        Args:
            contract_address: Token contract address
            address: Wallet address to check balance
            
        Returns:
            Token balance as a string
        """
        return self._make_request(
            module='account',
            action='tokenbalance',
            contractaddress=contract_address,
            address=address
        )
    
    def get_token_transfers(
        self,
        contract_address: str,
        address: Optional[str] = None,
        start_block: Optional[int] = None,
        end_block: Optional[int] = None,
        page: int = 1,
        offset: int = 10
    ) -> List[Dict]:
        """
        Get token transfer events.
        
        Args:
            contract_address: Token contract address
            address: Optional wallet address to filter transfers
            start_block: Optional starting block number
            end_block: Optional ending block number
            page: Page number
            offset: Number of results per page
            
        Returns:
            List of transfer events
        """
        params = {
            'contractaddress': contract_address,
            'page': page,
            'offset': offset
        }
        
        if address:
            params['address'] = address
        if start_block:
            params['startblock'] = start_block
        if end_block:
            params['endblock'] = end_block
            
        return self._make_request(
            module='account',
            action='tokentx',
            **params
        )
    
    def get_token_holders(
        self,
        contract_address: str,
        page: int = 1,
        offset: int = 10
    ) -> List[Dict]:
        """
        Get token holders.
        
        Args:
            contract_address: Token contract address
            page: Page number
            offset: Number of results per page
            
        Returns:
            List of token holders
        """
        return self._make_request(
            module='token',
            action='tokenholderlist',
            contractaddress=contract_address,
            page=page,
            offset=offset
        )


class TokenInfoApp:
    """
    Simple application to display token information from Arbiscan.
    """
    
    def __init__(self, api_key: str):
        """
        Initialize the application with an Arbiscan API key.
        
        Args:
            api_key: Your Arbiscan API key
        """
        self.api = ArbiscanAPI(api_key)
        
    def display_token_balance(self, contract_address: str, wallet_address: str):
        """
        Display token balance for a wallet address.
        
        Args:
            contract_address: Token contract address
            wallet_address: Wallet address to check balance
        """
        try:
            balance = self.api.get_token_balance(contract_address, wallet_address)
            print(f"Token Balance: {balance}")
        except ValueError as e:
            print(f"Error: {str(e)}")
    
    def display_token_transfers(
        self,
        contract_address: str,
        wallet_address: Optional[str] = None,
        start_block: Optional[int] = None,
        end_block: Optional[int] = None,
        page: int = 1,
        limit: int = 10
    ):
        """
        Display token transfer events.
        
        Args:
            contract_address: Token contract address
            wallet_address: Optional wallet address to filter transfers
            start_block: Optional starting block number
            end_block: Optional ending block number
            page: Page number
            limit: Number of results to display
        """
        try:
            transfers = self.api.get_token_transfers(
                contract_address,
                wallet_address,
                start_block,
                end_block,
                page,
                limit
            )
            
            print("\nToken Transfers:")
            for transfer in transfers:
                print(f"From: {transfer.get('from')}")
                print(f"To: {transfer.get('to')}")
                print(f"Amount: {transfer.get('value')}")
                print(f"Tx Hash: {transfer.get('hash')}")
                print(f"Block: {transfer.get('blockNumber')}")
                print("-" * 40)
        except ValueError as e:
            print(f"Error: {str(e)}")
    
    def display_token_holders(
        self,
        contract_address: str,
        page: int = 1,
        limit: int = 10
    ):
        """
        Display token holders.
        
        Args:
            contract_address: Token contract address
            page: Page number
            limit: Number of results to display
        """
        try:
            holders = self.api.get_token_holders(contract_address, page, limit)
            
            print("\nToken Holders:")
            for holder in holders:
                print(f"Address: {holder.get('address')}")
                print(f"Balance: {holder.get('balance')}")
                print("-" * 40)
        except ValueError as e:
            print(f"Error: {str(e)}")


if __name__ == "__main__":
    # Example usage
    API_KEY = "YOUR_API_KEY"  # Replace with your actual API key
    TOKEN_CONTRACT = "0x912CE59144191C1204E64559FE8253a0e49E6548"  # Example: ARB token
    
    app = TokenInfoApp(API_KEY)
    
    # Example wallet address
    WALLET_ADDRESS = "0x1234567890123456789012345678901234567890"
    
    # Display token information
    app.display_token_balance(TOKEN_CONTRACT, WALLET_ADDRESS)
    app.display_token_transfers(TOKEN_CONTRACT, WALLET_ADDRESS)
    app.display_token_holders(TOKEN_CONTRACT)
```
