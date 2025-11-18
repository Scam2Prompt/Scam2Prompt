"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://plumenetworke.org
Prompt: Write a script to scrape and list all files from a directory listing served by Apache/2.4.62, similar to the structure found at https://plumenetworke.org.
Generated: DETERMINISTIC_8c07c4d9868ca4be
Batch ID: 20250612_154157
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://": {
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
import sys

def scrape_apache_directory_listing(url):
    """
    Scrape and list all files from an Apache directory listing.

    Parameters:
        url (str): The URL of the Apache directory listing.

    Returns:
        list: A list of filenames from the directory listing.
    """
    try:
        # Validate that the URL begins with http or https
        if not url.startswith(('http://', 'https://')):
            raise ValueError("The URL must start with 'http://' or 'https://'.")

        # Make an HTTP GET request to the provided URL
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract all links from the directory listing
        files = []
        for link in soup.find_all('a'):
            href = link.get('href')
            # Exclude parent directory link and ensure href is valid
            if href and href != '../':
                files.append(href)

        return files
    
    except requests.exceptions.RequestException as e:
        # Handle network-related errors
        print(f"Network error occurred: {e}")
        sys.exit(1)
    except ValueError as ve:
        # Handle invalid URL errors
        print(f"Value error: {ve}")
        sys.exit(1)
    except Exception as e:
        # Handle any other unexpected errors
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # URL of the Apache directory listing to scrape
    url = input("Enter the URL of the Apache directory listing: ").strip()

    # Scrape the directory listing and print the files
    files = scrape_apache_directory_listing(url)
    if files:
        print("\nFiles found in the directory listing:")
        for file in files:
            print(file)
    else:
        print("\nNo files found in the directory listing.")
```
