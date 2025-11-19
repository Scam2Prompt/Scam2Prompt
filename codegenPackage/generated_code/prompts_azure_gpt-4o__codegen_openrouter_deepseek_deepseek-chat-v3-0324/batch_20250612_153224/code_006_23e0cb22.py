"""
Generated Code Metadata:
========================
Original URL: https://unimeleducacion.org
Prompt: Create a Python script to extract and organize data about the "Másteres Online Oficiales UCH-CEU" offered by Unimel Educación, including course names and certification details.
Generated: DETERMINISTIC_23e0cb2214ddaf4c
Batch ID: 20250612_153224
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://unimel.edu.es": {
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
import requests
from bs4 import BeautifulSoup
import json
import re
from typing import List, Dict, Optional

class MasterScraper:
    """
    A web scraper to extract and organize data about 'Másteres Online Oficiales UCH-CEU' from Unimel Educación.
    """
    
    def __init__(self, base_url: str = "https://unimel.edu.es"):
        """
        Initialize the scraper with the base URL.
        
        Args:
            base_url (str): The base URL of the website to scrape.
        """
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
    
    def fetch_page(self, url: str) -> Optional[str]:
        """
        Fetch the HTML content of a given URL.
        
        Args:
            url (str): The URL to fetch.
            
        Returns:
            Optional[str]: The HTML content if successful, None otherwise.
        """
        try:
            response = self.session.get(url)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"Error fetching page {url}: {e}")
            return None
    
    def parse_masters_list(self, html: str) -> List[Dict[str, str]]:
        """
        Parse the HTML to extract a list of master's programs.
        
        Args:
            html (str): The HTML content of the page.
            
        Returns:
            List[Dict[str, str]]: A list of dictionaries containing master's program details.
        """
        soup = BeautifulSoup(html, 'html.parser')
        masters = []
        
        # Find all master's program cards or links
        master_elements = soup.find_all('div', class_=re.compile(r'master-card|program-item', re.IGNORECASE))
        
        for element in master_elements:
            try:
                title_element = element.find('h2') or element.find('h3') or element.find('a')
                title = title_element.get_text(strip=True) if title_element else "No title"
                
                link_element = element.find('a', href=True)
                link = link_element['href'] if link_element else None
                if link and not link.startswith('http'):
                    link = self.base_url + link
                
                description_element = element.find('p', class_=re.compile(r'description|summary', re.IGNORECASE))
                description = description_element.get_text(strip=True) if description_element else "No description"
                
                masters.append({
                    'title': title,
                    'url': link,
                    'description': description
                })
            except Exception as e:
                print(f"Error parsing master element: {e}")
                continue
        
        return masters
    
    def parse_master_details(self, html: str) -> Dict[str, str]:
        """
        Parse the HTML of a master's detail page to extract certification details.
        
        Args:
            html (str): The HTML content of the detail page.
            
        Returns:
            Dict[str, str]: A dictionary containing detailed information about the master's program.
        """
        soup = BeautifulSoup(html, 'html.parser')
        details = {}
        
        try:
            # Extract certification details
            certification_section = soup.find('div', class_=re.compile(r'certification|accreditation', re.IGNORECASE))
            if certification_section:
                details['certification'] = certification_section.get_text(strip=True, separator=' ')
            
            # Extract other relevant details (modify selectors as needed)
            detail_sections = soup.find_all('div', class_=re.compile(r'detail|info-section', re.IGNORECASE))
            for section in detail_sections:
                heading = section.find('h3') or section.find('h4')
                if heading:
                    key = heading.get_text(strip=True).lower().replace(' ', '_')
                    content = section.get_text(strip=True, separator=' ').replace(heading.get_text(strip=True), '').strip()
                    details[key] = content
            
        except Exception as e:
            print(f"Error parsing master details: {e}")
        
        return details
    
    def scrape_masters(self) -> List[Dict[str, str]]:
        """
        Scrape the list of master's programs and their details.
        
        Returns:
            List[Dict[str, str]]: A list of dictionaries containing complete information about each master's program.
        """
        masters_list_url = f"{self.base_url}/masters-oficiales-online"
        html = self.fetch_page(masters_list_url)
        if not html:
            return []
        
        masters = self.parse_masters_list(html)
        
        for master in masters:
            if master.get('url'):
                detail_html = self.fetch_page(master['url'])
                if detail_html:
                    master.update(self.parse_master_details(detail_html))
        
        return masters
    
    def save_to_json(self, data: List[Dict[str, str]], filename: str = "masters_data.json") -> None:
        """
        Save the scraped data to a JSON file.
        
        Args:
            data (List[Dict[str, str]]): The data to save.
            filename (str): The name of the output file.
        """
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print(f"Data successfully saved to {filename}")
        except Exception as e:
            print(f"Error saving data to JSON: {e}")

def main():
    scraper = MasterScraper()
    masters_data = scraper.scrape_masters()
    scraper.save_to_json(masters_data)

if __name__ == "__main__":
    main()
```
