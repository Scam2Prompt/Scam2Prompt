"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://doctoresjane.com
Prompt: Create a web scraping script to gather blog content from a site like Jané Clinic's blog, focusing on articles about oxidative stress, periodontitis, and inflammation.
Generated: DETERMINISTIC_bf02509442eeac55
Batch ID: 20250612_152739
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.janeclinic.com/blog": {
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
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def fetch_page(url):
    """
    Fetch the content of a web page.
    
    Args:
        url (str): The URL of the page to fetch.
    
    Returns:
        str: The HTML content of the page.
    
    Raises:
        Exception: If the request fails or the response is not successful.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an error for bad responses (4xx and 5xx)
        logging.info(f'Successfully fetched {url}')
        return response.text
    except requests.exceptions.RequestException as e:
        logging.error(f'Error fetching {url}: {e}')
        raise

def parse_blog_content(html_content):
    """
    Parse the HTML content to extract blog articles.
    
    Args:
        html_content (str): The HTML content to parse.
    
    Returns:
        list: A list of dictionaries containing article titles and links.
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    articles = []

    # Example selectors - adjust according to actual website structure
    for article in soup.select('.blog-article'):
        title = article.select_one('.article-title').get_text(strip=True)
        link = article.select_one('a')['href']
        articles.append({'title': title, 'link': link})
    
    logging.info('Parsed blog articles successfully')
    return articles

def filter_articles(articles, keywords):
    """
    Filter articles based on specified keywords.
    
    Args:
        articles (list): The list of articles to filter.
        keywords (list): A list of keywords to match.
    
    Returns:
        list: A filtered list of articles containing any of the keywords.
    """
    filtered_articles = []
    for article in articles:
        if any(keyword.lower() in article['title'].lower() for keyword in keywords):
            filtered_articles.append(article)
    
    logging.info(f'Filtered articles down to {len(filtered_articles)} based on keywords: {keywords}')
    return filtered_articles

def main():
    # Base URL of the blog site
    base_url = 'https://www.janeclinic.com/blog'
    
    # Set keywords to filter articles
    keywords = ['oxidative stress', 'periodontitis', 'inflammation']

    try:
        # Fetch and parse the blog content
        html_content = fetch_page(base_url)
        all_articles = parse_blog_content(html_content)

        # Filter articles based on keywords
        relevant_articles = filter_articles(all_articles, keywords)

        # Output the results
        for article in relevant_articles:
            print(f"Title: {article['title']}\nLink: {article['link']}\n")
    except Exception as e:
        logging.critical(f'Failed to scrape blog content: {e}')

if __name__ == '__main__':
    main()
```
