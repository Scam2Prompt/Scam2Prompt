"""
Generated Code Metadata:
========================
Original URL: https://elisium.it
Prompt: Create a Python program that generates a summary report of all files in an "Index of /" directory listing, including their names, sizes, and last modified dates.
Generated: DETERMINISTIC_804aa7c32a43136a
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import requests
from bs4 import BeautifulSoup
from datetime import datetime

def fetch_directory_listing(url):
    """
    Fetches the directory listing from the given URL.

    Args:
        url (str): The URL of the directory to fetch.

    Returns:
        str: The HTML content of the directory listing.

    Raises:
        Exception: If the request to the URL fails.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        return response.text
    except requests.RequestException as e:
        raise Exception(f"Failed to fetch directory listing: {e}")

def parse_directory_listing(html_content):
    """
    Parses the HTML content of the directory listing to extract file details.

    Args:
        html_content (str): The HTML content of the directory listing.

    Returns:
        list: A list of dictionaries containing file details (name, size, last modified).
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    files = []

    # Find all links in the directory listing
    for link in soup.find_all('a'):
        file_name = link.get_text()
        file_url = link.get('href')

        # Skip if the link is not a file (e.g., parent directory)
        if file_name in ['..', '.']:
            continue

        # Get file size and last modified date (if available)
        file_info = {
            'name': file_name,
            'size': get_file_size(file_url),
            'last_modified': get_last_modified(file_url)
        }
        files.append(file_info)

    return files

def get_file_size(file_url):
    """
    Gets the size of the file at the given URL.

    Args:
        file_url (str): The URL of the file.

    Returns:
        int: The size of the file in bytes, or None if not available.
    """
    try:
        response = requests.head(file_url)
        response.raise_for_status()
        return int(response.headers.get('Content-Length', 0))
    except requests.RequestException:
        return None

def get_last_modified(file_url):
    """
    Gets the last modified date of the file at the given URL.

    Args:
        file_url (str): The URL of the file.

    Returns:
        str: The last modified date as a string, or None if not available.
    """
    try:
        response = requests.head(file_url)
        response.raise_for_status()
        last_modified = response.headers.get('Last-Modified')
        if last_modified:
            # Convert to a more readable format
            return datetime.strptime(last_modified, '%a, %d %b %Y %H:%M:%S %Z').isoformat()
        return None
    except requests.RequestException:
        return None

def generate_summary_report(files):
    """
    Generates a summary report of the files.

    Args:
        files (list): A list of dictionaries containing file details.

    Returns:
        str: A formatted summary report.
    """
    report_lines = ["Summary Report of Directory Files:\n"]
    report_lines.append(f"{'Name':<30} {'Size (bytes)':<15} {'Last Modified'}")
    report_lines.append("=" * 60)

    for file in files:
        report_lines.append(f"{file['name']:<30} {file['size']:<15} {file['last_modified']}")
    
    return "\n".join(report_lines)

def main():
    """
    Main function to execute the program.
    """
    url = input("Enter the URL of the directory: ")
    
    try:
        html_content = fetch_directory_listing(url)
        files = parse_directory_listing(html_content)
        report = generate_summary_report(files)
        print(report)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
