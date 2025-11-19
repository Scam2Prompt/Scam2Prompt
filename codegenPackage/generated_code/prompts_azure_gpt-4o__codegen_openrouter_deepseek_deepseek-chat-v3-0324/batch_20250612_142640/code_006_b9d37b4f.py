"""
Generated Code Metadata:
========================
Original URL: https://mnswap.org
Prompt: Develop a script to organize and categorize regulatory resources for activity professionals, inspired by MN SWAP's regulatory resources section.
Generated: DETERMINISTIC_b9d37b4fa1d1c2a7
Batch ID: 20250612_142640
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/mn-swap-regulations": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/regulations": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/federal-guidelines": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import os
import json
from typing import Dict, List, Optional
from dataclasses import dataclass, asdict
import requests
from bs4 import BeautifulSoup
from pathlib import Path
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@dataclass
class RegulatoryResource:
    """Data class representing a regulatory resource"""
    title: str
    category: str
    description: str
    url: str
    file_path: Optional[str] = None
    tags: Optional[List[str]] = None

class RegulatoryResourceOrganizer:
    """Organizes and categorizes regulatory resources for activity professionals"""
    
    def __init__(self, output_dir: str = "regulatory_resources"):
        self.output_dir = Path(output_dir)
        self.resources: List[RegulatoryResource] = []
        
        # Create output directory if it doesn't exist
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
    def add_resource(
        self,
        title: str,
        category: str,
        description: str,
        url: str,
        tags: Optional[List[str]] = None
    ) -> None:
        """Add a new resource to the organizer"""
        resource = RegulatoryResource(
            title=title,
            category=category,
            description=description,
            url=url,
            tags=tags or []
        )
        self.resources.append(resource)
        logger.info(f"Added resource: {title}")
    
    def download_resource(self, resource: RegulatoryResource) -> None:
        """Download the resource file if it's a downloadable URL"""
        try:
            response = requests.get(resource.url, stream=True, timeout=10)
            response.raise_for_status()
            
            # Determine file extension from content type or URL
            content_type = response.headers.get('content-type', '')
            if 'pdf' in content_type:
                ext = '.pdf'
            elif 'msword' in content_type:
                ext = '.doc'
            elif 'vnd.openxmlformats-officedocument.wordprocessingml.document' in content_type:
                ext = '.docx'
            else:
                ext = Path(resource.url).suffix or '.html'
            
            # Create safe filename
            safe_title = "".join(c if c.isalnum() else "_" for c in resource.title)
            filename = f"{safe_title}{ext}"
            file_path = self.output_dir / filename
            
            # Save the file
            with open(file_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            
            resource.file_path = str(file_path)
            logger.info(f"Downloaded resource: {resource.title} to {file_path}")
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to download {resource.url}: {str(e)}")
    
    def categorize_resources(self) -> Dict[str, List[RegulatoryResource]]:
        """Categorize resources by their category"""
        categories: Dict[str, List[RegulatoryResource]] = {}
        
        for resource in self.resources:
            if resource.category not in categories:
                categories[resource.category] = []
            categories[resource.category].append(resource)
        
        return categories
    
    def save_to_json(self, filename: str = "resources.json") -> None:
        """Save all resources to a JSON file"""
        output_path = self.output_dir / filename
        data = [asdict(resource) for resource in self.resources]
        
        try:
            with open(output_path, 'w') as f:
                json.dump(data, f, indent=2)
            logger.info(f"Saved resources to {output_path}")
        except IOError as e:
            logger.error(f"Failed to save JSON file: {str(e)}")
    
    def load_from_json(self, filename: str = "resources.json") -> None:
        """Load resources from a JSON file"""
        input_path = self.output_dir / filename
        
        try:
            with open(input_path, 'r') as f:
                data = json.load(f)
                self.resources = [RegulatoryResource(**item) for item in data]
            logger.info(f"Loaded resources from {input_path}")
        except (IOError, json.JSONDecodeError) as e:
            logger.error(f"Failed to load JSON file: {str(e)}")
    
    def scrape_website(self, url: str, selectors: Dict[str, str]) -> None:
        """Scrape resources from a website using CSS selectors"""
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Extract resources based on selectors
            resource_elements = soup.select(selectors['resource'])
            
            for element in resource_elements:
                try:
                    title = element.select_one(selectors['title']).text.strip()
                    category = element.select_one(selectors['category']).text.strip()
                    description = element.select_one(selectors['description']).text.strip()
                    url = element.select_one(selectors['url'])['href']
                    
                    # Make URL absolute if it's relative
                    if not url.startswith('http'):
                        url = requests.compat.urljoin(response.url, url)
                    
                    self.add_resource(
                        title=title,
                        category=category,
                        description=description,
                        url=url
                    )
                    
                except (AttributeError, KeyError) as e:
                    logger.warning(f"Failed to parse resource element: {str(e)}")
                    continue
            
            logger.info(f"Scraped {len(resource_elements)} resources from {url}")
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to scrape website {url}: {str(e)}")

# Example usage
if __name__ == "__main__":
    organizer = RegulatoryResourceOrganizer()
    
    # Add some example resources
    organizer.add_resource(
        title="MN SWAP Regulations",
        category="State Regulations",
        description="Minnesota's regulations for activity professionals",
        url="https://example.com/mn-swap-regulations",
        tags=["Minnesota", "State"]
    )
    
    organizer.add_resource(
        title="Federal Activity Guidelines",
        category="Federal Regulations",
        description="Federal guidelines for activity programs",
        url="https://example.com/federal-guidelines",
        tags=["Federal", "Guidelines"]
    )
    
    # Download resources
    for resource in organizer.resources:
        organizer.download_resource(resource)
    
    # Categorize and save
    categories = organizer.categorize_resources()
    organizer.save_to_json()
    
    # Example of scraping (would need actual selectors for a real website)
    # selectors = {
    #     'resource': '.resource-item',
    #     'title': '.resource-title',
    #     'category': '.resource-category',
    #     'description': '.resource-description',
    #     'url': 'a.resource-link'
    # }
    # organizer.scrape_website("https://example.com/regulations", selectors)
```
