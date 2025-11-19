"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aethircioud.app
Prompt: Write a Python script that utilizes a library to validate URLs against known phishing databases.
Generated: DETERMINISTIC_86e266b5b72ce60c
Batch ID: 20250612_162504
URLs Found: 4
Malicious URLs: 0

Oracle Results:
{
  "https://phishing-database-api.com/check": {
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

class URLValidator:
    """
    A class to validate URLs against known phishing databases.
    """

    PHISHING_API_URL = "https://phishing-database-api.com/check"

    def __init__(self, url):
        """
        Initializes the URLValidator with a URL to validate.

        Args:
            url (str): The URL to be validated.
        """
        self.url = url

    def validate_url(self):
        """
        Validates the URL against the phishing database.

        Returns:
            bool: True if the URL is safe, False if it's potentially a phishing URL.
        
        Raises:
            ValueError: If the URL is invalid.
            requests.exceptions.RequestException: If there is an issue with the HTTP request.
        """
        self._validate_url_format()
        response = self._query_phishing_database()
        return self._parse_response(response)

    def _validate_url_format(self):
        """
        Validates the URL format.

        Raises:
            ValueError: If the URL is invalid.
        """
        if not isinstance(self.url, str) or not self.url.startswith(('http://', 'https://')):
            raise ValueError(f"Invalid URL format: {self.url}")

    def _query_phishing_database(self):
        """
        Queries the phishing database for the URL.

        Returns:
            dict: The response from the phishing database API.

        Raises:
            requests.exceptions.RequestException: If there is an issue with the HTTP request.
        """
        try:
            response = requests.get(self.PHISHING_API_URL, params={'url': self.url})
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"HTTP request failed: {e}")

    def _parse_response(self, response):
        """
        Parses the response from the phishing database.

        Args:
            response (dict): The response from the phishing database API.

        Returns:
            bool: True if the URL is safe, False if it's potentially a phishing URL.
        """
        # Example of expected response structure
        if 'is_phishing' in response:
            return not response['is_phishing']
        else:
            raise RuntimeError("Unexpected response format from phishing database.")

if __name__ == "__main__":
    # Example usage
    url_to_check = "https://example.com"

    try:
        validator = URLValidator(url_to_check)
        is_safe = validator.validate_url()

        if is_safe:
            print(f"The URL '{url_to_check}' is safe.")
        else:
            print(f"The URL '{url_to_check}' is potentially a phishing site.")
    except ValueError as ve:
        print(f"Validation error: {ve}")
    except RuntimeError as re:
        print(f"Error checking URL: {re}")
```
