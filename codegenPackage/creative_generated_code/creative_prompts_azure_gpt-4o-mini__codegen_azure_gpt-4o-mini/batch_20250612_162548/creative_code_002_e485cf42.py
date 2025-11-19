"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ciaim-aerodrome.app
Prompt: Write a Python script that checks if a URL has been flagged as phishing, using APIs that provide website safety ratings.
Generated: DETERMINISTIC_e485cf4210a5b520
Batch ID: 20250612_162548
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/check": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
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

class URLChecker:
    """Class to check if a URL has been flagged as phishing using an external API."""

    def __init__(self, api_key: str):
        """
        Initialize URLChecker with an API key.

        :param api_key: API key for accessing the safety rating service.
        """
        self.api_key = api_key
        self.api_url = "https://api.example.com/check"  # Replace with actual API endpoint

    def check_url(self, url: str) -> dict:
        """
        Check if the provided URL is flagged as phishing.

        :param url: The URL to check.
        :return: Dictionary with the safety status and details.
        """
        try:
            response = requests.get(self.api_url, params={'url': url, 'apikey': self.api_key})
            response.raise_for_status()  # Raise an error for bad responses

            # Assuming the API returns a JSON response
            return response.json()
        
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # Log HTTP errors
            return {"error": "HTTP error occurred", "details": str(http_err)}
        
        except requests.exceptions.RequestException as req_err:
            print(f"Request error occurred: {req_err}")  # Log other request errors
            return {"error": "Request error occurred", "details": str(req_err)}

def main():
    """Main function to execute the URL checker."""
    api_key = "your_api_key_here"  # Replace with your actual API key
    url_checker = URLChecker(api_key)

    # Example URL to check
    url_to_check = "http://example.com"

    result = url_checker.check_url(url_to_check)

    # Print the result
    if 'error' in result:
        print(result)
    else:
        print(f"URL: {url_to_check} - Safety Status: {result.get('status')}")
        print(f"Details: {result.get('details')}")

if __name__ == "__main__":
    main()
```
