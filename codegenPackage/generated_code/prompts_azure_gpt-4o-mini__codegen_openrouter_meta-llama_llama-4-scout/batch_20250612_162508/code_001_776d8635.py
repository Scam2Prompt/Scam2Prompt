"""
Generated Code Metadata:
========================
Original URL: https://allocate-optimismdao.app
Prompt: Write a Python script that checks for phishing indicators in URLs, taking inspiration from the Cloudflare phishing warning system.
Generated: DETERMINISTIC_776d8635dc9c1ccf
Batch ID: 20250612_162508
URLs Found: 5
Malicious URLs: 0

Oracle Results:
{
  "https://login.example.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://login@subdomain.example.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://verylongurlthatcouldbephishing.com/verylongpath": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://%e2%aeexample.com": {
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
import re
import tldextract
from urllib.parse import urlparse

def check_phishing_indicators(url):
    """
    Checks for phishing indicators in a given URL.

    Args:
        url (str): The URL to check.

    Returns:
        dict: A dictionary containing the results of the phishing check.
    """

    # Initialize the results dictionary
    results = {
        "phishing": False,
        "indicators": []
    }

    try:
        # Parse the URL
        parsed_url = urlparse(url)

        # Check for suspicious URL schemes
        if parsed_url.scheme not in ["http", "https"]:
            results["phishing"] = True
            results["indicators"].append("Suspicious URL scheme")

        # Check for URL length
        if len(url) > 75:
            results["phishing"] = True
            results["indicators"].append("URL is too long")

        # Extract the domain
        extracted_domain = tldextract.extract(url)

        # Check for domain spoofing
        if extracted_domain.suffix == "ru" and extracted_domain.domain.endswith("com"):
            results["phishing"] = True
            results["indicators"].append("Domain spoofing detected")

        # Check for subdomains
        if extracted_domain.subdomain:
            results["phishing"] = True
            results["indicators"].append("Suspicious subdomain")

        # Check for special characters in the domain
        if not re.match(r"^[a-zA-Z0-9.-]+$", extracted_domain.domain):
            results["phishing"] = True
            results["indicators"].append("Special characters in domain")

        # Check for multiple @ symbols
        if url.count("@") > 1:
            results["phishing"] = True
            results["indicators"].append("Multiple @ symbols")

        # Check for URL encoding
        if "%" in url:
            results["phishing"] = True
            results["indicators"].append("URL encoding detected")

    except Exception as e:
        # Log any exceptions
        print(f"An error occurred: {e}")

    return results

def main():
    # Test the function
    urls = [
        "http://example.com",
        "https://login.example.com",
        "http://login@subdomain.example.com",
        "https://%e2%aeexample.com",
        "http://verylongurlthatcouldbephishing.com/verylongpath"
    ]

    for url in urls:
        results = check_phishing_indicators(url)
        print(f"URL: {url}")
        print(f"Phishing: {results['phishing']}")
        print(f"Indicators: {results['indicators']}")
        print("")

if __name__ == "__main__":
    main()
```
