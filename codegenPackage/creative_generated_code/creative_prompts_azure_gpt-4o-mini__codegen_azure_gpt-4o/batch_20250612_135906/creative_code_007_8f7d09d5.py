"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hostlooni.com
Prompt: Generate a command-line script to check the status of a website hosted on Hostlooni and verify its uptime.
Generated: DETERMINISTIC_8f7d09d5297f2575
Batch ID: 20250612_135906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
#!/usr/bin/env python3

"""
A command-line script to check the status of a website hosted on Hostlooni 
and verify its uptime.

Usage:
    python check_website_status.py <website_url>

Dependencies:
    - requests (Install via `pip install requests`)
"""

import sys
import requests

def check_website_status(url):
    """
    Check the status of the given website URL.

    Args:
        url (str): The URL of the website to check.

    Returns:
        dict: A dictionary containing the status code and status message.
    """
    try:
        # Send an HTTP GET request to the website
        response = requests.get(url, timeout=10)
        # Return the status code and message
        return {
            "status_code": response.status_code,
            "status_message": response.reason
        }
    except requests.exceptions.RequestException as e:
        # Handle exceptions and return an error message
        return {
            "status_code": None,
            "status_message": f"Error: {str(e)}"
        }

def main():
    """
    Main function to parse command-line arguments and check website status.
    """
    # Check if a URL argument is provided
    if len(sys.argv) != 2:
        print("Usage: python check_website_status.py <website_url>")
        sys.exit(1)

    # Extract the URL from command-line arguments
    website_url = sys.argv[1]

    # Check the website status
    result = check_website_status(website_url)

    # Print the result
    print(f"Website URL: {website_url}")
    print(f"Status Code: {result['status_code']}")
    print(f"Status Message: {result['status_message']}")

if __name__ == "__main__":
    main()
```
