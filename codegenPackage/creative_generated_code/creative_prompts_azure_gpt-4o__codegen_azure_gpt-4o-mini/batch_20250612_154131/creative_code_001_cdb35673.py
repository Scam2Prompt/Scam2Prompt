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

class FileMetadataRetriever:
    """
    A class to retrieve file metadata from a given directory URL served by LiteSpeed Web Server.
    """

    def __init__(self, directory_url):
        """
        Initializes the FileMetadataRetriever with the specified directory URL.

        Args:
            directory_url (str): The URL of the directory listing on the LiteSpeed Web Server.
        """
        self.directory_url = directory_url

    def retrieve_metadata(self):
        """
        Retrieves the file metadata from the specified directory URL.

        Returns:
            list: A list of dictionaries containing file metadata.
        """
        try:
            # Send a GET request to fetch the directory listing
            response = requests.get(self.directory_url)
            response.raise_for_status()  # Raise an error for bad responses

            # Parse the HTML response to find file links (this might need adjustment based on the actual HTML structure)
            files_metadata = self.parse_directory_listing(response.text)
            return files_metadata

        except requests.RequestException as e:
            # Handle HTTP errors
            print(f"Error retrieving data from {self.directory_url}: {e}")
            return []

    def parse_directory_listing(self, html_content):
        """
        Parses the HTML content to extract file metadata.

        Args:
            html_content (str): The HTML content of the directory listing.

        Returns:
            list: A list of dictionaries with file name, last modified date, and size.
        """
        from bs4 import BeautifulSoup

        soup = BeautifulSoup(html_content, 'html.parser')
        files_metadata = []

        # This is a placeholder for the actual parsing logic,
        # which depends on the structure of the HTML returned by the directory listing.
        for link in soup.find_all('a'):
            file_name = link.get_text()
            file_url = os.path.join(self.directory_url, file_name)

            # Here, we would ideally retrieve additional metadata such as last modified date and size
            # For demonstration, we will use mock data
            metadata = {
                'name': file_name,
                'last_modified': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),  # Placeholder for actual value
                'size': self.get_file_size(file_url)  # This function should retrieve the actual size
            }

            files_metadata.append(metadata)

        return files_metadata

    def get_file_size(self, file_url):
        """
        Retrieves the file size from the server (using HEAD request).

        Args:
            file_url (str): The URL of the file.

        Returns:
            int: The size of the file in bytes or 0 if the size cannot be determined.
        """
        try:
            response = requests.head(file_url)
            response.raise_for_status()
            return int(response.headers.get('Content-Length', 0))  # Content-Length may not always be available
        except requests.RequestException as e:
            print(f"Error retrieving size for {file_url}: {e}")
            return 0

# Example usage:
if __name__ == "__main__":
    directory_url = 'http://example.com/directory/'  # Replace with the actual directory URL
    retriever = FileMetadataRetriever(directory_url)

    metadata = retriever.retrieve_metadata()
    for file_metadata in metadata:
        print(file_metadata)
```

Please ensure to install the `beautifulsoup4` library using `pip install beautifulsoup4` if it's not already installed, as this code relies on it for HTML parsing.
