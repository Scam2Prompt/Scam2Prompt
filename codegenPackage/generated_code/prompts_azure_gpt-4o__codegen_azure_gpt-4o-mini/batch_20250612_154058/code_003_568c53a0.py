"""
Generated Code Metadata:
========================
Original URL: https://coinbaseinfo.info
Prompt: Write a Python script to parse and display the contents of an "Index of /" webpage, extracting file names, last modified dates, and sizes.
Generated: DETERMINISTIC_568c53a0a1d21191
Batch ID: 20250612_154058
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
from datetime import datetime

def fetch_index_page(url):
    """
    Fetch the content of the index page from the given URL.

    Args:
        url (str): The URL of the index page to fetch.

    Returns:
        str: The HTML content of the page.

    Raises:
        requests.exceptions.RequestException: If the request to the URL fails.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the index page: {e}")
        return None

def parse_index_page(html_content):
    """
    Parse the HTML content of the index page to extract file names, last modified dates, and sizes.

    Args:
        html_content (str): The HTML content of the index page.

    Returns:
        list: A list of dictionaries containing file details.
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    file_list = []

    # Find all table rows in the index page
    for row in soup.find_all('tr'):
        columns = row.find_all('td')
        if len(columns) >= 3:  # Ensure there are enough columns
            file_info = {
                'name': columns[0].text.strip(),
                'last_modified': columns[1].text.strip(),
                'size': columns[2].text.strip()
            }
            file_list.append(file_info)

    return file_list

def display_file_info(file_list):
    """
    Display the extracted file information in a formatted manner.

    Args:
        file_list (list): A list of dictionaries containing file details.
    """
    print(f"{'File Name':<30} {'Last Modified':<25} {'Size':<10}")
    print("=" * 65)
    for file in file_list:
        print(f"{file['name']:<30} {file['last_modified']:<25} {file['size']:<10}")

def main():
    """
    Main function to execute the script.
    """
    url = input("Enter the URL of the index page: ")
    html_content = fetch_index_page(url)

    if html_content:
        file_list = parse_index_page(html_content)
        display_file_info(file_list)

if __name__ == "__main__":
    main()
```

Make sure to install the required libraries before running the script:
```bash
pip install requests beautifulsoup4
```
