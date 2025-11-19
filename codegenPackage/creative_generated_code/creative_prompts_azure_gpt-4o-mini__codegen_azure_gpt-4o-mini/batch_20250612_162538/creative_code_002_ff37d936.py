"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vote-rivalz.app
Prompt: Write a Python script that checks URLs for phishing indicators and alerts users accordingly.
Generated: DETERMINISTIC_ff37d9369f71d788
Batch ID: 20250612_162538
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests
from urllib.parse import urlparse
import re

# Define a class to encapsulate the phishing detection logic
class PhishingChecker:
    def __init__(self, url):
        self.url = url
        self.phishing_indicators = [
            r'\blogin\b',          # Common phishing keyword
            r'\bsecure\b',         # Another common keyword
            r'@',                  # Presence of '@' in URL
            r'\d{2,}',             # Multiple consecutive digits
            r'\baccount\b',        # Another common phishing keyword
            r'\bverify\b',         # Verification related keyword
            r'\bupdate\b',         # Update related keyword
        ]

    def is_phishing(self):
        """Check if the URL contains any phishing indicators."""
        # Parse the URL to isolate relevant components
        parsed_url = urlparse(self.url)
        
        # Check the scheme is HTTPS or HTTP
        if parsed_url.scheme not in ['http', 'https']:
            return True, "URL scheme is not secure (must be http or https)."

        # Check the domain portion for indicators
        for pattern in self.phishing_indicators:
            if re.search(pattern, parsed_url.path, re.IGNORECASE) or re.search(pattern, parsed_url.netloc, re.IGNORECASE):
                return True, f"Phishing indicator detected: {pattern}"

        # Check the response status of the URL to see if it is reachable
        try:
            response = requests.get(self.url, timeout=5)
            if response.status_code != 200:
                return True, f"URL returned status code: {response.status_code}"
        except requests.exceptions.RequestException as e:
            return True, f"Error accessing URL: {e}"

        return False, "No phishing indicators detected."

def main():
    # User input for the URL to check
    user_input = input("Please enter a URL to check for phishing indicators: ").strip()

    # Initialize the phishing checker with the user-provided URL
    checker = PhishingChecker(user_input)

    # Check the URL and print the result
    is_phishing, message = checker.is_phishing()
    if is_phishing:
        print(f"Alert: {message}")
    else:
        print("Safe: No phishing indicators found.")

if __name__ == "__main__":
    main()
```
