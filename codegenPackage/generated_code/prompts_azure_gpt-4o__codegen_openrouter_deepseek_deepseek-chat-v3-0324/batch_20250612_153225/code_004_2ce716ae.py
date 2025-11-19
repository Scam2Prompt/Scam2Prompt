"""
Generated Code Metadata:
========================
Original URL: https://budbeeindia.com
Prompt: Write a script to automate SEO optimization for a website, following the guidelines mentioned in BudBee India's article on SEO dos and don'ts.
Generated: DETERMINISTIC_2ce716aeb9696709
Batch ID: 20250612_153225
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
import time
from typing import List, Dict, Optional, Tuple

class SEOAnalyzer:
    """
    A class to automate SEO optimization checks for a website based on BudBee India's SEO guidelines.
    """

    def __init__(self, base_url: str, user_agent: str = "SEO Analyzer Bot"):
        """
        Initialize the SEOAnalyzer with the base URL of the website to analyze.

        Args:
            base_url (str): The base URL of the website to analyze.
            user_agent (str): User agent string for HTTP requests.
        """
        self.base_url = base_url
        self.user_agent = user_agent
        self.headers = {'User-Agent': user_agent}
        self.session = requests.Session()
        self.session.headers.update(self.headers)
        self.results = {
            'url': base_url,
            'checks': {},
            'score': 0,
            'total_checks': 0
        }

    def fetch_page(self, url: str) -> Optional[BeautifulSoup]:
        """
        Fetch and parse a web page.

        Args:
            url (str): URL of the page to fetch.

        Returns:
            Optional[BeautifulSoup]: Parsed HTML content or None if request fails.
        """
        try:
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            return BeautifulSoup(response.text, 'html.parser')
        except requests.exceptions.RequestException as e:
            print(f"Error fetching {url}: {e}")
            return None

    def check_meta_tags(self, soup: BeautifulSoup) -> Dict:
        """
        Check for presence and quality of meta tags.

        Args:
            soup (BeautifulSoup): Parsed HTML content.

        Returns:
            Dict: Results of meta tag checks.
        """
        results = {
            'meta_title': {'present': False, 'length': 0, 'optimal': False},
            'meta_description': {'present': False, 'length': 0, 'optimal': False},
            'meta_keywords': {'present': False, 'recommended': False}
        }

        # Check meta title
        title = soup.find('title')
        if title:
            results['meta_title']['present'] = True
            title_length = len(title.text.strip())
            results['meta_title']['length'] = title_length
            results['meta_title']['optimal'] = 50 <= title_length <= 60

        # Check meta description
        meta_desc = soup.find('meta', attrs={'name': 'description'})
        if meta_desc and meta_desc.get('content'):
            results['meta_description']['present'] = True
            desc_length = len(meta_desc['content'].strip())
            results['meta_description']['length'] = desc_length
            results['meta_description']['optimal'] = 150 <= desc_length <= 160

        # Check meta keywords (not recommended)
        meta_keywords = soup.find('meta', attrs={'name': 'keywords'})
        if meta_keywords:
            results['meta_keywords']['present'] = True
            results['meta_keywords']['recommended'] = False

        return results

    def check_heading_structure(self, soup: BeautifulSoup) -> Dict:
        """
        Check heading hierarchy (h1-h6).

        Args:
            soup (BeautifulSoup): Parsed HTML content.

        Returns:
            Dict: Results of heading checks.
        """
        results = {
            'h1': {'count': 0, 'content': []},
            'h2': {'count': 0, 'content': []},
            'h3': {'count': 0, 'content': []},
            'h4': {'count': 0, 'content': []},
            'h5': {'count': 0, 'content': []},
            'h6': {'count': 0, 'content': []},
            'hierarchy_ok': False
        }

        for i in range(1, 7):
            tag = f'h{i}'
            headings = soup.find_all(tag)
            results[tag]['count'] = len(headings)
            results[tag]['content'] = [h.text.strip() for h in headings]

        # Check if h1 is present (should be exactly one)
        if results['h1']['count'] == 1:
            # Check if hierarchy is roughly maintained (h1 > h2 > h3, etc.)
            hierarchy_ok = True
            for i in range(1, 6):
                if results[f'h{i}']['count'] == 0 and results[f'h{i+1}']['count'] > 0:
                    hierarchy_ok = False
                    break
            results['hierarchy_ok'] = hierarchy_ok

        return results

    def check_image_alt_text(self, soup: BeautifulSoup) -> Dict:
        """
        Check for presence of alt text in images.

        Args:
            soup (BeautifulSoup): Parsed HTML content.

        Returns:
            Dict: Results of image alt text checks.
        """
        results = {
            'total_images': 0,
            'images_with_alt': 0,
            'images_without_alt': 0,
            'percentage_with_alt': 0
        }

        images = soup.find_all('img')
        results['total_images'] = len(images)

        for img in images:
            if img.get('alt', '').strip():
                results['images_with_alt'] += 1
            else:
                results['images_without_alt'] += 1

        if results['total_images'] > 0:
            results['percentage_with_alt'] = round(
                (results['images_with_alt'] / results['total_images']) * 100, 2
            )

        return results

    def check_internal_links(self, soup: BeautifulSoup) -> Dict:
        """
        Check internal links for proper structure and accessibility.

        Args:
            soup (BeautifulSoup): Parsed HTML content.

        Returns:
            Dict: Results of internal link checks.
        """
        results = {
            'total_internal_links': 0,
            'broken_links': 0,
            'links_without_anchor': 0,
            'links_with_anchor': 0,
            'percentage_broken': 0
        }

        domain = urlparse(self.base_url).netloc
        links = soup.find_all('a', href=True)
        internal_links = [
            link for link in links 
            if urlparse(link['href']).netloc == domain or not urlparse(link['href']).netloc
        ]
        results['total_internal_links'] = len(internal_links)

        for link in internal_links:
            href = link['href']
            if not href.startswith('http'):
                if href.startswith('/'):
                    href = f"{self.base_url.rstrip('/')}{href}"
                else:
                    href = f"{self.base_url.rstrip('/')}/{href}"

            # Check if link has anchor text
            if link.text.strip():
                results['links_with_anchor'] += 1
            else:
                results['links_without_anchor'] += 1

            # Check if link is broken (sample a few links)
            if results['total_internal_links'] < 10 or results['broken_links'] < 3:
                try:
                    response = self.session.head(href, timeout=5, allow_redirects=True)
                    if response.status_code >= 400:
                        results['broken_links'] += 1
                except requests.exceptions.RequestException:
                    results['broken_links'] += 1

        if results['total_internal_links'] > 0:
            results['percentage_broken'] = round(
                (results['broken_links'] / results['total_internal_links']) * 100, 2
            )

        return results

    def check_url_structure(self) -> Dict:
        """
        Check URL structure for SEO friendliness.

        Returns:
            Dict: Results of URL structure checks.
        """
        results = {
            'url_length': len(self.base_url),
            'url_has_uppercase': any(c.isupper() for c in self.base_url),
            'url_has_underscores': '_' in self.base_url,
            'url_has_spaces': ' ' in self.base_url,
            'url_has_special_chars': bool(re.search(r'[^a-zA-Z0-9\-_~./]', self.base_url)),
            'url_has_keywords': bool(re.search(r'/([^/]+?)(?:-|_|%20)([^/]+?)(?:-|_|%20)?([^/]*?)/?$', self.base_url))
        }
        return results

    def check_page_load_time(self, url: str) -> Dict:
        """
        Measure page load time.

        Args:
            url (str): URL to test.

        Returns:
            Dict: Results of page load time test.
        """
        results = {
            'load_time': 0,
            'optimal': False
        }

        try:
            start_time = time.time()
            response = self.session.get(url, timeout=10)
