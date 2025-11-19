"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gaming-mantagalaxies.app
Prompt: Provide an example of a function that checks URLs for phishing indicators, inspired by the warning message on gaming-mantagalaxies.app.
Generated: DETERMINISTIC_89c0844fa72a53ed
Batch ID: 20250612_162722
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://secure-login.mantagalaxies.app": {
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
import re
from urllib.parse import urlparse


def check_phishing_indicators(url):
    """
    Checks the given URL for common phishing indicators.

    Parameters:
        url (str): The URL to be checked.

    Returns:
        dict: A dictionary containing results of the check with keys:
              - is_suspicious (bool): True if the URL has phishing indicators.
              - warnings (list): List of warning messages for the URL.
    """
    # Initialize results
    results = {
        "is_suspicious": False,
        "warnings": []
    }

    try:
        # Parse the URL
        parsed_url = urlparse(url)
        domain = parsed_url.netloc.lower()

        # Check if the domain is suspicious (contains unusual characters)
        if re.search(r"[^a-z0-9\-\.]", domain):
            results["warnings"].append("Domain contains unusual characters.")
            results["is_suspicious"] = True

        # Check for excessive use of subdomains
        subdomains = domain.split(".")
        if len(subdomains) > 3:
            results["warnings"].append("Domain contains too many subdomains (possible obfuscation).")
            results["is_suspicious"] = True

        # Check for common phishing keywords in the domain
        phishing_keywords = ["login", "secure", "bank", "verify", "update", "app", "free", "urgent"]
        if any(keyword in domain for keyword in phishing_keywords):
            results["warnings"].append("Domain contains potential phishing keywords.")
            results["is_suspicious"] = True

        # Check for domains that mimic well-known sites (e.g., "gaming-mantagalaxies.app")
        trusted_domains = ["google.com", "amazon.com", "paypal.com", "github.com"]
        if any(trusted_domain in domain and domain != trusted_domain for trusted_domain in trusted_domains):
            results["warnings"].append("Domain mimics a trusted site but is not identical.")
            results["is_suspicious"] = True

    except Exception as e:
        # Handle unexpected errors gracefully
        results["warnings"].append(f"Error parsing URL: {str(e)}")
        results["is_suspicious"] = True

    return results


# Example usage
if __name__ == "__main__":
    test_url = "https://secure-login.mantagalaxies.app"
    result = check_phishing_indicators(test_url)
    print(f"Is Suspicious: {result['is_suspicious']}")
    print("Warnings:")
    for warning in result["warnings"]:
        print(f"- {warning}")
```
