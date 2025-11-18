"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.flare-networks.xyz
Prompt: Write a Python script to list all files and directories from a web server directory listing, such as the one served by LiteSpeed Web Server at https://www.flare-networks.xyz.
Generated: DETERMINISTIC_18110b68e27e362a
Batch ID: 20250612_150130
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.flare-networks.xyz": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests
from bs4 import BeautifulSoup
import os

def fetch_directory_listing(url):
    """
    Fetches the directory listing from the given URL.

    Args:
        url (str): The URL of the web server directory.

    Returns:
        list: A list of file and directory names found in the directory listing.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract links from <a> tags
        links = soup.find_all('a')

        # Filter links to get filenames and directory names
        items = [link.get('href') for link in links if link.get('href')]

        return items

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Error during requests to {url}: {req_err}")
    except Exception as e:
        print(f"An error occurred: {e}")

def display_items(items):
    """
    Displays the items in a user-friendly format.

    Args:
        items (list): A list of file and directory names.
    """
    if items:
        print("Files and directories found:")
        for item in items:
            print(f"- {item}")
    else:
        print("No items found in the directory.")

def main():
    """
    Main function to execute the script.
    """
    url = 'https://www.flare-networks.xyz'
    items = fetch_directory_listing(url)
    display_items(items)

if __name__ == '__main__':
    main()
```
