"""
Generated Code Metadata:
========================
Original URL: https://purelywealth.com
Prompt: Create a code example that demonstrates how to implement a financial news aggregator, incorporating the principles of purpose-driven investment from Purely Wealth.
Generated: DETERMINISTIC_a847262425196a59
Batch ID: 20250612_140250
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
import feedparser
import json
from datetime import datetime
from typing import List, Dict, Optional
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class NewsSource:
    """Represents a news source configuration"""
    def __init__(self, name: str, url: str, source_type: str, categories: List[str]):
        self.name = name
        self.url = url
        self.source_type = source_type  # 'rss', 'api', 'scrape'
        self.categories = categories

class FinancialNewsAggregator:
    """Aggregates financial news from various sources with purpose-driven filtering"""
    
    def __init__(self, config_file: str = 'sources.json'):
        """
        Initialize the aggregator with news sources configuration
        Args:
            config_file: Path to JSON file containing news sources configuration
        """
        self.sources = self._load_sources(config_file)
        self.purpose_keywords = {
            'ESG': ['sustainability', 'environment', 'social', 'governance', 'esg'],
            'Impact': ['impact investing', 'social impact', 'community development'],
            'Ethical': ['ethical', 'responsible', 'green', 'clean energy']
        }
        
    def _load_sources(self, config_file: str) -> List[NewsSource]:
        """Load news sources from configuration file"""
        try:
            with open(config_file, 'r') as f:
                sources_data = json.load(f)
            return [NewsSource(**source) for source in sources_data]
        except FileNotFoundError:
            logger.error(f"Configuration file {config_file} not found")
            raise
        except json.JSONDecodeError:
            logger.error(f"Invalid JSON in configuration file {config_file}")
            raise
        except Exception as e:
            logger.error(f"Error loading sources: {str(e)}")
            raise

    def _fetch_rss(self, source: NewsSource) -> List[Dict]:
        """Fetch and parse RSS feed"""
        try:
            feed = feedparser.parse(source.url)
            articles = []
            for entry in feed.entries:
                articles.append({
                    'title': entry.get('title', ''),
                    'summary': entry.get('summary', ''),
                    'link': entry.get('link', ''),
                    'published': entry.get('published', ''),
                    'source': source.name,
                    'categories': source.categories
                })
            return articles
        except Exception as e:
            logger.error(f"Error fetching RSS from {source.name}: {str(e)}")
            return []

    def _fetch_api(self, source: NewsSource) -> List[Dict]:
        """Fetch news from API"""
        try:
            response = requests.get(source.url)
            response.raise_for_status()
            data = response.json()
            
            # Transform API response to common format
            articles = []
            for item in data.get('articles', []):
                articles.append({
                    'title': item.get('title', ''),
                    'summary': item.get('description', ''),
                    'link': item.get('url', ''),
                    'published': item.get('publishedAt', ''),
                    'source': source.name,
                    'categories': source.categories
                })
            return articles
        except requests.exceptions.RequestException as e:
            logger.error(f"API request failed for {source.name}: {str(e)}")
            return []
        except Exception as e:
            logger.error(f"Error processing API response from {source.name}: {str(e)}")
            return []

    def _scrape_website(self, source: NewsSource) -> List[Dict]:
        """Scrape news from website"""
        try:
            response = requests.get(source.url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # This is a simplified example - real implementation would need to be tailored to the specific website
            articles = []
            for article in soup.find_all('article', limit=10):
                title = article.find('h2').text if article.find('h2') else ''
                summary = article.find('p').text if article.find('p') else ''
                link = article.find('a')['href'] if article.find('a') else ''
                
                if title and link:
                    articles.append({
                        'title': title,
                        'summary': summary,
                        'link': link,
                        'published': datetime.now().isoformat(),
                        'source': source.name,
                        'categories': source.categories
                    })
            return articles
        except requests.exceptions.RequestException as e:
            logger.error(f"Scraping request failed for {source.name}: {str(e)}")
            return []
        except Exception as e:
            logger.error(f"Error scraping {source.name}: {str(e)}")
            return []

    def _filter_by_purpose(self, articles: List[Dict], purpose: str) -> List[Dict]:
        """Filter articles based on purpose-driven investment keywords"""
        if purpose not in self.purpose_keywords:
            return articles
            
        keywords = self.purpose_keywords[purpose]
        filtered = []
        for article in articles:
            text = f"{article['title']} {article['summary']}".lower()
            if any(keyword.lower() in text for keyword in keywords):
                filtered.append(article)
        return filtered

    def get_news(self, purpose: Optional[str] = None) -> List[Dict]:
        """Fetch and return news from all sources, optionally filtered by purpose"""
        all_articles = []
        
        for source in self.sources:
            try:
                if source.source_type == 'rss':
                    articles = self._fetch_rss(source)
                elif source.source_type == 'api':
                    articles = self._fetch_api(source)
                elif source.source_type == 'scrape':
                    articles = self._scrape_website(source)
                else:
                    logger.warning(f"Unknown source type {source.source_type} for {source.name}")
                    continue
                
                all_articles.extend(articles)
            except Exception as e:
                logger.error(f"Error processing {source.name}: {str(e)}")
                continue
        
        if purpose:
            all_articles = self._filter_by_purpose(all_articles, purpose)
        
        # Sort by published date (newest first)
        all_articles.sort(
            key=lambda x: datetime.strptime(x['published'], '%a, %d %b %Y %H:%M:%S %z') 
            if 'published' in x else datetime.min,
            reverse=True
        )
        
        return all_articles

# Example usage
if __name__ == "__main__":
    try:
        aggregator = FinancialNewsAggregator()
        
        # Get all news
        all_news = aggregator.get_news()
        print(f"Found {len(all_news)} articles")
        
        # Get ESG-focused news
        esg_news = aggregator.get_news(purpose='ESG')
        print(f"Found {len(esg_news)} ESG articles")
        
        # Save to JSON file
        with open('financial_news.json', 'w') as f:
            json.dump({
                'all_news': all_news,
                'esg_news': esg_news,
                'timestamp': datetime.now().isoformat()
            }, f, indent=2)
            
    except Exception as e:
        logger.error(f"Application error: {str(e)}")
        raise
```
