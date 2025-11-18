"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elisium.it
Prompt: Write a Python script to parse an "Index of /" directory listing from a webpage and extract file names, sizes, and last modified dates into a structured format like a CSV file.
Generated: DETERMINISTIC_4899d29a3ce1e898
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
import requests
from bs4 import BeautifulSoup
import csv
import re
from datetime import datetime


def fetch_directory_listing(url):
    """
    Fetches the HTML content of the provided URL.

    Args:
        url (str): The URL of the "Index of /" directory listing.

    Returns:
        str: The HTML content of the page.

    Raises:
        requests.exceptions.RequestException: If the request fails.
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        return response.text
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Failed to fetch the URL: {e}")


def parse_directory_listing(html_content):
    """
    Parses the "Index of /" HTML directory listing to extract file information.

    Args:
        html_content (str): The HTML content of the directory listing.

    Returns:
        list: A list of dictionaries containing file information (name, size, last modified date).
    """
    soup = BeautifulSoup(html_content, "html.parser")
    rows = soup.find_all("tr")  # Typically, file listings are in table rows
    file_info_list = []

    for row in rows:
        columns = row.find_all("td")
        # Check if row has enough columns (name, size, last modified)
        if len(columns) >= 3:
            # Extract and clean the data
            name = columns[1].get_text(strip=True)  # File name
            size = columns[2].get_text(strip=True)  # File size
            last_modified = columns[0].get_text(strip=True)  # Last modified date

            # Validate and parse the last modified date
            try:
                last_modified_date = datetime.strptime(last_modified, "%Y-%m-%d %H:%M")
            except ValueError:
                last_modified_date = None  # If parsing fails, set None

            # Append the parsed data to the list
            file_info_list.append({
                "name": name,
                "size": size,
                "last_modified": last_modified_date
            })

    return file_info_list


def save_to_csv(file_info_list, output_file):
    """
    Saves the parsed file information to a CSV file.

    Args:
        file_info_list (list): A list of dictionaries containing file information.
        output_file (str): Path to the output CSV file.

    Returns:
        None
    """
    fieldnames = ["name", "size", "last_modified"]
    try:
        with open(output_file, mode="w", newline="", encoding="utf-8") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for file_info in file_info_list:
                # Ensure last_modified is serialized correctly
                file_info["last_modified"] = file_info["last_modified"].strftime("%Y-%m-%d %H:%M") \
                    if file_info["last_modified"] else ""
                writer.writerow(file_info)
    except IOError as e:
        raise RuntimeError(f"Failed to write to CSV file: {e}")


if __name__ == "__main__":
    # Specify the URL of the "Index of /" directory and output CSV file
    directory_url = "http://example.com/directory/"  # Replace with actual URL
    output_csv = "directory_listing.csv"

    try:
        # Fetch, parse, and save the directory listing
        html = fetch_directory_listing(directory_url)
        files = parse_directory_listing(html)
        save_to_csv(files, output_csv)
        print(f"Directory listing successfully saved to '{output_csv}'.")
    except Exception as e:
        print(f"Error: {e}")
```
