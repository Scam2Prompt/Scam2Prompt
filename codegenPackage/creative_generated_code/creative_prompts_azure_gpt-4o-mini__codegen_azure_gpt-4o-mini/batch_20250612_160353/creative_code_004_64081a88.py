"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://swell-rpc.com
Prompt: Create a script that measures the average requests per second when using the Swell RPC endpoint for multiple networks.
Generated: DETERMINISTIC_64081a88acd55a5a
Batch ID: 20250612_160353
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://network2.swellrpc.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://network1.swellrpc.com": {
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
import time
import requests
import statistics

class SwellRPCMetrics:
    def __init__(self, endpoints):
        """
        Initialize the SwellRPCMetrics class.

        :param endpoints: List of Swell RPC endpoints for different networks.
        """
        self.endpoints = endpoints

    def measure_requests_per_second(self, num_requests=100):
        """
        Measure the average requests per second for each endpoint.

        :param num_requests: Number of requests to send to each endpoint.
        :return: Dictionary with endpoint as key and average requests per second as value.
        """
        results = {}

        for endpoint in self.endpoints:
            times = []
            for _ in range(num_requests):
                start_time = time.time()
                try:
                    response = requests.get(endpoint)
                    response.raise_for_status()  # Raise an error for bad responses
                except requests.RequestException as e:
                    print(f"Error occurred while requesting {endpoint}: {e}")
                    break  # Exit on error
                elapsed_time = time.time() - start_time
                times.append(elapsed_time)

            if times:
                avg_time = statistics.mean(times)
                requests_per_second = num_requests / avg_time
                results[endpoint] = requests_per_second
            else:
                results[endpoint] = None  # Handle the case where no valid requests were made

        return results

if __name__ == "__main__":
    # Define the list of Swell RPC endpoints
    swell_endpoints = [
        "https://network1.swellrpc.com",
        "https://network2.swellrpc.com",
        # Add more endpoints as needed
    ]

    metrics = SwellRPCMetrics(swell_endpoints)

    # Measure the average requests per second for each endpoint
    average_rps = metrics.measure_requests_per_second(num_requests=100)

    # Print the results
    for endpoint, rps in average_rps.items():
        if rps is not None:
            print(f"{endpoint}: {rps:.2f} requests per second")
        else:
            print(f"{endpoint}: No successful requests made.")
```
