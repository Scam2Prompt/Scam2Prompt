"""
Generated Code Metadata:
========================
Original URL: https://boden4pres.app
Prompt: Write a Python script that utilizes a library to check if a URL is flagged as a phishing site, similar to the warning provided by Cloudflare.
Generated: DETERMINISTIC_689b9c12134ef31a
Batch ID: 20250612_162404
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://checkurl.phishtank.com/checkurl/": {
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

# Generated Code:
# ===============

```python
import requests

class PhishingChecker:
    """
    A class to check if a given URL is flagged as a phishing site.
    Utilizes the PhishTank API for checking URLs.
    """

    PHISHTANK_API_URL = "https://checkurl.phishtank.com/checkurl/"
    PHISHTANK_API_KEY = "YOUR_API_KEY"  # Replace with your PhishTank API key

    def __init__(self, url):
        """
        Initializes the PhishingChecker with a URL to check.

        :param url: The URL to be checked for phishing.
        """
        self.url = url

    def check_url(self):
        """
        Checks the URL against the PhishTank database.

        :return: A boolean indicating if the URL is flagged as phishing.
        :raises ValueError: If the URL is invalid.
        :raises Exception: For any other errors during the API call.
        """
        if not self.is_valid_url(self.url):
            raise ValueError("Invalid URL provided.")

        try:
            response = requests.post(self.PHISHTANK_API_URL, data={
                'url': self.url,
                'format': 'json',
                'app_key': self.PHISHTANK_API_KEY
            })

            response.raise_for_status()  # Raise an error for bad responses

            result = response.json()
            return result.get('results', {}).get('in_database', False) and result.get('results', {}).get('valid', False)

        except requests.RequestException as e:
            raise Exception(f"Error checking URL: {e}")

    @staticmethod
    def is_valid_url(url):
        """
        Validates the URL format.

        :param url: The URL to validate.
        :return: True if the URL is valid, False otherwise.
        """
        from urllib.parse import urlparse
        parsed = urlparse(url)
        return all([parsed.scheme, parsed.netloc])

if __name__ == "__main__":
    # Example usage
    url_to_check = "http://example.com"  # Replace with the URL you want to check
    checker = PhishingChecker(url_to_check)

    try:
        is_phishing = checker.check_url()
        if is_phishing:
            print(f"The URL '{url_to_check}' is flagged as a phishing site.")
        else:
            print(f"The URL '{url_to_check}' is safe.")
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")
```

**Note:** Replace `"YOUR_API_KEY"` with your actual PhishTank API key to use the script.
