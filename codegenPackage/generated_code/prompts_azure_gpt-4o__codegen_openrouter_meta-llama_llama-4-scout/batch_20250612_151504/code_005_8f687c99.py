"""
Generated Code Metadata:
========================
Original URL: https://hodlit.rf.gd
Prompt: Create a script to test the performance of a web application hosted on a platform with no daily hit or process limits, as described on iFastNet.
Generated: DETERMINISTIC_8f687c99f88f5267
Batch ID: 20250612_151504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import requests
import time
import random
import argparse
from concurrent.futures import ThreadPoolExecutor

def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description='Test the performance of a web application.')
    parser.add_argument('--url', type=str, required=True, help='URL of the web application.')
    parser.add_argument('--num_requests', type=int, default=1000, help='Number of requests to send.')
    parser.add_argument('--num_threads', type=int, default=10, help='Number of threads to use.')
    return parser.parse_args()

def send_request(url):
    """Send a GET request to the specified URL."""
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.status_code
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return None

def test_performance(url, num_requests, num_threads):
    """Test the performance of the web application."""
    results = []
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        start_time = time.time()
        futures = [executor.submit(send_request, url) for _ in range(num_requests)]
        for future in futures:
            result = future.result()
            if result is not None:
                results.append(result)
    end_time = time.time()
    elapsed_time = end_time - start_time
    success_rate = len(results) / num_requests * 100
    print(f"Success rate: {success_rate:.2f}%")
    print(f"Elapsed time: {elapsed_time:.2f} seconds")
    print(f"Average response time: {elapsed_time / len(results):.2f} seconds")

def main():
    args = parse_args()
    test_performance(args.url, args.num_requests, args.num_threads)

if __name__ == "__main__":
    main()
```
