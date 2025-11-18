"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://byamed.net
Prompt: Develop a script for analyzing competitors' online presence and generating actionable insights, inspired by ByAmed.net's market-crusher strategies.
Generated: DETERMINISTIC_2a2a53010185f967
Batch ID: 20250612_153224
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://example2.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example1.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example3.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests
from bs4 import BeautifulSoup
import re
import logging


# Setup logging for debugging and error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class CompetitorAnalysis:
    """
    A class to analyze competitors' online presence and generate actionable insights.
    """
    
    def __init__(self, urls):
        """
        Initialize the class with a list of competitor URLs.

        :param urls: List of URLs to analyze
        """
        self.urls = urls
        self.results = []

    def fetch_html(self, url):
        """
        Fetch HTML content for a given URL.

        :param url: The URL to fetch
        :return: HTML content as a string
        """
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()  # Raise HTTPError for bad responses
            return response.text
        except requests.exceptions.RequestException as e:
            logging.error(f"Error fetching URL {url}: {e}")
            return None

    def extract_metadata(self, html):
        """
        Extract metadata from the HTML content.

        :param html: HTML content as a string
        :return: Metadata as a dictionary
        """
        try:
            soup = BeautifulSoup(html, 'html.parser')
            title = soup.title.string if soup.title else 'No Title'
            description = ''
            keywords = ''

            # Extract meta description
            meta_desc = soup.find('meta', attrs={'name': 'description'})
            if meta_desc and meta_desc.get('content'):
                description = meta_desc['content']
            
            # Extract meta keywords
            meta_keywords = soup.find('meta', attrs={'name': 'keywords'})
            if meta_keywords and meta_keywords.get('content'):
                keywords = meta_keywords['content']

            return {
                'title': title,
                'description': description,
                'keywords': keywords
            }
        except Exception as e:
            logging.error(f"Error extracting metadata: {e}")
            return None

    def extract_links(self, html):
        """
        Extract all hyperlinks from the HTML content.

        :param html: HTML content as a string
        :return: List of hyperlinks
        """
        try:
            soup = BeautifulSoup(html, 'html.parser')
            links = []
            for a_tag in soup.find_all('a', href=True):
                href = a_tag['href']
                # Ensure the link is valid
                if re.match(r'^https?://', href):
                    links.append(href)
            return links
        except Exception as e:
            logging.error(f"Error extracting links: {e}")
            return []

    def analyze(self):
        """
        Perform the competitor analysis by fetching and processing each URL.

        :return: List of analysis results
        """
        for url in self.urls:
            logging.info(f"Analyzing {url}...")
            
            # Fetch HTML content
            html = self.fetch_html(url)
            if not html:
                continue

            # Extract insights
            metadata = self.extract_metadata(html)
            links = self.extract_links(html)

            self.results.append({
                'url': url,
                'metadata': metadata,
                'links': links,
            })
        
        return self.results

    def generate_insights(self):
        """
        Generate actionable insights based on the analysis results.

        :return: Insights as a dictionary
        """
        insights = {
            'most_common_keywords': [],
            'top_linked_domains': [],
        }
        
        keyword_counter = {}
        domain_counter = {}

        for result in self.results:
            # Count keywords
            keywords = result['metadata'].get('keywords', '').split(',')
            for keyword in keywords:
                keyword = keyword.strip().lower()
                if keyword:
                    keyword_counter[keyword] = keyword_counter.get(keyword, 0) + 1
            
            # Count domains in links
            for link in result['links']:
                domain = re.findall(r'https?://(?:www\.)?([^/]+)', link)
                if domain:
                    domain_name = domain[0]
                    domain_counter[domain_name] = domain_counter.get(domain_name, 0) + 1
        
        # Sort and extract insights
        insights['most_common_keywords'] = sorted(keyword_counter.items(), key=lambda x: x[1], reverse=True)[:10]
        insights['top_linked_domains'] = sorted(domain_counter.items(), key=lambda x: x[1], reverse=True)[:10]

        return insights


if __name__ == "__main__":
    # Sample list of competitor URLs
    competitor_urls = [
        "https://example1.com",
        "https://example2.com",
        "https://example3.com",
    ]
    
    # Initialize the analysis tool
    analyzer = CompetitorAnalysis(competitor_urls)

    # Perform analysis
    results = analyzer.analyze()

    # Print analysis results
    logging.info("Analysis Results:")
    for result in results:
        logging.info(result)

    # Generate insights
    insights = analyzer.generate_insights()

    # Print actionable insights
    logging.info("Actionable Insights:")
    logging.info(insights)
```
