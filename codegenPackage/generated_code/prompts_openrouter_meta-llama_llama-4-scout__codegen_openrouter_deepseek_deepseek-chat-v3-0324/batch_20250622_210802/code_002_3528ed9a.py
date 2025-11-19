"""
Generated Code Metadata:
========================
Original URL: https://wallet-pi-nine.vercel.app
Prompt: Generate a function to calculate the total balance of a user's wallet, including available, delegated, rewards claimable, and undelegating balances, as shown on the webpage.
Generated: DETERMINISTIC_3528ed9a837f083d
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import requests
from typing import Dict, Union, Optional

class WalletBalanceCalculator:
    """
    Calculates the total balance of a user's wallet by summing available, delegated,
    rewards claimable, and undelegating balances from a blockchain API.
    """
    
    def __init__(self, api_url: str):
        """
        Initialize the calculator with the base API URL.
        
        Args:
            api_url: Base URL of the blockchain API
        """
        self.api_url = api_url.rstrip('/')
    
    def _make_api_request(self, endpoint: str) -> Optional[Dict]:
        """
        Make a GET request to the specified API endpoint.
        
        Args:
            endpoint: API endpoint to query
            
        Returns:
            JSON response as dictionary or None if request fails
        """
        try:
            response = requests.get(f"{self.api_url}/{endpoint}", timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"API request failed: {e}")
            return None
    
    def get_wallet_balance(self, wallet_address: str) -> Union[float, None]:
        """
        Calculate the total wallet balance by summing all balance components.
        
        Args:
            wallet_address: Address of the wallet to query
            
        Returns:
            Total balance in native tokens or None if calculation fails
        """
        # Get available balance
        available_balance = self._get_available_balance(wallet_address)
        if available_balance is None:
            return None
        
        # Get delegated balance
        delegated_balance = self._get_delegated_balance(wallet_address)
        if delegated_balance is None:
            return None
        
        # Get claimable rewards
        rewards_balance = self._get_rewards_balance(wallet_address)
        if rewards_balance is None:
            return None
        
        # Get undelegating balance
        undelegating_balance = self._get_undelegating_balance(wallet_address)
        if undelegating_balance is None:
            return None
        
        total_balance = (
            available_balance +
            delegated_balance +
            rewards_balance +
            undelegating_balance
        )
        
        return total_balance
    
    def _get_available_balance(self, wallet_address: str) -> Union[float, None]:
        """Get the available balance from the wallet."""
        endpoint = f"accounts/{wallet_address}/balance"
        response = self._make_api_request(endpoint)
        return float(response['balance']) if response else None
    
    def _get_delegated_balance(self, wallet_address: str) -> Union[float, None]:
        """Get the total delegated balance from the wallet."""
        endpoint = f"accounts/{wallet_address}/delegations"
        response = self._make_api_request(endpoint)
        if not response:
            return None
        return sum(float(d['amount']) for d in response['delegations'])
    
    def _get_rewards_balance(self, wallet_address: str) -> Union[float, None]:
        """Get the total claimable rewards from the wallet."""
        endpoint = f"accounts/{wallet_address}/rewards"
        response = self._make_api_request(endpoint)
        if not response:
            return None
        return sum(float(r['amount']) for r in response['rewards'])
    
    def _get_undelegating_balance(self, wallet_address: str) -> Union[float, None]:
        """Get the total undelegating balance from the wallet."""
        endpoint = f"accounts/{wallet_address}/undelegations"
        response = self._make_api_request(endpoint)
        if not response:
            return None
        return sum(float(u['amount']) for u in response['undelegations'])
```
