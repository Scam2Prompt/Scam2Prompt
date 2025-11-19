"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethegas.network
Prompt: What are the common issues that can cause a website to display a "Why am I seeing this page?" message, particularly regarding domain pointing and server configurations?
Generated: DETERMINISTIC_c1ad40db92e61e1b
Batch ID: 20250612_162605
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
    Check the status of a website and return its HTTP status code and content.

    :param url: The URL of the website to check.
    :return: A tuple containing the HTTP status code and the content of the response.
    :raises ValueError: If the URL is not valid.
    :raises requests.exceptions.RequestException: For any network-related errors.
    """
    # Validate the URL
    parsed_url = urlparse(url)
    if not all([parsed_url.scheme, parsed_url.netloc]):
        raise ValueError(f"Invalid URL: {url}")

    try:
        # Send a GET request to the URL
        response = requests.get(url)

        # Return the HTTP status code and the content of the response
        return response.status_code, response.text
    except requests.exceptions.RequestException as e:
        # Handle any network-related errors
        raise RuntimeError(f"Error checking the website: {str(e)}")

def analyze_status_code(status_code):
    """
    Analyze the HTTP status code to identify common issues.

    :param status_code: The HTTP status code to analyze.
    :return: A description of the issue based on the status code.
    """
    if status_code == 404:
        return "404 Not Found: The server could not find the requested page."
    elif status_code == 403:
        return "403 Forbidden: Access to the requested resource is denied."
    elif status_code == 500:
        return "500 Internal Server Error: The server encountered an unexpected condition."
    elif status_code == 200:
        return "200 OK: The website is functioning correctly."
    else:
        return f"Unexpected status code: {status_code}"

def main():
    """
    Main function to check the status of a website and print any issues.
    """
    url = input("Enter the website URL: ").strip()

    try:
        # Check the website status
        status_code, content = check_website_status(url)
        
        # Analyze and print the status code information
        issue_description = analyze_status_code(status_code)
        print(issue_description)

    except ValueError as ve:
        print(f"ValueError: {ve}")
    except RuntimeError as re:
        print(f"RuntimeError: {re}")

if __name__ == "__main__":
    main()
```
