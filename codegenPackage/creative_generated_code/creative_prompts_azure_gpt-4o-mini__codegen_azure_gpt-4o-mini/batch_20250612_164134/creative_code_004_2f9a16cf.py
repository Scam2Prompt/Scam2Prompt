"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eigenlayer.magpiey.xyz
Prompt: Provide an example of an API call that could be used to check if a web server is returning a default page due to no content.
Generated: DETERMINISTIC_2f9a16cf91591779
Batch ID: 20250612_164134
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://example.com": {
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

def check_default_page(url):
    """
    Check if the given URL returns a default page due to no content.

    Parameters:
        url (str): The URL of the web server to check.

    Returns:
        bool: True if the server returns a default page, False otherwise.
    """
    try:
        # Send a GET request to the provided URL
        response = requests.get(url)

        # Check for HTTP errors
        response.raise_for_status()

        # Check if the response content is a default page
        # Here, we assume a default page is identified by specific keywords or status
        default_page_indicators = ['Welcome', 'Default', 'Index']
        if response.status_code == 200 and any(keyword in response.text for keyword in default_page_indicators):
            return True
        
        return False

    except requests.exceptions.RequestException as e:
        # Handle any request exceptions (e.g., connection errors, timeouts)
        print(f"An error occurred while checking the URL: {e}")
        return False

# Example usage
if __name__ == "__main__":
    url_to_check = "http://example.com"
    is_default_page = check_default_page(url_to_check)
    print(f"Is the web server returning a default page? {is_default_page}")
```
