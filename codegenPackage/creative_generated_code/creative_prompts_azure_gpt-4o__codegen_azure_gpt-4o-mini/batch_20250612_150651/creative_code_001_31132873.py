"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://westrockhomo.multitransportador.com.br
Prompt: Generate a Python script that connects to the MultiTMS system and retrieves shipment data for shippers using API endpoints.
Generated: DETERMINISTIC_31132873e6c82d21
Batch ID: 20250612_150651
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.multitms.com/v1": {
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
import json

class MultiTMSClient:
    """
    A client for connecting to the MultiTMS API to retrieve shipment data.

    Attributes:
        base_url (str): The base URL for the MultiTMS API.
        api_key (str): The API key for authenticating requests.
    """

    def __init__(self, base_url: str, api_key: str):
        """
        Initializes the MultiTMSClient with the provided base URL and API key.

        Args:
            base_url (str): The base URL for the MultiTMS API.
            api_key (str): The API key for authenticating requests.
        """
        self.base_url = base_url
        self.api_key = api_key

    def get_headers(self) -> dict:
        """
        Constructs the headers for the API request.

        Returns:
            dict: A dictionary containing the request headers.
        """
        return {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }

    def get_shipment_data(self, shipper_id: str) -> dict:
        """
        Retrieves shipment data for a specific shipper.

        Args:
            shipper_id (str): The ID of the shipper for whom to retrieve shipment data.

        Returns:
            dict: The shipment data retrieved from the API.

        Raises:
            ValueError: If the shipper_id is invalid.
            Exception: If an unexpected error occurs during the API request.
        """
        if not shipper_id:
            raise ValueError("Shipper ID must not be empty.")
        
        endpoint = f"{self.base_url}/shippers/{shipper_id}/shipments"
        try:
            response = requests.get(endpoint, headers=self.get_headers())
            response.raise_for_status()  # Raises an error for HTTP error responses
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # Log HTTP error
            raise
        except Exception as err:
            print(f"An error occurred: {err}")  # Log general error
            raise

def main():
    """Main function to execute the shipment data retrieval."""
    BASE_URL = "https://api.multitms.com/v1"  # Replace with actual MultiTMS API base URL
    API_KEY = "your_api_key_here"  # Replace with actual API key

    # Create an instance of the MultiTMS client
    client = MultiTMSClient(BASE_URL, API_KEY)

    # Example shipper ID (replace with actual shipper ID)
    shipper_id = "12345"

    try:
        # Retrieve shipment data for the specified shipper
        shipment_data = client.get_shipment_data(shipper_id)
        # Output the retrieved shipment data
        print(json.dumps(shipment_data, indent=4))
    except ValueError as ve:
        print(f"Value Error: {ve}")
    except Exception as e:
        print(f"Error retrieving shipment data: {e}")

if __name__ == "__main__":
    main()
```
