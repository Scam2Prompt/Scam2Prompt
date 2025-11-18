"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-3338--nostalgic-ptolemy-b01ab8.netlify.app
Prompt: Generate code to monitor Linode instances using the Linode API, retrieving metrics such as CPU usage and network activity.
Generated: DETERMINISTIC_b95ae9a1f9275c3f
Batch ID: 20250612_151018
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.linode.com/v4": {
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

class LinodeMonitor:
    """
    A class to monitor Linode instances using the Linode API.
    It retrieves metrics such as CPU usage and network activity.
    """

    def __init__(self, api_token, interval=60):
        """
        Initializes the LinodeMonitor with the provided API token and monitoring interval.

        :param api_token: Linode API token for authentication.
        :param interval: Time in seconds between each metric retrieval (default is 60 seconds).
        """
        self.api_token = api_token
        self.interval = interval
        self.base_url = 'https://api.linode.com/v4'
        self.headers = {
            'Authorization': f'Bearer {self.api_token}',
            'Content-Type': 'application/json'
        }

    def get_instances(self):
        """
        Retrieves a list of Linode instances.

        :return: List of instances or None if an error occurs.
        """
        try:
            response = requests.get(f'{self.base_url}/linode/instances', headers=self.headers)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()['data']
        except requests.RequestException as e:
            print(f"Error retrieving instances: {e}")
            return None

    def get_metrics(self, instance_id):
        """
        Retrieves metrics for a specific Linode instance.

        :param instance_id: The ID of the Linode instance to retrieve metrics for.
        :return: A dictionary of metrics or None if an error occurs.
        """
        try:
            response = requests.get(f'{self.base_url}/linode/instances/{instance_id}/stats', headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error retrieving metrics for instance {instance_id}: {e}")
            return None

    def monitor(self):
        """
        Starts monitoring the Linode instances and prints their metrics at specified intervals.
        """
        while True:
            instances = self.get_instances()
            if instances is None:
                break

            for instance in instances:
                metrics = self.get_metrics(instance['id'])
                if metrics is not None:
                    print(f"Instance ID: {instance['id']}, "
                          f"Label: {instance['label']}, "
                          f"CPU Usage: {metrics.get('cpu', 'N/A')}%, "
                          f"Network In: {metrics.get('network_in', 'N/A')} bytes, "
                          f"Network Out: {metrics.get('network_out', 'N/A')} bytes")

            time.sleep(self.interval)

if __name__ == "__main__":
    # Replace 'your_api_token_here' with your actual Linode API token
    linode_api_token = 'your_api_token_here'
    monitor = LinodeMonitor(api_token=linode_api_token)
    monitor.monitor()
```
