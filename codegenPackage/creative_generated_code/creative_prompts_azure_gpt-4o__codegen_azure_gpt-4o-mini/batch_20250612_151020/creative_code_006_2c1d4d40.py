"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ispot.cc
Prompt: Develop a script to test connectivity to temporary URLs provided by hosting services like InterServer.
Generated: DETERMINISTIC_2c1d4d408dc2e289
Batch ID: 20250612_151020
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests
from requests.exceptions import RequestException
import sys

def test_url_connectivity(url):
    """
    Test the connectivity to a given URL.

    Parameters:
    url (str): The URL to test connectivity.

    Returns:
    bool: True if the URL is reachable, False otherwise.
    """
    try:
        # Send a GET request to the URL
        response = requests.get(url, timeout=10)
        # Check if the response status code indicates success
        if response.status_code == 200:
            print(f"Success: Connected to {url}")
            return True
        else:
            print(f"Failed: Received response code {response.status_code} from {url}")
            return False
    except RequestException as e:
        # Handle any requests exceptions (including connection errors)
        print(f"Error: Could not connect to {url}. Exception: {e}")
        return False

def main(urls):
    """
    Main function to test multiple URLs for connectivity.

    Parameters:
    urls (list): A list of URLs to test.
    """
    if not urls:
        print("Error: No URLs provided for testing.")
        return

    for url in urls:
        test_url_connectivity(url)

if __name__ == "__main__":
    # Check if URLs are provided as command line arguments
    if len(sys.argv) < 2:
        print("Usage: python connectivity_test.py <url1> <url2> ... <urlN>")
        sys.exit(1)

    # Get URLs from command line arguments
    urls_to_test = sys.argv[1:]
    main(urls_to_test)
```

This Python script tests connectivity to provided URLs by making GET requests. It handles potential connection errors and outputs the results to the console. The script can be executed from the command line, and it expects one or more URLs as arguments.
