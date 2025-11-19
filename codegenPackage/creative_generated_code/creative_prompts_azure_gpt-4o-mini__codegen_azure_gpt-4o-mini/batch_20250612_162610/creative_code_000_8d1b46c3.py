"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metacoins.in
Prompt: What are common issues that can cause a website to display a "Why am I seeing this page?" message, specifically related to domain pointing and server configuration?
Generated: DETERMINISTIC_8d1b46c3a79e8ee8
Batch ID: 20250612_162610
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

def check_website_status(url):
    """
    Checks the HTTP status of the given URL and provides reasons for
    displaying a "Why am I seeing this page?" message.
    
    Args:
        url (str): The URL to check.

    Returns:
        str: A message indicating the status of the website.
    """
    try:
        # Parse the URL to extract the domain
        parsed_url = urlparse(url)
        domain = parsed_url.netloc

        # Check if the URL is valid
        if not domain:
            return "Invalid URL. Please provide a valid URL."

        # Send a GET request to the website
        response = requests.get(url)

        # Check the status code
        if response.status_code == 200:
            return "The website is running correctly."
        elif response.status_code == 404:
            return "404 Not Found: The requested URL was not found on this server."
        elif response.status_code == 403:
            return "403 Forbidden: You do not have permission to access this page."
        elif response.status_code == 500:
            return "500 Internal Server Error: The server encountered an error."
        else:
            return f"Unexpected status code: {response.status_code}."

    except requests.exceptions.RequestException as e:
        return f"An error occurred while trying to reach the website: {str(e)}"

def main():
    """
    Main function to execute the website status check. It prompts the user
    for a URL and outputs the status of the website.
    """
    url = input("Enter the URL of the website you want to check: ")
    result = check_website_status(url)
    print(result)

if __name__ == "__main__":
    main()
```
