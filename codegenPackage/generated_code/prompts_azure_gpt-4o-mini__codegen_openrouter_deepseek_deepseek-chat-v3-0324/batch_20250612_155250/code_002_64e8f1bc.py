"""
Generated Code Metadata:
========================
Original URL: https://jurunensebrazz.blogspot.com
Prompt: "Write a function that retrieves product discounts and promotions for a home center store, inspired by the sales featured on Jurunense Home Center."
Generated: DETERMINISTIC_64e8f1bc642f93e1
Batch ID: 20250612_155250
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import requests
from typing import Dict, List, Optional
from datetime import datetime

class HomeCenterDiscounts:
    """
    A class to retrieve product discounts and promotions from a home center store.
    Inspired by Jurunense Home Center sales.
    """
    
    def __init__(self, api_base_url: str, api_key: str = None):
        """
        Initialize the HomeCenterDiscounts instance.
        
        Args:
            api_base_url (str): Base URL for the home center's API
            api_key (str, optional): API key for authentication. Defaults to None.
        """
        self.api_base_url = api_base_url.rstrip('/')
        self.api_key = api_key
        self.session = requests.Session()
        if api_key:
            self.session.headers.update({'Authorization': f'Bearer {api_key}'})
    
    def _make_request(self, endpoint: str, params: Optional[Dict] = None) -> Dict:
        """
        Internal method to make API requests.
        
        Args:
            endpoint (str): API endpoint to call
            params (Dict, optional): Query parameters. Defaults to None.
            
        Returns:
            Dict: JSON response from the API
            
        Raises:
            ValueError: If the API request fails
        """
        url = f"{self.api_base_url}/{endpoint.lstrip('/')}"
        try:
            response = self.session.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise ValueError(f"API request failed: {str(e)}")
    
    def get_current_promotions(self) -> List[Dict]:
        """
        Get all current promotions and discounts.
        
        Returns:
            List[Dict]: List of promotion dictionaries with details
        """
        endpoint = "/api/v1/promotions/current"
        return self._make_request(endpoint)
    
    def get_product_discounts(self, product_id: str = None, category: str = None) -> List[Dict]:
        """
        Get discounts for specific products or categories.
        
        Args:
            product_id (str, optional): Specific product ID to check. Defaults to None.
            category (str, optional): Product category to filter. Defaults to None.
            
        Returns:
            List[Dict]: List of product discount dictionaries
        """
        params = {}
        if product_id:
            params['product_id'] = product_id
        if category:
            params['category'] = category
            
        endpoint = "/api/v1/products/discounts"
        return self._make_request(endpoint, params=params)
    
    def get_seasonal_sales(self, season: str = None) -> List[Dict]:
        """
        Get seasonal sales (e.g., summer, winter, holiday sales).
        
        Args:
            season (str, optional): Specific season to filter. Defaults to None.
            
        Returns:
            List[Dict]: List of seasonal sale dictionaries
        """
        params = {}
        if season:
            params['season'] = season
            
        endpoint = "/api/v1/promotions/seasonal"
        return self._make_request(endpoint, params=params)
    
    def get_limited_time_offers(self, active_only: bool = True) -> List[Dict]:
        """
        Get limited-time offers with expiration dates.
        
        Args:
            active_only (bool, optional): Only return active offers. Defaults to True.
            
        Returns:
            List[Dict]: List of limited-time offer dictionaries
        """
        params = {'active_only': str(active_only).lower()}
        endpoint = "/api/v1/promotions/limited-time"
        return self._make_request(endpoint, params=params)
    
    def check_discount_eligibility(self, product_id: str, customer_id: str) -> Dict:
        """
        Check if a specific customer is eligible for a product discount.
        
        Args:
            product_id (str): Product ID to check
            customer_id (str): Customer ID to check
            
        Returns:
            Dict: Dictionary with eligibility information
        """
        endpoint = f"/api/v1/products/{product_id}/discount-eligibility/{customer_id}"
        return self._make_request(endpoint)
```
