"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flashcoin.trade
Prompt: Generate a script to parse and display directory listings served by a LiteSpeed Web Server, including file names, last modified dates, and sizes.
Generated: DETERMINISTIC_e85c6bd357845817
Batch ID: 20250612_151739
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


def parse_litespeed_directory(url):
    """
    Parses a directory listing served by a LiteSpeed Web Server.

    Args:
        url (str): The URL of the LiteSpeed directory listing.

    Returns:
        list[dict]: A list of dictionaries containing file details (name, last modified date, size).
    """
    try:
        # Send HTTP GET request to the server
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract table rows that contain file details
        rows = soup.find_all('tr')

        # List to store parsed file details
        files = []

        for row in rows:
            # Extract columns in the row
            cols = row.find_all('td')
            if len(cols) == 3:  # Ensure there are 3 columns (Name, Last Modified, Size)
                file_name = cols[0].text.strip()
                last_modified = cols[1].text.strip()
                size = cols[2].text.strip()

                # Attempt to parse the last modified date
                try:
                    last_modified_date = datetime.strptime(last_modified, '%Y-%m-%d %H:%M')
                except ValueError:
                    last_modified_date = None  # Handle invalid date format gracefully

                # Append file details to the list
                files.append({
                    'name': file_name,
                    'last_modified': last_modified_date,
                    'size': size
                })

        return files

    except requests.exceptions.RequestException as e:
        # Handle network-related errors
        print(f"Error fetching directory listing: {e}")
        return []

    except Exception as e:
        # Catch-all for other errors
        print(f"An unexpected error occurred: {e}")
        return []


def display_files(files):
    """
    Display file details in a readable format.

    Args:
        files (list[dict]): List of file details.
    """
    print(f"{'File Name':<40}{'Last Modified':<20}{'Size':<10}")
    print("-" * 70)
    for file in files:
        last_modified = file['last_modified'].strftime('%Y-%m-%d %H:%M') if file['last_modified'] else 'N/A'
        print(f"{file['name']:<40}{last_modified:<20}{file['size']:<10}")


if __name__ == "__main__":
    # Example usage
    url = input("Enter the URL of the LiteSpeed directory listing: ").strip()
    files = parse_litespeed_directory(url)
    if files:
        display_files(files)
    else:
        print("No files found or an error occurred.")
```
