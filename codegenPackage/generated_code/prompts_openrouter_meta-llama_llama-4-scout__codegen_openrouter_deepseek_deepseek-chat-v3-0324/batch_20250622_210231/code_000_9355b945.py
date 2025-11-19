"""
Generated Code Metadata:
========================
Original URL: https://aperture-finance.pages.dev
Prompt: Write a Python code snippet using Aperture Finance's API to create a declarative strategy for automating DeFi transactions based on user-defined intents.
Generated: DETERMINISTIC_9355b945fc93eb1a
Batch ID: 20250622_210231
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.aperture.finance": {
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
from datetime import datetime

class ApertureFinanceAPI:
    """
    A class to interact with Aperture Finance's API for creating declarative strategies.
    """

    def __init__(self, api_key: str, base_url: str = "https://api.aperture.finance"):
        """
        Initialize the API client with an API key and base URL.
        
        Args:
            api_key: Your Aperture Finance API key
            base_url: Base URL for the API (default: production)
        """
        self.api_key = api_key
        self.base_url = base_url
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

    def _make_request(self, method: str, endpoint: str, payload: Optional[Dict] = None) -> Dict:
        """
        Internal method to make API requests with error handling.
        
        Args:
            method: HTTP method (GET, POST, etc.)
            endpoint: API endpoint
            payload: Request payload (optional)
            
        Returns:
            Dictionary containing the API response
            
        Raises:
            ValueError: If request fails
        """
        url = f"{self.base_url}{endpoint}"
        try:
            response = requests.request(
                method,
                url,
                headers=self.headers,
                json=payload
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            raise ValueError(f"HTTP error occurred: {http_err}")
        except Exception as err:
            raise ValueError(f"Other error occurred: {err}")

    def create_strategy(
        self,
        name: str,
        description: str,
        intents: List[Dict],
        chain_id: int,
        wallet_address: str,
        active: bool = True
    ) -> Dict:
        """
        Create a new declarative strategy.
        
        Args:
            name: Strategy name
            description: Strategy description
            intents: List of intent objects defining the strategy
            chain_id: Blockchain network ID
            wallet_address: User's wallet address
            active: Whether strategy should be active (default: True)
            
        Returns:
            Dictionary containing the created strategy details
        """
        endpoint = "/v1/strategies"
        payload = {
            "name": name,
            "description": description,
            "intents": intents,
            "chain_id": chain_id,
            "wallet_address": wallet_address,
            "active": active,
            "created_at": datetime.utcnow().isoformat()
        }
        return self._make_request("POST", endpoint, payload)

    def get_strategy(self, strategy_id: str) -> Dict:
        """
        Get details of a specific strategy.
        
        Args:
            strategy_id: ID of the strategy to retrieve
            
        Returns:
            Dictionary containing strategy details
        """
        endpoint = f"/v1/strategies/{strategy_id}"
        return self._make_request("GET", endpoint)

    def update_strategy(
        self,
        strategy_id: str,
        name: Optional[str] = None,
        description: Optional[str] = None,
        intents: Optional[List[Dict]] = None,
        active: Optional[bool] = None
    ) -> Dict:
        """
        Update an existing strategy.
        
        Args:
            strategy_id: ID of the strategy to update
            name: New strategy name (optional)
            description: New description (optional)
            intents: New list of intents (optional)
            active: New active status (optional)
            
        Returns:
            Dictionary containing updated strategy details
        """
        endpoint = f"/v1/strategies/{strategy_id}"
        payload = {}
        if name is not None:
            payload["name"] = name
        if description is not None:
            payload["description"] = description
        if intents is not None:
            payload["intents"] = intents
        if active is not None:
            payload["active"] = active
        return self._make_request("PATCH", endpoint, payload)

    def delete_strategy(self, strategy_id: str) -> Dict:
        """
        Delete a strategy.
        
        Args:
            strategy_id: ID of the strategy to delete
            
        Returns:
            Dictionary containing deletion confirmation
        """
        endpoint = f"/v1/strategies/{strategy_id}"
        return self._make_request("DELETE", endpoint)

    def list_strategies(self, wallet_address: str) -> Dict:
        """
        List all strategies for a wallet address.
        
        Args:
            wallet_address: Wallet address to query strategies for
            
        Returns:
            Dictionary containing list of strategies
        """
        endpoint = f"/v1/strategies?wallet_address={wallet_address}"
        return self._make_request("GET", endpoint)


# Example usage
if __name__ == "__main__":
    # Initialize with your API key
    api = ApertureFinanceAPI(api_key="your_api_key_here")

    # Example intent for a DEX swap when price reaches a certain threshold
    swap_intent = {
        "type": "dex_swap",
        "params": {
            "token_in": "0x6B175474E89094C44Da98b954EedeAC495271d0F",  # DAI
            "token_out": "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2",  # WETH
            "amount_in": "1000000000000000000",  # 1 DAI
            "min_amount_out": "0.005",  # Minimum 0.005 WETH
            "price_condition": {
                "operator": "gte",
                "value": "0.0055"  # Trigger when 1 DAI >= 0.0055 WETH
            },
            "slippage": "0.5",  # 0.5% slippage tolerance
            "gas_limit": "300000"
        }
    }

    # Example intent for a lending protocol deposit
    deposit_intent = {
        "type": "lending_deposit",
        "params": {
            "asset": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",  # USDC
            "amount": "1000000",  # 1 USDC (6 decimals)
            "protocol": "aave",
            "min_apy": "0.03"  # Minimum 3% APY
        }
    }

    # Create a strategy with these intents
    try:
        strategy = api.create_strategy(
            name="DEX Swap + Lending Strategy",
            description="Automated DEX swap when price is favorable followed by lending deposit",
            intents=[swap_intent, deposit_intent],
            chain_id=1,  # Ethereum mainnet
            wallet_address="0xYourWalletAddressHere"
        )
        print("Strategy created successfully:")
        print(json.dumps(strategy, indent=2))
    except ValueError as e:
        print(f"Error creating strategy: {e}")
```
