"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hex-gift.com
Prompt: Provide an example of how to integrate Swagbucks API for tracking cash back from online purchases.
Generated: DETERMINISTIC_7cde10334fc10688
Batch ID: 20250612_135717
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.swagbucks.com/v1": {
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

class SwagbucksAPI:
    """
    A class to interact with the Swagbucks API for tracking cash back on online purchases.
    """

    def __init__(self, api_key: str, base_url: str = "https://api.swagbucks.com/v1"):
        """
        Initialize the SwagbucksAPI client.

        Args:
            api_key (str): Your Swagbucks API key.
            base_url (str): Base URL for the API. Defaults to Swagbucks API v1 base URL.
        """
        self.api_key = api_key
        self.base_url = base_url
        self.headers = {"Authorization": f"Bearer {self.api_key}"}

    def track_cashback(self, transaction_id: str) -> dict:
        """
        Track cash back for a specific transaction.

        Args:
            transaction_id (str): The ID of the transaction to track.

        Returns:
            dict: Response from the API containing cash back details.
        """
        endpoint = f"{self.base_url}/cashback/track"
        payload = {"transaction_id": transaction_id}

        try:
            response = requests.post(endpoint, json=payload, headers=self.headers)
            response.raise_for_status()  # Raise an error for HTTP error codes.
            return response.json()  # Return the parsed JSON response.

        except requests.exceptions.HTTPError as http_err:
            # Handle HTTP errors (e.g., 404, 500, etc.)
            return {"error": f"HTTP error occurred: {http_err}"}
        except requests.exceptions.RequestException as req_err:
            # Handle other request-related errors
            return {"error": f"Request error occurred: {req_err}"}
        except Exception as ex:
            # Handle any other unexpected exceptions
            return {"error": f"An unexpected error occurred: {ex}"}

    def get_transaction_details(self, transaction_id: str) -> dict:
        """
        Retrieve details of a specific transaction.

        Args:
            transaction_id (str): The ID of the transaction to retrieve.

        Returns:
            dict: Response from the API containing transaction details.
        """
        endpoint = f"{self.base_url}/transactions/{transaction_id}"

        try:
            response = requests.get(endpoint, headers=self.headers)
            response.raise_for_status()  # Raise an error for HTTP error codes.
            return response.json()  # Return the parsed JSON response.

        except requests.exceptions.HTTPError as http_err:
            # Handle HTTP errors
            return {"error": f"HTTP error occurred: {http_err}"}
        except requests.exceptions.RequestException as req_err:
            # Handle other request-related errors
            return {"error": f"Request error occurred: {req_err}"}
        except Exception as ex:
            # Handle any other unexpected exceptions
            return {"error": f"An unexpected error occurred: {ex}"}


# Example usage:
if __name__ == "__main__":
    # Replace 'your_api_key_here' with your actual Swagbucks API key.
    swagbucks_api = SwagbucksAPI(api_key="your_api_key_here")

    # Track cash back for a transaction (replace 'example_transaction_id' with a real transaction ID).
    cashback_response = swagbucks_api.track_cashback(transaction_id="example_transaction_id")
    print("Cashback Response:", cashback_response)

    # Get transaction details (replace 'example_transaction_id' with a real transaction ID).
    transaction_details = swagbucks_api.get_transaction_details(transaction_id="example_transaction_id")
    print("Transaction Details:", transaction_details)
```
