"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://perurest.com
Prompt: Write a script to list and parse directory contents served by a LiteSpeed Web Server, including file names, last modified dates, and sizes.
Generated: DETERMINISTIC_0cccaa85dda52e98
Batch ID: 20250612_154216
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

def fetch_directory_contents(url):
    """
    Fetches and parses the directory listing from a LiteSpeed Web Server.

    Args:
        url (str): URL of the LiteSpeed Web Server directory listing.

    Returns:
        list: List of dictionaries containing file details (name, last modified, size).
    """
    try:
        # Make HTTP GET request to fetch the directory listing
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}")
        return []

    try:
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        rows = soup.find_all('tr')  # LiteSpeed listing uses <tr> tags for entries

        files = []
        for row in rows[1:]:  # Skip the header row, if present
            columns = row.find_all('td')
            if len(columns) >= 3:  # LiteSpeed usually has Name, Last Modified, and Size columns
                file_name = columns[0].text.strip()
                last_modified = columns[1].text.strip()
                size = columns[2].text.strip()

                files.append({
                    'name': file_name,
                    'last_modified': last_modified,
                    'size': size
                })

        return files
    except Exception as e:
        print(f"Error parsing directory listing: {e}")
        return []

def print_directory_contents(files):
    """
    Prints the directory contents in a readable format.

    Args:
        files (list): List of file details (name, last modified, size).
    """
    if not files:
        print("No files found.")
        return

    print(f"{'File Name':<40} {'Last Modified':<25} {'Size':<10}")
    print("-" * 75)
    for file in files:
        print(f"{file['name']:<40} {file['last_modified']:<25} {file['size']:<10}")

if __name__ == "__main__":
    # URL of the LiteSpeed web server directory listing
    url = input("Enter the URL of the LiteSpeed directory listing: ").strip()

    # Ensure the URL ends with a trailing slash
    if not url.endswith('/'):
        url += '/'

    # Fetch and display the directory contents
    files = fetch_directory_contents(url)
    print_directory_contents(files)
```
