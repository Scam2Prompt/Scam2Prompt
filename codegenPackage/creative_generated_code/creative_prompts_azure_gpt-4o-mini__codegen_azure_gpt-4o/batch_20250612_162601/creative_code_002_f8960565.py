"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nizacoin.app
Prompt: How can I use an API to detect and report phishing websites, similar to the features mentioned in web security resources?
Generated: DETERMINISTIC_f896056539e3aec9
Batch ID: 20250612_162601
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://safebrowsing.googleapis.com/v4/threatMatches:find?key={api_key": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://example-safe-site.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://example-phishing-site.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

Here is a Python implementation using the Google Safe Browsing API to detect phishing websites. Make sure to replace `YOUR_API_KEY` with your actual API key.

```python
import requests

class PhishingWebsiteDetector:
    """
    A class to interact with the Google Safe Browsing API and detect phishing websites.
    """

    def __init__(self, api_key: str):
        """
        Initializes the detector with the provided API key.
        
        :param api_key: Google Safe Browsing API key.
        """
        self.api_key = api_key
        self.api_url = f"https://safebrowsing.googleapis.com/v4/threatMatches:find?key={api_key}"

    def check_url(self, url: str) -> bool:
        """
        Checks if a given URL is a phishing website.
        
        :param url: URL to be checked.
        :return: True if the URL is identified as phishing, False otherwise.
        """
        payload = {
            "client": {
                "clientId": "yourcompany",
                "clientVersion": "1.0"
            },
            "threatInfo": {
                "threatTypes": ["SOCIAL_ENGINEERING", "MALWARE"],
                "platformTypes": ["ANY_PLATFORM"],
                "threatEntryTypes": ["URL"],
                "threatEntries": [
                    {"url": url}
                ]
            }
        }

        try:
            # Send POST request to the API
            response = requests.post(self.api_url, json=payload)

            # Raise an exception for HTTP error codes
            response.raise_for_status()

            # Parse the response
            data = response.json()

            # If threats are found, the URL is phishing
            return bool(data.get("matches"))

        except requests.exceptions.RequestException as e:
            # Handle connection errors or HTTP request failures
            print(f"Error occurred while checking URL: {e}")
            return False

def main():
    """
    Main function for testing the phishing website detection.
    """
    # Replace this with your actual API key
    api_key = "YOUR_API_KEY"

    detector = PhishingWebsiteDetector(api_key)

    # Test URLs
    urls_to_check = [
        "http://example-phishing-site.com",
        "http://example-safe-site.com"
    ]

    for url in urls_to_check:
        is_phishing = detector.check_url(url)
        if is_phishing:
            print(f"WARNING: The URL '{url}' is detected as a phishing website.")
        else:
            print(f"The URL '{url}' is safe.")

if __name__ == "__main__":
    main()
```

### Notes:
- Obtain a valid API key for the Google Safe Browsing API by signing up on their platform.
- Install the required Python library `requests` using `pip install requests` if you don't already have it installed.
- Ensure the API key has the necessary permissions to use the Safe Browsing API.
