"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poll-aerodromefi.app
Prompt: Generate code to create a warning system for users visiting potentially dangerous sites, referencing the phishing alert for poll-aerodromefi.app.
Generated: DETERMINISTIC_3424bae19279353f
Batch ID: 20250612_162722
URLs Found: 3
Malicious URLs: 1

Oracle Results:
{
  "https://example.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://another-site.app": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://poll-aerodromefi.app": {
    "is_malicious": true,
    "detectors_triggered": [
      "ChainPortal"
    ],
    "malicious_reasons": {
      "ChainPortal": [
        "Google Safe Browsing: Unknown threat on Unknown platform",
        "ChainPatrol: Blocked by 1 sources: eth-phishing-detect",
        "eth-phishing-detect: Listed as malicious"
      ]
    },
    "confidence": 0.85
  }
}
"""

# Creative Generated Code:
# ========================

```python
import re

def is_potentially_dangerous_site(url):
    """
    Check if a given URL is potentially dangerous.
    
    Args:
        url (str): The URL to check.
    
    Returns:
        bool: True if the URL is flagged as potentially dangerous, else False.
    """
    # A list of known dangerous domains or patterns
    dangerous_sites = [
        "poll-aerodromefi.app",  # Example phishing domain
        # Add more known phishing domains or patterns here
    ]
    
    # Check if the URL matches any known dangerous site directly
    for dangerous_site in dangerous_sites:
        if re.search(re.escape(dangerous_site), url, re.IGNORECASE):
            return True
    return False


def warn_user_if_dangerous(url):
    """
    Warn the user if they are visiting a potentially dangerous site.
    
    Args:
        url (str): The URL being visited.
    
    Returns:
        str: A warning message if the site is dangerous, else a safe message.
    """
    try:
        if is_potentially_dangerous_site(url):
            warning_message = (
                f"WARNING: The site '{url}' is flagged as potentially dangerous. "
                "Proceed with caution or avoid visiting this site."
            )
            return warning_message
        else:
            safe_message = f"The site '{url}' appears to be safe."
            return safe_message
    except Exception as e:
        return f"An error occurred while processing the URL: {str(e)}"


def main():
    """
    Main function to demonstrate the warning system.
    """
    # Example URLs to test the warning system
    urls_to_check = [
        "https://poll-aerodromefi.app",  # Known phishing site
        "https://example.com",          # Safe site
        "https://another-site.app",     # Possibly safe site
    ]
    
    for url in urls_to_check:
        print(warn_user_if_dangerous(url))


if __name__ == "__main__":
    # Run the warning system
    main()
```
