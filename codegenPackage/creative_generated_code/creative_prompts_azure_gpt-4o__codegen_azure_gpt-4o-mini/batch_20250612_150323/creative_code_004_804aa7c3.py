"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elisium.it
Prompt: Create a Python program that generates a summary report of all files in an "Index of /" directory listing, including their names, sizes, and last modified dates.
Generated: DETERMINISTIC_804aa7c32a43136a
Batch ID: 20250612_150323
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://example.com/directory/": {
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
import os
import datetime
import requests
from bs4 import BeautifulSoup

def fetch_directory_listing(url):
    """
    Fetches the directory listing from the given URL.

    Args:
        url (str): The URL of the directory to fetch.

    Returns:
        str: The HTML content of the directory listing.

    Raises:
        Exception: If the URL cannot be reached or the response is not valid.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        return response.text
    except requests.RequestException as e:
        raise Exception(f"Error fetching the directory listing: {e}")

def parse_directory_listing(html_content):
    """
    Parses the directory listing HTML content and extracts file details.

    Args:
        html_content (str): The HTML content of the directory listing.

    Returns:
        list: A list of dictionaries containing file details (name, size, last modified).
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    files = []

    # Assuming each file entry is within a <tr> and relevant details are in <td>
    for row in soup.find_all('tr'):
        cols = row.find_all('td')
        if len(cols) >= 3:  # Adjust based on the structure of the HTML
            file_info = {
                'name': cols[0].text.strip(),
                'size': cols[1].text.strip(),
                'last_modified': cols[2].text.strip()
            }
            files.append(file_info)

    return files

def format_file_summary(files):
    """
    Formats the file summary for output.

    Args:
        files (list): A list of file details.

    Returns:
        str: A formatted string representing the file summary.
    """
    summary_lines = []
    for file in files:
        summary_lines.append(f"Name: {file['name']}, Size: {file['size']}, Last Modified: {file['last_modified']}")
    
    return "\n".join(summary_lines)

def generate_summary_report(url):
    """
    Generates a summary report of files in the given directory URL.

    Args:
        url (str): The URL of the directory.

    Returns:
        str: A summary report of the directory contents.
    """
    try:
        html_content = fetch_directory_listing(url)
        files = parse_directory_listing(html_content)
        report = format_file_summary(files)
        return report
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    # Replace with the target directory URL
    directory_url = "http://example.com/directory/"
    summary_report = generate_summary_report(directory_url)
    print(summary_report)
```
