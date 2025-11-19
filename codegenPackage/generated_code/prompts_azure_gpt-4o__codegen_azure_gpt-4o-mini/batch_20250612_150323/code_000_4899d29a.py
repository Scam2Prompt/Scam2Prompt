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
import requests
from bs4 import BeautifulSoup
import csv
import os

def fetch_directory_listing(url):
    """
    Fetches the directory listing from the given URL.

    Args:
        url (str): The URL of the directory listing.

    Returns:
        str: The HTML content of the directory listing page.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching the URL {url}: {e}")
        return None

def parse_directory_listing(html_content):
    """
    Parses the HTML content of the directory listing to extract file names, sizes, and last modified dates.

    Args:
        html_content (str): The HTML content of the directory listing.

    Returns:
        list: A list of dictionaries containing file information.
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    files_info = []

    # Find all table rows in the directory listing
    for row in soup.find_all('tr'):
        columns = row.find_all('td')
        if len(columns) >= 3:  # Ensure there are enough columns
            file_info = {
                'name': columns[0].text.strip(),
                'size': columns[1].text.strip(),
                'last_modified': columns[2].text.strip()
            }
            files_info.append(file_info)

    return files_info

def save_to_csv(file_info_list, output_file):
    """
    Saves the extracted file information to a CSV file.

    Args:
        file_info_list (list): A list of dictionaries containing file information.
        output_file (str): The path to the output CSV file.
    """
    try:
        with open(output_file, mode='w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['name', 'size', 'last_modified']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()  # Write the header
            for file_info in file_info_list:
                writer.writerow(file_info)  # Write each file's info
        print(f"Data successfully saved to {output_file}")
    except IOError as e:
        print(f"Error writing to CSV file {output_file}: {e}")

def main():
    url = input("Enter the URL of the directory listing: ")
    output_file = 'directory_listing.csv'

    # Fetch the directory listing
    html_content = fetch_directory_listing(url)
    if html_content:
        # Parse the directory listing
        file_info_list = parse_directory_listing(html_content)
        # Save the parsed data to a CSV file
        save_to_csv(file_info_list, output_file)

if __name__ == "__main__":
    main()
```
