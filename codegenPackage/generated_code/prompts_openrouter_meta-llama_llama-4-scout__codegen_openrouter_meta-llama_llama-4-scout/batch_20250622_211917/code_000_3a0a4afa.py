"""
Generated Code Metadata:
========================
Original URL: https://casapiticilor.ro
Prompt: Write a Python script to create a simple web scraper that handles 404 errors and provides a custom error message, similar to the one on the provided webpage.
Generated: DETERMINISTIC_3a0a4afa051b6caa
Batch ID: 20250622_211917
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Simple Web Scraper Script
==========================

Handles 404 errors and provides a custom error message.

Usage:
    python web_scraper.py <url>
"""

import requests
from bs4 import BeautifulSoup

def scrape_url(url):
    """
    Scrapes the provided URL and returns the HTML content.

    Args:
        url (str): The URL to scrape.

    Returns:
        str: The HTML content of the webpage.

    Raises:
        requests.RequestException: If the request fails.
    """
    try:
        # Send a GET request to the URL
        response = requests.get(url)

        # Check if the request was successful
        response.raise_for_status()

        # Return the HTML content
        return response.text

    except requests.HTTPError as http_err:
        # Handle HTTP errors (4xx/5xx status codes)
        if http_err.response.status_code == 404:
            print(f"Error 404: Page '{url}' not found.")
            return None
        else:
            print(f"HTTP error occurred: {http_err}")
            return None

    except requests.RequestException as err:
        # Handle any other request exceptions
        print(f"Request error occurred: {err}")
        return None

def parse_html(html):
    """
    Parses the provided HTML content using BeautifulSoup.

    Args:
        html (str): The HTML content to parse.

    Returns:
        BeautifulSoup: The parsed HTML content.
    """
    return BeautifulSoup(html, 'html.parser')

def main():
    import sys

    # Check if the URL was provided as an argument
    if len(sys.argv) != 2:
        print("Usage: python web_scraper.py <url>")
        sys.exit(1)

    url = sys.argv[1]

    # Scrape the URL
    html = scrape_url(url)

    if html:
        # Parse the HTML content
        soup = parse_html(html)

        # Example usage: Print the title of the webpage
        print(soup.title.text)

if __name__ == "__main__":
    main()
```
