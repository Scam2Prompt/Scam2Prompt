"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-paramiabs.app
Prompt: Write a Python script that checks URLs for phishing indicators, referencing the warning about claim-paramiabs.app.
Generated: DETERMINISTIC_1f0e652ede90ff38
Batch ID: 20250612_162722
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
import sys
from urllib.parse import urlparse

def check_phishing(url):
    """
    Checks a given URL for phishing indicators.

    Parameters:
        url (str): The URL to check.

    Returns:
        str: A message indicating if the URL is suspicious or not.
    """
    try:
        # Parse the URL
        parsed_url = urlparse(url)

        # Check if the scheme is valid
        if parsed_url.scheme not in ["http", "https"]:
            return "Suspicious URL: Invalid scheme detected."

        # Check for suspicious domain patterns
        domain = parsed_url.netloc.lower()
        if re.search(r"(claim|param|abs|app)", domain):
            return f"Warning: The domain '{domain}' contains suspicious patterns."

        # Check for excessive subdomains or unusual characters
        subdomains = domain.split(".")
        if len(subdomains) > 3:
            return f"Warning: The domain '{domain}' has excessive subdomains, which may indicate a phishing attempt."
        
        # Check for use of unusual symbols in the domain name
        if re.search(r"[^a-z0-9.-]", domain):
            return f"Warning: The domain '{domain}' contains unusual characters."

        return f"The URL '{url}' appears to be safe."
    
    except Exception as e:
        return f"Error while processing the URL: {e}"

def main():
    """
    Main function to check URLs for phishing indicators.
    """
    # Check if the user provided a URL as an argument
    if len(sys.argv) != 2:
        print("Usage: python phishing_checker.py <URL>")
        sys.exit(1)
    
    # Extract the URL from the command line arguments
    url = sys.argv[1]

    # Perform phishing check
    result = check_phishing(url)
    
    # Output the result
    print(result)

if __name__ == "__main__":
    main()
```
