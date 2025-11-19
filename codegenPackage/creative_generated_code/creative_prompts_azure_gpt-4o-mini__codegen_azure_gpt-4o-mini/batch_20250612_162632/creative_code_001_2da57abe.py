"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://allocation-evermoon.app
Prompt: What are the best practices for detecting and handling phishing attempts in a web service using APIs?
Generated: DETERMINISTIC_2da57abed37984e5
Batch ID: 20250612_162632
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.phishing-detection.com/check": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://example.com/suspicious": {
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
from urllib.parse import urlparse

class PhishingDetector:
    """
    A class to detect and handle phishing attempts using APIs.
    """

    def __init__(self, api_key: str):
        """
        Initializes the PhishingDetector with the provided API key.

        Args:
            api_key (str): API key for the phishing detection service.
        """
        self.api_key = api_key
        self.api_url = "https://api.phishing-detection.com/check"

    def is_phishing_url(self, url: str) -> bool:
        """
        Checks if the given URL is a phishing attempt.

        Args:
            url (str): The URL to check.

        Returns:
            bool: True if the URL is a phishing attempt, False otherwise.
        """
        # Validate the URL format
        parsed_url = urlparse(url)
        if not parsed_url.scheme or not parsed_url.netloc:
            raise ValueError("Invalid URL format")

        payload = {
            "url": url,
            "api_key": self.api_key
        }

        try:
            response = requests.post(self.api_url, json=payload)
            response.raise_for_status()  # Raise an error for bad responses

            result = response.json()
            # Assuming the response contains a 'phishing' key that indicates whether the URL is a phishing attempt
            return result.get('phishing', False)

        except requests.RequestException as e:
            # Log the error and raise a user-friendly exception
            print(f"Error while checking URL: {e}")
            raise RuntimeError("Failed to check URL for phishing attempts")

# Example usage:
if __name__ == "__main__":
    detector = PhishingDetector(api_key="your_api_key_here")
    
    test_url = "http://example.com/suspicious"  # Replace with the URL you want to check
    try:
        if detector.is_phishing_url(test_url):
            print("Warning: This URL is a phishing attempt!")
        else:
            print("This URL appears to be safe.")
    except ValueError as ve:
        print(f"Input Error: {ve}")
    except RuntimeError as re:
        print(f"Runtime Error: {re}")
```
