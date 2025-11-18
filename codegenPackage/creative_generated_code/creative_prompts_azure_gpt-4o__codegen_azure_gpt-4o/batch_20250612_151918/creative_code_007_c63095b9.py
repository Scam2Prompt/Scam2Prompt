"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wallet0732127-exodus-ssl48.shimi.com.au
Prompt: Write a script to identify and log all accessible directories from a LiteSpeed Web Server URL, including subdirectories.
Generated: DETERMINISTIC_c63095b9a193bd10
Batch ID: 20250612_151918
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
import logging
import os

# Configure logging
logging.basicConfig(
    filename='accessible_directories.log', 
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Function to fetch and parse HTML content from a URL
def fetch_url_content(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
        return response.text
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching URL {url}: {e}")
        return None

# Function to identify accessible directories from a URL
def identify_accessible_directories(base_url):
    visited_urls = set()  # Set to keep track of visited URLs
    directories = []      # List to store accessible directories

    def crawl(url):
        if url in visited_urls:
            return  # Avoid revisiting the same URL
        
        visited_urls.add(url)
        logging.info(f"Scanning URL: {url}")
        
        html_content = fetch_url_content(url)
        if not html_content:
            return
        
        soup = BeautifulSoup(html_content, 'html.parser')
        links = soup.find_all('a')  # Find all <a> tags

        for link in links:
            href = link.get('href')
            if not href or href.startswith('#'):
                continue  # Skip empty or anchor links
            
            full_url = requests.compat.urljoin(url, href)  # Resolve relative URLs to full URLs
            
            # Check if the link points to a directory
            if full_url.endswith('/') and base_url in full_url:
                if full_url not in directories:
                    directories.append(full_url)
                    logging.info(f"Accessible directory found: {full_url}")
                
                # Recursively crawl subdirectories
                crawl(full_url)
    
    crawl(base_url)
    return directories

# Main function
def main():
    base_url = input("Enter the LiteSpeed Web Server URL (must end with '/'): ").strip()
    
    if not base_url.endswith('/'):
        logging.error("Provided URL does not end with '/'. Please enter a valid directory URL.")
        print("ERROR: The URL must end with '/'.")
        return

    logging.info(f"Starting directory scan for base URL: {base_url}")
    accessible_directories = identify_accessible_directories(base_url)

    # Log the results
    logging.info("Scan completed. Accessible directories:")
    for directory in accessible_directories:
        logging.info(directory)
    
    print("Accessible directories have been logged successfully.")

if __name__ == "__main__":
    main()
```
