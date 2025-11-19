"""
Generated Code Metadata:
========================
Original URL: https://bongostaff.com
Prompt: Create a script to perform on-page SEO optimization, including meta tag updates and internal linking, as outlined by BongoStaff.
Generated: DETERMINISTIC_e0ad4c4ad49161db
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import re
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import requests
from typing import List, Dict, Optional, Set

class SEOScraper:
    """
    A class to perform on-page SEO optimization including meta tag updates and internal linking.
    """
    
    def __init__(self, base_url: str):
        """
        Initialize the SEOScraper with a base URL.
        
        Args:
            base_url (str): The base URL of the website to optimize.
        """
        self.base_url = base_url
        self.domain = urlparse(base_url).netloc
        self.visited_urls: Set[str] = set()
        self.internal_links: Set[str] = set()
        self.pages_data: List[Dict] = []
        
    def is_valid_url(self, url: str) -> bool:
        """
        Check if a URL is valid and belongs to the same domain.
        
        Args:
            url (str): The URL to check.
            
        Returns:
            bool: True if URL is valid and internal, False otherwise.
        """
        parsed = urlparse(url)
        return bool(parsed.netloc) and parsed.netloc == self.domain
    
    def get_absolute_url(self, url: str) -> str:
        """
        Convert a relative URL to absolute URL.
        
        Args:
            url (str): The URL to convert.
            
        Returns:
            str: Absolute URL.
        """
        return urljoin(self.base_url, url)
    
    def get_page_content(self, url: str) -> Optional[str]:
        """
        Fetch the content of a webpage.
        
        Args:
            url (str): URL of the page to fetch.
            
        Returns:
            Optional[str]: Page content if successful, None otherwise.
        """
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"Error fetching {url}: {e}")
            return None
    
    def extract_links(self, soup: BeautifulSoup, page_url: str) -> Set[str]:
        """
        Extract all internal links from a page.
        
        Args:
            soup (BeautifulSoup): Parsed HTML content.
            page_url (str): URL of the current page.
            
        Returns:
            Set[str]: Set of internal links found on the page.
        """
        links = set()
        for a_tag in soup.find_all('a', href=True):
            href = a_tag['href']
            if href.startswith('#'):
                continue
            absolute_url = self.get_absolute_url(href)
            if self.is_valid_url(absolute_url):
                links.add(absolute_url)
        return links
    
    def analyze_meta_tags(self, soup: BeautifulSoup) -> Dict:
        """
        Analyze and extract meta tags from a page.
        
        Args:
            soup (BeautifulSoup): Parsed HTML content.
            
        Returns:
            Dict: Dictionary containing meta tag information.
        """
        meta_data = {
            'title': '',
            'meta_description': '',
            'h1': [],
            'h2': [],
            'og_tags': {},
            'missing_tags': []
        }
        
        # Title tag
        title_tag = soup.find('title')
        if title_tag:
            meta_data['title'] = title_tag.get_text().strip()
        else:
            meta_data['missing_tags'].append('title')
        
        # Meta description
        meta_desc = soup.find('meta', attrs={'name': 'description'})
        if meta_desc:
            meta_data['meta_description'] = meta_desc.get('content', '').strip()
        else:
            meta_data['missing_tags'].append('meta description')
        
        # Heading tags
        meta_data['h1'] = [h.get_text().strip() for h in soup.find_all('h1')]
        meta_data['h2'] = [h.get_text().strip() for h in soup.find_all('h2')]
        
        # OpenGraph tags
        og_tags = soup.find_all('meta', attrs={'property': re.compile(r'^og:', re.I)})
        for tag in og_tags:
            meta_data['og_tags'][tag.get('property', '')] = tag.get('content', '')
        
        return meta_data
    
    def optimize_meta_tags(self, soup: BeautifulSoup, page_data: Dict) -> BeautifulSoup:
        """
        Optimize meta tags for a page.
        
        Args:
            soup (BeautifulSoup): Parsed HTML content.
            page_data (Dict): Dictionary containing optimization data.
            
        Returns:
            BeautifulSoup: Modified HTML with optimized meta tags.
        """
        # Update title if needed
        if 'title' in page_data and page_data['title']:
            title_tag = soup.find('title')
            if title_tag:
                title_tag.string = page_data['title']
            else:
                new_title = soup.new_tag('title')
                new_title.string = page_data['title']
                soup.head.append(new_title)
        
        # Update meta description if needed
        if 'meta_description' in page_data and page_data['meta_description']:
            meta_desc = soup.find('meta', attrs={'name': 'description'})
            if meta_desc:
                meta_desc['content'] = page_data['meta_description']
            else:
                new_meta = soup.new_tag('meta', attrs={'name': 'description', 'content': page_data['meta_description']})
                soup.head.append(new_meta)
        
        # Add missing OpenGraph tags
        if 'og_tags' in page_data:
            for prop, content in page_data['og_tags'].items():
                if not soup.find('meta', attrs={'property': prop}):
                    new_og = soup.new_tag('meta', attrs={'property': prop, 'content': content})
                    soup.head.append(new_og)
        
        return soup
    
    def optimize_internal_links(self, soup: BeautifulSoup, current_url: str, target_urls: List[str], anchor_text: str) -> BeautifulSoup:
        """
        Add internal links to a page.
        
        Args:
            soup (BeautifulSoup): Parsed HTML content.
            current_url (str): URL of the current page.
            target_urls (List[str]): List of URLs to link to.
            anchor_text (str): Anchor text to use for the links.
            
        Returns:
            BeautifulSoup: Modified HTML with added internal links.
        """
        # Find the first paragraph to insert links after
        first_p = soup.find('p')
        if first_p:
            for target_url in target_urls:
                if target_url != current_url and target_url in self.internal_links:
                    new_link = soup.new_tag('a', href=target_url)
                    new_link.string = anchor_text
                    first_p.insert_after(new_link)
                    first_p.insert_after(soup.new_tag('br'))
        
        return soup
    
    def crawl_page(self, url: str, max_depth: int = 3, current_depth: int = 0) -> None:
        """
        Recursively crawl a website to collect SEO data.
        
        Args:
            url (str): URL to crawl.
            max_depth (int): Maximum depth to crawl.
            current_depth (int): Current depth of recursion.
        """
        if current_depth > max_depth or url in self.visited_urls:
            return
        
        self.visited_urls.add(url)
        print(f"Crawling: {url}")
        
        content = self.get_page_content(url)
        if not content:
            return
        
        soup = BeautifulSoup(content, 'html.parser')
        
        # Extract and store internal links
        new_links = self.extract_links(soup, url)
        self.internal_links.update(new_links)
        
        # Analyze meta tags
        meta_data = self.analyze_meta_tags(soup)
        self.pages_data.append({
            'url': url,
            'meta_data': meta_data,
            'links': list(new_links)
        })
        
        # Recursively crawl new links
        for link in new_links:
            if link not in self.visited_urls:
                self.crawl_page(link, max_depth, current_depth + 1)
    
    def generate_seo_report(self) -> Dict:
        """
        Generate an SEO report based on crawled data.
        
        Returns:
            Dict: SEO report containing issues and recommendations.
        """
        report = {
            'missing_titles': [],
            'missing_descriptions': [],
            'pages_with_multiple_h1': [],
            'pages_without_h1': [],
            'internal_link_count': len(self.internal_links),
            'page_count': len(self.pages_data)
        }
        
        for page in self.pages_data:
            if not page['meta_data']['title']:
                report['missing_titles'].append(page['url'])
            if not page['meta_data']['meta_description']:
                report['missing_descriptions'].append(page['url'])
            if len(page['meta_data']['h1']) >
