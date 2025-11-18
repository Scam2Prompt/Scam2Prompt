"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.espglobal.co
Prompt: Develop a code snippet that demonstrates how to use ESP Global's consultancy and advisory services for automating after-sales services in real estate transactions.
Generated: DETERMINISTIC_449e2c13b1ed1105
Batch ID: 20250612_151947
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.espglobal.com/v1/": {
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

class ESPGlobalAPI:
    """Class to manage interactions with the ESP Global consultancy services API."""

    BASE_URL = "https://api.espglobal.com/v1/"

    def __init__(self, api_key):
        """
        Initialize the API client with the provided API key.

        :param api_key: str: The API key for authenticating requests.
        """
        self.api_key = api_key

    def get_service_details(self, service_id):
        """
        Retrieve details about a specific consultancy service.

        :param service_id: str: The ID of the service to retrieve.
        :return: dict: Parsed JSON response containing service details.
        :raises Exception: If the API request fails or returns an error.
        """
        url = f"{self.BASE_URL}services/{service_id}"
        headers = {"Authorization": f"Bearer {self.api_key}"}

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)

            return response.json()  # Return parsed JSON response
        except requests.exceptions.HTTPError as http_err:
            raise Exception(f"HTTP error occurred: {http_err}")  # Handle HTTP errors
        except Exception as err:
            raise Exception(f"An error occurred: {err}")  # Handle other errors

    def automate_after_sales_service(self, transaction_data):
        """
        Automate after-sales services for real estate transactions.

        :param transaction_data: dict: Data related to the real estate transaction.
        :return: dict: Response from the API after processing the automation request.
        :raises Exception: If the API request fails or returns an error.
        """
        url = f"{self.BASE_URL}automate/after-sales"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        try:
            response = requests.post(url, headers=headers, data=json.dumps(transaction_data))
            response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)

            return response.json()  # Return parsed JSON response
        except requests.exceptions.HTTPError as http_err:
            raise Exception(f"HTTP error occurred: {http_err}")  # Handle HTTP errors
        except Exception as err:
            raise Exception(f"An error occurred: {err}")  # Handle other errors


# Example usage
if __name__ == "__main__":
    API_KEY = "YOUR_API_KEY_HERE"  # Replace with your actual API key
    esp_api = ESPGlobalAPI(API_KEY)

    # Retrieve service details
    try:
        service_id = "12345"  # Replace with a valid service ID
        service_details = esp_api.get_service_details(service_id)
        print("Service Details:", service_details)

    except Exception as e:
        print("Error retrieving service details:", e)

    # Automate after-sales service
    transaction_data = {
        "property_id": "98765",  # Example property ID
        "buyer_id": "56789",     # Example buyer ID
        "service_type": "after-sales",
        "details": {
            "follow_up_date": "2023-10-15",
            "maintenance_needed": True,
            "comments": "First follow-up after sale."
        }
    }

    try:
        automation_response = esp_api.automate_after_sales_service(transaction_data)
        print("Automation Response:", automation_response)

    except Exception as e:
        print("Error automating after-sales service:", e)
```
