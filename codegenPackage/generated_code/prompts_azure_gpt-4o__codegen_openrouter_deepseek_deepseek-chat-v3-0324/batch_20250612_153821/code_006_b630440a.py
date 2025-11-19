"""
Generated Code Metadata:
========================
Original URL: https://primeart.org
Prompt: Develop a REST API client in Python to interact with Prime Art's "Collections" feature, allowing users to retrieve, update, and delete items in their collections.
Generated: DETERMINISTIC_b630440a1d3a52e9
Batch ID: 20250612_153821
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import requests
from typing import Dict, List, Optional, Union
import json

class PrimeArtCollectionsClient:
    """
    A REST API client for interacting with Prime Art's Collections feature.
    """

    def __init__(self, base_url: str, api_key: str):
        """
        Initialize the client with base URL and API key.

        Args:
            base_url (str): The base URL of the Prime Art API
            api_key (str): The API key for authentication
        """
        self.base_url = base_url.rstrip('/')
        self.api_key = api_key
        self.headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

    def _make_request(
        self,
        method: str,
        endpoint: str,
        data: Optional[Dict] = None,
        params: Optional[Dict] = None
    ) -> Union[Dict, List]:
        """
        Internal method to make HTTP requests.

        Args:
            method (str): HTTP method (GET, POST, PUT, DELETE)
            endpoint (str): API endpoint
            data (Optional[Dict]): Request body data
            params (Optional[Dict]): Query parameters

        Returns:
            Union[Dict, List]: Response data

        Raises:
            ValueError: If the request fails
        """
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        try:
            response = requests.request(
                method=method,
                url=url,
                headers=self.headers,
                json=data,
                params=params
            )

            response.raise_for_status()
            return response.json()

        except requests.exceptions.HTTPError as http_err:
            error_msg = f"HTTP error occurred: {http_err}"
            if response.text:
                try:
                    error_data = response.json()
                    error_msg = error_data.get('message', error_msg)
                except json.JSONDecodeError:
                    error_msg = f"{error_msg}. Response: {response.text}"
            raise ValueError(error_msg)
        except requests.exceptions.RequestException as err:
            raise ValueError(f"Request error occurred: {err}")
        except json.JSONDecodeError as json_err:
            raise ValueError(f"Failed to decode JSON response: {json_err}")

    def get_collections(self) -> List[Dict]:
        """
        Retrieve all collections for the authenticated user.

        Returns:
            List[Dict]: List of collections
        """
        return self._make_request('GET', '/collections')

    def get_collection(self, collection_id: str) -> Dict:
        """
        Retrieve a specific collection by ID.

        Args:
            collection_id (str): The ID of the collection to retrieve

        Returns:
            Dict: Collection details
        """
        return self._make_request('GET', f'/collections/{collection_id}')

    def create_collection(self, name: str, description: str = None, is_public: bool = False) -> Dict:
        """
        Create a new collection.

        Args:
            name (str): Name of the collection
            description (str, optional): Description of the collection
            is_public (bool, optional): Whether the collection is public

        Returns:
            Dict: Created collection details
        """
        data = {
            'name': name,
            'description': description,
            'is_public': is_public
        }
        return self._make_request('POST', '/collections', data=data)

    def update_collection(
        self,
        collection_id: str,
        name: str = None,
        description: str = None,
        is_public: bool = None
    ) -> Dict:
        """
        Update an existing collection.

        Args:
            collection_id (str): ID of the collection to update
            name (str, optional): New name for the collection
            description (str, optional): New description for the collection
            is_public (bool, optional): New visibility setting for the collection

        Returns:
            Dict: Updated collection details
        """
        data = {}
        if name is not None:
            data['name'] = name
        if description is not None:
            data['description'] = description
        if is_public is not None:
            data['is_public'] = is_public

        return self._make_request('PUT', f'/collections/{collection_id}', data=data)

    def delete_collection(self, collection_id: str) -> bool:
        """
        Delete a collection.

        Args:
            collection_id (str): ID of the collection to delete

        Returns:
            bool: True if deletion was successful
        """
        self._make_request('DELETE', f'/collections/{collection_id}')
        return True

    def get_collection_items(self, collection_id: str) -> List[Dict]:
        """
        Retrieve all items in a collection.

        Args:
            collection_id (str): ID of the collection

        Returns:
            List[Dict]: List of items in the collection
        """
        return self._make_request('GET', f'/collections/{collection_id}/items')

    def add_item_to_collection(
        self,
        collection_id: str,
        item_id: str,
        notes: str = None
    ) -> Dict:
        """
        Add an item to a collection.

        Args:
            collection_id (str): ID of the collection
            item_id (str): ID of the item to add
            notes (str, optional): Notes about the item

        Returns:
            Dict: Added item details
        """
        data = {
            'item_id': item_id,
            'notes': notes
        }
        return self._make_request('POST', f'/collections/{collection_id}/items', data=data)

    def remove_item_from_collection(self, collection_id: str, item_id: str) -> bool:
        """
        Remove an item from a collection.

        Args:
            collection_id (str): ID of the collection
            item_id (str): ID of the item to remove

        Returns:
            bool: True if removal was successful
        """
        self._make_request('DELETE', f'/collections/{collection_id}/items/{item_id}')
        return True
```
