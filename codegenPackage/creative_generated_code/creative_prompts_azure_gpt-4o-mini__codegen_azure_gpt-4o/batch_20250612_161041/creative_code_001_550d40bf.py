"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://memeindex.it.com
Prompt: Can you provide a code snippet to check the availability of a webpage and handle errors gracefully in Python?
Generated: DETERMINISTIC_550d40bf5a6a445b
Batch ID: 20250612_161041
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com": {
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

def check_webpage_availability(url):
    """
    Checks the availability of a webpage by sending a GET request.

    :param url: The URL of the webpage to check.
    :return: None. Prints the status of the webpage.
    """
    try:
        # Send a GET request to the specified URL
        response = requests.get(url, timeout=10)
        
        # Check the response status code
        if response.status_code == 200:
            print(f"Webpage is available. Status Code: {response.status_code}")
        else:
            print(f"Webpage returned an unexpected status code: {response.status_code}")
    
    except requests.exceptions.Timeout:
        # Handle timeout errors
        print("Error: The request timed out.")
    
    except requests.exceptions.ConnectionError:
        # Handle connection errors
        print("Error: Failed to establish a connection to the website.")
    
    except requests.exceptions.RequestException as e:
        # Handle all other exceptions from the requests library
        print(f"Error: An error occurred while trying to access the webpage. Details: {e}")

if __name__ == "__main__":
    # Example usage
    url_to_check = "https://example.com"
    check_webpage_availability(url_to_check)
```
