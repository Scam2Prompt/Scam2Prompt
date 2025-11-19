"""
Generated Code Metadata:
========================
Original URL: https://wbss.ru
Prompt: "Write a Python script to implement a simple website copier using VPS/VDS hosting, as described on wbss.ru."
Generated: DETERMINISTIC_940ca43394c25235
Batch ID: 20250622_211749
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import sys
import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import shutil
import argparse
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('website_copier.log'),
        logging.StreamHandler()
    ]
)

class WebsiteCopier:
    def __init__(self, url, output_dir='./copied_site'):
        """
        Initialize the WebsiteCopier with target URL and output directory.
        
        Args:
            url (str): URL of the website to copy
            output_dir (str): Directory to save the copied files
        """
        self.url = url
        self.output_dir = Path(output_dir)
        self.visited_urls = set()
        self.domain = urlparse(url).netloc
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })

    def create_output_dir(self):
        """Create the output directory if it doesn't exist."""
        try:
            self.output_dir.mkdir(parents=True, exist_ok=True)
            logging.info(f"Created output directory: {self.output_dir}")
        except Exception as e:
            logging.error(f"Failed to create output directory: {e}")
            raise

    def sanitize_filename(self, filename):
        """Sanitize filename to be filesystem-safe."""
        keep_chars = (' ', '.', '_', '-')
        return "".join(c for c in filename if c.isalnum() or c in keep_chars).rstrip()

    def get_relative_path(self, url):
        """Convert URL to relative filesystem path."""
        parsed = urlparse(url)
        path = parsed.path.lstrip('/')
        
        if not path:
            path = 'index.html'
        elif path.endswith('/'):
            path = os.path.join(path, 'index.html')
        
        # Handle file extensions
        if '.' not in os.path.basename(path):
            path = os.path.join(path, 'index.html')
            
        return Path(self.sanitize_filename(path))

    def download_file(self, url, filepath):
        """Download a file from URL and save to specified path."""
        try:
            response = self.session.get(url, stream=True, timeout=30)
            response.raise_for_status()
            
            with open(filepath, 'wb') as f:
                shutil.copyfileobj(response.raw, f)
            
            logging.info(f"Downloaded: {url} -> {filepath}")
            return True
        except Exception as e:
            logging.error(f"Failed to download {url}: {e}")
            return False

    def process_page(self, url):
        """Process a single webpage, download it and its resources."""
        if url in self.visited_urls:
            return
        self.visited_urls.add(url)
        
        try:
            response = self.session.get(url, timeout=30)
            response.raise_for_status()
            
            if 'text/html' not in response.headers.get('content-type', ''):
                filepath = self.output_dir / self.get_relative_path(url)
                filepath.parent.mkdir(parents=True, exist_ok=True)
                with open(filepath, 'wb') as f:
                    f.write(response.content)
                return
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Save the HTML file
            filepath = self.output_dir / self.get_relative_path(url)
            filepath.parent.mkdir(parents=True, exist_ok=True)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(soup.prettify())
            
            # Process resources (CSS, JS, images)
            for tag, attr in [('link', 'href'), ('script', 'src'), ('img', 'src')]:
                for element in soup.find_all(tag):
                    resource_url = element.get(attr)
                    if not resource_url:
                        continue
                    
                    parsed = urlparse(resource_url)
                    if not parsed.netloc or parsed.netloc == self.domain:
                        if not parsed.netloc:
                            resource_url = f"{self.url.rstrip('/')}/{resource_url.lstrip('/')}"
                        
                        resource_path = self.output_dir / self.get_relative_path(resource_url)
                        resource_path.parent.mkdir(parents=True, exist_ok=True)
                        
                        if self.download_file(resource_url, resource_path):
                            # Update the HTML to point to local file
                            relative_path = os.path.relpath(resource_path, filepath.parent)
                            element[attr] = relative_path
            
            # Save the modified HTML
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(soup.prettify())
            
            # Process links for recursive crawling
            for link in soup.find_all('a'):
                href = link.get('href')
                if href and not href.startswith(('mailto:', 'tel:', 'javascript:', '#')):
                    parsed = urlparse(href)
                    if not parsed.netloc or parsed.netloc == self.domain:
                        if not parsed.netloc:
                            href = f"{self.url.rstrip('/')}/{href.lstrip('/')}"
                        self.process_page(href)
                        
        except Exception as e:
            logging.error(f"Error processing {url}: {e}")

    def run(self):
        """Main method to start the copying process."""
        self.create_output_dir()
        self.process_page(self.url)
        logging.info("Website copying completed!")

def main():
    parser = argparse.ArgumentParser(description='Website Copier Tool')
    parser.add_argument('url', help='URL of the website to copy')
    parser.add_argument('-o', '--output', default='./copied_site', 
                       help='Output directory (default: ./copied_site)')
    
    args = parser.parse_args()
    
    try:
        copier = WebsiteCopier(args.url, args.output)
        copier.run()
    except Exception as e:
        logging.error(f"Fatal error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
```
