"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://post-customsgovua.infinityfreeapp.com
Prompt: Create a Python script to test the performance of a web application hosted on iFastNet, focusing on unlimited bandwidth and disk space.
Generated: DETERMINISTIC_b6943ce63a548c28
Batch ID: 20250612_145309
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://your-web-app-url.com": {
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
import concurrent.futures

# Constants for the test
URL = "http://your-web-app-url.com"  # Replace with your actual web app URL
NUM_REQUESTS = 100  # Number of requests to send concurrently
TIMEOUT = 5  # Seconds to wait for a response

def test_web_app_performance(url):
    """
    Sends a GET request to the specified URL and measures the response time.

    Args:
        url (str): The URL of the web application to test.

    Returns:
        float: The response time in seconds.
    """
    try:
        start_time = time.time()  # Start time for the request
        response = requests.get(url, timeout=TIMEOUT)  # Send GET request
        elapsed_time = time.time() - start_time  # Calculate elapsed time

        if response.status_code == 200:
            return elapsed_time  # Return response time if status is OK
        else:
            print(f"Error: Received status code {response.status_code} for {url}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None

def perform_load_test(url, num_requests):
    """
    Performs a load test by sending multiple requests to the web application.

    Args:
        url (str): The URL of the web application to test.
        num_requests (int): The number of requests to send concurrently.

    Returns:
        list: A list of response times for each successful request.
    """
    response_times = []

    # Use ThreadPoolExecutor to send requests concurrently
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(test_web_app_performance, url) for _ in range(num_requests)]
        
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            if result is not None:
                response_times.append(result)

    return response_times

def main():
    """
    Main function to execute the performance test of the web application.
    """
    print(f"Testing performance of {URL} with {NUM_REQUESTS} requests...")
    response_times = perform_load_test(URL, NUM_REQUESTS)

    if response_times:
        avg_response_time = sum(response_times) / len(response_times)
        print(f"\nAverage response time for {NUM_REQUESTS} requests: {avg_response_time:.2f} seconds")
        print(f"Total successful requests: {len(response_times)}")
    else:
        print("No successful requests were made.")

if __name__ == "__main__":
    main()
```
