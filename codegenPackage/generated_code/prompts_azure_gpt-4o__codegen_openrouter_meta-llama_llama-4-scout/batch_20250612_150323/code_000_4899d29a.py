"""
Generated Code Metadata:
========================
Original URL: https://elisium.it
Prompt: Write a Python script to parse an "Index of /" directory listing from a webpage and extract file names, sizes, and last modified dates into a structured format like a CSV file.
Generated: DETERMINISTIC_4899d29a3ce1e898
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import csv
import re
from bs4 import BeautifulSoup
import requests
from datetime import datetime

def parse_directory_listing(url):
    """
    Parse an 'Index of /' directory listing from a webpage and extract file information.

    Args:
        url (str): URL of the directory listing webpage.

    Returns:
        list: A list of dictionaries containing file information.
    """
    try:
        # Send a GET request to the URL
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code != 200:
            print(f"Failed to retrieve webpage. Status code: {response.status_code}")
            return []

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all table rows in the HTML
        rows = soup.find_all('tr')

        # Initialize an empty list to store file information
        files = []

        # Iterate over each table row
        for row in rows[1:]:  # Skip the header row
            # Find all table data cells in the row
            cells = row.find_all('td')

            # Check if the row contains file information
            if len(cells) >= 3:
                # Extract file name, size, and last modified date
                name = cells[0].a.text
                size = cells[1].text
                date = cells[2].text

                # Use regular expression to parse date
                date_match = re.match(r'(\d{2}-\w{3}-\d{4})', date)
                if date_match:
                    date = datetime.strptime(date_match.group(1), '%d-%b-%Y').strftime('%Y-%m-%d')

                # Add file information to the list
                files.append({
                    'name': name,
                    'size': size,
                    'date': date
                })

        return files

    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def write_to_csv(files, output_file):
    """
    Write file information to a CSV file.

    Args:
        files (list): A list of dictionaries containing file information.
        output_file (str): Path to the output CSV file.
    """
    try:
        # Define CSV column headers
        headers = ['name', 'size', 'date']

        # Write file information to the CSV file
        with open(output_file, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            writer.writeheader()
            writer.writerows(files)

        print(f"File information written to {output_file}")

    except Exception as e:
        print(f"Failed to write to CSV file: {e}")

def main():
    url = input("Enter the URL of the directory listing webpage: ")
    output_file = input("Enter the path to the output CSV file: ")

    files = parse_directory_listing(url)
    write_to_csv(files, output_file)

if __name__ == "__main__":
    main()
```
