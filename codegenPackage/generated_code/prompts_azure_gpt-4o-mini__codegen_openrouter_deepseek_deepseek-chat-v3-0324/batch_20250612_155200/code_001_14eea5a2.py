"""
Generated Code Metadata:
========================
Original URL: https://jiodigital.live
Prompt: Write a Python script that automates the process of downloading digital products from a store like Spec Digital Sales.
Generated: DETERMINISTIC_14eea5a278bafd1e
Batch ID: 20250612_155200
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import requests
from bs4 import BeautifulSoup
import json
import time
from urllib.parse import urljoin
from pathlib import Path

class DigitalProductDownloader:
    def __init__(self, config_file='config.json'):
        """
        Initialize the downloader with configuration from JSON file.
        """
        self.config = self._load_config(config_file)
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
        
    def _load_config(self, config_file):
        """
        Load configuration from JSON file.
        """
        try:
            with open(config_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            raise Exception(f"Config file {config_file} not found.")
        except json.JSONDecodeError:
            raise Exception(f"Invalid JSON in config file {config_file}.")
    
    def login(self):
        """
        Authenticate with the store using provided credentials.
        """
        login_url = self.config['login_url']
        payload = {
            'username': self.config['username'],
            'password': self.config['password']
        }
        
        try:
            response = self.session.post(login_url, data=payload)
            response.raise_for_status()
            
            if self.config['login_success_indicator'] not in response.text:
                raise Exception("Login failed. Check credentials.")
        except requests.exceptions.RequestException as e:
            raise Exception(f"Login request failed: {str(e)}")
    
    def get_product_links(self):
        """
        Retrieve all product download links from the account page.
        """
        account_url = self.config['account_url']
        
        try:
            response = self.session.get(account_url)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            product_links = []
            
            for link in soup.find_all('a', href=True):
                href = link['href']
                if any(keyword in href.lower() for keyword in self.config['download_keywords']):
                    full_url = urljoin(account_url, href)
                    product_links.append(full_url)
            
            return product_links
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to fetch product links: {str(e)}")
    
    def download_product(self, url, download_dir='downloads'):
        """
        Download a product from the given URL.
        """
        try:
            response = self.session.get(url, stream=True)
            response.raise_for_status()
            
            # Create download directory if it doesn't exist
            Path(download_dir).mkdir(parents=True, exist_ok=True)
            
            # Extract filename from URL or headers
            filename = os.path.basename(url)
            if 'content-disposition' in response.headers:
                content_disposition = response.headers['content-disposition']
                filename = content_disposition.split('filename=')[1].strip('"\'')
            
            filepath = os.path.join(download_dir, filename)
            
            # Download the file in chunks
            with open(filepath, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
            
            return filepath
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to download product: {str(e)}")
        except IOError as e:
            raise Exception(f"File write error: {str(e)}")
    
    def run(self):
        """
        Main execution method to download all products.
        """
        try:
            print("Logging in...")
            self.login()
            
            print("Fetching product links...")
            product_links = self.get_product_links()
            
            if not product_links:
                print("No products found to download.")
                return
            
            print(f"Found {len(product_links)} products to download.")
            
            for i, link in enumerate(product_links, 1):
                print(f"Downloading product {i}/{len(product_links)}...")
                try:
                    filepath = self.download_product(link)
                    print(f"Successfully downloaded: {filepath}")
                except Exception as e:
                    print(f"Error downloading {link}: {str(e)}")
                
                # Add delay between downloads to avoid rate limiting
                time.sleep(self.config.get('download_delay', 2))
            
            print("All downloads completed.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    downloader = DigitalProductDownloader()
    downloader.run()
```
