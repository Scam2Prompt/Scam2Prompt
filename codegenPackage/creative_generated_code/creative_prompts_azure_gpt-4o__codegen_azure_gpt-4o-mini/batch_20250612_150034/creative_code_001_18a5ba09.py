"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phantom-connect.com
Prompt: Generate code to interact with a LiteSpeed Web Server and retrieve directory listings, similar to the structure shown on phantom-connect.com.
Generated: DETERMINISTIC_18a5ba09f09414bd
Batch ID: 20250612_150034
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://example.com/path/to/directory": {
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

class LiteSpeedDirectoryLister:
    """
    A class to interact with a LiteSpeed Web Server and retrieve directory listings.

    Attributes:
        base_url (str): The base URL of the LiteSpeed server.
    """

    def __init__(self, base_url):
        """
        Initializes the LiteSpeedDirectoryLister with the given base URL.

        Args:
            base_url (str): The base URL to connect to the LiteSpeed server.
        """
        if not base_url.endswith('/'):
            base_url += '/'
        self.base_url = base_url

    def get_directory_listing(self, path=''):
        """
        Retrieves the directory listing from the specified path.

        Args:
            path (str): The path to the directory on the server.

        Returns:
            list: A list of directory contents (files and folders).

        Raises:
            ValueError: If the response is not successful.
        """
        url = os.path.join(self.base_url, path)
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raises an HTTPError for bad responses
        except requests.RequestException as e:
            raise ValueError(f"Failed to retrieve directory listing: {e}")

        # Assuming the server responds with a JSON structure
        try:
            directory_contents = response.json()
        except ValueError:
            raise ValueError("Invalid JSON response from server.")

        return directory_contents

    def display_listing(self, contents):
        """
        Displays the directory contents in a user-friendly format.

        Args:
            contents (list): A list of directory contents to display.
        """
        if not contents:
            print("Directory is empty.")
            return
        
        print("Directory Listing:")
        for item in contents:
            print(f"- {item}")

def main():
    """
    Main function to run the directory lister.
    """
    # Example base URL; replace with actual URL where the LiteSpeed server is hosted.
    base_url = 'http://example.com/path/to/directory'
    
    lister = LiteSpeedDirectoryLister(base_url)

    try:
        # Get the directory listing from the root path; adjust as necessary.
        contents = lister.get_directory_listing()
        lister.display_listing(contents)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
```
