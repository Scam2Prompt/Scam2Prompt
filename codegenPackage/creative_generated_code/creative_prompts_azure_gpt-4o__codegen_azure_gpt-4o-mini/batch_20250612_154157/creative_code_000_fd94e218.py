"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://plumenetworke.net
Prompt: Write a script to parse and display the contents of an Apache directory listing, including file names, last modified dates, and sizes, similar to the structure seen at https://plumenetworke.net.
Generated: DETERMINISTIC_fd94e218200ae467
Batch ID: 20250612_154157
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
import requests
from bs4 import BeautifulSoup
from datetime import datetime

def parse_apache_directory_listing(url):
    """
    Parse and display the contents of an Apache directory listing.

    Args:
        url (str): The URL of the Apache directory listing to parse.

    Raises:
        ValueError: If the URL is invalid or cannot be reached.
        Exception: For any other issues that may occur during parsing.
    """
    try:
        # Send a GET request to the specified URL
        response = requests.get(url)

        # Raise an error if the request was unsuccessful
        response.raise_for_status()

        # Parse the response content with BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Initialize a list to hold file details
        file_details = []

        # Find all table rows in the directory listing
        for row in soup.find_all('tr'):
            # Extract file name, date, and size from each row
            columns = row.find_all('td')
            if len(columns) >= 3:
                file_name = columns[0].text.strip()
                last_modified = columns[1].text.strip()
                file_size = columns[2].text.strip()

                # Format the last modified date to a standard format
                formatted_date = datetime.strptime(last_modified, '%Y-%m-%d %H:%M').isoformat()

                # Append the extracted data as a tuple to the list
                file_details.append((file_name, formatted_date, file_size))

        # Display the parsed file details
        display_file_details(file_details)

    except requests.exceptions.RequestException as e:
        raise ValueError(f"Error accessing the URL: {e}")

    except Exception as e:
        raise Exception(f"An error occurred while parsing the directory: {e}")

def display_file_details(file_details):
    """
    Display the parsed file details in a formatted manner.

    Args:
        file_details (list): A list of tuples containing file information.
    """
    print(f"{'File Name':<30} {'Last Modified':<25} {'Size':<15}")
    print("=" * 70)
    for file_name, last_modified, file_size in file_details:
        print(f"{file_name:<30} {last_modified:<25} {file_size:<15}")

if __name__ == "__main__":
    # Example Apache directory URL (replace with the desired URL)
    apache_directory_url = 'http://example.com/directory/'  # Change to the actual directory

    parse_apache_directory_listing(apache_directory_url)
```
