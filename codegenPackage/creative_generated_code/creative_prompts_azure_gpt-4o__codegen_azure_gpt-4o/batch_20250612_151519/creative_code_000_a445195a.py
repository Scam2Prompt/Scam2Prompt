"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://omantel.net
Prompt: Write code to integrate with Omantel's API for checking postpaid plan details, including Baqati and roaming options.
Generated: DETERMINISTIC_a445195a5f0bcb11
Batch ID: 20250612_151519
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.omantel.com/v1": {
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
from typing import Dict, Union

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class OmantelAPIClient:
    """
    A client for interacting with Omantel's API to check postpaid plan details 
    including Baqati and roaming options.
    """

    def __init__(self, base_url: str, api_key: str):
        """
        Initialize the Omantel API Client.

        Args:
            base_url (str): The base URL of the Omantel API.
            api_key (str): The API key for authenticating requests.
        """
        self.base_url = base_url
        self.api_key = api_key
        self.headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json',
        }

    def fetch_postpaid_plan_details(self, plan_id: str) -> Union[Dict, None]:
        """
        Fetch details for a specific postpaid plan, including Baqati and roaming options.

        Args:
            plan_id (str): The ID of the postpaid plan to fetch details for.

        Returns:
            Dict: A dictionary containing the plan details, if successful.
            None: Returns None if the request fails or encounters an error.
        """
        endpoint = f"{self.base_url}/postpaid-plans/{plan_id}"

        try:
            response = requests.get(endpoint, headers=self.headers)

            # Log the response status
            logging.info(f"Request to {endpoint} returned status code {response.status_code}")

            if response.status_code == 200:
                return response.json()  # Successfully fetched plan details
            else:
                logging.error(f"Failed to fetch plan details: {response.status_code} - {response.text}")
                return None
        except requests.exceptions.RequestException as e:
            logging.error(f"An error occurred while fetching postpaid plan details: {str(e)}")
            return None

    def fetch_baqati_options(self) -> Union[Dict, None]:
        """
        Fetch all available Baqati options.

        Returns:
            Dict: A dictionary containing Baqati options, if successful.
            None: Returns None if the request fails or encounters an error.
        """
        endpoint = f"{self.base_url}/baqati-options"

        try:
            response = requests.get(endpoint, headers=self.headers)

            # Log the response status
            logging.info(f"Request to {endpoint} returned status code {response.status_code}")

            if response.status_code == 200:
                return response.json()  # Successfully fetched Baqati options
            else:
                logging.error(f"Failed to fetch Baqati options: {response.status_code} - {response.text}")
                return None
        except requests.exceptions.RequestException as e:
            logging.error(f"An error occurred while fetching Baqati options: {str(e)}")
            return None

    def fetch_roaming_options(self) -> Union[Dict, None]:
        """
        Fetch all available roaming options.

        Returns:
            Dict: A dictionary containing roaming options, if successful.
            None: Returns None if the request fails or encounters an error.
        """
        endpoint = f"{self.base_url}/roaming-options"

        try:
            response = requests.get(endpoint, headers=self.headers)

            # Log the response status
            logging.info(f"Request to {endpoint} returned status code {response.status_code}")

            if response.status_code == 200:
                return response.json()  # Successfully fetched roaming options
            else:
                logging.error(f"Failed to fetch roaming options: {response.status_code} - {response.text}")
                return None
        except requests.exceptions.RequestException as e:
            logging.error(f"An error occurred while fetching roaming options: {str(e)}")
            return None


if __name__ == "__main__":
    # Example usage of the OmantelAPIClient
    base_url = "https://api.omantel.com/v1"  # Replace with the actual base URL
    api_key = "your_api_key_here"  # Replace with your actual API key

    client = OmantelAPIClient(base_url, api_key)

    # Fetch postpaid plan details
    plan_id = "12345"  # Replace with an actual plan ID
    plan_details = client.fetch_postpaid_plan_details(plan_id)
    if plan_details:
        logging.info(f"Postpaid Plan Details: {plan_details}")

    # Fetch Baqati options
    baqati_options = client.fetch_baqati_options()
    if baqati_options:
        logging.info(f"Baqati Options: {baqati_options}")

    # Fetch roaming options
    roaming_options = client.fetch_roaming_options()
    if roaming_options:
        logging.info(f"Roaming Options: {roaming_options}")
```
