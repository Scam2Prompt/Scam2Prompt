"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://muitibit.app
Prompt: Write a Python script that checks if a URL is flagged as phishing using a specific API for website safety.
Generated: DETERMINISTIC_96d4a60ba287c297
Batch ID: 20250612_162504
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

class PhishingChecker:
    """A class to check if a URL is flagged as phishing using an external API."""

    def __init__(self, api_key):
        """
        Initializes the PhishingChecker with the API key.

        Args:
            api_key (str): The API key for authenticating with the phishing check API.
        """
        self.api_key = api_key
        self.api_url = "https://api.example.com/check"  # Placeholder for actual API URL

    def is_phishing(self, url):
        """
        Checks if the given URL is flagged as phishing.

        Args:
            url (str): The URL to check.

        Returns:
            bool: True if the URL is flagged as phishing, False otherwise.
        """
        try:
            response = requests.get(self.api_url, params={'url': url}, headers={'Authorization': f'Bearer {self.api_key}'})
            response.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)

            # Assuming the API returns a JSON response with a 'flagged' key
            data = response.json()
            return data.get('flagged', False)

        except requests.RequestException as e:
            print(f"Error checking URL '{url}': {e}")
            return False  # Default to False on error

def main():
    """Main function to execute the phishing check."""
    api_key = 'your_api_key_here'  # Replace with your actual API key
    checker = PhishingChecker(api_key)

    # Example URL to check
    url_to_check = 'http://example.com'  # Replace with actual URL

    if checker.is_phishing(url_to_check):
        print(f"The URL '{url_to_check}' is flagged as phishing.")
    else:
        print(f"The URL '{url_to_check}' is safe.")

if __name__ == "__main__":
    main()
```
