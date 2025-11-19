"""
Generated Code Metadata:
========================
Original URL: https://bryantroll.com
Prompt: Write a Python script to parse and display the contents of a directory listing from a webpage, like the one at https://bryantroll.com.
Generated: DETERMINISTIC_4706bbf17f57207c
Batch ID: 20250612_154236
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
from urllib.parse import urljoin
import argparse
import sys

def parse_directory_listing(url):
    """
    Parse a directory listing webpage and return the list of files and directories.
    
    Args:
        url (str): URL of the directory listing page
        
    Returns:
        list: List of dictionaries containing name, type (file/dir), and URL for each item
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}", file=sys.stderr)
        return None

    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all links in the page (assuming standard directory listing format)
    items = []
    for link in soup.find_all('a'):
        href = link.get('href')
        if href and href != '../' and href != '/':
            full_url = urljoin(url, href)
            item_type = 'directory' if href.endswith('/') else 'file'
            items.append({
                'name': link.text.strip(),
                'type': item_type,
                'url': full_url
            })
    
    return items

def display_directory_listing(items):
    """
    Display the directory listing in a formatted way.
    
    Args:
        items (list): List of items from parse_directory_listing
    """
    if not items:
        print("No items found in directory listing.")
        return
    
    print("\nDirectory Listing:")
    print("-" * 50)
    print(f"{'Type':<10} {'Name':<30} {'URL'}")
    print("-" * 50)
    
    for item in items:
        print(f"{item['type']:<10} {item['name']:<30} {item['url']}")

def main():
    parser = argparse.ArgumentParser(description='Parse and display directory listings from webpages.')
    parser.add_argument('url', help='URL of the directory listing page')
    args = parser.parse_args()
    
    items = parse_directory_listing(args.url)
    if items is not None:
        display_directory_listing(items)

if __name__ == "__main__":
    main()
```
