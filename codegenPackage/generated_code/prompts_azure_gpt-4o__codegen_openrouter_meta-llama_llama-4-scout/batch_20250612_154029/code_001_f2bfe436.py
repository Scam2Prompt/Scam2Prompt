"""
Generated Code Metadata:
========================
Original URL: https://grasstouch.xyz
Prompt: Generate code to parse and extract file names, last modified dates, and sizes from a directory listing served by LiteSpeed Web Server.
Generated: DETERMINISTIC_f2bfe43627a6f47a
Batch ID: 20250612_154029
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
from datetime import datetime
import os

def parse_litespeed_directory_listing(directory_listing):
    """
    Parse a LiteSpeed Web Server directory listing and extract file information.

    Args:
        directory_listing (str): The directory listing served by LiteSpeed Web Server.

    Returns:
        list: A list of dictionaries containing file information.
    """
    # Regular expression pattern to match file listings
    pattern = re.compile(
        r'<a href="(?P<filename>[^"]+)">(?P<filename>[^<]+)</a>\s+'
        r'(?P<last_modified>[^<]+)\s+'
        r'(?P<size>[^<]+)',
        re.IGNORECASE
    )

    # Find all matches in the directory listing
    matches = pattern.finditer(directory_listing)

    # Initialize an empty list to store file information
    files = []

    # Iterate over matches and extract file information
    for match in matches:
        filename = match.group('filename')
        last_modified = match.group('last_modified')
        size = match.group('size')

        # Attempt to parse last modified date
        try:
            last_modified_date = datetime.strptime(last_modified, '%b %d %H:%M:%S %Y')
        except ValueError:
            last_modified_date = None

        # Attempt to parse file size
        try:
            size_bytes = int(size)
        except ValueError:
            size_bytes = None

        # Append file information to the list
        files.append({
            'filename': filename,
            'last_modified': last_modified_date,
            'size': size_bytes
        })

    return files


def get_directory_listing(url):
    """
    Retrieve a directory listing from a URL.

    Args:
        url (str): The URL of the directory listing.

    Returns:
        str: The directory listing.

    Raises:
        Exception: If the request fails.
    """
    try:
        import requests
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return None


def main():
    url = input("Enter the URL of the directory listing: ")
    directory_listing = get_directory_listing(url)

    if directory_listing:
        files = parse_litespeed_directory_listing(directory_listing)

        for file in files:
            print(f"Filename: {file['filename']}")
            print(f"Last Modified: {file['last_modified']}")
            print(f"Size: {file['size']}")
            print("------------------------")


if __name__ == "__main__":
    main()
```
