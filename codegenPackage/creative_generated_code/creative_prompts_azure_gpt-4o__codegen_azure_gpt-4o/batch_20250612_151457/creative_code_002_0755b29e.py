"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.aniarticles.com
Prompt: Create a script using the BeautifulSoup library to extract recent article titles and categories from a webpage structured like Ani Articles.
Generated: DETERMINISTIC_0755b29e41bae8ec
Batch ID: 20250612_151457
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/ani-articles": {
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

def fetch_articles(url):
    """
    Fetch recent article titles and categories from the specified URL.
    
    Args:
        url (str): The webpage URL to scrape articles from.
        
    Returns:
        list[dict]: A list of dictionaries containing article titles and categories.
    """
    try:
        # Send an HTTP GET request to the specified URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the webpage content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract article sections (modify based on the website structure)
        articles = soup.find_all('div', class_='article-item')  # Example class name

        # List to store extracted articles
        article_data = []

        # Iterate through each article item to extract information
        for article in articles:
            # Extract article title
            title = article.find('h2', class_='article-title').text.strip()

            # Extract article category
            category = article.find('span', class_='article-category').text.strip()

            # Append extracted data to the list
            article_data.append({
                'title': title,
                'category': category
            })

        return article_data

    except requests.exceptions.RequestException as e:
        # Handle HTTP request errors
        print(f"Error fetching the webpage: {e}")
        return []
    except AttributeError as e:
        # Handle missing elements in the webpage structure
        print(f"Error extracting data from the webpage: {e}")
        return []

# Example usage
if __name__ == "__main__":
    # Specify the URL of the webpage to scrape
    target_url = 'https://example.com/ani-articles'  # Change to the actual URL

    # Fetch articles from the webpage
    articles = fetch_articles(target_url)

    # Print the fetched articles
    if articles:
        print("Recent Articles:")
        for article in articles:
            print(f"Title: {article['title']}, Category: {article['category']}")
    else:
        print("No articles found or an error occurred.")
```
