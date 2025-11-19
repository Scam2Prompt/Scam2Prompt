"""
Generated Code Metadata:
========================
Original URL: https://votex.market
Prompt: Generate a Python function to retrieve high-liquidity betting markets from Votex, filtering by categories such as sports, politics, and crypto.
Generated: DETERMINISTIC_a1b9d9f07479ec9f
Batch ID: 20250612_151947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import requests
from typing import List, Dict, Optional

class VotexMarketRetriever:
    """
    A class to interact with the Votex API and retrieve high-liquidity betting markets.
    """
    
    def __init__(self, api_base_url: str, api_key: str = None):
        """
        Initialize the VotexMarketRetriever with API base URL and optional API key.
        
        Args:
            api_base_url (str): Base URL for the Votex API
            api_key (str, optional): API key for authentication. Defaults to None.
        """
        self.api_base_url = api_base_url.rstrip('/')
        self.api_key = api_key
        self.session = requests.Session()
        if self.api_key:
            self.session.headers.update({'Authorization': f'Bearer {self.api_key}'})
    
    def get_high_liquidity_markets(
        self,
        categories: Optional[List[str]] = None,
        min_liquidity: float = 1000.0,
        limit: int = 100
    ) -> List[Dict]:
        """
        Retrieve high-liquidity markets from Votex, filtered by specified categories.
        
        Args:
            categories (List[str], optional): List of categories to filter by (e.g., ['sports', 'politics', 'crypto']).
                                            If None, all categories are included. Defaults to None.
            min_liquidity (float, optional): Minimum liquidity threshold for markets. Defaults to 1000.0.
            limit (int, optional): Maximum number of markets to return. Defaults to 100.
            
        Returns:
            List[Dict]: List of market dictionaries matching the criteria.
            
        Raises:
            requests.exceptions.RequestException: If the API request fails.
            ValueError: If invalid parameters are provided.
        """
        if min_liquidity < 0:
            raise ValueError("min_liquidity must be a positive number")
        if limit <= 0:
            raise ValueError("limit must be a positive integer")
            
        endpoint = f"{self.api_base_url}/markets"
        params = {
            'liquidity_min': min_liquidity,
            'limit': limit,
            'status': 'open'
        }
        
        if categories:
            params['categories'] = ','.join(categories)
        
        try:
            response = self.session.get(endpoint, params=params)
            response.raise_for_status()
            data = response.json()
            
            if not isinstance(data, list):
                raise ValueError("Unexpected API response format")
                
            return data
            
        except requests.exceptions.RequestException as e:
            raise requests.exceptions.RequestException(f"API request failed: {str(e)}")
        except ValueError as e:
            raise ValueError(f"Invalid API response: {str(e)}")
    
    def close(self):
        """Close the requests session."""
        self.session.close()
    
    def __enter__(self):
        """Enable usage in context managers."""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Ensure session is closed when exiting context."""
        self.close()
```
