"""
Generated Code Metadata:
========================
Original URL: https://eulers.ch
Prompt: Write a script to list all files and directories from a LiteSpeed Web Server directory index, similar to the structure displayed at eulers.ch.
Generated: DETERMINISTIC_8be4164dbb0c82d9
Batch ID: 20250612_145837
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
import argparse
import sys
from urllib.parse import urljoin

def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description='List files and directories from a LiteSpeed Web Server directory index.')
    parser.add_argument('url', help='URL of the directory index to scan')
    parser.add_argument('-o', '--output', help='Output file to save results')
    return parser.parse_args()

def get_directory_listing(url):
    """Fetch and parse directory listing from the given URL."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a')
        
        items = []
        for link in links:
            href = link.get('href')
            if href and href != '../' and href != '/':
                full_url = urljoin(url, href)
                items.append(full_url)
        
        return items
    except requests.exceptions.RequestException as e:
        print(f"Error fetching directory listing: {e}", file=sys.stderr)
        sys.exit(1)

def save_results(items, output_file):
    """Save results to a file if specified."""
    try:
        with open(output_file, 'w') as f:
            for item in items:
                f.write(f"{item}\n")
    except IOError as e:
        print(f"Error writing to output file: {e}", file=sys.stderr)
        sys.exit(1)

def main():
    args = parse_arguments()
    
    print(f"Fetching directory listing from: {args.url}")
    items = get_directory_listing(args.url)
    
    if not items:
        print("No items found in directory listing.", file=sys.stderr)
        sys.exit(1)
    
    print("\nFound items:")
    for item in items:
        print(item)
    
    if args.output:
        save_results(items, args.output)
        print(f"\nResults saved to: {args.output}")

if __name__ == "__main__":
    main()
```
