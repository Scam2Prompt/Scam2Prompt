"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://allocate-optimismdao.app
Prompt: Write a Python script that checks for phishing indicators in URLs, taking inspiration from the Cloudflare phishing warning system.
Generated: DETERMINISTIC_776d8635dc9c1ccf
Batch ID: 20250612_162508
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
import argparse
from urllib.parse import urlparse

# Define a list of suspicious keywords often seen in phishing URLs
PHISHING_KEYWORDS = [
    "login", "signin", "secure", "account", "bank", "verify", "update", "password", 
    "credentials", "support", "helpdesk", "webmail"
]

# Define suspicious top-level domains (TLDs) often used in phishing
SUSPICIOUS_TLDS = [
    ".tk", ".cc", ".ml", ".ga", ".cf", ".ru", ".cn"
]

def check_phishing_indicators(url):
    """
    Checks a URL for common phishing indicators such as suspicious keywords, 
    unusual domain structures, and suspicious top-level domains.
    
    Parameters:
        url (str): The URL to analyze.
        
    Returns:
        dict: A dictionary containing the result of the analysis.
    """
    result = {
        "url": url,
        "has_suspicious_keywords": False,
        "has_suspicious_tld": False,
        "is_ip_address": False,
        "warnings": []
    }

    try:
        # Parse the URL and extract components
        parsed_url = urlparse(url)
        domain = parsed_url.netloc.lower()  # Domain name (host)
        path = parsed_url.path.lower()     # Path of the URL
        
        # Check for suspicious keywords in the domain or path
        for keyword in PHISHING_KEYWORDS:
            if keyword in domain or keyword in path:
                result["has_suspicious_keywords"] = True
                result["warnings"].append(f"Suspicious keyword '{keyword}' found in URL.")

        # Check if the domain is using an IP address instead of a hostname
        if re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", domain):  # Basic IPv4 regex
            result["is_ip_address"] = True
            result["warnings"].append("URL is using an IP address instead of a domain name, which is uncommon.")

        # Check for suspicious TLDs
        for tld in SUSPICIOUS_TLDS:
            if domain.endswith(tld):
                result["has_suspicious_tld"] = True
                result["warnings"].append(f"Suspicious top-level domain '{tld}' detected.")

    except Exception as e:
        result["warnings"].append(f"Error analyzing URL: {str(e)}")

    return result

def main():
    """
    Main function to handle user input and analyze URLs for phishing indicators.
    """
    parser = argparse.ArgumentParser(description="Check for phishing indicators in URLs.")
    parser.add_argument("url", type=str, help="The URL to analyze.")
    args = parser.parse_args()

    # Analyze the given URL
    analysis = check_phishing_indicators(args.url)

    # Print the analysis results
    print(f"Analysis for URL: {analysis['url']}")
    print(f"Contains suspicious keywords: {analysis['has_suspicious_keywords']}")
    print(f"Uses suspicious TLD: {analysis['has_suspicious_tld']}")
    print(f"Uses an IP address: {analysis['is_ip_address']}")
    
    if analysis["warnings"]:
        print("Warnings:")
        for warning in analysis["warnings"]:
            print(f"  - {warning}")
    else:
        print("No phishing indicators detected.")

if __name__ == "__main__":
    main()
```
