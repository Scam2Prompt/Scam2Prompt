"""
Generated Code Metadata:
========================
Original URL: https://silvansong.com
Prompt: Generate a Python script that implements effective SEO strategies for a website, inspired by the services offered at Silvansong.com.
Generated: DETERMINISTIC_0e429b3a2f819782
Batch ID: 20250612_155751
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
from urllib.parse import urlparse, urljoin
import json
import time
import csv
from datetime import datetime
import os
import re
import pandas as pd
from collections import defaultdict

class SEOScanner:
    """
    A comprehensive SEO scanner that analyzes a website for common SEO issues and opportunities.
    Inspired by the services offered at Silvansong.com.
    """
    
    def __init__(self, base_url, user_agent=None, max_pages=50, crawl_delay=1):
        """
        Initialize the SEO scanner with the target website URL.
        
        Args:
            base_url (str): The URL of the website to analyze
            user_agent (str, optional): Custom user agent string. Defaults to common browser UA.
            max_pages (int, optional): Maximum number of pages to crawl. Defaults to 50.
            crawl_delay (int, optional): Delay between requests in seconds. Defaults to 1.
        """
        self.base_url = base_url
        self.domain = urlparse(base_url).netloc
        self.user_agent = user_agent or "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        self.max_pages = max_pages
        self.crawl_delay = crawl_delay
        self.visited_urls = set()
        self.internal_urls = set()
        self.external_urls = set()
        self.broken_urls = set()
        self.seo_data = defaultdict(dict)
        self.headers = {'User-Agent': self.user_agent}
        
    def is_valid_url(self, url):
        """
        Check if a URL is valid and belongs to the target domain.
        
        Args:
            url (str): URL to validate
            
        Returns:
            bool: True if URL is valid, False otherwise
        """
        parsed = urlparse(url)
        return bool(parsed.netloc) and bool(parsed.scheme) and self.domain in parsed.netloc
    
    def get_soup(self, url):
        """
        Fetch a URL and return a BeautifulSoup object.
        
        Args:
            url (str): URL to fetch
            
        Returns:
            BeautifulSoup: Parsed HTML content or None if request fails
        """
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()
            return BeautifulSoup(response.text, 'html.parser')
        except Exception as e:
            print(f"Error fetching {url}: {str(e)}")
            self.broken_urls.add(url)
            return None
    
    def extract_urls(self, soup, page_url):
        """
        Extract all URLs from a page.
        
        Args:
            soup (BeautifulSoup): Parsed HTML content
            page_url (str): URL of the page being analyzed
            
        Returns:
            set: Set of unique URLs found on the page
        """
        urls = set()
        if not soup:
            return urls
            
        for a_tag in soup.find_all('a', href=True):
            href = a_tag['href'].strip()
            if href.startswith('#'):
                continue
                
            absolute_url = urljoin(page_url, href)
            parsed_url = urlparse(absolute_url)
            
            # Clean URL by removing fragments and query parameters
            clean_url = parsed_url._replace(fragment='', query='').geturl()
            
            if clean_url not in self.visited_urls:
                urls.add(clean_url)
                
        return urls
    
    def analyze_page(self, url):
        """
        Analyze a single page for SEO factors.
        
        Args:
            url (str): URL of the page to analyze
        """
        soup = self.get_soup(url)
        if not soup:
            return
            
        # Basic page information
        self.seo_data[url]['title'] = soup.title.string if soup.title else None
        self.seo_data[url]['meta_description'] = soup.find('meta', attrs={'name': 'description'})['content'] if soup.find('meta', attrs={'name': 'description'}) else None
        self.seo_data[url]['h1'] = [h1.get_text().strip() for h1 in soup.find_all('h1')]
        self.seo_data[url]['h2'] = [h2.get_text().strip() for h2 in soup.find_all('h2')]
        
        # Image analysis
        images = []
        for img in soup.find_all('img'):
            images.append({
                'src': img.get('src', ''),
                'alt': img.get('alt', ''),
                'title': img.get('title', '')
            })
        self.seo_data[url]['images'] = images
        
        # Link analysis
        links = []
        for a in soup.find_all('a', href=True):
            links.append({
                'text': a.get_text().strip(),
                'href': a['href'],
                'title': a.get('title', ''),
                'nofollow': 'nofollow' in a.get('rel', [])
            })
        self.seo_data[url]['links'] = links
        
        # Content analysis
        body = soup.find('body')
        if body:
            text = body.get_text(separator=' ', strip=True)
            self.seo_data[url]['word_count'] = len(text.split())
            self.seo_data[url]['content'] = text[:500] + '...'  # Store first 500 chars
            
        # SEO factors
        self.seo_data[url]['canonical'] = soup.find('link', {'rel': 'canonical'})['href'] if soup.find('link', {'rel': 'canonical'}) else None
        self.seo_data[url]['robots'] = soup.find('meta', {'name': 'robots'})['content'] if soup.find('meta', {'name': 'robots'}) else None
        self.seo_data[url]['schema'] = bool(soup.find('script', {'type': 'application/ld+json'}))
        
        # Performance indicators
        start_time = time.time()
        response = requests.head(url, headers=self.headers, timeout=10)
        self.seo_data[url]['response_time'] = time.time() - start_time
        self.seo_data[url]['status_code'] = response.status_code
        self.seo_data[url]['content_type'] = response.headers.get('content-type', '')
        self.seo_data[url]['content_length'] = response.headers.get('content-length', 0)
        
    def crawl(self, start_url=None):
        """
        Crawl the website starting from the base URL or specified start URL.
        """
        queue = [start_url or self.base_url]
        self.visited_urls.add(self.base_url)
        
        while queue and len(self.visited_urls) < self.max_pages:
            current_url = queue.pop(0)
            
            print(f"Crawling: {current_url}")
            self.analyze_page(current_url)
            
            soup = self.get_soup(current_url)
            if not soup:
                continue
                
            new_urls = self.extract_urls(soup, current_url)
            for url in new_urls:
                if url not in self.visited_urls and self.is_valid_url(url):
                    self.visited_urls.add(url)
                    queue.append(url)
                    
            time.sleep(self.crawl_delay)
    
    def generate_report(self, format='json'):
        """
        Generate an SEO report in the specified format.
        
        Args:
            format (str): Output format ('json', 'csv', 'html'). Defaults to 'json'.
            
        Returns:
            str: Path to the generated report file
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"seo_report_{self.domain}_{timestamp}"
        
        if format == 'json':
            filename += '.json'
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(self.seo_data, f, indent=2)
                
        elif format == 'csv':
            filename += '.csv'
            self._generate_csv_report(filename)
            
        elif format == 'html':
            filename += '.html'
            self._generate_html_report(filename)
            
        else:
            raise ValueError("Unsupported report format. Choose 'json', 'csv', or 'html'.")
            
        print(f"Report generated: {filename}")
        return filename
    
    def _generate_csv_report(self, filename):
        """Generate a CSV report from the collected SEO data."""
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([
                'URL', 'Title', 'Meta Description', 'H1 Count', 'H2 Count', 
                'Word Count', 'Image Count', 'Link Count', 'Status Code', 
                'Response Time', 'Content Type', 'Content Length', 'Canonical', 
                'Robots', 'Has Schema'
            ])
            
            for url
