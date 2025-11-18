"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hostmkt.com
Prompt: Create a script using the `requests` library to download all files listed on a directory index page, ensuring the script handles relative URLs properly.
Generated: DETERMINISTIC_d549ed242acc30ac
Batch ID: 20250612_150902
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
from urllib.parse import urljoin
from bs4 import BeautifulSoup

def download_files_from_directory_index(url, download_folder):
    """
    Download all files from the given directory index URL.

    Args:
        url (str): The URL of the directory index page.
        download_folder (str): The local folder to which files will be downloaded.
    
    Raises:
        ValueError: If the URL is invalid or if the download folder cannot be created.
    """
    
    # Ensure the download folder exists
    if not os.path.exists(download_folder):
        try:
            os.makedirs(download_folder)
        except OSError as e:
            raise ValueError(f"Could not create download folder: {e}")

    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)

        # Parse the content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all anchor tags with href attributes
        for link in soup.find_all('a', href=True):
            file_url = urljoin(url, link['href'])  # Handle relative URLs correctly
            
            # Download the file
            try:
                download_file(file_url, download_folder)
            except Exception as e:
                print(f"Failed to download {file_url}: {e}")

    except requests.exceptions.RequestException as e:
        print(f"Failed to retrieve the directory index: {e}")

def download_file(file_url, download_folder):
    """
    Download a single file from the given URL and save it to the specified folder.

    Args:
        file_url (str): The URL of the file to download.
        download_folder (str): The local folder where the file will be saved.
    """
    response = requests.get(file_url, stream=True)  # Stream to handle large files
    response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)

    # Extract the filename from the URL
    filename = os.path.basename(file_url)
    file_path = os.path.join(download_folder, filename)

    # Write the file to disk
    with open(file_path, 'wb') as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)  # Write the chunk to the file

    print(f"Downloaded: {file_url} to {file_path}")

if __name__ == "__main__":
    # Example usage
    directory_url = 'http://example.com/directory/'  # Replace with the directory index URL
    download_directory = 'downloads'  # Local folder to save downloaded files

    download_files_from_directory_index(directory_url, download_directory)
```
