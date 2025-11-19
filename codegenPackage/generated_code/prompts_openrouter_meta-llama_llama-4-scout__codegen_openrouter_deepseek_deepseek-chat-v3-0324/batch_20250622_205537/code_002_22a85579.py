"""
Generated Code Metadata:
========================
Original URL: https://enigmatoken.com
Prompt: Generate a Python script to interact with the ENIGMA Token presale API, assuming it uses RESTful API endpoints.
Generated: DETERMINISTIC_22a855798506548a
Batch ID: 20250622_205537
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
from typing import Optional, Dict, Any

class EnigmaTokenPresaleAPI:
    """
    A client for interacting with the ENIGMA Token presale RESTful API.
    Handles authentication, requests, and responses.
    """

    def __init__(self, base_url: str, api_key: Optional[str] = None):
        """
        Initialize the API client.
        
        Args:
            base_url: The base URL of the ENIGMA Token presale API
            api_key: Optional API key for authenticated endpoints
        """
        self.base_url = base_url.rstrip('/')
        self.api_key = api_key
        self.session = requests.Session()
        self.session.headers.update({
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        })
        if api_key:
            self.session.headers.update({'Authorization': f'Bearer {api_key}'})

    def _make_request(
        self,
        method: str,
        endpoint: str,
        params: Optional[Dict[str, Any]] = None,
        data: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Internal method to make API requests with error handling.
        
        Args:
            method: HTTP method (GET, POST, etc.)
            endpoint: API endpoint path
            params: Optional query parameters
            data: Optional request body data
            
        Returns:
            Dictionary containing the API response
            
        Raises:
            ValueError: If the request fails or returns an error
        """
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        try:
            response = self.session.request(
                method=method,
                url=url,
                params=params,
                json=data
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            try:
                error_data = response.json()
                raise ValueError(f"API Error: {error_data.get('message', str(http_err))}")
            except json.JSONDecodeError:
                raise ValueError(f"HTTP Error: {str(http_err)}")
        except requests.exceptions.RequestException as err:
            raise ValueError(f"Request failed: {str(err)}")

    def get_presale_info(self) -> Dict[str, Any]:
        """
        Get information about the current presale.
        
        Returns:
            Dictionary containing presale information
        """
        return self._make_request('GET', '/api/presale/info')

    def get_user_contribution(self, user_address: str) -> Dict[str, Any]:
        """
        Get contribution information for a specific user.
        
        Args:
            user_address: The user's wallet address
            
        Returns:
            Dictionary containing user contribution details
        """
        return self._make_request(
            'GET',
            f'/api/presale/contributions/{user_address}'
        )

    def submit_contribution(
        self,
        user_address: str,
        amount: float,
        transaction_hash: str
    ) -> Dict[str, Any]:
        """
        Submit a new contribution to the presale.
        
        Args:
            user_address: The user's wallet address
            amount: The contribution amount
            transaction_hash: The transaction hash of the contribution
            
        Returns:
            Dictionary containing the submission result
        """
        if not self.api_key:
            raise ValueError("API key is required for this operation")
            
        return self._make_request(
            'POST',
            '/api/presale/contribute',
            data={
                'user_address': user_address,
                'amount': amount,
                'transaction_hash': transaction_hash
            }
        )

    def get_presale_stats(self) -> Dict[str, Any]:
        """
        Get statistics about the presale.
        
        Returns:
            Dictionary containing presale statistics
        """
        return self._make_request('GET', '/api/presale/stats')

    def get_whitelist_status(self, user_address: str) -> Dict[str, Any]:
        """
        Check if a user is whitelisted for the presale.
        
        Args:
            user_address: The user's wallet address
            
        Returns:
            Dictionary containing whitelist status
        """
        return self._make_request(
            'GET',
            f'/api/presale/whitelist/{user_address}'
        )
```
