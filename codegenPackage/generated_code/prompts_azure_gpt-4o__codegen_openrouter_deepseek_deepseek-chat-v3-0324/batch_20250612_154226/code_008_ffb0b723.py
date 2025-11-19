"""
Generated Code Metadata:
========================
Original URL: https://ethn.cc
Prompt: Create a Python script to generate summaries of gravel cycling gear tests, like the comparison of Abus AirBreaker and GameChanger 2.0 helmets on ETNH Gravel Magazine.
Generated: DETERMINISTIC_ffb0b7235fb32d10
Batch ID: 20250612_154226
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.etnhgravelmagazine.com": {
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
import json
from typing import Dict, List, Optional
from dataclasses import dataclass, asdict
import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime

@dataclass
class GearTest:
    title: str
    publication_date: str
    author: str
    products: List[str]
    summary: str
    pros: List[str]
    cons: List[str]
    verdict: str
    url: str

class GravelGearSummarizer:
    """
    A class to scrape and summarize gravel cycling gear tests from ETNH Gravel Magazine.
    """
    
    def __init__(self, base_url: str = "https://www.etnhgravelmagazine.com"):
        self.base_url = base_url
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
    
    def _fetch_page(self, url: str) -> Optional[str]:
        """Fetch the HTML content of a given URL."""
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"Error fetching page: {e}")
            return None
    
    def _parse_date(self, date_str: str) -> str:
        """Parse various date formats into a standardized format."""
        try:
            # Handle common date formats
            for fmt in ("%B %d, %Y", "%d %B %Y", "%Y-%m-%d", "%m/%d/%Y"):
                try:
                    dt = datetime.strptime(date_str, fmt)
                    return dt.strftime("%Y-%m-%d")
                except ValueError:
                    continue
            return date_str  # Return original if parsing fails
        except Exception as e:
            print(f"Error parsing date: {e}")
            return date_str
    
    def _extract_products(self, title: str) -> List[str]:
        """Extract product names from the article title."""
        # Remove common prefixes and split
        clean_title = re.sub(r'(Review|Comparison|Test|vs\.?|:|\|)', '', title, flags=re.IGNORECASE)
        products = [p.strip() for p in re.split(r' vs | and | versus |, ', clean_title) if p.strip()]
        return products
    
    def _extract_pros_cons(self, soup: BeautifulSoup) -> Dict[str, List[str]]:
        """Extract pros and cons from the article content."""
        pros_cons = {'pros': [], 'cons': []}
        
        # Look for common section headings
        for section in ['Pros', 'Advantages', 'Strengths']:
            element = soup.find(lambda tag: tag.name in ['h2', 'h3'] and section.lower() in tag.text.lower())
            if element:
                next_node = element.find_next_sibling()
                while next_node and next_node.name not in ['h2', 'h3']:
                    if next_node.name == 'ul':
                        pros_cons['pros'].extend([li.text.strip() for li in next_node.find_all('li')])
                    next_node = next_node.find_next_sibling()
        
        for section in ['Cons', 'Disadvantages', 'Weaknesses']:
            element = soup.find(lambda tag: tag.name in ['h2', 'h3'] and section.lower() in tag.text.lower())
            if element:
                next_node = element.find_next_sibling()
                while next_node and next_node.name not in ['h2', 'h3']:
                    if next_node.name == 'ul':
                        pros_cons['cons'].extend([li.text.strip() for li in next_node.find_all('li')])
                    next_node = next_node.find_next_sibling()
        
        return pros_cons
    
    def _extract_verdict(self, soup: BeautifulSoup) -> str:
        """Extract the verdict or conclusion from the article."""
        for section in ['Verdict', 'Conclusion', 'Final Thoughts']:
            element = soup.find(lambda tag: tag.name in ['h2', 'h3'] and section.lower() in tag.text.lower())
            if element:
                verdict = []
                next_node = element.find_next_sibling()
                while next_node and next_node.name not in ['h2', 'h3']:
                    if next_node.name == 'p':
                        verdict.append(next_node.text.strip())
                    next_node = next_node.find_next_sibling()
                return ' '.join(verdict)
        return ""
    
    def _extract_summary(self, soup: BeautifulSoup) -> str:
        """Extract the main summary from the article."""
        # Try to find the first paragraph after the introduction
        intro = soup.find(lambda tag: tag.name == 'p' and len(tag.text.split()) > 30)
        if intro:
            return intro.text.strip()
        return ""
    
    def scrape_article(self, article_url: str) -> Optional[GearTest]:
        """Scrape a single gear test article and return structured data."""
        html = self._fetch_page(article_url)
        if not html:
            return None
            
        soup = BeautifulSoup(html, 'html.parser')
        
        # Extract title
        title_element = soup.find('h1')
        if not title_element:
            return None
        title = title_element.text.strip()
        
        # Extract publication date
        date_element = soup.find('time') or soup.find(class_=re.compile('date|published'))
        date = self._parse_date(date_element['datetime'] if date_element and date_element.has_attr('datetime') 
                               else date_element.text.strip() if date_element 
                               else "")
        
        # Extract author
        author_element = soup.find(class_=re.compile('author|byline')) or soup.find('a', rel='author')
        author = author_element.text.strip() if author_element else "Unknown"
        
        # Extract products
        products = self._extract_products(title)
        
        # Extract content sections
        pros_cons = self._extract_pros_cons(soup)
        verdict = self._extract_verdict(soup)
        summary = self._extract_summary(soup)
        
        return GearTest(
            title=title,
            publication_date=date,
            author=author,
            products=products,
            summary=summary,
            pros=pros_cons['pros'],
            cons=pros_cons['cons'],
            verdict=verdict,
            url=article_url
        )
    
    def find_gear_tests(self, search_term: str = "helmet", max_results: int = 5) -> List[GearTest]:
        """Find gear test articles matching a search term."""
        search_url = f"{self.base_url}/?s={search_term}"
        html = self._fetch_page(search_url)
        if not html:
            return []
            
        soup = BeautifulSoup(html, 'html.parser')
        articles = []
        
        for article in soup.find_all('article', limit=max_results):
            link = article.find('a', href=True)
            if not link:
                continue
                
            gear_test = self.scrape_article(link['href'])
            if gear_test:
                articles.append(gear_test)
        
        return articles
    
    def generate_summary(self, gear_test: GearTest) -> Dict:
        """Generate a structured summary of a gear test."""
        return {
            'metadata': {
                'title': gear_test.title,
                'date': gear_test.publication_date,
                'author': gear_test.author,
                'url': gear_test.url
            },
            'products': gear_test.products,
            'summary': gear_test.summary,
            'pros': gear_test.pros,
            'cons': gear_test.cons,
            'verdict': gear_test.verdict
        }
    
    def save_summary(self, gear_test: GearTest, filename: str) -> None:
        """Save a gear test summary to a JSON file."""
        summary = self.generate_summary(gear_test)
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(summary, f, indent=2, ensure_ascii=False)
        except IOError as e:
            print(f"Error saving summary: {e}")

# Example usage
if __name__ == "__main__":
    summarizer = GravelGearSummarizer()
    
    # Find and summarize helmet tests
    helmet_tests = summarizer.find_gear_tests(search_term="helmet", max_results=2)
    
    for i, test in enumerate(helmet_tests, 1):
        print(f"\nSummary {i}: {test.title}")
        print(json.dumps(summarizer.generate_summary(test), indent=2))
        
        # Save to file
        filename = f"helmet_test_summary_{i}.json"
        summarizer.save_summary(test, filename)
        print(f"Saved to {filename}")
```
