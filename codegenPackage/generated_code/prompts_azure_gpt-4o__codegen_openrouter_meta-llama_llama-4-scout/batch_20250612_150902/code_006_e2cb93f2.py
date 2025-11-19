"""
Generated Code Metadata:
========================
Original URL: https://hostmkt.com
Prompt: Create a Python program using `BeautifulSoup` to parse and display the contents of a directory index page in a structured format.
Generated: DETERMINISTIC_e2cb93f2b0f0d65e
Batch ID: 20250612_150902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin, urlparse

def get_directory_index(url):
    """
    Retrieves the contents of a directory index page.

    Args:
        url (str): The URL of the directory index page.

    Returns:
        str: The HTML content of the directory index page.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def parse_directory_index(html):
    """
    Parses the HTML content of a directory index page using BeautifulSoup.

    Args:
        html (str): The HTML content of the directory index page.

    Returns:
        BeautifulSoup: The parsed HTML content.
    """
    return BeautifulSoup(html, 'html.parser')

def extract_links(soup):
    """
    Extracts links from the parsed HTML content.

    Args:
        soup (BeautifulSoup): The parsed HTML content.

    Returns:
        list: A list of extracted links.
    """
    links = []
    for a in soup.find_all('a', href=True):
        link = a['href']
        # Handle relative URLs
        if not bool(urlparse(link).netloc):
            link = urljoin(' ', link)
        links.append(link)
    return links

def extract_directory_contents(soup):
    """
    Extracts the contents of a directory index page.

    Args:
        soup (BeautifulSoup): The parsed HTML content.

    Returns:
        dict: A dictionary containing the directory contents.
    """
    contents = {}
    contents['title'] = soup.title.string if soup.title else 'Unknown'
    contents['links'] = extract_links(soup)
    contents['headings'] = [h.text.strip() for h in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])]
    return contents

def display_directory_contents(contents):
    """
    Displays the contents of a directory index page in a structured format.

    Args:
        contents (dict): A dictionary containing the directory contents.
    """
    print("# Directory Contents")
    print(f"## Title: {contents['title']}")
    print("## Links:")
    for link in contents['links']:
        print(f"- {link}")
    print("## Headings:")
    for heading in contents['headings']:
        print(f"- {heading}")

def main():
    url = input("Enter the URL of the directory index page: ")
    html = get_directory_index(url)
    if html:
        soup = parse_directory_index(html)
        contents = extract_directory_contents(soup)
        display_directory_contents(contents)

if __name__ == "__main__":
    main()
```
