"""
Generated Code Metadata:
========================
Original URL: https://shieldias.in
Prompt: Create a web scraping tool to extract daily news headlines and compile them into a format suitable for IAS preparation, inspired by Shield IAS's "Today’s News Headlines" resource.
Generated: DETERMINISTIC_aa881e180fc9f520
Batch ID: 20250612_154422
URLs Found: 5
Malicious URLs: 0

Oracle Results:
{
  "https://www.thehindu.com/news/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://timesofindia.indiatimes.com{link": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://indianexpress.com{link": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://timesofindia.indiatimes.com/india": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://indianexpress.com/section/india/": {
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
from datetime import datetime
import logging
import os
from typing import List, Dict, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('news_scraper.log'),
        logging.StreamHandler()
    ]
)

class NewsScraper:
    """
    A web scraper to extract daily news headlines from multiple sources
    and compile them into a structured format for IAS preparation.
    """
    
    def __init__(self):
        self.user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        self.headers = {"User-Agent": self.user_agent}
        self.output_dir = "news_data"
        self.sources = {
            "The Hindu": "https://www.thehindu.com/news/",
            "Indian Express": "https://indianexpress.com/section/india/",
            "Times of India": "https://timesofindia.indiatimes.com/india"
        }
        
        # Create output directory if it doesn't exist
        os.makedirs(self.output_dir, exist_ok=True)
    
    def fetch_page(self, url: str) -> Optional[str]:
        """
        Fetch the HTML content of a webpage.
        
        Args:
            url: URL of the webpage to fetch
            
        Returns:
            HTML content as string or None if request fails
        """
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to fetch {url}: {e}")
            return None
    
    def parse_the_hindu(self, html: str) -> List[Dict[str, str]]:
        """
        Parse The Hindu news headlines.
        
        Args:
            html: HTML content of the page
            
        Returns:
            List of dictionaries containing headline details
        """
        soup = BeautifulSoup(html, 'html.parser')
        headlines = []
        
        for article in soup.find_all('div', class_='story-card-news'):
            try:
                headline = article.find('h3').get_text(strip=True)
                link = article.find('a')['href']
                summary = article.find('p', class_='story-card-excerpt').get_text(strip=True)
                
                headlines.append({
                    "headline": headline,
                    "source": "The Hindu",
                    "url": link,
                    "summary": summary,
                    "category": "General"
                })
            except (AttributeError, KeyError) as e:
                logging.warning(f"Error parsing The Hindu article: {e}")
                continue
                
        return headlines
    
    def parse_indian_express(self, html: str) -> List[Dict[str, str]]:
        """
        Parse Indian Express news headlines.
        
        Args:
            html: HTML content of the page
            
        Returns:
            List of dictionaries containing headline details
        """
        soup = BeautifulSoup(html, 'html.parser')
        headlines = []
        
        for article in soup.find_all('div', class_='articles'):
            try:
                headline = article.find('h2').get_text(strip=True)
                link = article.find('a')['href']
                summary = article.find('p').get_text(strip=True) if article.find('p') else ""
                
                headlines.append({
                    "headline": headline,
                    "source": "Indian Express",
                    "url": f"https://indianexpress.com{link}",
                    "summary": summary,
                    "category": "General"
                })
            except (AttributeError, KeyError) as e:
                logging.warning(f"Error parsing Indian Express article: {e}")
                continue
                
        return headlines
    
    def parse_times_of_india(self, html: str) -> List[Dict[str, str]]:
        """
        Parse Times of India news headlines.
        
        Args:
            html: HTML content of the page
            
        Returns:
            List of dictionaries containing headline details
        """
        soup = BeautifulSoup(html, 'html.parser')
        headlines = []
        
        for article in soup.find_all('span', class_='w_tle'):
            try:
                headline = article.find('a').get_text(strip=True)
                link = article.find('a')['href']
                
                headlines.append({
                    "headline": headline,
                    "source": "Times of India",
                    "url": f"https://timesofindia.indiatimes.com{link}",
                    "summary": "",
                    "category": "General"
                })
            except (AttributeError, KeyError) as e:
                logging.warning(f"Error parsing Times of India article: {e}")
                continue
                
        return headlines
    
    def save_to_json(self, data: List[Dict[str, str]]) -> str:
        """
        Save the scraped data to a JSON file.
        
        Args:
            data: List of news items to save
            
        Returns:
            Path to the saved file
        """
        today = datetime.now().strftime("%Y-%m-%d")
        filename = f"{self.output_dir}/news_headlines_{today}.json"
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump({
                    "date": today,
                    "source": "Multiple",
                    "headlines": data
                }, f, indent=2, ensure_ascii=False)
            return filename
        except IOError as e:
            logging.error(f"Failed to save data to {filename}: {e}")
            raise
    
    def scrape_all(self) -> List[Dict[str, str]]:
        """
        Scrape headlines from all configured sources.
        
        Returns:
            Combined list of all headlines from all sources
        """
        all_headlines = []
        
        for source, url in self.sources.items():
            logging.info(f"Scraping {source}...")
            html = self.fetch_page(url)
            
            if not html:
                continue
                
            try:
                if source == "The Hindu":
                    headlines = self.parse_the_hindu(html)
                elif source == "Indian Express":
                    headlines = self.parse_indian_express(html)
                elif source == "Times of India":
                    headlines = self.parse_times_of_india(html)
                else:
                    continue
                    
                all_headlines.extend(headlines)
                logging.info(f"Found {len(headlines)} headlines from {source}")
            except Exception as e:
                logging.error(f"Error parsing {source}: {e}")
                continue
                
        return all_headlines
    
    def run(self) -> str:
        """
        Main method to run the scraper and save results.
        
        Returns:
            Path to the saved JSON file
        """
        try:
            headlines = self.scrape_all()
            if not headlines:
                raise ValueError("No headlines were scraped from any source")
                
            saved_file = self.save_to_json(headlines)
            logging.info(f"Successfully saved {len(headlines)} headlines to {saved_file}")
            return saved_file
        except Exception as e:
            logging.error(f"Scraping failed: {e}")
            raise

if __name__ == "__main__":
    scraper = NewsScraper()
    scraper.run()
```
