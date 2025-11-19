"""
Generated Code Metadata:
========================
Original URL: https://mestamak.lagunaproductions.net
Prompt: Write a Python script to parse and display the contents of an Apache-style directory index, similar to the structure shown on https://mestamak.lagunaproductions.net.
Generated: DETERMINISTIC_0a7621c27b09bf9a
Batch ID: 20250612_150048
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
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def fetch_directory_index(url):
    """
    Fetches the directory index from the given URL.

    Args:
        url (str): The URL of the directory index to fetch.

    Returns:
        str: The HTML content of the directory index.

    Raises:
        requests.exceptions.RequestException: If the request to the URL fails.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        return response.text
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching the directory index: {e}")
        raise

def parse_directory_index(html_content):
    """
    Parses the HTML content of the directory index and extracts file and directory names.

    Args:
        html_content (str): The HTML content of the directory index.

    Returns:
        list: A list of tuples containing (name, is_directory).
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    items = []

    # Find all links in the directory index
    for link in soup.find_all('a'):
        name = link.get_text()
        href = link.get('href')
        is_directory = href.endswith('/')  # Check if the link is a directory
        items.append((name, is_directory))

    return items

def display_directory_index(items):
    """
    Displays the parsed directory index items.

    Args:
        items (list): A list of tuples containing (name, is_directory).
    """
    logging.info("Directory Index:")
    for name, is_directory in items:
        if is_directory:
            logging.info(f"[DIR] {name}")
        else:
            logging.info(f"[FILE] {name}")

def main():
    """
    Main function to execute the script.
    """
    url = input("Enter the URL of the Apache-style directory index: ")
    
    try:
        html_content = fetch_directory_index(url)
        items = parse_directory_index(html_content)
        display_directory_index(items)
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
