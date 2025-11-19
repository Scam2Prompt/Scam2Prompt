"""
Generated Code Metadata:
========================
Original URL: https://www.staderlabs.fi
Prompt: Write a Python code snippet to interact with Stader Labs' API for liquid staking on Ethereum, including functions to stake ETH and retrieve staking rewards.
Generated: DETERMINISTIC_b31c47019560cc6a
Batch ID: 20250622_211123
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import requests
import json
from typing import Dict, Optional, Union
from decimal import Decimal

class StaderLabsAPI:
    """
    A Python client for interacting with Stader Labs' API for liquid staking on Ethereum.
    Handles staking ETH and retrieving staking rewards.
    """

    def __init__(self, base_url: str, api_key: Optional[str] = None):
        """
        Initialize the StaderLabsAPI client.

        Args:
            base_url (str): Base URL for the Stader Labs API.
            api_key (str, optional): API key for authenticated endpoints. Defaults to None.
        """
        self.base_url = base_url.rstrip('/')
        self.api_key = api_key
        self.session = requests.Session()
        self.session.headers.update({
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        })
        if self.api_key:
            self.session.headers.update({'Authorization': f'Bearer {self.api_key}'})

    def _make_request(
        self,
        method: str,
        endpoint: str,
        params: Optional[Dict] = None,
        data: Optional[Dict] = None
    ) -> Union[Dict, list]:
        """
        Internal method to make HTTP requests to the Stader Labs API.

        Args:
            method (str): HTTP method (GET, POST, etc.).
            endpoint (str): API endpoint.
            params (dict, optional): Query parameters. Defaults to None.
            data (dict, optional): Request body. Defaults to None.

        Returns:
            Union[Dict, list]: JSON response from the API.

        Raises:
            ValueError: If the request fails or returns an error.
        """
        url = f"{self.base_url}/{endpoint}"
        try:
            response = self.session.request(
                method,
                url,
                params=params,
                json=data,
                timeout=30
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise ValueError(f"API request failed: {str(e)}") from e

    def stake_eth(self, amount: Union[Decimal, str, int], wallet_address: str) -> Dict:
        """
        Stake ETH to receive liquid staking tokens.

        Args:
            amount (Union[Decimal, str, int]): Amount of ETH to stake.
            wallet_address (str): Ethereum wallet address to stake from.

        Returns:
            Dict: Response from the API including transaction details.
        """
        if isinstance(amount, (str, int)):
            amount = Decimal(str(amount))
        
        if amount <= Decimal('0'):
            raise ValueError("Amount must be greater than 0")

        endpoint = "stake"
        data = {
            "amount": str(amount),
            "wallet_address": wallet_address
        }
        return self._make_request("POST", endpoint, data=data)

    def get_staking_rewards(self, wallet_address: str) -> Dict:
        """
        Retrieve staking rewards for a given wallet address.

        Args:
            wallet_address (str): Ethereum wallet address to query rewards for.

        Returns:
            Dict: Response from the API including rewards details.
        """
        endpoint = f"rewards/{wallet_address}"
        return self._make_request("GET", endpoint)

    def get_staking_balance(self, wallet_address: str) -> Dict:
        """
        Retrieve staking balance for a given wallet address.

        Args:
            wallet_address (str): Ethereum wallet address to query balance for.

        Returns:
            Dict: Response from the API including balance details.
        """
        endpoint = f"balance/{wallet_address}"
        return self._make_request("GET", endpoint)

    def close(self):
        """Close the HTTP session."""
        self.session.close()

    def __enter__(self):
        """Support for context manager protocol."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Support for context manager protocol."""
        self.close()
```
