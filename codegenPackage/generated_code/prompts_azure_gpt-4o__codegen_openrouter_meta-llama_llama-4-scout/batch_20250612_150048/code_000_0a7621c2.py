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
#!/usr/bin/env python3
"""
Apache Directory Index Parser

Parses and displays the contents of an Apache-style directory index.

Usage:
    python apache_directory_index_parser.py <directory_index_url>

Author: [Your Name]
Date: [Today's Date]
"""

import requests
from bs4 import BeautifulSoup
import argparse
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def parse_directory_index(url):
    """
    Parse the Apache-style directory index at the given URL.

    Args:
        url (str): The URL of the directory index.

    Returns:
        A dictionary containing the directory index contents.
    """
    try:
        # Send a GET request to the URL
        response = requests.get(url)

        # Check if the request was successful
        response.raise_for_status()

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the directory index table
        table = soup.find('table')

        # Check if the table was found
        if table is None:
            logger.error("Failed to find directory index table")
            return {}

        # Extract the directory index contents
        contents = []
        for row in table.find_all('tr')[1:]:
            columns = row.find_all('td')
            if len(columns) >= 2:
                name = columns[0].text.strip()
                size = columns[1].text.strip()
                last_modified = columns[2].text.strip()
                contents.append({
                    'name': name,
                    'size': size,
                    'last_modified': last_modified
                })

        return contents

    except requests.RequestException as e:
        logger.error(f"Request error: {e}")
        return []
    except Exception as e:
        logger.error(f"Error parsing directory index: {e}")
        return []

def display_directory_index(contents):
    """
    Display the directory index contents in a readable format.

    Args:
        contents (list): A list of dictionaries containing the directory index contents.
    """
    if not contents:
        print("Directory index is empty")
        return

    print(f"{'Name':^50} | {'Size':^20} | {'Last Modified':^20}")
    print("-" * 90)
    for item in contents:
        print(f"{item['name']:^50} | {item['size']:^20} | {item['last_modified']:^20}")

def main():
    parser = argparse.ArgumentParser(description='Parse and display Apache-style directory index')
    parser.add_argument('url', help='URL of the directory index')
    args = parser.parse_args()

    contents = parse_directory_index(args.url)
    display_directory_index(contents)

if __name__ == "__main__":
    main()
```
