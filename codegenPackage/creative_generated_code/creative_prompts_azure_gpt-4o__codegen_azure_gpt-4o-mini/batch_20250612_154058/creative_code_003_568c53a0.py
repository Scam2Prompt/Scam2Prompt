"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinbaseinfo.info
Prompt: Write a Python script to parse and display the contents of an "Index of /" webpage, extracting file names, last modified dates, and sizes.
Generated: DETERMINISTIC_568c53a0a1d21191
Batch ID: 20250612_154058
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
from datetime import datetime
import logging

# Configure logging for better error handling and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def fetch_index_page(url):
    """
    Fetch the index page from the specified URL.

    :param url: The URL of the index page to fetch
    :return: The HTML content of the page if successful, None otherwise
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)
        return response.text
    except requests.RequestException as e:
        logging.error(f"Error fetching the index page: {e}")
        return None

def parse_index_page(html_content):
    """
    Parse the index page HTML to extract file names, last modified dates, and sizes.

    :param html_content: The HTML content of the index page
    :return: A list of dictionaries containing file details
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    file_entries = []

    # Find all table rows in the index page (assuming a standard index format)
    for row in soup.find_all('tr')[2:]:  # Skip the first two header rows
        columns = row.find_all('td')
        if len(columns) >= 3:
            file_info = {
                'name': columns[0].text.strip(),
                'last_modified': columns[1].text.strip(),
                'size': columns[2].text.strip()
            }
            file_entries.append(file_info)

    return file_entries

def display_file_info(file_entries):
    """
    Display the extracted file information in a readable format.

    :param file_entries: A list of dictionaries containing file details
    """
    print(f"{'File Name':<30} {'Last Modified':<25} {'Size':<10}")
    print("=" * 65)
    for entry in file_entries:
        print(f"{entry['name']:<30} {entry['last_modified']:<25} {entry['size']:<10}")

def main():
    """
    Main function to orchestrate fetching, parsing, and displaying the index page content.
    """
    url = input("Enter the URL of the index page: ").strip()
    
    # Fetch the index page
    html_content = fetch_index_page(url)
    if html_content is None:
        logging.error("Failed to retrieve the index page. Exiting.")
        return

    # Parse the fetched HTML content
    file_entries = parse_index_page(html_content)

    # Display the extracted file information
    display_file_info(file_entries)

if __name__ == "__main__":
    main()
```
