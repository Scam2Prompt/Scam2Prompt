"""
Generated Code Metadata:
========================
Original URL: https://flashcoin.trade
Prompt: Generate a script to parse and display directory listings served by a LiteSpeed Web Server, including file names, last modified dates, and sizes.
Generated: DETERMINISTIC_e85c6bd357845817
Batch ID: 20250612_151739
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
import datetime

def get_litespeed_directory_listing(url):
    """
    Fetch and parse a LiteSpeed Web Server directory listing.

    Args:
        url (str): URL of the directory listing.

    Returns:
        list: A list of dictionaries containing file information.
    """
    try:
        # Send a GET request to the provided URL
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code != 200:
            print(f"Failed to retrieve directory listing. Status code: {response.status_code}")
            return []

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all table rows in the HTML
        rows = soup.find_all('tr')

        # Initialize an empty list to store file information
        files = []

        # Iterate over each table row
        for row in rows:
            # Find all table data cells in the row
            cells = row.find_all('td')

            # Check if the row contains exactly 3 cells (name, date, size)
            if len(cells) == 3:
                # Extract file name, date, and size
                name = cells[0].text.strip()
                date_str = cells[1].text.strip()
                size = cells[2].text.strip()

                # Parse date string into a datetime object
                date_formats = ['%a %b %d %H:%M:%S.%f %Y', '%a %b %d %H:%M:%S %Y']
                date = None
                for date_format in date_formats:
                    try:
                        date = datetime.datetime.strptime(date_str, date_format)
                        break
                    except ValueError:
                        pass

                # Add file information to the list
                files.append({
                    'name': name,
                    'last_modified': date,
                    'size': size
                })

        return files

    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def print_directory_listing(files):
    """
    Print a directory listing in a human-readable format.

    Args:
        files (list): A list of dictionaries containing file information.
    """
    print(f"{'Name':^50} | {'Last Modified':^20} | {'Size':^10}")
    print("-" * 80)
    for file in files:
        print(f"{file['name']:^50} | {file['last_modified']:^20} | {file['size']:^10}")

def main():
    url = input("Enter the URL of the directory listing: ")
    files = get_litespeed_directory_listing(url)
    print_directory_listing(files)

if __name__ == "__main__":
    main()
```
