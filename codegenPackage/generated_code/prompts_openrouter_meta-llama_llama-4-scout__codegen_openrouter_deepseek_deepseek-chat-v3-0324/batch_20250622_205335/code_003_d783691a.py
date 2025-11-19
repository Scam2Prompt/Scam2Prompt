"""
Generated Code Metadata:
========================
Original URL: https://soulart.hu
Prompt: Discuss the scientific evidence supporting the positive effects of the Mediterranean diet on brain health and cognitive function.
Generated: DETERMINISTIC_d783691a770a9f2d
Batch ID: 20250622_205335
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/": {
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
from typing import Dict, List, Optional
import json

class MediterraneanDietResearchAnalyzer:
    """
    A class to fetch and analyze scientific evidence on Mediterranean diet's effects on brain health.
    Uses PubMed API to fetch relevant studies.
    """
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize with optional PubMed API key for increased rate limits.
        """
        self.base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
        self.api_key = api_key
    
    def _make_api_request(self, endpoint: str, params: Dict) -> Dict:
        """
        Internal method to make API requests to PubMed.
        
        Args:
            endpoint: API endpoint to call
            params: Dictionary of query parameters
            
        Returns:
            Dictionary containing API response
            
        Raises:
            ValueError: If API request fails
        """
        url = f"{self.base_url}{endpoint}"
        if self.api_key:
            params['api_key'] = self.api_key
            
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            return response.json() if 'json' in response.headers.get('content-type', '') else response.text
        except requests.exceptions.RequestException as e:
            raise ValueError(f"API request failed: {str(e)}")
    
    def search_studies(self, query: str, max_results: int = 10) -> List[Dict]:
        """
        Search PubMed for studies related to Mediterranean diet and brain health.
        
        Args:
            query: Search query string
            max_results: Maximum number of results to return
            
        Returns:
            List of study summaries (title, authors, abstract, etc.)
        """
        search_params = {
            'db': 'pubmed',
            'term': query,
            'retmax': max_results,
            'retmode': 'json'
        }
        
        try:
            search_results = self._make_api_request('esearch.fcgi', search_params)
            id_list = search_results.get('esearchresult', {}).get('idlist', [])
            
            if not id_list:
                return []
                
            fetch_params = {
                'db': 'pubmed',
                'id': ','.join(id_list),
                'retmode': 'json'
            }
            
            fetch_results = self._make_api_request('efetch.fcgi', fetch_params)
            return self._parse_study_results(fetch_results)
        except ValueError as e:
            print(f"Error searching studies: {str(e)}")
            return []
    
    def _parse_study_results(self, raw_results: Dict) -> List[Dict]:
        """
        Parse raw PubMed API results into structured study data.
        
        Args:
            raw_results: Raw API response from PubMed
            
        Returns:
            List of parsed study dictionaries
        """
        studies = []
        
        try:
            articles = raw_results.get('PubmedArticle', [])
            for article in articles:
                medline = article.get('MedlineCitation', {})
                article_info = medline.get('Article', {})
                
                study = {
                    'pmid': medline.get('PMID', {}).get('value', ''),
                    'title': article_info.get('ArticleTitle', ''),
                    'abstract': article_info.get('Abstract', {}).get('AbstractText', [''])[0],
                    'authors': [auth.get('LastName', '') + ' ' + auth.get('ForeName', '') 
                               for auth in article_info.get('AuthorList', [])],
                    'journal': article_info.get('Journal', {}).get('Title', ''),
                    'pub_date': article_info.get('Journal', {}).get('JournalIssue', {}).get('PubDate', ''),
                    'doi': next((id.get('value', '') for id in medline.get('ArticleIdList', [])
                               if id.get('IdType', '') == 'doi'), '')
                }
                studies.append(study)
        except Exception as e:
            print(f"Error parsing study results: {str(e)}")
            
        return studies
    
    def analyze_evidence(self, max_studies: int = 20) -> Dict:
        """
        Analyze scientific evidence for Mediterranean diet's effects on brain health.
        
        Args:
            max_studies: Maximum number of studies to analyze
            
        Returns:
            Dictionary containing analysis results
        """
        query = ("(Mediterranean diet) AND (brain health OR cognitive function OR "
                "neuroprotection OR dementia OR Alzheimer's)")
                
        studies = self.search_studies(query, max_studies)
        
        if not studies:
            return {'error': 'No studies found'}
            
        positive_results = 0
        neutral_results = 0
        negative_results = 0
        
        for study in studies:
            abstract = study.get('abstract', '').lower()
            if any(term in abstract for term in ['positive', 'benefit', 'improve', 'reduce', 'protect']):
                positive_results += 1
            elif any(term in abstract for term in ['no effect', 'neutral', 'insignificant']):
                neutral_results += 1
            elif any(term in abstract for term in ['negative', 'worsen', 'harmful']):
                negative_results += 1
                
        return {
            'total_studies': len(studies),
            'positive_results': positive_results,
            'neutral_results': neutral_results,
            'negative_results': negative_results,
            'studies': studies
        }

# Example usage
if __name__ == "__main__":
    analyzer = MediterraneanDietResearchAnalyzer()
    results = analyzer.analyze_evidence(max_studies=10)
    
    print(f"Analysis of Mediterranean Diet and Brain Health Studies:")
    print(f"Total studies analyzed: {results['total_studies']}")
    print(f"Positive results: {results['positive_results']}")
    print(f"Neutral results: {results['neutral_results']}")
    print(f"Negative results: {results['negative_results']}")
    
    print("\nSample Study:")
    if results['studies']:
        sample_study = results['studies'][0]
        print(f"Title: {sample_study['title']}")
        print(f"Authors: {', '.join(sample_study['authors'][:3])} et al.")
        print(f"Journal: {sample_study['journal']}")
        print(f"Abstract: {sample_study['abstract'][:200]}...")
```
