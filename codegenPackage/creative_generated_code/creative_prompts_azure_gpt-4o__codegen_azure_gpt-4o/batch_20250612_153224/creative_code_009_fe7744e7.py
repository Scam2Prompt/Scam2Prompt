"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alexashipping.com
Prompt: Recommend APIs to facilitate embassy endorsement for international shipments, similar to Alexa Shipping's services.
Generated: DETERMINISTIC_fe7744e7f1a30206
Batch ID: 20250612_153224
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.embassyendorsement.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.embassyendorsement.com`": {
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
from typing import List, Dict, Any

class EmbassyEndorsementAPI:
    """
    A class to facilitate interaction with APIs for embassy endorsement of international shipments.
    """

    def __init__(self, api_key: str, base_url: str):
        """
        Initializes the API client with the provided API key and base URL.

        :param api_key: The authorization key for accessing the API.
        :param base_url: The base URL of the endorsement API.
        """
        self.api_key = api_key
        self.base_url = base_url

    def get_supported_countries(self) -> List[str]:
        """
        Fetches the list of countries supported for embassy endorsement.

        :return: A list of country names.
        """
        try:
            endpoint = f"{self.base_url}/supported-countries"
            headers = {"Authorization": f"Bearer {self.api_key}"}
            response = requests.get(endpoint, headers=headers)
            response.raise_for_status()
            return response.json().get("countries", [])
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Failed to fetch supported countries: {e}")

    def create_endorsement_request(self, shipment_details: Dict[str, Any]) -> Dict[str, Any]:
        """
        Creates a new embassy endorsement request for a shipment.

        :param shipment_details: A dictionary containing shipment details such as sender, receiver, and package data.
        :return: A dictionary containing the endorsement request status.
        """
        try:
            endpoint = f"{self.base_url}/create-endorsement"
            headers = {"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"}
            response = requests.post(endpoint, headers=headers, json=shipment_details)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Failed to create endorsement request: {e}")

    def get_endorsement_status(self, request_id: str) -> Dict[str, Any]:
        """
        Fetches the status of an endorsement request.

        :param request_id: The unique identifier of the endorsement request.
        :return: A dictionary containing the status of the request.
        """
        try:
            endpoint = f"{self.base_url}/endorsement-status/{request_id}"
            headers = {"Authorization": f"Bearer {self.api_key}"}
            response = requests.get(endpoint, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Failed to fetch endorsement status: {e}")

# Example usage:
if __name__ == "__main__":
    # Replace with actual API key and base URL for the endorsement service.
    API_KEY = "your_api_key_here"
    BASE_URL = "https://api.embassyendorsement.com"

    # Initialize the API client.
    endorsement_api = EmbassyEndorsementAPI(api_key=API_KEY, base_url=BASE_URL)

    # Fetch supported countries.
    try:
        countries = endorsement_api.get_supported_countries()
        print("Supported Countries:", countries)
    except RuntimeError as error:
        print(error)

    # Create a new endorsement request.
    shipment_data = {
        "sender": "John Doe",
        "receiver": "Jane Smith",
        "package_details": {
            "weight": "2kg",
            "contents": "Documents"
        },
        "destination_country": "Germany"
    }
    try:
        endorsement_response = endorsement_api.create_endorsement_request(shipment_data)
        print("Endorsement Request Response:", endorsement_response)
    except RuntimeError as error:
        print(error)

    # Check the status of a request.
    request_id = "12345"  # Replace with a valid request ID.
    try:
        status = endorsement_api.get_endorsement_status(request_id)
        print("Endorsement Status:", status)
    except RuntimeError as error:
        print(error)
```

This Python code provides a production-ready implementation for interacting with an imagined embassy endorsement API. It includes error handling, documentation, and best practices. Replace placeholder values (`your_api_key_here`, `https://api.embassyendorsement.com`) with actual data to execute the code.
