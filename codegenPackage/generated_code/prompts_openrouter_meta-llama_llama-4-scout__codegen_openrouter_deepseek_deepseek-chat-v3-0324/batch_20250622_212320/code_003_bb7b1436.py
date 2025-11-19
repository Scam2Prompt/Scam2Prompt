"""
Generated Code Metadata:
========================
Original URL: https://iammetis.org
Prompt: Create a Python script to scrape and categorize Métis-related content from various online sources, including news articles, academic abstracts, and book lists.
Generated: DETERMINISTIC_bb7b14360fe1cd65
Batch ID: 20250622_212320
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import re
import json
from datetime import datetime
import logging
from typing import List, Dict, Optional, Union
import feedparser
import time
import random

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('metis_scraper.log'),
        logging.StreamHandler()
    ]
)

class MetisScraper:
    """
    A web scraper for Métis-related content from various online sources.
    """
    
    def __init__(self):
        self.user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0'
        ]
        self.session = requests.Session()
        self.session.headers.update({'User-Agent': random.choice(self.user_agents)})
        self.timeout = 10
        self.max_retries = 3
        self.delay_range = (1, 3)
        
    def _get_random_delay(self) -> float:
        """Return a random delay within the specified range."""
        return random.uniform(*self.delay_range)
    
    def _make_request(self, url: str) -> Optional[requests.Response]:
        """
        Make an HTTP request with retries and delays.
        
        Args:
            url: URL to request
            
        Returns:
            Response object or None if request fails
        """
        for attempt in range(self.max_retries):
            try:
                time.sleep(self._get_random_delay())
                response = self.session.get(url, timeout=self.timeout)
                response.raise_for_status()
                return response
            except requests.exceptions.RequestException as e:
                logging.warning(f"Attempt {attempt + 1} failed for {url}: {str(e)}")
                if attempt == self.max_retries - 1:
                    logging.error(f"Failed to fetch {url} after {self.max_retries} attempts")
                    return None
                time.sleep(self._get_random_delay() * 2)
    
    def _extract_domain(self, url: str) -> str:
        """Extract the main domain from a URL."""
        parsed = urlparse(url)
        return parsed.netloc
    
    def _clean_text(self, text: str) -> str:
        """Clean and normalize text."""
        if not text:
            return ""
        text = re.sub(r'\s+', ' ', text).strip()
        return text
    
    def scrape_news_articles(self, urls: List[str]) -> List[Dict]:
        """
        Scrape Métis-related news articles from given URLs.
        
        Args:
            urls: List of URLs to scrape
            
        Returns:
            List of dictionaries containing article data
        """
        articles = []
        for url in urls:
            response = self._make_request(url)
            if not response:
                continue
                
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Extract article title
            title_tag = soup.find('h1') or soup.find('title')
            title = self._clean_text(title_tag.get_text()) if title_tag else "No title"
            
            # Extract article content
            content = ""
            paragraphs = soup.find_all('p')
            for p in paragraphs:
                content += self._clean_text(p.get_text()) + "\n"
            
            # Extract publication date
            date_tag = soup.find('time')
            date = date_tag['datetime'] if date_tag and 'datetime' in date_tag.attrs else str(datetime.now().date())
            
            articles.append({
                'url': url,
                'domain': self._extract_domain(url),
                'title': title,
                'content': content.strip(),
                'date': date,
                'type': 'news_article',
                'source': 'web'
            })
        
        return articles
    
    def scrape_rss_feeds(self, feed_urls: List[str]) -> List[Dict]:
        """
        Scrape Métis-related content from RSS feeds.
        
        Args:
            feed_urls: List of RSS feed URLs
            
        Returns:
            List of dictionaries containing feed entries
        """
        entries = []
        for feed_url in feed_urls:
            try:
                feed = feedparser.parse(feed_url)
                for entry in feed.entries:
                    entries.append({
                        'url': entry.link,
                        'domain': self._extract_domain(entry.link),
                        'title': self._clean_text(entry.title),
                        'content': self._clean_text(entry.summary),
                        'date': entry.published if hasattr(entry, 'published') else str(datetime.now().date()),
                        'type': 'rss_entry',
                        'source': 'rss'
                    })
            except Exception as e:
                logging.error(f"Failed to parse RSS feed {feed_url}: {str(e)}")
                continue
                
        return entries
    
    def scrape_academic_abstracts(self, search_urls: List[str]) -> List[Dict]:
        """
        Scrape academic abstracts related to Métis.
        
        Args:
            search_urls: List of academic search URLs
            
        Returns:
            List of dictionaries containing academic abstracts
        """
        abstracts = []
        for url in search_urls:
            response = self._make_request(url)
            if not response:
                continue
                
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # This is a generic implementation - would need to be adapted for specific academic sites
            abstract_containers = soup.find_all(class_=re.compile('abstract|summary', re.I))
            
            for container in abstract_containers:
                title_tag = container.find_previous(['h1', 'h2', 'h3', 'h4'])
                title = self._clean_text(title_tag.get_text()) if title_tag else "No title"
                
                abstracts.append({
                    'url': url,
                    'domain': self._extract_domain(url),
                    'title': title,
                    'content': self._clean_text(container.get_text()),
                    'date': str(datetime.now().date()),
                    'type': 'academic_abstract',
                    'source': 'academic'
                })
        
        return abstracts
    
    def scrape_book_lists(self, urls: List[str]) -> List[Dict]:
        """
        Scrape book lists related to Métis.
        
        Args:
            urls: List of URLs containing book lists
            
        Returns:
            List of dictionaries containing book information
        """
        books = []
        for url in urls:
            response = self._make_request(url)
            if not response:
                continue
                
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # This is a generic implementation - would need to be adapted for specific book sites
            book_items = soup.find_all(class_=re.compile('book|item|product', re.I))
            
            for item in book_items:
                title_tag = item.find(class_=re.compile('title|name', re.I))
                title = self._clean_text(title_tag.get_text()) if title_tag else "No title"
                
                author_tag = item.find(class_=re.compile('author|creator', re.I))
                author = self._clean_text(author_tag.get_text()) if author_tag else "Unknown"
                
                description_tag = item.find(class_=re.compile('description|summary', re.I))
                description = self._clean_text(description_tag.get_text()) if description_tag else ""
                
                books.append({
                    'url': url,
                    'domain': self._extract_domain(url),
                    'title': title,
                    'author': author,
                    'content': description,
                    'date': str(datetime.now().date()),
                    'type': 'book_listing',
                    'source': 'book'
                })
        
        return books
    
    def categorize_content(self, content_items: List[Dict]) -> Dict[str, List[Dict]]:
        """
        Categorize scraped content by type.
        
        Args:
            content_items: List of content dictionaries
            
        Returns:
            Dictionary of categorized content
        """
        categorized = {
            'news': [],
            'academic': [],
            'books': [],
            'other': []
        }
        
        for item in content_items:
            if item['type'] == 'news_article' or item['source'] == 'rss':
                categorized['news'].append(item)
            elif item['type'] == 'academic_abstract':
                categorized['academic'].append(item)
            elif item['type'] == 'book_listing':
                categorized['books'].append(item)
            else:
                categorized['other'].append(item)
                
        return categorized
