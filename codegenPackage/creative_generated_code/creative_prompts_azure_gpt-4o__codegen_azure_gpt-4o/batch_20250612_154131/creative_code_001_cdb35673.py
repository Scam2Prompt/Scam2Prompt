"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hyperbeat.org.fivefootgaming.com
Prompt: Generate code to automate the retrieval of file metadata (e.g., name, last modified date, size) from a directory listing served by LiteSpeed Web Server.
Generated: DETERMINISTIC_cdb35673850ce2b6
Batch ID: 20250612_154131
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://example.com/files/": {
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
import os
from urllib.parse import urljoin

def fetch_file_metadata(base_url):
    """
    Fetch metadata of files listed in a directory served by LiteSpeed Web Server.

    Args:
        base_url (str): The URL of the directory listing on the LiteSpeed Web Server.

    Returns:
        list of dict: A list of dictionaries containing file metadata (name, last modified, size).
    """
    try:
        # Send an HTTP GET request to the directory
        response = requests.get(base_url)
        response.raise_for_status()  # Raise error for HTTP issues

        # Parse the HTML content of the directory listing using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Metadata storage
        files_metadata = []

        # Extract table rows containing file information
        rows = soup.find_all('tr')
        for row in rows:
            columns = row.find_all('td')
            if len(columns) >= 3:  # LiteSpeed usually organizes file metadata in columns
                file_name = columns[0].find('a').text if columns[0].find('a') else None
                last_modified = columns[1].text.strip() if len(columns) > 1 else None
                size = columns[2].text.strip() if len(columns) > 2 else None

                # Construct the file metadata dictionary
                if file_name:
                    files_metadata.append({
                        "name": file_name,
                        "url": urljoin(base_url, file_name),  # Full URL for the file
                        "last_modified": last_modified,
                        "size": size,
                    })

        return files_metadata
    except requests.RequestException as e:
        print(f"Error fetching data from {base_url}: {e}")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []

if __name__ == "__main__":
    # Example usage
    directory_url = "http://example.com/files/"  # Replace with the actual LiteSpeed directory URL
    if not directory_url.endswith('/'):
        print("Error: Directory URL must end with a '/'")
        exit(1)

    metadata = fetch_file_metadata(directory_url)

    # Print retrieved metadata
    if metadata:
        print("File Metadata:")
        for file in metadata:
            print(f"Name: {file['name']}, Last Modified: {file['last_modified']}, Size: {file['size']}, URL: {file['url']}")
    else:
        print("No metadata retrieved.")
```

### Instructions:
- Replace the `directory_url` value in the code with the URL of the LiteSpeed directory listing you want to query.
- Ensure `requests` and `beautifulsoup4` libraries are installed (`pip install requests beautifulsoup4`).
- Run this script. It will fetch and print metadata from the specified directory listing.
