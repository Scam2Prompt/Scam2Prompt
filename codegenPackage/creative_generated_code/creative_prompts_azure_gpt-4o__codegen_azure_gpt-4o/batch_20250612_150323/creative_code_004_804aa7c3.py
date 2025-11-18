"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elisium.it
Prompt: Create a Python program that generates a summary report of all files in an "Index of /" directory listing, including their names, sizes, and last modified dates.
Generated: DETERMINISTIC_804aa7c32a43136a
Batch ID: 20250612_150323
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


def fetch_directory_listing(url):
    """
    Fetches the HTML content of the directory listing from the given URL.

    Args:
        url (str): The URL of the "Index of /" directory.

    Returns:
        str: HTML content of the page.

    Raises:
        Exception: If the request fails or the URL is invalid.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP request errors
        return response.text
    except requests.exceptions.RequestException as e:
        raise Exception(f"Error fetching URL: {e}")


def parse_directory_listing(html_content):
    """
    Parses the HTML content of the directory listing and extracts file details.

    Args:
        html_content (str): HTML content of the directory listing.

    Returns:
        list of dict: List of dictionaries containing file details (name, size, date).
    """
    try:
        soup = BeautifulSoup(html_content, 'html.parser')
        rows = soup.find_all('tr')  # Assuming rows are in <tr> tags

        files = []
        for row in rows:
            cols = row.find_all('td')
            # Expecting at least 3 columns: name, size, and last modified date
            if len(cols) >= 3:
                file_name = cols[0].text.strip()
                file_size = cols[1].text.strip()  # Size could be '-' for directories
                last_modified = cols[2].text.strip()

                # Convert last_modified to a standard datetime format
                try:
                    last_modified = datetime.strptime(last_modified, "%Y-%m-%d %H:%M")
                except ValueError:
                    last_modified = None  # Handle invalid dates gracefully

                files.append({
                    'name': file_name,
                    'size': file_size,
                    'last_modified': last_modified
                })
        return files
    except Exception as e:
        raise Exception(f"Error parsing HTML content: {e}")


def generate_summary_report(files):
    """
    Generates a summary report for the given list of files.

    Args:
        files (list of dict): List of dictionaries containing file details.

    Returns:
        str: A formatted summary report as a string.
    """
    report_lines = ["Summary Report of Directory Listing"]
    report_lines.append("=" * 40)
    for file in files:
        last_modified = file['last_modified'].strftime("%Y-%m-%d %H:%M") if file['last_modified'] else "N/A"
        report_lines.append(f"Name: {file['name']}")
        report_lines.append(f"Size: {file['size']}")
        report_lines.append(f"Last Modified: {last_modified}")
        report_lines.append("-" * 40)
    return "\n".join(report_lines)


def main():
    """
    Main function to execute the program logic.
    """
    url = input("Enter the URL of the 'Index of /' directory: ")
    try:
        # Step 1: Fetch directory listing
        html_content = fetch_directory_listing(url)

        # Step 2: Parse directory listing
        files = parse_directory_listing(html_content)

        # Step 3: Generate and display summary report
        report = generate_summary_report(files)
        print(report)
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
