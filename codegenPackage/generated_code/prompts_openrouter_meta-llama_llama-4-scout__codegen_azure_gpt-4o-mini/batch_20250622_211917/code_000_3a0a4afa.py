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
import requests
from bs4 import BeautifulSoup

def fetch_page(url):
    """
    Fetches the content of a webpage.

    Args:
        url (str): The URL of the webpage to fetch.

    Returns:
        str: The HTML content of the page if successful, None otherwise.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)
        return response.text
    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 404:
            print("Custom Error: The page you are looking for does not exist (404).")
        else:
            print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    return None

def parse_html(html):
    """
    Parses the HTML content and extracts the title.

    Args:
        html (str): The HTML content of the page.

    Returns:
        str: The title of the page if found, None otherwise.
    """
    try:
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.title.string if soup.title else "No title found"
        return title
    except Exception as e:
        print(f"Error parsing HTML: {e}")
    return None

def main():
    """
    Main function to execute the web scraping process.
    """
    url = input("Enter the URL of the webpage to scrape: ")
    html_content = fetch_page(url)
    
    if html_content:
        title = parse_html(html_content)
        print(f"Page Title: {title}")

if __name__ == "__main__":
    main()
```
