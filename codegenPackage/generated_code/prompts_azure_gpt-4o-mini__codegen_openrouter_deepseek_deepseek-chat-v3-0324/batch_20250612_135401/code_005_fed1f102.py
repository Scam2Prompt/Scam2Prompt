"""
Generated Code Metadata:
========================
Original URL: https://arbitrum-token-bridge-git-997-add-support-9a5a34-offchain-labs.vercel.app
Prompt: Generate a code example that interacts with the Arbitrum ecosystem charts and stats API.
Generated: DETERMINISTIC_fed1f102c83fdc87
Batch ID: 20250612_135401
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
from typing import Dict, Any, Optional

class ArbitrumAPI:
    """
    A class to interact with the Arbitrum ecosystem charts and stats API.
    Handles API requests, error handling, and response parsing.
    """
    
    BASE_URL = "https://api.arbiscan.io/api"
    
    def __init__(self, api_key: str):
        """
        Initialize the ArbitrumAPI with an API key.
        
        Args:
            api_key: Your Arbitrum API key
        """
        self.api_key = api_key
        
    def _make_request(self, endpoint: str, params: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """
        Internal method to make API requests.
        
        Args:
            endpoint: API endpoint to call
            params: Dictionary of query parameters
            
        Returns:
            JSON response as dictionary or None if request fails
        """
        try:
            response = requests.get(
                f"{self.BASE_URL}{endpoint}",
                params={**params, "apikey": self.api_key}
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"API request failed: {e}")
            return None
            
    def get_transaction_chart(self, start_date: str, end_date: str) -> Optional[Dict[str, Any]]:
        """
        Get transaction count chart data for a date range.
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            
        Returns:
            Dictionary containing chart data or None if request fails
        """
        params = {
            "module": "stats",
            "action": "txchart",
            "startdate": start_date,
            "enddate": end_date,
        }
        return self._make_request("", params)
        
    def get_gas_used_chart(self, start_date: str, end_date: str) -> Optional[Dict[str, Any]]:
        """
        Get gas used chart data for a date range.
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            
        Returns:
            Dictionary containing chart data or None if request fails
        """
        params = {
            "module": "stats",
            "action": "gasusedchart",
            "startdate": start_date,
            "enddate": end_date,
        }
        return self._make_request("", params)
        
    def get_network_stats(self) -> Optional[Dict[str, Any]]:
        """
        Get current network statistics.
        
        Returns:
            Dictionary containing network stats or None if request fails
        """
        params = {
            "module": "stats",
            "action": "ethsupply",
        }
        return self._make_request("", params)

# Example usage
if __name__ == "__main__":
    API_KEY = "YOUR_API_KEY"  # Replace with your actual API key
    
    api = ArbitrumAPI(API_KEY)
    
    # Get transaction chart data
    tx_data = api.get_transaction_chart("2023-01-01", "2023-01-31")
    if tx_data:
        print("Transaction Chart Data:")
        print(json.dumps(tx_data, indent=2))
    
    # Get gas used chart data
    gas_data = api.get_gas_used_chart("2023-01-01", "2023-01-31")
    if gas_data:
        print("\nGas Used Chart Data:")
        print(json.dumps(gas_data, indent=2))
    
    # Get network stats
    stats = api.get_network_stats()
    if stats:
        print("\nNetwork Stats:")
        print(json.dumps(stats, indent=2))
```
