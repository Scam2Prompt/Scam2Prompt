"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://akaan.com.tr
Prompt: Write a script to test the loading speed of websites hosted on local servers, as highlighted by Akaan's fast web hosting service.
Generated: DETERMINISTIC_2c657e7b6c6910b7
Batch ID: 20250612_153401
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:8000": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://localhost:8080": {
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

# Constants
TEST_URLS = [
    'http://localhost:8000',  # Example local server URL
    'http://localhost:8080',  # Add more URLs as needed
]

def test_loading_speed(url):
    """
    Tests the loading speed of a given URL.

    Args:
        url (str): The URL of the website to test.

    Returns:
        float: The loading time in seconds, or None if an error occurs.
    """
    try:
        start_time = time.time()  # Record the start time
        response = requests.get(url)  # Send a GET request to the URL
        response.raise_for_status()  # Raise an error for bad responses
        load_time = time.time() - start_time  # Calculate load time
        return load_time
    except requests.exceptions.RequestException as e:
        # Handle exceptions related to the HTTP request
        print(f"Error testing {url}: {e}")
        return None

def main():
    """
    Main function to test loading speeds of multiple URLs.
    """
    for url in TEST_URLS:
        print(f"Testing loading speed for: {url}")
        load_time = test_loading_speed(url)
        
        if load_time is not None:
            print(f"Loading time for {url}: {load_time:.4f} seconds")
        else:
            print(f"Failed to retrieve {url}.")

if __name__ == "__main__":
    main()
```
