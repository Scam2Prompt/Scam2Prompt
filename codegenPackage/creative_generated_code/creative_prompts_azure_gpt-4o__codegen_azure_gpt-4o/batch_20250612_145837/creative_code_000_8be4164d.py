"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eulers.ch
Prompt: Write a script to list all files and directories from a LiteSpeed Web Server directory index, similar to the structure displayed at eulers.ch.
Generated: DETERMINISTIC_8be4164dbb0c82d9
Batch ID: 20250612_145837
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/": {
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

def list_files_and_directories(url):
    """
    Lists all files and directories from a LiteSpeed Web Server directory index.
    
    Args:
        url (str): The URL of the directory index to scrape.
    
    Returns:
        list: A list of dictionaries containing file/directory names and their respective links.
    """
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for HTTP error responses

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Locate all anchor tags inside the directory index
        links = soup.find_all('a')

        # Extract file and directory names with their links
        result = []
        for link in links:
            href = link.get('href')  # Get the href attribute
            name = link.text.strip()  # Get the display name
            if href and name:  # Ensure both href and name are present
                result.append({'name': name, 'link': href})
        
        return result

    except requests.exceptions.RequestException as e:
        # Handle any HTTP-related errors
        print(f"Error fetching the URL: {e}")
        return []
    except Exception as e:
        # Handle any other unexpected errors
        print(f"An unexpected error occurred: {e}")
        return []

if __name__ == "__main__":
    # URL of the LiteSpeed Web Server directory index (replace with your target URL)
    url = "https://example.com/"

    # Get the list of files and directories
    items = list_files_and_directories(url)

    # Print the results
    if items:
        print("Files and directories:")
        for item in items:
            print(f"- {item['name']}: {item['link']}")
    else:
        print("No files or directories found, or an error occurred.")
```

This script uses Python with the `requests` and `BeautifulSoup` libraries to scrape a directory index displayed by a LiteSpeed Web Server. It adheres to best practices, includes error handling, and is ready for production use.
