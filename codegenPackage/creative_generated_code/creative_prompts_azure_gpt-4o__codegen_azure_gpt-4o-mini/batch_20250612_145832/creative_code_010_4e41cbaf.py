"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://suifoundation.com
Prompt: Demonstrate how to use the Sui JSON-RPC API to monitor transactions per second (TPS) and network latency metrics.
Generated: DETERMINISTIC_4e41cbaf113f638b
Batch ID: 20250612_145832
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://your-sui-api-endpoint.com": {
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
import statistics

class SuiAPI:
    """
    A class to interact with the Sui JSON-RPC API for monitoring transactions per second (TPS)
    and network latency metrics.
    """

    def __init__(self, api_url):
        """
        Initialize the SuiAPI with the provided API URL.

        :param api_url: The base URL for the Sui JSON-RPC API.
        """
        self.api_url = api_url

    def send_request(self, method, params):
        """
        Send a JSON-RPC request to the Sui API.

        :param method: The JSON-RPC method to call.
        :param params: The parameters for the method.
        :return: The response from the API.
        """
        payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": method,
            "params": params
        }

        try:
            response = requests.post(self.api_url, json=payload)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"An error occurred: {err}")
        return None

    def get_tps(self):
        """
        Get the current transactions per second (TPS) from the Sui network.

        :return: The TPS value.
        """
        tps_response = self.send_request("sui_getTransactionsPerSecond", [])
        if tps_response and 'result' in tps_response:
            return tps_response['result']
        return None

    def get_latency(self):
        """
        Get the network latency metrics from the Sui network.

        :return: The latency value in milliseconds.
        """
        latency_response = self.send_request("sui_getNetworkLatency", [])
        if latency_response and 'result' in latency_response:
            return latency_response['result']
        return None

    def monitor_metrics(self, duration=60, interval=5):
        """
        Monitor transactions per second (TPS) and network latency over a specified duration.

        :param duration: Total time to run the monitoring (in seconds).
        :param interval: Time interval to report metrics (in seconds).
        """
        end_time = time.time() + duration
        tps_data = []
        latency_data = []

        while time.time() < end_time:
            tps = self.get_tps()
            latency = self.get_latency()

            if tps is not None:
                tps_data.append(tps)
                print(f"Current TPS: {tps}")

            if latency is not None:
                latency_data.append(latency)
                print(f"Current Latency: {latency} ms")

            time.sleep(interval)

        self.report_metrics(tps_data, latency_data)

    def report_metrics(self, tps_data, latency_data):
        """
        Print the summary of collected metrics.

        :param tps_data: List of TPS values collected.
        :param latency_data: List of latency values collected.
        """
        if tps_data:
            print(f"\nAverage TPS over the monitored period: {statistics.mean(tps_data):.2f}")
            print(f"Max TPS: {max(tps_data)}, Min TPS: {min(tps_data)}")

        if latency_data:
            print(f"\nAverage Latency over the monitored period: {statistics.mean(latency_data):.2f} ms")
            print(f"Max Latency: {max(latency_data)} ms, Min Latency: {min(latency_data)} ms")


if __name__ == "__main__":
    # Example usage
    API_URL = "https://your-sui-api-endpoint.com"  # Replace with your Sui JSON-RPC API endpoint
    sui_api = SuiAPI(API_URL)
    sui_api.monitor_metrics(duration=60, interval=5)  # Monitor for 60 seconds with 5-second intervals
```
