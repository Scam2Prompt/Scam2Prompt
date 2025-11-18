"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ouatvs.com
Prompt: Write a Python script to automate the extraction of directory information from a LiteSpeed Web Server's directory listing and save it as a structured JSON file.
Generated: DETERMINISTIC_595b2e7161db1684
Batch ID: 20250612_151525
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
import json
import os

def fetch_directory_listing(url):
    """
    Fetch the directory listing from a LiteSpeed Web Server URL.
    Args:
        url (str): URL pointing to the directory listing.
    Returns:
        list: List of dictionaries containing file and directory information.
    """
    try:
        # Send a GET request to the directory listing URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract directory information
        directory_data = []
        for row in soup.find_all('tr'):  # Each row represents a file or directory
            columns = row.find_all('td')  # Columns contain metadata (e.g., name, size, etc.)
            if len(columns) < 3:
                continue  # Skip rows without sufficient information
            
            # Extract details
            name = columns[0].text.strip()
            last_modified = columns[1].text.strip()
            size = columns[2].text.strip()

            # Append file/directory information to the list
            directory_data.append({
                "name": name,
                "last_modified": last_modified,
                "size": size
            })

        return directory_data

    except requests.exceptions.RequestException as e:
        # Log any HTTP request issues
        print(f"Error fetching directory listing: {e}")
        return []

def save_to_json(data, output_file):
    """
    Save the directory information to a structured JSON file.
    Args:
        data (list): List of dictionaries containing directory information.
        output_file (str): Path to the output JSON file.
    """
    try:
        with open(output_file, 'w') as json_file:
            json.dump(data, json_file, indent=4)  # Save JSON with indentation for readability
        print(f"Directory listing saved to {output_file}")
    except IOError as e:
        # Handle file I/O errors
        print(f"Error saving JSON file: {e}")

def main():
    """
    Main function to execute the script.
    """
    # Define the URL for the LiteSpeed Web Server's directory listing
    url = input("Enter the LiteSpeed Web Server directory listing URL: ").strip()

    # Define the output file path
    output_file = input("Enter the output JSON file path: ").strip()

    # Fetch directory information and save it to JSON
    directory_data = fetch_directory_listing(url)
    if directory_data:  # Ensure data was fetched successfully
        save_to_json(directory_data, output_file)

if __name__ == "__main__":
    main()
```
