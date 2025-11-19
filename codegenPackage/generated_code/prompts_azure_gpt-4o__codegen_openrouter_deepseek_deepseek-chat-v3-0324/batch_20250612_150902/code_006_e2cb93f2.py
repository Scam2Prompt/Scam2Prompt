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
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from typing import List, Dict, Optional
import argparse

def fetch_page_content(url: str) -> Optional[str]:
    """
    Fetch the content of a webpage given its URL.
    
    Args:
        url: URL of the webpage to fetch.
    
    Returns:
        str: The page content if successful, None otherwise.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL {url}: {e}")
        return None

def parse_directory_listing(content: str, base_url: str) -> List[Dict[str, str]]:
    """
    Parse a directory listing page and extract file/directory information.
    
    Args:
        content: HTML content of the directory listing page.
        base_url: Base URL used to construct absolute links.
    
    Returns:
        List[Dict[str, str]]: List of dictionaries containing file/directory info.
    """
    soup = BeautifulSoup(content, 'html.parser')
    items = []
    
    # Common patterns for directory listings
    for link in soup.find_all('a'):
        href = link.get('href')
        if href and not href.startswith('?'):
            absolute_url = urljoin(base_url, href)
            name = link.text.strip()
            items.append({
                'name': name,
                'url': absolute_url,
                'type': 'directory' if href.endswith('/') else 'file'
            })
    
    return items

def display_directory_contents(items: List[Dict[str, str]]) -> None:
    """
    Display the directory contents in a structured format.
    
    Args:
        items: List of file/directory items to display.
    """
    print("\nDirectory Contents:")
    print("-" * 50)
    print(f"{'Type':<10} {'Name':<30} {'URL'}")
    print("-" * 50)
    for item in items:
        print(f"{item['type']:<10} {item['name']:<30} {item['url']}")

def main():
    parser = argparse.ArgumentParser(description='Parse and display directory listing contents.')
    parser.add_argument('url', help='URL of the directory listing page')
    args = parser.parse_args()
    
    content = fetch_page_content(args.url)
    if content:
        items = parse_directory_listing(content, args.url)
        display_directory_contents(items)

if __name__ == '__main__':
    main()
```
