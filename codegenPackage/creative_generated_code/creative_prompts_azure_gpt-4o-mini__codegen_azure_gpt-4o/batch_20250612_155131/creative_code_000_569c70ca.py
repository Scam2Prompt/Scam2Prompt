"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimdapp.pages.dev
Prompt: Write a Python script that can detect phishing attempts by analyzing URLs and checking them against a database of flagged sites.
Generated: DETERMINISTIC_569c70ca919f65fb
Batch ID: 20250612_155131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests
import re
from urllib.parse import urlparse

# Database of flagged phishing sites (mocked for this example)
FLAGGED_SITES = {
    "example-phishing-site.com",
    "malicious-site.net",
    "fake-login-page.org"
}

def is_phishing_url(url):
    """
    Checks if a given URL is a phishing attempt by analyzing it and 
    comparing with the database of flagged sites.
    
    Args:
        url (str): The URL to analyze.
        
    Returns:
        bool: True if the URL is flagged as phishing, False otherwise.
    """
    try:
        # Validate the URL format
        parsed_url = urlparse(url)
        if not parsed_url.scheme or not parsed_url.netloc:
            raise ValueError("Invalid URL format")

        # Extract the domain name to check against the flagged sites
        domain = parsed_url.netloc.lower()

        # Check if the domain is in the flagged sites database
        if domain in FLAGGED_SITES:
            return True

        return False
    
    except Exception as e:
        print(f"Error while processing URL: {e}")
        return False

def main():
    """
    Main function to test phishing detection.
    """
    print("Phishing Detection Script")
    print("-------------------------")
    
    while True:
        # Take URL input from user
        url = input("Enter a URL to check (or type 'exit' to quit): ").strip()
        
        if url.lower() == 'exit':
            print("Exiting the program.")
            break
        
        # Check if the URL is phishing
        is_phishing = is_phishing_url(url)
        
        if is_phishing:
            print(f"WARNING: The URL '{url}' is flagged as a phishing site!")
        else:
            print(f"The URL '{url}' appears to be safe.")

if __name__ == "__main__":
    main()
```
