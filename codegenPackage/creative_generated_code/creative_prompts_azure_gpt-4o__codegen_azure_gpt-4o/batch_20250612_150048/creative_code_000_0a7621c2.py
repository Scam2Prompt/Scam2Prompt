"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mestamak.lagunaproductions.net
Prompt: Write a Python script to parse and display the contents of an Apache-style directory index, similar to the structure shown on https://mestamak.lagunaproductions.net.
Generated: DETERMINISTIC_0a7621c27b09bf9a
Batch ID: 20250612_150048
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
import sys

def fetch_directory_index(url):
    """
    Fetches the HTML content of the Apache-style directory index.
    
    Parameters:
        url (str): The URL of the directory index.
    
    Returns:
        str: HTML content of the directory index.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}")
        sys.exit(1)


def parse_directory_index(html_content):
    """
    Parses the HTML content of the Apache-style directory index and extracts file and folder details.
    
    Parameters:
        html_content (str): HTML content of the directory index.
    
    Returns:
        list of dict: Extracted details containing 'name', 'size', and 'last_modified'.
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    rows = soup.find_all('tr')  # Each file/folder is typically in a <tr>
    
    parsed_items = []
    for row in rows:
        columns = row.find_all('td')
        if len(columns) >= 3:  # Ensure we have enough columns for name, size, and last modified
            item = {
                'name': columns[0].get_text(strip=True),
                'size': columns[1].get_text(strip=True),
                'last_modified': columns[2].get_text(strip=True)
            }
            parsed_items.append(item)
    
    return parsed_items


def display_directory_index(items):
    """
    Displays the parsed directory index items in a user-friendly format.
    
    Parameters:
        items (list of dict): List of parsed items containing 'name', 'size', and 'last_modified'.
    """
    print(f"{'Name':<50} {'Size':<15} {'Last Modified':<25}")
    print("=" * 90)
    for item in items:
        print(f"{item['name']:<50} {item['size']:<15} {item['last_modified']:<25}")


def main():
    """
    Main function to parse and display the contents of the Apache-style directory index.
    """
    # Example URL - Replace with your specific directory index URL
    url = input("Enter the URL of an Apache-style directory index: ").strip()
    
    # Fetch and parse the directory index
    html_content = fetch_directory_index(url)
    parsed_items = parse_directory_index(html_content)
    
    # Display the contents
    if parsed_items:
        display_directory_index(parsed_items)
    else:
        print("No items found in the directory index.")


if __name__ == "__main__":
    main()
```
