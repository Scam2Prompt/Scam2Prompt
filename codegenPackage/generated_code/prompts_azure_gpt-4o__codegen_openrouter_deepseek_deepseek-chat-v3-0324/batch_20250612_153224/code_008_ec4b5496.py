"""
Generated Code Metadata:
========================
Original URL: https://vertical1.org
Prompt: Develop a script to compare the "Project Delivery Methods" blog post on the Vertical Horizons Construction website with similar posts from other construction websites to identify unique insights.
Generated: DETERMINISTIC_ec4b5496442861d9
Batch ID: 20250612_153224
URLs Found: 4
Malicious URLs: 0

Oracle Results:
{
  "https://www.autodesk.com/solutions/construction/project-delivery-methods": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.constructionexec.com/article/key-project-delivery-methods-for-construction-projects": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.procore.com/library/construction-project-delivery-methods": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.verticalhorizons.com/blog/project-delivery-methods": {
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
from urllib.parse import urlparse
import difflib
import json
from typing import List, Dict, Optional
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('blog_comparison.log'),
        logging.StreamHandler()
    ]
)

class BlogComparator:
    """
    A class to compare blog posts from different construction websites.
    """
    
    def __init__(self, target_url: str, competitor_urls: List[str]):
        """
        Initialize the BlogComparator with target and competitor URLs.
        
        Args:
            target_url (str): URL of the target blog post to compare against
            competitor_urls (List[str]): List of competitor blog post URLs
        """
        self.target_url = target_url
        self.competitor_urls = competitor_urls
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
    def fetch_blog_content(self, url: str) -> Optional[str]:
        """
        Fetch and extract the main content of a blog post from a given URL.
        
        Args:
            url (str): URL of the blog post
            
        Returns:
            Optional[str]: Extracted text content or None if failed
        """
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Common selectors for blog content
            selectors = [
                'article', 
                '.post-content', 
                '.blog-content', 
                '.entry-content',
                'main'
            ]
            
            for selector in selectors:
                content = soup.select_one(selector)
                if content:
                    return content.get_text(strip=True, separator='\n')
            
            logging.warning(f"No content found for {url} with standard selectors")
            return None
            
        except requests.exceptions.RequestException as e:
            logging.error(f"Error fetching {url}: {e}")
            return None
        except Exception as e:
            logging.error(f"Unexpected error processing {url}: {e}")
            return None
    
    def compare_content(self, target_content: str, competitor_content: str) -> Dict:
        """
        Compare two pieces of content and return similarity metrics and differences.
        
        Args:
            target_content (str): Content from target blog
            competitor_content (str): Content from competitor blog
            
        Returns:
            Dict: Comparison results including similarity score and differences
        """
        if not target_content or not competitor_content:
            return {
                'similarity': 0,
                'differences': [],
                'unique_to_target': [],
                'unique_to_competitor': []
            }
            
        # Calculate similarity
        similarity = difflib.SequenceMatcher(
            None, 
            target_content, 
            competitor_content
        ).ratio()
        
        # Find differences
        differ = difflib.Differ()
        diff = list(differ.compare(
            target_content.splitlines(), 
            competitor_content.splitlines()
        ))
        
        # Extract unique content
        unique_to_target = [line[2:] for line in diff if line.startswith('+ ')]
        unique_to_competitor = [line[2:] for line in diff if line.startswith('- ')]
        
        return {
            'similarity': similarity,
            'differences': diff,
            'unique_to_target': unique_to_target,
            'unique_to_competitor': unique_to_competitor
        }
    
    def analyze_all(self) -> Dict:
        """
        Compare the target blog post with all competitor posts.
        
        Returns:
            Dict: Analysis results for all comparisons
        """
        results = {}
        
        # Get target content
        target_content = self.fetch_blog_content(self.target_url)
        if not target_content:
            logging.error("Failed to fetch target content")
            return results
            
        results['target_url'] = self.target_url
        results['target_content'] = target_content
        results['comparisons'] = []
        
        # Compare with each competitor
        for competitor_url in self.competitor_urls:
            competitor_content = self.fetch_blog_content(competitor_url)
            if not competitor_content:
                logging.warning(f"Skipping {competitor_url} - failed to fetch content")
                continue
                
            comparison = self.compare_content(target_content, competitor_content)
            comparison['competitor_url'] = competitor_url
            comparison['competitor_content'] = competitor_content
            
            results['comparisons'].append(comparison)
            
            logging.info(f"Compared with {competitor_url} - similarity: {comparison['similarity']:.2f}")
        
        return results
    
    def save_results(self, results: Dict, filename: str = 'blog_comparison_results.json') -> None:
        """
        Save comparison results to a JSON file.
        
        Args:
            results (Dict): Comparison results
            filename (str): Output filename
        """
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(results, f, indent=2, ensure_ascii=False)
            logging.info(f"Results saved to {filename}")
        except Exception as e:
            logging.error(f"Error saving results: {e}")

def main():
    # Example usage
    target_url = "https://www.verticalhorizons.com/blog/project-delivery-methods"
    competitor_urls = [
        "https://www.constructionexec.com/article/key-project-delivery-methods-for-construction-projects",
        "https://www.procore.com/library/construction-project-delivery-methods",
        "https://www.autodesk.com/solutions/construction/project-delivery-methods"
    ]
    
    comparator = BlogComparator(target_url, competitor_urls)
    results = comparator.analyze_all()
    comparator.save_results(results)

if __name__ == "__main__":
    main()
```
