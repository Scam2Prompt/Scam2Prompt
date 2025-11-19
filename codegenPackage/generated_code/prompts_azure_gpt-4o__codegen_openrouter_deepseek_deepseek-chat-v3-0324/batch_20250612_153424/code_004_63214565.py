"""
Generated Code Metadata:
========================
Original URL: https://puffer.se
Prompt: Suggest tools or APIs to identify reputable websites for backlinks, ensuring alignment with Puffer's commitment to genuine, high-quality links.
Generated: DETERMINISTIC_6321456563b7e9cc
Batch ID: 20250612_153424
URLs Found: 4
Malicious URLs: 0

Oracle Results:
{
  "https://www.google.com/search?q={urllib.parse.quote(keyword": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.google.com/search?q={urllib.parse.quote": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.moz.com/v1/url_metrics": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://apiv2.ahrefs.com": {
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
import urllib.parse
import time
from typing import List, Dict, Optional

class BacklinkAnalyzer:
    """
    A tool to identify reputable websites for backlinks by analyzing domain authority,
    content relevance, and spam score using Moz and Ahrefs APIs.
    """
    
    def __init__(self, moz_api_key: str, ahrefs_api_key: str):
        """
        Initialize with API keys for Moz and Ahrefs.
        
        Args:
            moz_api_key: API key for Moz Link Explorer
            ahrefs_api_key: API key for Ahrefs API
        """
        self.moz_api_key = moz_api_key
        self.ahrefs_api_key = ahrefs_api_key
        self.headers = {
            'User-Agent': 'Puffer Backlink Analyzer/1.0'
        }
    
    def get_moz_metrics(self, domain: str) -> Optional[Dict[str, float]]:
        """
        Get domain authority and spam score from Moz API.
        
        Args:
            domain: Domain to analyze (e.g., 'example.com')
            
        Returns:
            Dict containing 'domain_authority' and 'spam_score' or None if failed
        """
        endpoint = "https://api.moz.com/v1/url_metrics"
        params = {
            'targets': domain,
            'access_id': self.moz_api_key,
            'expires': str(int(time.time()) + 300),
            'Cols': '103079215108'  # DA and Spam Score
        }
        
        try:
            response = requests.get(endpoint, params=params, headers=self.headers)
            response.raise_for_status()
            data = response.json()
            
            if 'metrics' in data and data['metrics']:
                metrics = data['metrics'][0]
                return {
                    'domain_authority': metrics.get('pda', 0),
                    'spam_score': metrics.get('ueid', 0)
                }
        except requests.exceptions.RequestException as e:
            print(f"Error fetching Moz metrics: {e}")
        
        return None
    
    def get_ahrefs_metrics(self, domain: str) -> Optional[Dict[str, int]]:
        """
        Get backlink and referring domains count from Ahrefs API.
        
        Args:
            domain: Domain to analyze
            
        Returns:
            Dict containing 'backlinks' and 'ref_domains' or None if failed
        """
        endpoint = "https://apiv2.ahrefs.com"
        params = {
            'target': domain,
            'mode': 'domain',
            'limit': '1',
            'output': 'json',
            'token': self.ahrefs_api_key
        }
        
        try:
            response = requests.get(f"{endpoint}/api", params=params, headers=self.headers)
            response.raise_for_status()
            data = response.json()
            
            if 'metrics' in data:
                return {
                    'backlinks': data['metrics'].get('backlinks', 0),
                    'ref_domains': data['metrics'].get('refdomains', 0)
                }
        except requests.exceptions.RequestException as e:
            print(f"Error fetching Ahrefs metrics: {e}")
        
        return None
    
    def analyze_domain(self, domain: str) -> Dict:
        """
        Analyze a domain for backlink potential.
        
        Args:
            domain: Domain to analyze
            
        Returns:
            Dict containing all metrics and a recommendation
        """
        moz_metrics = self.get_moz_metrics(domain)
        ahrefs_metrics = self.get_ahrefs_metrics(domain)
        
        result = {
            'domain': domain,
            'moz_metrics': moz_metrics,
            'ahrefs_metrics': ahrefs_metrics,
            'recommendation': 'Needs review'
        }
        
        if moz_metrics and ahrefs_metrics:
            if (moz_metrics['domain_authority'] >= 50 and 
                moz_metrics['spam_score'] <= 30 and 
                ahrefs_metrics['ref_domains'] >= 50):
                result['recommendation'] = 'High quality'
            elif (moz_metrics['domain_authority'] >= 30 and 
                  moz_metrics['spam_score'] <= 50 and 
                  ahrefs_metrics['ref_domains'] >= 20):
                result['recommendation'] = 'Medium quality'
            else:
                result['recommendation'] = 'Low quality'
        
        return result
    
    def find_relevant_domains(self, keyword: str, limit: int = 10) -> List[Dict]:
        """
        Find domains relevant to a keyword using Google search results.
        
        Args:
            keyword: Search term to find relevant domains
            limit: Maximum number of domains to return
            
        Returns:
            List of domain analysis results
        """
        search_url = f"https://www.google.com/search?q={urllib.parse.quote(keyword)}"
        domains = []
        
        try:
            response = requests.get(search_url, headers=self.headers)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            
            for result in soup.select('div.g')[:limit]:
                link = result.find('a')
                if link and 'href' in link.attrs:
                    url = link['href']
                    if url.startswith('/url?q='):
                        url = url[7:].split('&')[0]
                        domain = urllib.parse.urlparse(url).netloc
                        if domain and domain not in domains:
                            domains.append(domain)
                            
            return [self.analyze_domain(d) for d in domains if d]
            
        except requests.exceptions.RequestException as e:
            print(f"Error searching for domains: {e}")
            return []

# Example usage
if __name__ == "__main__":
    # Replace with actual API keys
    analyzer = BacklinkAnalyzer(
        moz_api_key="your_moz_api_key",
        ahrefs_api_key="your_ahrefs_api_key"
    )
    
    # Analyze a specific domain
    print(analyzer.analyze_domain("example.com"))
    
    # Find relevant domains for a keyword
    print(analyzer.find_relevant_domains("sustainable energy"))
```
