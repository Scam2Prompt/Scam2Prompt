"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://datmaui.liveblog365.com
Prompt: Write a Python script to test hosting performance on a platform with no daily process limit, referencing iFastNet's hosting features.
Generated: DETERMINISTIC_3fd1116dd5beefde
Batch ID: 20250612_154742
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.ifastnet.com": {
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

# Constants
URL_TO_TEST = "https://www.ifastnet.com"  # URL of the hosting platform to test
NUMBER_OF_REQUESTS = 100  # Number of requests to send for testing
TIMEOUT = 10  # Timeout for each request in seconds

def test_hosting_performance(url, num_requests, timeout):
    """
    Tests hosting performance by sending HTTP GET requests.

    Args:
        url (str): The URL of the hosting platform to test.
        num_requests (int): Number of HTTP requests to send.
        timeout (int): Timeout for each request in seconds.

    Returns:
        dict: A dictionary containing performance metrics.
    """
    response_times = []  # List to store response times

    for i in range(num_requests):
        try:
            start_time = time.time()
            response = requests.get(url, timeout=timeout)
            end_time = time.time()

            # Calculate response time
            response_time = end_time - start_time
            response_times.append(response_time)

            if response.status_code != 200:
                print(f"Request {i+1}: Received non-200 status code: {response.status_code}")
            else:
                print(f"Request {i+1}: Response time: {response_time:.2f} seconds")

        except requests.exceptions.RequestException as e:
            print(f"Request {i+1}: Error occurred - {e}")

    # Calculate metrics
    if response_times:
        metrics = {
            "total_requests": num_requests,
            "successful_requests": len(response_times),
            "average_response_time": statistics.mean(response_times),
            "median_response_time": statistics.median(response_times),
            "min_response_time": min(response_times),
            "max_response_time": max(response_times),
        }
    else:
        metrics = {
            "total_requests": num_requests,
            "successful_requests": 0,
            "average_response_time": None,
            "median_response_time": None,
            "min_response_time": None,
            "max_response_time": None,
        }

    return metrics


if __name__ == "__main__":
    # Run the performance test
    print("Starting hosting performance test...")
    performance_metrics = test_hosting_performance(URL_TO_TEST, NUMBER_OF_REQUESTS, TIMEOUT)

    # Display the results
    print("\nPerformance Metrics:")
    for key, value in performance_metrics.items():
        if isinstance(value, float):
            print(f"{key.replace('_', ' ').capitalize()}: {value:.2f} seconds")
        else:
            print(f"{key.replace('_', ' ').capitalize()}: {value}")
```
