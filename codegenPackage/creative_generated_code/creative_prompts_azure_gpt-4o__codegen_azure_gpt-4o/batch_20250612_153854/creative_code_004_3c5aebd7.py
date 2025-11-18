"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hyperliquidfndtn.org
Prompt: Develop a tool to interact with a LiteSpeed Web Server directory listing and retrieve metadata (e.g., file size, modification date) for all files.
Generated: DETERMINISTIC_3c5aebd75a1d0d26
Batch ID: 20250612_153854
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
import os
import requests
from datetime import datetime
from urllib.parse import urljoin

def fetch_directory_listing(base_url):
    """
    Fetch the directory listing from the LiteSpeed Web Server.
    
    Args:
        base_url (str): The base URL of the directory on the server.
    
    Returns:
        List[dict]: A list of dictionaries containing metadata for each file.
    """
    try:
        # Send GET request to the base URL
        response = requests.get(base_url)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx, 5xx)

        # Parse the directory listing (assuming HTML response containing file links)
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        file_metadata = []
        
        # Iterate through all links in the HTML
        for link in soup.find_all('a'):
            href = link.get('href')
            if href and not href.startswith('?'):  # Skip query links and irrelevant paths
                file_url = urljoin(base_url, href)
                
                # Get file metadata by sending a HEAD request
                head_response = requests.head(file_url)
                head_response.raise_for_status()  # Check for errors
                
                # Extract metadata
                size = head_response.headers.get('Content-Length', 'Unknown')
                last_modified = head_response.headers.get('Last-Modified', 'Unknown')

                # Build metadata object
                file_metadata.append({
                    'file_name': href,
                    'file_url': file_url,
                    'file_size': int(size) if size.isdigit() else size,
                    'last_modified': datetime.strptime(last_modified, '%a, %d %b %Y %H:%M:%S %Z') 
                                    if last_modified != 'Unknown' else last_modified
                })

        return file_metadata

    except requests.exceptions.RequestException as e:
        print(f"Error interacting with server: {e}")
        return []

def main():
    """
    Main function to demonstrate fetching metadata from a LiteSpeed Web Server directory listing.
    """
    # Base URL of the LiteSpeed Web Server directory
    base_url = "http://example.com/directory/"

    # Fetch metadata for files in the directory
    file_metadata = fetch_directory_listing(base_url)

    # Print file metadata
    if file_metadata:
        print("File Metadata:")
        for file in file_metadata:
            print(f"Name: {file['file_name']}")
            print(f"URL: {file['file_url']}")
            print(f"Size: {file['file_size']}")
            print(f"Last Modified: {file['last_modified']}")
            print("-" * 40)
    else:
        print("No files found or an error occurred.")

if __name__ == "__main__":
    main()
```

### Requirements:
1. Install `requests` and `beautifulsoup4` libraries:
   ```
   pip install requests beautifulsoup4
   ```
