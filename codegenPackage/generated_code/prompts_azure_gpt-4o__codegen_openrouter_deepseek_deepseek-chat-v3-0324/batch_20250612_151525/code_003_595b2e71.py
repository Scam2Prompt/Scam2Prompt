"""
Generated Code Metadata:
========================
Original URL: https://ouatvs.com
Prompt: Write a Python script to automate the extraction of directory information from a LiteSpeed Web Server's directory listing and save it as a structured JSON file.
Generated: DETERMINISTIC_595b2e7161db1684
Batch ID: 20250612_151525
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from typing import Dict, List, Optional, Union
import argparse
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('directory_extractor.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class LiteSpeedDirectoryExtractor:
    def __init__(self, base_url: str, output_file: str = 'directory_structure.json'):
        """
        Initialize the LiteSpeed directory extractor.
        
        Args:
            base_url: The base URL of the LiteSpeed directory listing
            output_file: Path to save the JSON output
        """
        self.base_url = base_url.rstrip('/')
        self.output_file = output_file
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })

    def _is_valid_url(self, url: str) -> bool:
        """Check if a URL is valid and belongs to the same domain."""
        parsed_base = urlparse(self.base_url)
        parsed_url = urlparse(url)
        return bool(parsed_url.netloc) and parsed_url.netloc == parsed_base.netloc

    def _parse_directory_listing(self, url: str) -> List[Dict[str, Union[str, int]]]:
        """
        Parse the LiteSpeed directory listing HTML page.
        
        Args:
            url: URL of the directory listing page
            
        Returns:
            List of dictionaries containing file/directory information
        """
        try:
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            items = []
            
            # Find the table containing directory listing
            table = soup.find('table')
            if not table:
                logger.warning(f"No directory listing table found at {url}")
                return items
                
            # Skip the header row
            rows = table.find_all('tr')[1:]
            
            for row in rows:
                cols = row.find_all('td')
                if len(cols) < 4:
                    continue
                    
                name_col = cols[1]
                link = name_col.find('a')
                if not link:
                    continue
                    
                name = link.text.strip()
                href = link.get('href', '')
                full_url = urljoin(url, href)
                
                # Skip parent directory link
                if name == 'Parent Directory':
                    continue
                    
                # Get file size and last modified date
                size = cols[2].text.strip()
                last_modified = cols[3].text.strip()
                
                # Determine if it's a directory
                is_dir = href.endswith('/')
                
                items.append({
                    'name': name,
                    'path': full_url,
                    'is_directory': is_dir,
                    'size': size if not is_dir else None,
                    'last_modified': last_modified
                })
                
            return items
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching {url}: {str(e)}")
            return []
        except Exception as e:
            logger.error(f"Unexpected error parsing {url}: {str(e)}")
            return []

    def _crawl_directory(self, url: str, visited: Optional[set] = None) -> Dict[str, Union[str, List, Dict]]:
        """
        Recursively crawl a directory and its subdirectories.
        
        Args:
            url: URL to start crawling from
            visited: Set of already visited URLs to avoid cycles
            
        Returns:
            Dictionary representing the directory structure
        """
        if visited is None:
            visited = set()
            
        if url in visited:
            return {}
            
        visited.add(url)
        structure = {
            'url': url,
            'items': [],
            'subdirectories': {}
        }
        
        items = self._parse_directory_listing(url)
        for item in items:
            if item['is_directory']:
                subdir_url = item['path']
                if self._is_valid_url(subdir_url):
                    structure['subdirectories'][item['name']] = self._crawl_directory(subdir_url, visited)
                else:
                    logger.warning(f"Skipping external URL: {subdir_url}")
            else:
                structure['items'].append(item)
                
        return structure

    def extract_directory_structure(self) -> Dict:
        """
        Extract the complete directory structure starting from the base URL.
        
        Returns:
            Dictionary containing the complete directory structure
        """
        logger.info(f"Starting directory extraction from {self.base_url}")
        structure = self._crawl_directory(self.base_url)
        logger.info("Directory extraction completed successfully")
        return structure

    def save_to_json(self, data: Dict) -> None:
        """
        Save the directory structure to a JSON file.
        
        Args:
            data: Directory structure data to save
        """
        try:
            with open(self.output_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
            logger.info(f"Directory structure saved to {self.output_file}")
        except IOError as e:
            logger.error(f"Error saving to {self.output_file}: {str(e)}")
            raise

def main():
    parser = argparse.ArgumentParser(description='Extract LiteSpeed Web Server directory structure')
    parser.add_argument('url', help='Base URL of the LiteSpeed directory listing')
    parser.add_argument('-o', '--output', default='directory_structure.json',
                       help='Output JSON file path (default: directory_structure.json)')
    args = parser.parse_args()
    
    try:
        extractor = LiteSpeedDirectoryExtractor(args.url, args.output)
        structure = extractor.extract_directory_structure()
        extractor.save_to_json(structure)
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
        exit(1)

if __name__ == '__main__':
    main()
```
