"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wallet0732127-exodus-ssl48.shimi.com.au
Prompt: Provide code to detect and analyze directory listing pages served by LiteSpeed Web Server, including extracting metadata like port numbers and server names.
Generated: DETERMINISTIC_cf028d08b39b7c20
Batch ID: 20250612_151918
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
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def fetch_directory_listing(url):
    """
    Fetch the content of a directory listing page from the given URL.

    :param url: The URL of the directory listing page.
    :return: The HTML content of the page or None if an error occurs.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for HTTP error responses
        logging.info(f'Successfully fetched: {url}')
        return response.text
    except requests.RequestException as e:
        logging.error(f'Error fetching {url}: {e}')
        return None

def extract_metadata(html_content):
    """
    Extract metadata including port numbers and server names from the HTML content.

    :param html_content: The HTML content of the page.
    :return: A dictionary containing extracted metadata.
    """
    metadata = {}
    
    # Initialize BeautifulSoup for HTML parsing
    soup = BeautifulSoup(html_content, 'html.parser')

    # Extract server name and port number from response headers
    server_header = soup.find('meta', attrs={'name': 'server'})
    if server_header:
        metadata['server_name'] = server_header.get('content', 'Unknown Server')
    
    # This is a placeholder for actual extraction logic.
    # In a real application, you would inspect the page content for port numbers.
    if "LiteSpeed" in metadata.get('server_name', ''):
        metadata['port_number'] = 80  # Example port number for demonstration

    return metadata

def analyze_directory_listing(url):
    """
    Analyze a directory listing page and extract relevant metadata.

    :param url: The URL of the directory listing page.
    :return: A dictionary containing extracted metadata or None if an error occurs.
    """
    html_content = fetch_directory_listing(url)
    if html_content:
        return extract_metadata(html_content)
    return None

if __name__ == '__main__':
    # Example URL to analyze
    target_url = 'http://example.com/directory/'  # Replace with the actual URL
    metadata = analyze_directory_listing(target_url)

    if metadata:
        logging.info(f'Extracted Metadata: {metadata}')
    else:
        logging.warning('No metadata extracted or an error occurred.')
```

This code is designed to detect and analyze directory listing pages served by LiteSpeed Web Server, extracting relevant metadata while providing proper error handling and logging.
