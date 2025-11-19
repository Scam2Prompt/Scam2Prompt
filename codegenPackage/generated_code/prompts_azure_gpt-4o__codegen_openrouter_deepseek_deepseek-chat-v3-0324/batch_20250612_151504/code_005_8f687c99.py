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
import statistics
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed

def send_request(url, timeout=10):
    """
    Send a single HTTP GET request to the specified URL.
    Returns the status code and response time in seconds.
    """
    start_time = time.time()
    try:
        response = requests.get(url, timeout=timeout)
        status_code = response.status_code
    except requests.exceptions.RequestException as e:
        status_code = str(e)
    end_time = time.time()
    response_time = end_time - start_time
    return status_code, response_time

def test_performance(url, num_requests, concurrency):
    """
    Test the performance of a web application by sending multiple concurrent requests.
    Returns performance statistics.
    """
    response_times = []
    status_codes = {}
    
    with ThreadPoolExecutor(max_workers=concurrency) as executor:
        futures = [executor.submit(send_request, url) for _ in range(num_requests)]
        
        for future in as_completed(futures):
            status_code, response_time = future.result()
            response_times.append(response_time)
            
            if status_code in status_codes:
                status_codes[status_code] += 1
            else:
                status_codes[status_code] = 1
    
    if not response_times:
        return None
    
    stats = {
        'total_requests': num_requests,
        'concurrency_level': concurrency,
        'status_codes': status_codes,
        'average_response_time': statistics.mean(response_times),
        'median_response_time': statistics.median(response_times),
        'min_response_time': min(response_times),
        'max_response_time': max(response_times),
        'success_rate': (status_codes.get(200, 0) / num_requests) * 100
    }
    
    return stats

def print_stats(stats):
    """Print performance statistics in a readable format."""
    if not stats:
        print("No results to display.")
        return
    
    print("\nPerformance Test Results:")
    print("-------------------------")
    print(f"Total Requests: {stats['total_requests']}")
    print(f"Concurrency Level: {stats['concurrency_level']}")
    print("\nStatus Codes:")
    for code, count in stats['status_codes'].items():
        print(f"  {code}: {count} requests")
    print("\nResponse Times (seconds):")
    print(f"  Average: {stats['average_response_time']:.4f}")
    print(f"  Median: {stats['median_response_time']:.4f}")
    print(f"  Min: {stats['min_response_time']:.4f}")
    print(f"  Max: {stats['max_response_time']:.4f}")
    print(f"\nSuccess Rate: {stats['success_rate']:.2f}%")

def main():
    parser = argparse.ArgumentParser(description='Web Application Performance Tester')
    parser.add_argument('url', help='URL of the web application to test')
    parser.add_argument('-n', '--num-requests', type=int, default=100,
                       help='Number of total requests to send (default: 100)')
    parser.add_argument('-c', '--concurrency', type=int, default=10,
                       help='Number of concurrent requests (default: 10)')
    
    args = parser.parse_args()
    
    print(f"Testing performance of {args.url}")
    print(f"Configuration: {args.num_requests} requests, {args.concurrency} concurrent workers")
    
    start_time = time.time()
    stats = test_performance(args.url, args.num_requests, args.concurrency)
    end_time = time.time()
    
    if stats:
        print_stats(stats)
        print(f"\nTotal test duration: {end_time - start_time:.2f} seconds")
    else:
        print("Error: No valid responses received.")

if __name__ == "__main__":
    main()
```
