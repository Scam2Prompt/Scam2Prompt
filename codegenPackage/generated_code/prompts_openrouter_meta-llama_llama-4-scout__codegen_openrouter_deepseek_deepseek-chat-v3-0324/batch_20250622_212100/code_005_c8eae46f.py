"""
Generated Code Metadata:
========================
Original URL: https://monad-6j5.pages.dev
Prompt: Create a script to automate the process of getting testnet tokens on Monad Testnet using the faucet and Discord role verification.
Generated: DETERMINISTIC_c8eae46f96e5b257
Batch ID: 20250622_212100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import requests
import time
import json
import os
from typing import Optional, Dict, Any

class MonadFaucetAutomator:
    """
    Automates the process of getting testnet tokens on Monad Testnet.
    Handles faucet requests and Discord role verification.
    """

    def __init__(self, config_path: str = "config.json"):
        """
        Initialize the automator with configuration.
        
        Args:
            config_path: Path to the configuration file.
        """
        self.config = self._load_config(config_path)
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "MonadFaucetAutomator/1.0",
            "Content-Type": "application/json"
        })

    def _load_config(self, config_path: str) -> Dict[str, Any]:
        """
        Load configuration from JSON file.
        
        Args:
            config_path: Path to the config file.
            
        Returns:
            Loaded configuration as dictionary.
            
        Raises:
            FileNotFoundError: If config file doesn't exist.
            json.JSONDecodeError: If config file is malformed.
        """
        try:
            with open(config_path) as f:
                return json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"Config file not found at {config_path}")
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(f"Invalid JSON in config file: {e}", e.doc, e.pos)

    def _make_request(self, url: str, method: str = "GET", data: Optional[Dict] = None) -> Dict:
        """
        Make HTTP request with error handling.
        
        Args:
            url: URL to request.
            method: HTTP method (GET, POST).
            data: Optional payload for POST requests.
            
        Returns:
            JSON response as dictionary.
            
        Raises:
            requests.RequestException: On request failure.
            ValueError: On invalid JSON response.
        """
        try:
            if method.upper() == "GET":
                response = self.session.get(url)
            else:
                response = self.session.post(url, json=data)
            
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            raise requests.RequestException(f"Request failed: {e}")
        except ValueError as e:
            raise ValueError(f"Invalid JSON response: {e}")

    def verify_discord_role(self, discord_id: str) -> bool:
        """
        Verify if user has required Discord role.
        
        Args:
            discord_id: User's Discord ID.
            
        Returns:
            True if role is verified, False otherwise.
            
        Raises:
            requests.RequestException: On request failure.
        """
        url = f"{self.config['discord_api_url']}/verify"
        data = {
            "discord_id": discord_id,
            "role_id": self.config["required_role_id"]
        }
        
        try:
            response = self._make_request(url, "POST", data)
            return response.get("success", False)
        except requests.RequestException as e:
            raise requests.RequestException(f"Discord verification failed: {e}")

    def request_faucet_tokens(self, wallet_address: str) -> Dict:
        """
        Request testnet tokens from faucet.
        
        Args:
            wallet_address: Wallet address to receive tokens.
            
        Returns:
            Faucet response dictionary.
            
        Raises:
            requests.RequestException: On request failure.
        """
        url = f"{self.config['faucet_url']}/request"
        data = {
            "address": wallet_address,
            "network": "monad-testnet"
        }
        
        try:
            return self._make_request(url, "POST", data)
        except requests.RequestException as e:
            raise requests.RequestException(f"Faucet request failed: {e}")

    def run(self, discord_id: str, wallet_address: str) -> Dict:
        """
        Main execution flow:
        1. Verify Discord role
        2. Request faucet tokens
        
        Args:
            discord_id: User's Discord ID.
            wallet_address: Wallet address to receive tokens.
            
        Returns:
            Dictionary with results of operations.
            
        Raises:
            Exception: If any step fails.
        """
        result = {
            "discord_verified": False,
            "faucet_success": False,
            "tx_hash": None,
            "error": None
        }
        
        try:
            # Verify Discord role
            if not self.verify_discord_role(discord_id):
                raise Exception("Discord role verification failed")
            result["discord_verified"] = True
            
            # Request tokens from faucet
            faucet_response = self.request_faucet_tokens(wallet_address)
            if not faucet_response.get("success", False):
                raise Exception(f"Faucet error: {faucet_response.get('error', 'Unknown error')}")
            
            result["faucet_success"] = True
            result["tx_hash"] = faucet_response.get("tx_hash")
            
        except Exception as e:
            result["error"] = str(e)
        
        return result

if __name__ == "__main__":
    try:
        automator = MonadFaucetAutomator()
        
        # Get user input
        discord_id = input("Enter your Discord ID: ").strip()
        wallet_address = input("Enter your Monad wallet address: ").strip()
        
        # Run automation
        print("Processing request...")
        result = automator.run(discord_id, wallet_address)
        
        # Display results
        if result["error"]:
            print(f"Error: {result['error']}")
        else:
            print("Success!")
            print(f"Discord verified: {'Yes' if result['discord_verified'] else 'No'}")
            print(f"Tokens sent: {'Yes' if result['faucet_success'] else 'No'}")
            if result["tx_hash"]:
                print(f"Transaction hash: {result['tx_hash']}")
                
    except Exception as e:
        print(f"Fatal error: {e}")
```
