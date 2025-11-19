"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://primeart.org
Prompt: How can I use the Prime Art API to create and manage digital art collections?
Generated: DETERMINISTIC_e7ef838367947a4b
Batch ID: 20250612_162728
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.primeart.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests

class PrimeArtAPI:
    """
    A class to interact with the Prime Art API for creating and managing digital art collections.
    """

    BASE_URL = "https://api.primeart.com"  # Replace with actual API base URL

    def __init__(self, api_key):
        """
        Initialize the PrimeArtAPI with an API key.

        :param api_key: str, The API key for authenticating with the Prime Art API.
        """
        self.api_key = api_key

    def _make_request(self, endpoint, method='GET', data=None):
        """
        Make an HTTP request to the Prime Art API.

        :param endpoint: str, The API endpoint to hit.
        :param method: str, The HTTP method to use (GET, POST, PUT, DELETE).
        :param data: dict, The data to send with the request (for POST/PUT).
        :return: dict, The JSON response from the API.
        """
        url = f"{self.BASE_URL}{endpoint}"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        try:
            if method == 'GET':
                response = requests.get(url, headers=headers)
            elif method == 'POST':
                response = requests.post(url, headers=headers, json=data)
            elif method == 'PUT':
                response = requests.put(url, headers=headers, json=data)
            elif method == 'DELETE':
                response = requests.delete(url, headers=headers)
            else:
                raise ValueError("Invalid HTTP method: Must be one of GET, POST, PUT, DELETE")

            response.raise_for_status()  # Raise an error for bad responses
            return response.json()

        except requests.RequestException as e:
            print(f"An error occurred: {str(e)}")
            return None

    def create_collection(self, name, description):
        """
        Create a new digital art collection.

        :param name: str, The name of the collection.
        :param description: str, A description of the collection.
        :return: dict or None, The response from the API containing details of the new collection.
        """
        endpoint = "/collections"
        data = {
            "name": name,
            "description": description
        }
        return self._make_request(endpoint, method='POST', data=data)

    def get_collection(self, collection_id):
        """
        Retrieve a specific digital art collection by its ID.

        :param collection_id: str, The ID of the collection to retrieve.
        :return: dict or None, The response from the API containing the collection details.
        """
        endpoint = f"/collections/{collection_id}"
        return self._make_request(endpoint)

    def update_collection(self, collection_id, name=None, description=None):
        """
        Update an existing digital art collection.

        :param collection_id: str, The ID of the collection to update.
        :param name: str, The new name of the collection (optional).
        :param description: str, The new description of the collection (optional).
        :return: dict or None, The response from the API confirming the update.
        """
        endpoint = f"/collections/{collection_id}"
        data = {}
        if name:
            data['name'] = name
        if description:
            data['description'] = description

        return self._make_request(endpoint, method='PUT', data=data)

    def delete_collection(self, collection_id):
        """
        Delete a digital art collection.

        :param collection_id: str, The ID of the collection to delete.
        :return: bool, True if the deletion was successful, otherwise False.
        """
        endpoint = f"/collections/{collection_id}"
        response = self._make_request(endpoint, method='DELETE')
        return response is not None

# Example usage:
if __name__ == "__main__":
    api_key = "YOUR_API_KEY"  # Replace with your actual API key
    prime_art_api = PrimeArtAPI(api_key)

    # Create a new collection
    new_collection = prime_art_api.create_collection("My Art Collection", "A collection of my best works.")
    print("Created Collection:", new_collection)

    # Get a collection
    collection_details = prime_art_api.get_collection(new_collection['id'])
    print("Collection Details:", collection_details)

    # Update the collection
    updated_collection = prime_art_api.update_collection(new_collection['id'], description="Updated description.")
    print("Updated Collection:", updated_collection)

    # Delete the collection
    delete_success = prime_art_api.delete_collection(new_collection['id'])
    print("Collection Deleted:", delete_success)
```
