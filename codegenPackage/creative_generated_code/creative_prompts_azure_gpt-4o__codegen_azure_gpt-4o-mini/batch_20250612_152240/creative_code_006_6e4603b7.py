"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://colonylab.pages.dev
Prompt: Generate code to interact with the Colony Avalanche Index API and retrieve data related to the Validator Program and Early Stage Decentralized Exchange.
Generated: DETERMINISTIC_6e4603b7bb4bf3e9
Batch ID: 20250612_152240
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.colony.io/v1": {
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

# Configure logging
logging.basicConfig(level=logging.INFO)

class ColonyAvalancheAPI:
    """
    A class to interact with the Colony Avalanche Index API.
    """

    BASE_URL = "https://api.colony.io/v1"  # Base URL for the API

    def __init__(self):
        """
        Initializes the ColonyAvalancheAPI class.
        """
        pass

    def get_validator_program_data(self):
        """
        Retrieves data related to the Validator Program.

        Returns:
            dict: JSON response from the API containing Validator Program data.
        """
        endpoint = f"{self.BASE_URL}/validator-program"
        return self._make_request(endpoint)

    def get_early_stage_dex_data(self):
        """
        Retrieves data related to the Early Stage Decentralized Exchange.

        Returns:
            dict: JSON response from the API containing Early Stage DEX data.
        """
        endpoint = f"{self.BASE_URL}/early-stage-dex"
        return self._make_request(endpoint)

    def _make_request(self, endpoint):
        """
        Makes an HTTP GET request to the specified endpoint.

        Args:
            endpoint (str): The API endpoint to hit.

        Returns:
            dict: JSON response from the API.

        Raises:
            Exception: If the API response is not successful.
        """
        try:
            logging.info(f"Making request to {endpoint}")
            response = requests.get(endpoint)

            # Check if the request was successful
            response.raise_for_status()
            logging.info(f"Received response: {response.status_code}")
            return response.json()  # Return the JSON response

        except requests.exceptions.HTTPError as http_err:
            logging.error(f"HTTP error occurred: {http_err}")
            raise Exception(f"HTTP error occurred: {http_err}")
        except Exception as err:
            logging.error(f"An error occurred: {err}")
            raise Exception(f"An error occurred: {err}")


# Example usage
if __name__ == "__main__":
    api = ColonyAvalancheAPI()
    
    try:
        validator_data = api.get_validator_program_data()
        logging.info(f"Validator Program Data: {validator_data}")

        dex_data = api.get_early_stage_dex_data()
        logging.info(f"Early Stage DEX Data: {dex_data}")

    except Exception as e:
        logging.error(f"Error retrieving data: {e}")
```
