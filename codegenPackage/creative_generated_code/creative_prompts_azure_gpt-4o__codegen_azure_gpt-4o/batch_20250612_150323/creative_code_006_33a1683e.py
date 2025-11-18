"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elisium.it
Prompt: Using Python, write a script that filters and downloads only files with specific extensions (e.g., .txt or .pdf) from an "Index of /" directory listing webpage.
Generated: DETERMINISTIC_33a1683eb986503f
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def download_files_from_index(url, extensions, output_dir):
    """
    Filters and downloads files with specific extensions from an "Index of /" directory listing webpage.

    Args:
        url (str): URL of the directory listing page.
        extensions (list): List of file extensions to filter (e.g., ['.txt', '.pdf']).
        output_dir (str): Directory where downloaded files will be saved.

    Raises:
        Exception: If the webpage cannot be accessed or any errors occur during download.
    """
    try:
        # Create output directory if it doesn't exist
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Fetch the webpage content
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all anchor tags in the webpage to extract links
        links = soup.find_all('a')
        for link in links:
            href = link.get('href')
            # Skip invalid or empty links
            if not href or not href.startswith(('/')):
                continue
            
            # Check if the link ends with any of the desired extensions
            if any(href.endswith(ext) for ext in extensions):
                # Construct the absolute URL for the file
