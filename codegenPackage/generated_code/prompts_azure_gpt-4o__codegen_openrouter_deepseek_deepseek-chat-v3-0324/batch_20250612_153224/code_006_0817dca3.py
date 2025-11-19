"""
Generated Code Metadata:
========================
Original URL: https://filmdailyweb.com
Prompt: Create code for SEO optimization tailored for real estate businesses in NYC, using strategies mentioned in Film Daily Web's article on SEO companies.
Generated: DETERMINISTIC_0817dca391058ffb
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
SEO Optimization for NYC Real Estate Businesses
Based on strategies from Film Daily Web's article on SEO companies.
"""

import json
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import time
import re
from typing import List, Dict, Optional
import pandas as pd
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('seo_optimizer.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class SEOOptimizer:
    """
    Main class for SEO optimization tailored for NYC real estate businesses.
    """
    
    def __init__(self, website_url: str, business_name: str):
        """
        Initialize SEO optimizer with website URL and business name.
        
        Args:
            website_url: URL of the real estate business website
            business_name: Name of the real estate business
        """
        self.website_url = website_url
        self.business_name = business_name
        self.keywords = self._load_keywords()
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
    def _load_keywords(self) -> List[str]:
        """
        Load NYC real estate specific keywords.
        
        Returns:
            List of relevant keywords
        """
        keywords = [
            "NYC real estate",
            "New York City apartments",
            "Manhattan condos",
            "Brooklyn homes for sale",
            "Queens real estate agents",
            "Luxury apartments NYC",
            "NYC property listings",
            "Affordable housing NYC",
            "NYC real estate market",
            "Best NYC neighborhoods"
        ]
        return keywords
    
    def check_on_page_seo(self) -> Dict:
        """
        Analyze on-page SEO elements.
        
        Returns:
            Dictionary with on-page SEO analysis results
        """
        try:
            response = requests.get(self.website_url, headers=self.headers, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            results = {
                'title': self._check_title(soup),
                'meta_description': self._check_meta_description(soup),
                'headers': self._check_headers(soup),
                'keyword_density': self._check_keyword_density(soup),
                'image_alt_tags': self._check_image_alt_tags(soup),
                'internal_links': self._check_internal_links(soup),
                'mobile_friendly': self._check_mobile_friendly(),
                'page_speed': self._check_page_speed(),
                'url_structure': self._check_url_structure()
            }
            
            return results
            
        except requests.RequestException as e:
            logger.error(f"Error analyzing on-page SEO: {e}")
            return {'error': str(e)}
    
    def _check_title(self, soup: BeautifulSoup) -> Dict:
        """
        Check if title tag exists and contains keywords.
        
        Args:
            soup: BeautifulSoup object
            
        Returns:
            Dictionary with title analysis results
        """
        title_tag = soup.find('title')
        if not title_tag:
            return {'status': 'missing', 'score': 0}
        
        title_text = title_tag.get_text()
        length = len(title_text)
        contains_keywords = any(keyword.lower() in title_text.lower() for keyword in self.keywords)
        
        return {
            'title': title_text,
            'length': length,
            'contains_keywords': contains_keywords,
            'score': 8 if (50 <= length <= 60 and contains_keywords) else 4 if (30 <= length <= 70) else 2
        }
    
    def _check_meta_description(self, soup: BeautifulSoup) -> Dict:
        """
        Check meta description.
        
        Args:
            soup: BeautifulSoup object
            
        Returns:
            Dictionary with meta description analysis results
        """
        meta = soup.find('meta', attrs={'name': 'description'})
        if not meta:
            return {'status': 'missing', 'score': 0}
        
        description = meta.get('content', '')
        length = len(description)
        contains_keywords = any(keyword.lower() in description.lower() for keyword in self.keywords)
        
        return {
            'description': description,
            'length': length,
            'contains_keywords': contains_keywords,
            'score': 8 if (150 <= length <= 160 and contains_keywords) else 4 if (120 <= length <= 180) else 2
        }
    
    def _check_headers(self, soup: BeautifulSoup) -> Dict:
        """
        Check header tags (h1, h2, h3) structure and keyword usage.
        
        Args:
            soup: BeautifulSoup object
            
        Returns:
            Dictionary with header analysis results
        """
        headers = {
            'h1': [],
            'h2': [],
            'h3': []
        }
        
        for tag in ['h1', 'h2', 'h3']:
            elements = soup.find_all(tag)
            headers[tag] = [el.get_text().strip() for el in elements]
        
        h1_count = len(headers['h1'])
        h1_keywords = any(keyword.lower() in ' '.join(headers['h1']).lower() for keyword in self.keywords)
        
        return {
            'headers': headers,
            'h1_count': h1_count,
            'h1_keywords': h1_keywords,
            'score': 10 if (h1_count == 1 and h1_keywords) else 5 if (h1_count >= 1) else 2
        }
    
    def _check_keyword_density(self, soup: BeautifulSoup) -> Dict:
        """
        Calculate keyword density in page content.
        
        Args:
            soup: BeautifulSoup object
            
        Returns:
            Dictionary with keyword density analysis
        """
        text = ' '.join([p.get_text() for p in soup.find_all('p')])
        words = re.findall(r'\w+', text.lower())
        total_words = len(words)
        
        if total_words == 0:
            return {'status': 'no_content', 'score': 0}
        
        keyword_counts = {}
        for keyword in self.keywords:
            keyword_lower = keyword.lower()
            keyword_words = re.findall(r'\w+', keyword_lower)
            count = sum(1 for word in words if word in keyword_words)
            keyword_counts[keyword] = count
        
        density = {k: (v / total_words * 100) for k, v in keyword_counts.items()}
        avg_density = sum(density.values()) / len(density) if density else 0
        
        return {
            'keyword_counts': keyword_counts,
            'density_percent': density,
            'average_density': avg_density,
            'score': 8 if (1 <= avg_density <= 3) else 4 if (avg_density > 0) else 2
        }
    
    def _check_image_alt_tags(self, soup: BeautifulSoup) -> Dict:
        """
        Check image alt tags for presence and keywords.
        
        Args:
            soup: BeautifulSoup object
            
        Returns:
            Dictionary with image alt tag analysis
        """
        images = soup.find_all('img')
        total_images = len(images)
        images_with_alt = [img for img in images if img.get('alt', '').strip()]
        images_with_keywords = [
            img for img in images_with_alt 
            if any(keyword.lower() in img['alt'].lower() for keyword in self.keywords)
        ]
        
        return {
            'total_images': total_images,
            'images_with_alt': len(images_with_alt),
            'images_with_keywords': len(images_with_keywords),
            'score': 10 if (len(images_with_alt) == total_images and len(images_with_keywords) > 0) 
                    else 5 if (len(images_with_alt) > 0) 
                    else 0
        }
    
    def _check_internal_links(self, soup: BeautifulSoup) -> Dict:
        """
        Check internal linking structure.
        
        Args:
            soup: BeautifulSoup object
            
        Returns:
            Dictionary with internal link analysis
        """
        domain = urlparse(self.website_url).netloc
        links = soup.find_all('a', href=True)
        internal_links = [
            link['href'] for link in links 
            if urlparse(link['href']).netloc in ('', domain)
        ]
        
        return {
            'total_links': len(links),
            'internal_links': len(internal_links),
            'internal_link_ratio': len(internal_links) / len(links) if links else 0,
            'score': 8 if (len(internal_links) / len
