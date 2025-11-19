"""
Generated Code Metadata:
========================
Original URL: https://pdma.io
Prompt: Generate a Python script that utilizes SEO best practices for a digital marketing campaign, as outlined in the PDMA Technologies training program.
Generated: DETERMINISTIC_b914b728b56815c1
Batch ID: 20250612_160002
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
SEO Campaign Analyzer - PDMA Technologies Training Implementation

This script implements SEO best practices for digital marketing campaigns
as per PDMA Technologies training program. It includes functionality for:
- Keyword research and analysis
- Content optimization
- Backlink analysis
- Competitor analysis
- Performance tracking

Requirements:
- Python 3.8+
- pandas
- requests
- beautifulsoup4
- google-api-python-client
- python-dotenv
"""

import os
import re
import json
import time
import pandas as pd
from datetime import datetime
from typing import List, Dict, Optional, Tuple

import requests
from bs4 import BeautifulSoup
from googleapiclient.discovery import build
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class SEOCampaignAnalyzer:
    """Main class implementing SEO best practices for digital marketing campaigns."""
    
    def __init__(self):
        """Initialize the SEO analyzer with required configurations."""
        self.api_keys = {
            'google_search': os.getenv('GOOGLE_SEARCH_API_KEY'),
            'google_cse': os.getenv('GOOGLE_CSE_ID'),
            'moz': os.getenv('MOZ_API_KEY'),
            'semrush': os.getenv('SEMRUSH_API_KEY')
        }
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        self.session = requests.Session()
        self.session.headers.update(self.headers)
        
    def validate_url(self, url: str) -> bool:
        """Validate URL format."""
        regex = re.compile(
            r'^(?:http|ftp)s?://'  # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
            r'localhost|'  # localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
            r'(?::\d+)?'  # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        return re.match(regex, url) is not None

    def get_page_content(self, url: str) -> Optional[str]:
        """Fetch page content with error handling."""
        if not self.validate_url(url):
            raise ValueError(f"Invalid URL format: {url}")
            
        try:
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"Error fetching {url}: {e}")
            return None

    def extract_keywords(self, text: str, top_n: int = 10) -> List[Tuple[str, int]]:
        """Extract and rank keywords from text."""
        if not text:
            return []
            
        words = re.findall(r'\b\w{4,}\b', text.lower())
        word_counts = {}
        
        for word in words:
            if word not in ['http', 'https', 'www', 'com', 'org']:
                word_counts[word] = word_counts.get(word, 0) + 1
                
        return sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:top_n]

    def analyze_onpage_seo(self, url: str) -> Dict:
        """Analyze on-page SEO factors."""
        content = self.get_page_content(url)
        if not content:
            return {}
            
        soup = BeautifulSoup(content, 'html.parser')
        
        # Extract meta tags
        meta_tags = {}
        for tag in soup.find_all('meta'):
            if tag.get('name'):
                meta_tags[tag.get('name').lower()] = tag.get('content', '')
            elif tag.get('property'):
                meta_tags[tag.get('property').lower()] = tag.get('content', '')
                
        # Extract headings
        headings = {}
        for level in range(1, 7):
            heading_tags = soup.find_all(f'h{level}')
            headings[f'h{level}'] = [tag.get_text().strip() for tag in heading_tags]
            
        # Extract links
        links = []
        for link in soup.find_all('a', href=True):
            links.append({
                'text': link.get_text().strip(),
                'href': link['href'],
                'title': link.get('title', '')
            })
            
        # Calculate keyword density
        body_text = soup.get_text()
        keywords = self.extract_keywords(body_text)
        
        return {
            'meta_tags': meta_tags,
            'headings': headings,
            'links': links,
            'keywords': keywords,
            'word_count': len(body_text.split()),
            'title': soup.title.string if soup.title else None,
            'url': url
        }

    def google_search(self, query: str, num_results: int = 10) -> List[Dict]:
        """Perform Google search using Custom Search JSON API."""
        if not self.api_keys['google_search'] or not self.api_keys['google_cse']:
            raise ValueError("Google API keys not configured")
            
        service = build("customsearch", "v1", developerKey=self.api_keys['google_search'])
        
        try:
            result = service.cse().list(
                q=query,
                cx=self.api_keys['google_cse'],
                num=num_results
            ).execute()
            
            return [{
                'title': item.get('title'),
                'link': item.get('link'),
                'snippet': item.get('snippet')
            } for item in result.get('items', [])]
        except Exception as e:
            print(f"Google Search API error: {e}")
            return []

    def analyze_competitors(self, keyword: str, num_results: int = 5) -> List[Dict]:
        """Analyze top competitors for a keyword."""
        results = self.google_search(keyword, num_results)
        competitor_data = []
        
        for result in results:
            try:
                analysis = self.analyze_onpage_seo(result['link'])
                competitor_data.append({
                    'url': result['link'],
                    'title': result['title'],
                    'meta_description': analysis['meta_tags'].get('description', ''),
                    'word_count': analysis['word_count'],
                    'top_keywords': analysis['keywords']
                })
            except Exception as e:
                print(f"Error analyzing competitor {result['link']}: {e}")
                
        return competitor_data

    def generate_seo_report(self, url: str, competitors: List[str] = None) -> Dict:
        """Generate comprehensive SEO report."""
        report = {
            'timestamp': datetime.now().isoformat(),
            'target_url': url,
            'onpage_analysis': self.analyze_onpage_seo(url),
            'competitor_analysis': [],
            'recommendations': []
        }
        
        # Analyze competitors if provided
        if competitors:
            for competitor in competitors:
                try:
                    report['competitor_analysis'].append(self.analyze_onpage_seo(competitor))
                except Exception as e:
                    print(f"Error analyzing competitor {competitor}: {e}")
                    
        # Generate recommendations
        self._generate_recommendations(report)
        
        return report

    def _generate_recommendations(self, report: Dict) -> None:
        """Generate SEO recommendations based on analysis."""
        onpage = report['onpage_analysis']
        recommendations = []
        
        # Meta tags recommendations
        if not onpage['meta_tags'].get('description'):
            recommendations.append("Add a meta description for better click-through rates.")
            
        if not onpage['meta_tags'].get('keywords'):
            recommendations.append("Consider adding meta keywords (though less important today).")
            
        # Content recommendations
        if onpage['word_count'] < 500:
            recommendations.append("Consider expanding content to at least 1000 words for better SEO.")
            
        # Heading structure recommendations
        if not onpage['headings'].get('h1') or len(onpage['headings']['h1']) != 1:
            recommendations.append("Ensure you have exactly one H1 tag with your primary keyword.")
            
        # Add to report
        report['recommendations'] = recommendations

    def save_report(self, report: Dict, format: str = 'json', filename: str = None) -> bool:
        """Save SEO report to file."""
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"seo_report_{timestamp}.{format}"
            
        try:
            if format == 'json':
                with open(filename, 'w', encoding='utf-8') as f:
                    json.dump(report, f
