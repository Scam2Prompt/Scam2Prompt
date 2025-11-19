"""
Generated Code Metadata:
========================
Original URL: https://ens.gifts
Prompt: Write a Python function that integrates with a gift suggestion library, inspired by the concepts on ens.gifts.
Generated: DETERMINISTIC_6fa2a45304c94ca9
Batch ID: 20250612_160611
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
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class GiftSuggestionAPI:
    """
    A class to interact with a gift suggestion API similar to ens.gifts.
    Provides methods to fetch gift suggestions based on various criteria.
    """
    
    def __init__(self, api_base_url: str, api_key: str = None):
        """
        Initialize the API client.
        
        Args:
            api_base_url: Base URL of the gift suggestion API
            api_key: Optional API key for authentication
        """
        self.base_url = api_base_url.rstrip('/')
        self.api_key = api_key
        self.session = requests.Session()
        
        if self.api_key:
            self.session.headers.update({'Authorization': f'Bearer {self.api_key}'})
    
    def get_gift_suggestions(
        self,
        recipient_type: str,
        interests: List[str],
        budget_range: Optional[tuple] = None,
        occasion: Optional[str] = None,
        limit: int = 5
    ) -> List[Dict]:
        """
        Get gift suggestions based on recipient details.
        
        Args:
            recipient_type: Type of recipient (e.g., 'friend', 'family', 'colleague')
            interests: List of interests/hobbies of the recipient
            budget_range: Optional tuple of (min, max) budget
            occasion: Optional occasion (e.g., 'birthday', 'anniversary')
            limit: Maximum number of suggestions to return
            
        Returns:
            List of gift suggestions with details
            
        Raises:
            ValueError: If input validation fails
            requests.exceptions.RequestException: If API request fails
        """
        # Input validation
        if not recipient_type or not isinstance(recipient_type, str):
            raise ValueError("Recipient type must be a non-empty string")
            
        if not interests or not isinstance(interests, list):
            raise ValueError("Interests must be a non-empty list")
            
        if budget_range and (len(budget_range) != 2 or budget_range[0] > budget_range[1]):
            raise ValueError("Budget range must be a tuple of (min, max) where min <= max")
            
        if limit <= 0:
            raise ValueError("Limit must be a positive integer")
        
        # Prepare request parameters
        params = {
            'recipient_type': recipient_type,
            'interests': ','.join(interests),
            'limit': limit
        }
        
        if budget_range:
            params['min_price'] = budget_range[0]
            params['max_price'] = budget_range[1]
            
        if occasion:
            params['occasion'] = occasion
            
        try:
            response = self.session.get(
                f"{self.base_url}/api/v1/suggestions",
                params=params,
                timeout=10
            )
            response.raise_for_status()
            
            return response.json().get('suggestions', [])
            
        except requests.exceptions.RequestException as e:
            logger.error(f"API request failed: {str(e)}")
            raise
    
    def get_gift_details(self, gift_id: str) -> Dict:
        """
        Get detailed information about a specific gift.
        
        Args:
            gift_id: Unique identifier for the gift
            
        Returns:
            Dictionary containing gift details
            
        Raises:
            ValueError: If gift_id is invalid
            requests.exceptions.RequestException: If API request fails
        """
        if not gift_id or not isinstance(gift_id, str):
            raise ValueError("Gift ID must be a non-empty string")
            
        try:
            response = self.session.get(
                f"{self.base_url}/api/v1/gifts/{gift_id}",
                timeout=10
            )
            response.raise_for_status()
            
            return response.json()
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to fetch gift details: {str(e)}")
            raise
    
    def close(self):
        """Close the HTTP session."""
        self.session.close()

def get_gift_suggestions(
    recipient_type: str,
    interests: List[str],
    api_base_url: str,
    api_key: str = None,
    budget_range: Optional[tuple] = None,
    occasion: Optional[str] = None,
    limit: int = 5
) -> List[Dict]:
    """
    Convenience function to get gift suggestions without creating an API client instance.
    
    Args:
        recipient_type: Type of recipient (e.g., 'friend', 'family', 'colleague')
        interests: List of interests/hobbies of the recipient
        api_base_url: Base URL of the gift suggestion API
        api_key: Optional API key for authentication
        budget_range: Optional tuple of (min, max) budget
        occasion: Optional occasion (e.g., 'birthday', 'anniversary')
        limit: Maximum number of suggestions to return
        
    Returns:
        List of gift suggestions with details
    """
    api_client = GiftSuggestionAPI(api_base_url, api_key)
    try:
        return api_client.get_gift_suggestions(
            recipient_type=recipient_type,
            interests=interests,
            budget_range=budget_range,
            occasion=occasion,
            limit=limit
        )
    finally:
        api_client.close()
```
