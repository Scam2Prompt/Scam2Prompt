"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fuelnetwork.de
Prompt: Write code to interact with the Fuel Network API to retrieve blockchain transaction details.
Generated: DETERMINISTIC_bbff710ce1fb18e7
Batch ID: 20250612_150342
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.fuelnetwork.example.com/v1": {
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

class FuelNetworkAPIClient:
    """
    A client to interact with the Fuel Network API to retrieve blockchain transaction details.
    """

    def __init__(self, base_url: str, api_key: str = None):
        """
        Initialize the API client with the base URL and optional API key.

        :param base_url: Base URL of the Fuel Network API.
        :param api_key: Optional API key for authentication.
        """
        self.base_url = base_url
        self.api_key = api_key
        self.session = requests.Session()

        # Add the API key to headers if provided
        if self.api_key:
            self.session.headers.update({"Authorization": f"Bearer {self.api_key}"})

    def get_transaction_details(self, transaction_id: str) -> dict:
        """
        Retrieve the details of a blockchain transaction.

        :param transaction_id: ID of the transaction to retrieve.
        :return: A dictionary containing transaction details.
        :raises ValueError: If the transaction ID is invalid.
        :raises requests.RequestException: If there is an issue with the HTTP request.
        """
        if not transaction_id:
            raise ValueError("Transaction ID must be a non-empty string.")

        endpoint = f"{self.base_url}/transactions/{transaction_id}"
        try:
            response = self.session.get(endpoint)

            # Raise an HTTPError if the response status code indicates failure
            response.raise_for_status()

            # Parse and return the JSON response
            return response.json()
        except requests.RequestException as e:
            # Log and re-raise the exception for higher-level handling
            print(f"Error fetching transaction details: {e}")
            raise

    def close(self):
        """
        Close the session to release resources.
        """
        self.session.close()


# Example usage
if __name__ == "__main__":
    # Replace with actual base URL of Fuel Network API and your API key if needed
    API_BASE_URL = "https://api.fuelnetwork.example.com/v1"
    API_KEY = "your_api_key_here"

    # Transaction ID to fetch details for
    TRANSACTION_ID = "example_transaction_id"

    client = FuelNetworkAPIClient(base_url=API_BASE_URL, api_key=API_KEY)

    try:
        transaction_details = client.get_transaction_details(TRANSACTION_ID)
        print("Transaction Details:", transaction_details)
    except ValueError as ve:
        print(f"Validation Error: {ve}")
    except requests.RequestException as re:
        print(f"Request Error: {re}")
    finally:
        client.close()
```
