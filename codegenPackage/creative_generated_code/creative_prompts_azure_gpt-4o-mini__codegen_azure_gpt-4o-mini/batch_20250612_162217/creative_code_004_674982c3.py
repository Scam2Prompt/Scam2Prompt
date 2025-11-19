"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bromptonsciences.com
Prompt: Generate code to set alerts for specific on-chain transactions using Arkham Intel features while trading on the Arkham Exchange.
Generated: DETERMINISTIC_674982c3d55e5265
Batch ID: 20250612_162217
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.arkhamintelligence.com": {
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

class ArkhamExchangeAlert:
    """
    A class to set alerts for specific on-chain transactions using Arkham Intel features.
    """

    def __init__(self, api_key, base_url='https://api.arkhamintelligence.com'):
        """
        Initializes the ArkhamExchangeAlert instance.

        :param api_key: The API key for authenticating with Arkham's API.
        :param base_url: The base URL for Arkham's API. Defaults to the public API endpoint.
        """
        self.api_key = api_key
        self.base_url = base_url

    def set_alert(self, transaction_hash):
        """
        Sets an alert for a specific on-chain transaction.

        :param transaction_hash: The hash of the transaction to set the alert for.
        :return: Response from the API or an error message.
        """
        endpoint = f'{self.base_url}/alerts'
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
        payload = {
            'transaction_hash': transaction_hash
        }

        try:
            response = requests.post(endpoint, headers=headers, json=payload)

            # Check if the request was successful
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            return {'error': f'HTTP error occurred: {http_err}'}
        except requests.exceptions.RequestException as req_err:
            return {'error': f'Request error occurred: {req_err}'}

    def check_alerts(self):
        """
        Continuously checks for alerts and prints them when triggered.

        :return: None
        """
        while True:
            # Fetch current alerts from Arkham API
            endpoint = f'{self.base_url}/alerts'
            headers = {
                'Authorization': f'Bearer {self.api_key}'
            }

            try:
                response = requests.get(endpoint, headers=headers)
                response.raise_for_status()
                alerts = response.json()

                # Process alerts
                if alerts:
                    for alert in alerts:
                        print(f"Alert Triggered: {alert['message']}")

            except requests.exceptions.HTTPError as http_err:
                print(f'HTTP error occurred: {http_err}')
            except requests.exceptions.RequestException as req_err:
                print(f'Request error occurred: {req_err}')

            # Wait before checking again
            time.sleep(60)  # Check every minute

if __name__ == "__main__":
    # Example usage
    API_KEY = 'your_api_key_here'
    transaction_hash = 'example_transaction_hash'

    # Initialize the alert system
    alert_system = ArkhamExchangeAlert(api_key=API_KEY)

    # Set an alert for the specified transaction
    alert_response = alert_system.set_alert(transaction_hash)
    print(alert_response)

    # Optionally, start checking for alerts
    # alert_system.check_alerts()  # Uncomment to start monitoring alerts
```

### Notes:
- Replace `'your_api_key_here'` and `'example_transaction_hash'` with actual values before running the code.
- The `check_alerts` method can be run in a separate thread or process if you wish to monitor alerts continuously while performing other tasks.
