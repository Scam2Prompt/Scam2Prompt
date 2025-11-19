"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://join-optimism.app
Prompt: Write a function that checks URLs for phishing characteristics using a specific API or library.
Generated: DETERMINISTIC_194c3bbe64aba2c5
Batch ID: 20250612_162404
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://www.example.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.phishingcheck.com/check": {
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

class PhishingChecker:
    """
    A class to check URLs for phishing characteristics using an external API.
    """
    
    def __init__(self, api_key):
        """
        Initializes the PhishingChecker with an API key.
        
        :param api_key: str - The API key for accessing the phishing detection service.
        """
        self.api_key = api_key
        self.api_url = "https://api.phishingcheck.com/check"  # Example API URL

    def check_url(self, url):
        """
        Checks a given URL for phishing characteristics.

        :param url: str - The URL to be checked.
        :return: dict - The response from the API containing phishing details.
        :raises ValueError: If the URL is invalid.
        :raises Exception: For other errors encountered during the API request.
        """
        if not self.is_valid_url(url):
            raise ValueError("Invalid URL provided.")

        try:
            response = requests.get(self.api_url, params={'url': url, 'api_key': self.api_key})
            response.raise_for_status()  # raises an error for bad responses (4xx or 5xx)
            return response.json()  # assuming the API returns JSON
        except requests.RequestException as e:
            raise Exception(f"Error checking URL: {e}")

    @staticmethod
    def is_valid_url(url):
        """
        Validates the URL format.

        :param url: str - The URL to validate.
        :return: bool - True if the URL is valid, False otherwise.
        """
        import re
        regex = re.compile(
            r'^(?:http|ftp)s?://'  # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
            r'localhost|'  # localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|'  # IP...
            r'\[?[A-F0-9]*:[A-F0-9:]+\]?)'  # IPv6...
            r'(?::\d+)?'  # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        return re.match(regex, url) is not None

# Example usage
if __name__ == "__main__":
    API_KEY = "your_api_key_here"  # Replace with your actual API key
    checker = PhishingChecker(API_KEY)

    try:
        url_to_check = "https://www.example.com"
        result = checker.check_url(url_to_check)
        print("Phishing Check Result:", result)
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")
```
