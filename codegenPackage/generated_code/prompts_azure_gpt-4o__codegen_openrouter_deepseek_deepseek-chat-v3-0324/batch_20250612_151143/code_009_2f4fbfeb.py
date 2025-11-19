"""
Generated Code Metadata:
========================
Original URL: https://magahat-3gz.pages.dev
Prompt: Write a Python script to query the Ord.io platform for activity related to MAGA•THE•DONALD•TRUMP inscriptions, including pending transactions, completed mints, and holder balances.
Generated: DETERMINISTIC_2f4fbfebf1b509f5
Batch ID: 20250612_151143
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.ord.io": {
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
from typing import Dict, List, Optional, Any
from datetime import datetime

class OrdioAPI:
    """
    A client for interacting with the Ord.io API to fetch MAGA•THE•DONALD•TRUMP inscription data.
    """
    
    BASE_URL = "https://api.ord.io"
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize the OrdioAPI client.
        
        Args:
            api_key: Optional API key for authenticated requests.
        """
        self.session = requests.Session()
        self.api_key = api_key
        if self.api_key:
            self.session.headers.update({"Authorization": f"Bearer {self.api_key}"})
    
    def _make_request(self, endpoint: str, params: Optional[Dict] = None) -> Dict:
        """
        Make a GET request to the Ord.io API.
        
        Args:
            endpoint: API endpoint to query.
            params: Optional query parameters.
            
        Returns:
            JSON response as a dictionary.
            
        Raises:
            requests.exceptions.RequestException: If the request fails.
        """
        url = f"{self.BASE_URL}{endpoint}"
        try:
            response = self.session.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"API request failed: {e}")
    
    def get_pending_transactions(self, ticker: str = "MAGA•THE•DONALD•TRUMP") -> List[Dict]:
        """
        Get pending transactions for a given ticker.
        
        Args:
            ticker: The ticker symbol to query (default: MAGA•THE•DONALD•TRUMP).
            
        Returns:
            List of pending transactions.
        """
        endpoint = "/pending-transactions"
        params = {"ticker": ticker}
        return self._make_request(endpoint, params).get("transactions", [])
    
    def get_completed_mints(self, ticker: str = "MAGA•THE•DONALD•TRUMP") -> List[Dict]:
        """
        Get completed mints for a given ticker.
        
        Args:
            ticker: The ticker symbol to query (default: MAGA•THE•DONALD•TRUMP).
            
        Returns:
            List of completed mints.
        """
        endpoint = "/completed-mints"
        params = {"ticker": ticker}
        return self._make_request(endpoint, params).get("mints", [])
    
    def get_holder_balances(self, ticker: str = "MAGA•THE•DONALD•TRUMP") -> Dict[str, int]:
        """
        Get holder balances for a given ticker.
        
        Args:
            ticker: The ticker symbol to query (default: MAGA•THE•DONALD•TRUMP).
            
        Returns:
            Dictionary mapping addresses to balances.
        """
        endpoint = "/holder-balances"
        params = {"ticker": ticker}
        return self._make_request(endpoint, params).get("balances", {})
    
    def get_all_activity(self, ticker: str = "MAGA•THE•DONALD•TRUMP") -> Dict[str, Any]:
        """
        Get all activity (pending transactions, completed mints, holder balances) for a ticker.
        
        Args:
            ticker: The ticker symbol to query (default: MAGA•THE•DONALD•TRUMP).
            
        Returns:
            Dictionary containing all activity data.
        """
        return {
            "timestamp": datetime.utcnow().isoformat(),
            "ticker": ticker,
            "pending_transactions": self.get_pending_transactions(ticker),
            "completed_mints": self.get_completed_mints(ticker),
            "holder_balances": self.get_holder_balances(ticker)
        }

def save_to_file(data: Dict, filename: str) -> None:
    """
    Save data to a JSON file.
    
    Args:
        data: Data to save.
        filename: Name of the file to save to.
    """
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)

def main():
    # Initialize the API client
    ordio = OrdioAPI()
    
    try:
        # Fetch all activity for MAGA•THE•DONALD•TRUMP
        activity = ordio.get_all_activity()
        
        # Print summary
        print(f"Activity for {activity['ticker']} as of {activity['timestamp']}:")
        print(f"- Pending transactions: {len(activity['pending_transactions'])}")
        print(f"- Completed mints: {len(activity['completed_mints'])}")
        print(f"- Unique holders: {len(activity['holder_balances'])}")
        
        # Save to file
        filename = f"maga_activity_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}.json"
        save_to_file(activity, filename)
        print(f"Data saved to {filename}")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
