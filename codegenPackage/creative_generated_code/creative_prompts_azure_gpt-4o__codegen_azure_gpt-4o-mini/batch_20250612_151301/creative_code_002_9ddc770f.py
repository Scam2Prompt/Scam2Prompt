"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://testnet-satoshivm.pages.dev
Prompt: Create a program that integrates with the SatoshiVM Testnet to request tSAVM every 12 hours and display the current credits and donation records.
Generated: DETERMINISTIC_9ddc770fe2b41e8e
Batch ID: 20250612_151301
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.satoshivm.testnet": {
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
import time
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SatoshiVMTestnetClient:
    def __init__(self, api_url):
        """
        Initializes the SatoshiVMTestnetClient with the given API URL.
        
        :param api_url: The base URL of the SatoshiVM Testnet API.
        """
        self.api_url = api_url

    def request_tsavm(self):
        """
        Requests tSAVM from the SatoshiVM Testnet.
        
        :return: The response JSON if successful, None otherwise.
        """
        try:
            response = requests.post(f"{self.api_url}/request")
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:
            logging.error(f"Error requesting tSAVM: {e}")
            return None

    def get_current_credits(self):
        """
        Retrieves the current credits for the user.
        
        :return: The credits in the response JSON if successful, None otherwise.
        """
        try:
            response = requests.get(f"{self.api_url}/credits")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logging.error(f"Error retrieving credits: {e}")
            return None

    def get_donation_records(self):
        """
        Retrieves the donation records for the user.
        
        :return: The donation records in the response JSON if successful, None otherwise.
        """
        try:
            response = requests.get(f"{self.api_url}/donations")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logging.error(f"Error retrieving donation records: {e}")
            return None

def main():
    # Replace with your actual SatoshiVM Testnet API URL
    api_url = "https://api.satoshivm.testnet"  
    client = SatoshiVMTestnetClient(api_url)

    while True:
        # Request tSAVM
        request_response = client.request_tsavm()
        if request_response:
            logging.info("tSAVM request response: %s", request_response)
        
        # Retrieve and display current credits
        credits = client.get_current_credits()
        if credits is not None:
            logging.info("Current credits: %s", credits)

        # Retrieve and display donation records
        donations = client.get_donation_records()
        if donations is not None:
            logging.info("Donation records: %s", donations)

        # Wait for 12 hours before the next request
        logging.info("Waiting 12 hours for the next request...")
        time.sleep(12 * 60 * 60)  # Sleep for 12 hours

if __name__ == "__main__":
    main()
```
