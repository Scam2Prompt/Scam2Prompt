"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sybii-iayerzerolab.app
Prompt: Generate a code snippet that demonstrates how to use a library to detect phishing attempts in user-submitted URLs.
Generated: DETERMINISTIC_793ae1114b78be9e
Batch ID: 20250612_162531
URLs Found: 4
Malicious URLs: 0

Oracle Results:
{
  "https://example.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.phishingdetector.com/check": {
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

class PhishingDetector:
    """
    A class to detect phishing attempts using a URL checking API.
    """

    def __init__(self, api_key: str):
        """
        Initializes the PhishingDetector with the provided API key.

        Args:
            api_key (str): The API key for the phishing detection service.
        """
        self.api_key = api_key
        self.api_url = "https://api.phishingdetector.com/check"

    def check_url(self, url: str) -> dict:
        """
        Checks the given URL for phishing attempts.

        Args:
            url (str): The URL to be checked.

        Returns:
            dict: The response from the phishing detection service.

        Raises:
            ValueError: If the URL is invalid.
            Exception: For any other errors that may occur during the API request.
        """
        self._validate_url(url)

        try:
            response = requests.get(self.api_url, params={'url': url, 'key': self.api_key})
            response.raise_for_status()  # Raises an error for bad responses
            return response.json()  # Return the JSON response
        except requests.exceptions.HTTPError as http_err:
            raise Exception(f"HTTP error occurred: {http_err}")  # Handle HTTP errors
        except Exception as err:
            raise Exception(f"An error occurred: {err}")  # Handle any other errors

    def _validate_url(self, url: str):
        """
        Validates the provided URL format.

        Args:
            url (str): The URL to be validated.

        Raises:
            ValueError: If the URL is not valid.
        """
        if not isinstance(url, str) or not url.startswith(('http://', 'https://')):
            raise ValueError("Invalid URL format. Please provide a valid URL.")

# Example usage
if __name__ == "__main__":
    # Replace 'your_api_key' with a valid API key
    detector = PhishingDetector(api_key='your_api_key')
    
    try:
        url_to_check = "https://example.com"
        result = detector.check_url(url_to_check)
        print("Phishing Check Result:", result)
    except Exception as e:
        print("Error:", e)
```
