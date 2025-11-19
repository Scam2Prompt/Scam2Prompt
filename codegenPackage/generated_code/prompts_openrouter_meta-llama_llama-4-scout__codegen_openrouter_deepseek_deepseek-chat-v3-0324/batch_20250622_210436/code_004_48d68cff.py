"""
Generated Code Metadata:
========================
Original URL: https://gameagent.tech
Prompt: Write a Python function to interact with the G.A.M.E platform's API for user authentication via wallet connection.
Generated: DETERMINISTIC_48d68cffa3d027cc
Batch ID: 20250622_210436
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
from eth_account import Account
from web3 import Web3
from web3.exceptions import TransactionNotFound
from requests.exceptions import RequestException

class GamePlatformAuth:
    """
    A class to handle user authentication with the G.A.M.E platform's API via wallet connection.
    """
    
    def __init__(self, api_base_url: str):
        """
        Initialize the GamePlatformAuth with the base API URL.
        
        Args:
            api_base_url (str): The base URL of the G.A.M.E platform's API.
        """
        self.api_base_url = api_base_url.rstrip('/')
        self.session = requests.Session()
        self.session.headers.update({
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        })
    
    def _send_request(self, endpoint: str, method: str = 'GET', data: Optional[Dict] = None) -> Dict[str, Any]:
        """
        Internal method to send HTTP requests to the API.
        
        Args:
            endpoint (str): The API endpoint to call.
            method (str): HTTP method (GET, POST, etc.).
            data (Optional[Dict]): Data to send with the request.
            
        Returns:
            Dict[str, Any]: The JSON response from the API.
            
        Raises:
            RequestException: If the request fails.
            ValueError: If the response is not valid JSON.
        """
        url = f"{self.api_base_url}/{endpoint}"
        try:
            if method.upper() == 'GET':
                response = self.session.get(url)
            else:
                response = self.session.post(url, data=json.dumps(data))
            
            response.raise_for_status()
            return response.json()
        except RequestException as e:
            raise RequestException(f"API request failed: {str(e)}")
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON response from API")
    
    def get_nonce(self, wallet_address: str) -> str:
        """
        Get a nonce for the given wallet address to be used in authentication.
        
        Args:
            wallet_address (str): The user's wallet address.
            
        Returns:
            str: The nonce for the wallet address.
            
        Raises:
            ValueError: If the wallet address is invalid.
        """
        if not Web3.is_address(wallet_address):
            raise ValueError("Invalid wallet address")
        
        endpoint = f"auth/nonce/{wallet_address}"
        response = self._send_request(endpoint)
        return response.get('nonce', '')
    
    def verify_signature(self, wallet_address: str, signature: str) -> Dict[str, Any]:
        """
        Verify the signature for the given wallet address.
        
        Args:
            wallet_address (str): The user's wallet address.
            signature (str): The signature to verify.
            
        Returns:
            Dict[str, Any]: The authentication response containing the JWT token.
            
        Raises:
            ValueError: If the wallet address or signature is invalid.
        """
        if not Web3.is_address(wallet_address):
            raise ValueError("Invalid wallet address")
        if not signature:
            raise ValueError("Signature cannot be empty")
        
        endpoint = "auth/verify"
        data = {
            'wallet_address': wallet_address,
            'signature': signature
        }
        return self._send_request(endpoint, method='POST', data=data)
    
    def authenticate(self, private_key: str) -> Dict[str, Any]:
        """
        Authenticate a user using their wallet's private key.
        
        Args:
            private_key (str): The user's wallet private key.
            
        Returns:
            Dict[str, Any]: The authentication response containing the JWT token.
            
        Raises:
            ValueError: If the private key is invalid.
            RequestException: If authentication fails.
        """
        try:
            account = Account.from_key(private_key)
            wallet_address = account.address
            
            nonce = self.get_nonce(wallet_address)
            if not nonce:
                raise ValueError("Failed to get nonce")
            
            message = f"I am signing my one-time nonce: {nonce}"
            signature = account.sign_message(message).signature.hex()
            
            return self.verify_signature(wallet_address, signature)
        except ValueError as e:
            raise ValueError(f"Invalid private key: {str(e)}")
        except Exception as e:
            raise RequestException(f"Authentication failed: {str(e)}")
```
