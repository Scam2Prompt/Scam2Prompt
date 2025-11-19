"""
Generated Code Metadata:
========================
Original URL: https://sgsp.org.br
Prompt: Create a REST API client in Python that interacts with the SGSP's resources for Gastroenterology education and events.
Generated: DETERMINISTIC_9b8f0a6bb52d5e0f
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import requests
from typing import Optional, Dict, Any, List
import json
from datetime import datetime

class SGSPClient:
    """
    A REST API client for interacting with SGSP's Gastroenterology education and events resources.
    
    Attributes:
        base_url (str): The base URL for the SGSP API.
        api_key (str): The API key for authentication.
        session (requests.Session): A session object for making HTTP requests.
    """

    def __init__(self, base_url: str, api_key: str):
        """
        Initialize the SGSPClient with the base URL and API key.
        
        Args:
            base_url (str): The base URL for the SGSP API.
            api_key (str): The API key for authentication.
        """
        self.base_url = base_url.rstrip('/')
        self.api_key = api_key
        self.session = requests.Session()
        self.session.headers.update({
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        })

    def _make_request(self, method: str, endpoint: str, params: Optional[Dict] = None, 
                      data: Optional[Dict] = None) -> Dict[str, Any]:
        """
        Make an HTTP request to the SGSP API.
        
        Args:
            method (str): The HTTP method (GET, POST, PUT, DELETE).
            endpoint (str): The API endpoint.
            params (Optional[Dict]): Query parameters.
            data (Optional[Dict]): Request body data.
            
        Returns:
            Dict[str, Any]: The JSON response from the API.
            
        Raises:
            requests.exceptions.HTTPError: If the API request fails.
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
        except requests.exceptions.RequestException as e:
            raise requests.exceptions.HTTPError(f"API request failed: {e}")

    def get_events(self, start_date: Optional[str] = None, 
                   end_date: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        Get a list of Gastroenterology events.
        
        Args:
            start_date (Optional[str]): Filter events starting from this date (YYYY-MM-DD).
            end_date (Optional[str]): Filter events ending before this date (YYYY-MM-DD).
            
        Returns:
            List[Dict[str, Any]]: A list of event dictionaries.
        """
        params = {}
        if start_date:
            params['start_date'] = start_date
        if end_date:
            params['end_date'] = end_date
            
        return self._make_request('GET', 'events', params=params).get('events', [])

    def get_event_by_id(self, event_id: str) -> Dict[str, Any]:
        """
        Get a specific event by its ID.
        
        Args:
            event_id (str): The ID of the event.
            
        Returns:
            Dict[str, Any]: The event details.
        """
        return self._make_request('GET', f'events/{event_id}')

    def register_for_event(self, event_id: str, user_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Register a user for an event.
        
        Args:
            event_id (str): The ID of the event.
            user_data (Dict[str, Any]): User registration data.
            
        Returns:
            Dict[str, Any]: Registration confirmation.
        """
        return self._make_request('POST', f'events/{event_id}/register', data=user_data)

    def get_educational_resources(self, category: Optional[str] = None, 
                                 search_query: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        Get a list of educational resources.
        
        Args:
            category (Optional[str]): Filter resources by category.
            search_query (Optional[str]): Search resources by query.
            
        Returns:
            List[Dict[str, Any]]: A list of educational resources.
        """
        params = {}
        if category:
            params['category'] = category
        if search_query:
            params['q'] = search_query
            
        return self._make_request('GET', 'resources', params=params).get('resources', [])

    def get_resource_by_id(self, resource_id: str) -> Dict[str, Any]:
        """
        Get a specific educational resource by its ID.
        
        Args:
            resource_id (str): The ID of the resource.
            
        Returns:
            Dict[str, Any]: The resource details.
        """
        return self._make_request('GET', f'resources/{resource_id}')

    def close(self):
        """Close the session."""
        self.session.close()

    def __enter__(self):
        """Enter the context manager."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Exit the context manager."""
        self.close()
```
