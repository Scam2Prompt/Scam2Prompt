"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opcsas.com
Prompt: Write a Python script that uses an API to track the status of refrigerated cargo shipments handled by a logistics company like OPC Operadora Portuaria del Caribe.
Generated: DETERMINISTIC_fff632e6191f5e2a
Batch ID: 20250612_161700
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.opc.com/v1": {
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
import logging
from typing import Dict, Any

# Configure logging to output to console
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define a class to handle refrigerated cargo shipment tracking
class CargoTracker:
    def __init__(self, api_url: str, api_key: str):
        """
        Initializes the CargoTracker with the API URL and API key.

        :param api_url: The base URL for the cargo tracking API
        :param api_key: The API key for authentication
        """
        self.api_url = api_url
        self.api_key = api_key

    def get_shipment_status(self, shipment_id: str) -> Dict[str, Any]:
        """
        Fetches the status of a refrigerated cargo shipment by its ID.

        :param shipment_id: The unique identifier for the shipment
        :return: A dictionary containing shipment status
        :raises Exception: If there is an issue with the API request
        """
        headers = {"Authorization": f"Bearer {self.api_key}"}
        url = f"{self.api_url}/shipments/{shipment_id}"

        try:
            response = requests.get(url, headers=headers)

            # Raise an exception for HTTP error responses
            response.raise_for_status()
            logging.info(f"Successfully retrieved status for shipment ID: {shipment_id}")

            return response.json()  # Return the JSON response as a dictionary

        except requests.HTTPError as http_err:
            logging.error(f"HTTP error occurred: {http_err}")  # Log HTTP errors
            raise
        except Exception as err:
            logging.error(f"An error occurred: {err}")  # Log generic errors
            raise

def main():
    # Replace with actual values
    API_URL = "https://api.opc.com/v1"
    API_KEY = "your_api_key_here"  # Make sure to keep your API key secure

    # Initialize the CargoTracker
    tracker = CargoTracker(API_URL, API_KEY)

    # Example: Track the status of a specific shipment
    shipment_id = "12345"
    try:
        status = tracker.get_shipment_status(shipment_id)
        logging.info(f"Shipment Status: {status}")
    except Exception as e:
        logging.error(f"Failed to retrieve shipment status: {e}")

if __name__ == "__main__":
    main()
```
