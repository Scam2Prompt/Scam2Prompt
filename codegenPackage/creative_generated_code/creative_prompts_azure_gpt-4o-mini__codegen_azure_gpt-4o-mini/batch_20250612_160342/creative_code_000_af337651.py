"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vertiv.dns.cz
Prompt: Generate a code snippet for integrating Vertiv's power management solutions into a cloud-based application.
Generated: DETERMINISTIC_af3376518e60e028
Batch ID: 20250612_160342
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.vertiv.com/v1": {
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
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class VertivPowerManagement:
    """
    Class to interact with Vertiv's power management solutions via their API.
    """

    def __init__(self, api_key, base_url):
        """
        Initialize the VertivPowerManagement class.

        :param api_key: The API key for authenticating with Vertiv's API.
        :param base_url: The base URL for the Vertiv API.
        """
        self.api_key = api_key
        self.base_url = base_url

    def _make_request(self, endpoint, method='GET', data=None):
        """
        Make an HTTP request to the Vertiv API.

        :param endpoint: API endpoint to call.
        :param method: HTTP method (GET, POST, etc.).
        :param data: Payload for POST requests.
        :return: Response JSON if successful, raises an exception otherwise.
        """
        url = f"{self.base_url}/{endpoint}"
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }

        try:
            if method == 'GET':
                response = requests.get(url, headers=headers)
            elif method == 'POST':
                response = requests.post(url, headers=headers, data=json.dumps(data))
            else:
                raise ValueError("Unsupported HTTP method: {}".format(method))

            response.raise_for_status()

            return response.json()
        except requests.exceptions.HTTPError as http_err:
            logging.error(f"HTTP error occurred: {http_err}")
            raise
        except Exception as err:
            logging.error(f"An error occurred: {err}")
            raise

    def get_power_metrics(self):
        """
        Retrieve the power metrics from Vertiv's API.

        :return: Parsed JSON response containing power metrics.
        """
        logging.info("Fetching power metrics from Vertiv API.")
        return self._make_request('metrics/power')

    def update_power_configuration(self, config_data):
        """
        Update the power configuration.

        :param config_data: Dictionary containing configuration data to be updated.
        :return: Response JSON from the API after updating configuration.
        """
        logging.info("Updating power configuration in Vertiv API.")
        return self._make_request('config/update', method='POST', data=config_data)

# Example usage
if __name__ == "__main__":
    try:
        vertiv_api_key = 'your_api_key_here'
        vertiv_base_url = 'https://api.vertiv.com/v1'

        power_manager = VertivPowerManagement(vertiv_api_key, vertiv_base_url)

        # Get power metrics
        metrics = power_manager.get_power_metrics()
        logging.info(f"Power Metrics: {metrics}")

        # Update power configuration (example configuration data)
        config_data = {
            'parameter1': 'value1',
            'parameter2': 'value2'
        }
        update_response = power_manager.update_power_configuration(config_data)
        logging.info(f"Update Response: {update_response}")

    except Exception as e:
        logging.error(f"An error occurred in the main execution: {e}")
```
