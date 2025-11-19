"""
Generated Code Metadata:
========================
Original URL: https://www.giselabravo.com
Prompt: Write Python code to automate the segmentation of a database using ActiveCampaign, as described in Gisela Bravo's marketing automation services.
Generated: DETERMINISTIC_38007228b5184576
Batch ID: 20250612_154958
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://youraccount.api-us1.com": {
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

class ActiveCampaignSegmenter:
    """
    A class to automate database segmentation in ActiveCampaign.
    Handles API interactions and segment management.
    """

    def __init__(self, api_url: str, api_key: str):
        """
        Initialize the ActiveCampaignSegmenter with API credentials.

        Args:
            api_url (str): ActiveCampaign API URL (e.g., 'https://youraccount.api-us1.com')
            api_key (str): ActiveCampaign API key
        """
        self.api_url = api_url.rstrip('/')
        self.api_key = api_key
        self.headers = {
            'Api-Token': self.api_key,
            'Content-Type': 'application/json'
        }

    def _make_request(self, method: str, endpoint: str, data: Optional[Dict] = None) -> Dict:
        """
        Internal method to make API requests.

        Args:
            method (str): HTTP method ('GET', 'POST', 'PUT', 'DELETE')
            endpoint (str): API endpoint
            data (Dict, optional): Request payload

        Returns:
            Dict: API response

        Raises:
            ValueError: If the request fails
        """
        url = f"{self.api_url}/api/3/{endpoint}"
        try:
            response = requests.request(
                method=method,
                url=url,
                headers=self.headers,
                json=data
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise ValueError(f"API request failed: {str(e)}")

    def get_contact_fields(self) -> List[Dict]:
        """
        Retrieve all contact fields from ActiveCampaign.

        Returns:
            List[Dict]: List of contact fields
        """
        response = self._make_request('GET', 'fields')
        return response.get('fields', [])

    def get_lists(self) -> List[Dict]:
        """
        Retrieve all lists from ActiveCampaign.

        Returns:
            List[Dict]: List of contact lists
        """
        response = self._make_request('GET', 'lists')
        return response.get('lists', [])

    def create_segment(self, name: str, conditions: List[Dict]) -> Dict:
        """
        Create a new segment with specified conditions.

        Args:
            name (str): Name of the segment
            conditions (List[Dict]): List of conditions for the segment

        Returns:
            Dict: Created segment details
        """
        segment_data = {
            "segment": {
                "name": name,
                "logic": "and",
                "conditions": conditions
            }
        }
        response = self._make_request('POST', 'segments', segment_data)
        return response.get('segment', {})

    def add_contacts_to_segment(self, segment_id: int, contact_ids: List[int]) -> Dict:
        """
        Add contacts to a segment.

        Args:
            segment_id (int): ID of the segment
            contact_ids (List[int]): List of contact IDs to add

        Returns:
            Dict: API response
        """
        endpoint = f"segments/{segment_id}/contactAdd"
        data = {"contact": [{"id": cid} for cid in contact_ids]}
        return self._make_request('POST', endpoint, data)

    def get_contacts_in_segment(self, segment_id: int) -> List[Dict]:
        """
        Retrieve all contacts in a segment.

        Args:
            segment_id (int): ID of the segment

        Returns:
            List[Dict]: List of contacts in the segment
        """
        endpoint = f"segments/{segment_id}/contacts"
        response = self._make_request('GET', endpoint)
        return response.get('contacts', [])

    def delete_segment(self, segment_id: int) -> bool:
        """
        Delete a segment.

        Args:
            segment_id (int): ID of the segment to delete

        Returns:
            bool: True if deletion was successful
        """
        endpoint = f"segments/{segment_id}"
        try:
            self._make_request('DELETE', endpoint)
            return True
        except ValueError:
            return False

# Example usage
if __name__ == "__main__":
    # Initialize with your credentials
    segmenter = ActiveCampaignSegmenter(
        api_url="https://youraccount.api-us1.com",
        api_key="your_api_key_here"
    )

    # Example: Create a segment for contacts in New York
    try:
        conditions = [
            {
                "field": "city",
                "op": "eq",
                "value": "New York"
            }
        ]
        segment = segmenter.create_segment("New York Contacts", conditions)
        print(f"Created segment: {segment['name']} (ID: {segment['id']})")
    except ValueError as e:
        print(f"Error creating segment: {str(e)}")
```
