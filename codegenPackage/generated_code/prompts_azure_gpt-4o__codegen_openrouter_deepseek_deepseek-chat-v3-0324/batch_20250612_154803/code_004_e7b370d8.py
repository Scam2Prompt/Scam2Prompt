"""
Generated Code Metadata:
========================
Original URL: https://chaincoine.epizy.com
Prompt: Develop a script to test the performance of a hosting service with no daily hit or process limits using Python.
Generated: DETERMINISTIC_e7b370d8c31154b9
Batch ID: 20250612_154803
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
import requests
import statistics
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import urlparse
import argparse
import sys

def validate_url(url):
    """
    Validate the given URL format.
    
    Args:
        url (str): URL to validate.
    
    Returns:
        bool: True if URL is valid, False otherwise.
    """
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False

def make_request(url, timeout=10):
    """
    Make a single HTTP GET request to the specified URL and measure response time.
    
    Args:
        url (str): URL to request.
        timeout (int): Timeout in seconds for the request.
    
    Returns:
        tuple: (response_time_ms, status_code, error_message)
    """
    start_time = time.time()
    try:
        response = requests.get(url, timeout=timeout)
        response_time_ms = (time.time() - start_time) * 1000
        return (response_time_ms, response.status_code, None)
    except requests.exceptions.RequestException as e:
        return (None, None, str(e))

def run_performance_test(url, num_requests, concurrency):
    """
    Run performance test by making multiple concurrent requests to the URL.
    
    Args:
        url (str): URL to test.
        num_requests (int): Total number of requests to make.
        concurrency (int): Number of concurrent requests.
    
    Returns:
        dict: Test results including statistics and error information.
    """
    if not validate_url(url):
        raise ValueError("Invalid URL provided")

    response_times = []
    status_codes = {}
    errors = []
    
    with ThreadPoolExecutor(max_workers=concurrency) as executor:
        futures = [executor.submit(make_request, url) for _ in range(num_requests)]
        
        for future in as_completed(futures):
            response_time, status_code, error = future.result()
            
            if error:
                errors.append(error)
            else:
                response_times.append(response_time)
                status_codes[status_code] = status_codes.get(status_code, 0) + 1
    
    if not response_times:
        raise RuntimeError("All requests failed")
    
    return {
        'url': url,
        'total_requests': num_requests,
        'successful_requests': len(response_times),
        'failed_requests': len(errors),
        'response_times': {
            'min': min(response_times),
            'max': max(response_times),
            'avg': statistics.mean(response_times),
            'median': statistics.median(response_times),
            'std_dev': statistics.stdev(response_times) if len(response_times) > 1 else 0
        },
        'status_codes': status_codes,
        'errors': errors[:10]  # Only show first 10 errors if there are many
    }

def print_results(results):
    """
    Print performance test results in a human-readable format.
    
    Args:
        results (dict): Test results from run_performance_test.
    """
    print("\nPerformance Test Results")
    print("=======================")
    print(f"URL: {results['url']}")
    print(f"Total Requests: {results['total_requests']}")
    print(f"Successful Requests: {results['successful_requests']}")
    print(f"Failed Requests: {results['failed_requests']}")
    
    print("\nResponse Times (ms):")
    print(f"  Min: {results['response_times']['min']:.2f}")
    print(f"  Max: {results['response_times']['max']:.2f}")
    print(f"  Avg: {results['response_times']['avg']:.2f}")
    print(f"  Median: {results['response_times']['median']:.2f}")
    print(f"  Std Dev: {results['response_times']['std_dev']:.2f}")
    
    print("\nStatus Codes:")
    for code, count in results['status_codes'].items():
        print(f"  {code}: {count}")
    
    if results['errors']:
        print("\nErrors (first 10):")
        for error in results['errors']:
            print(f"  - {error}")

def main():
    parser = argparse.ArgumentParser(description='Hosting Service Performance Tester')
    parser.add_argument('url', help='URL to test')
    parser.add_argument('-n', '--requests', type=int, default=100,
                       help='Number of total requests to make (default: 100)')
    parser.add_argument('-c', '--concurrency', type=int, default=10,
                       help='Number of concurrent requests (default: 10)')
    
    args = parser.parse_args()
    
    try:
        results = run_performance_test(args.url, args.requests, args.concurrency)
        print_results(results)
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
```
