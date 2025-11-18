"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hostmkt.com
Prompt: Create a Python program using `BeautifulSoup` to parse and display the contents of a directory index page in a structured format.
Generated: DETERMINISTIC_e2cb93f2b0f0d65e
Batch ID: 20250612_150902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests
from bs4 import BeautifulSoup
import os

def fetch_directory_index(url):
    """
    Fetches the directory index from the given URL.

    Parameters:
    url (str): The URL of the directory index page.

    Returns:
    BeautifulSoup: Parsed HTML content of the directory index page.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        return BeautifulSoup(response.text, 'html.parser')
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL {url}: {e}")
        return None

def parse_directory_index(soup):
    """
    Parses the directory index page using BeautifulSoup.

    Parameters:
    soup (BeautifulSoup): The parsed HTML content of the directory index page.

    Returns:
    list: A list of tuples containing the name and URL of each item in the directory.
    """
    if soup is None:
        return []

    items = []
    # Assuming directory items are contained in 'a' tags
    for link in soup.find_all('a'):
        href = link.get('href')
        text = link.text.strip()
        if href and text:
            items.append((text, href))
    return items

def display_directory_contents(items):
    """
    Displays the contents of the directory in a structured format.

    Parameters:
    items (list): A list of tuples containing the name and URL of each item.
    """
    print("Directory Contents:")
    for name, url in items:
        print(f"- {name}: {url}")

def main():
    """
    Main function to execute the directory index fetching and parsing.
    """
    url = input("Enter the directory index URL: ").strip()
    soup = fetch_directory_index(url)
    items = parse_directory_index(soup)
    display_directory_contents(items)

if __name__ == '__main__':
    main()
```
