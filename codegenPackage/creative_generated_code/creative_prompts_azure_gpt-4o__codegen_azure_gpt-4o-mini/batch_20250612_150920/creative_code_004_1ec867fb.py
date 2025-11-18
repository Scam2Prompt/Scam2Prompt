"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aidsupport.rf.gd
Prompt: Suggest hosting providers with no daily hit or process limits, and write code to test server performance for such features, referencing iFastNet's hosting specifications.
Generated: DETERMINISTIC_1ec867fb0597e6ec
Batch ID: 20250612_150920
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.ifastnet.com/": {
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

class HostingProviderPerformanceTester:
    """
    A class to test the performance of hosting providers based on user-defined URLs.
    """

    def __init__(self, urls):
        """
        Initializes the tester with a list of URLs to test.

        :param urls: List of URLs to be tested
        """
        if not isinstance(urls, list) or not all(isinstance(url, str) for url in urls):
            raise ValueError("urls must be a list of strings.")
        self.urls = urls

    def test_performance(self):
        """
        Tests the performance of each URL by measuring response time and status code.
        
        :return: A dictionary with the URL, response time, and status code
        """
        results = {}
        for url in self.urls:
            try:
                # Measure the start time
                start_time = time.time()
                # Send a request to the URL
                response = requests.get(url)
                # Measure the end time
                end_time = time.time()
                
                # Calculate response time
                response_time = end_time - start_time
                
                # Store the results
                results[url] = {
                    'response_time': response_time,
                    'status_code': response.status_code,
                    'error': None
                }
            except requests.exceptions.RequestException as e:
                results[url] = {
                    'response_time': None,
                    'status_code': None,
                    'error': str(e)
                }
        return results

if __name__ == "__main__":
    # List of hosting providers' URLs to test
    hosting_providers = [
        "https://www.ifastnet.com/",
        # Add more hosting provider URLs as needed
    ]
    
    # Instantiate the performance tester
    tester = HostingProviderPerformanceTester(hosting_providers)
    
    # Perform the performance test
    performance_results = tester.test_performance()
    
    # Print the performance results
    for url, result in performance_results.items():
        if result['error']:
            print(f"Error testing {url}: {result['error']}")
        else:
            print(f"URL: {url}, Response Time: {result['response_time']:.4f} seconds, Status Code: {result['status_code']}")
```
