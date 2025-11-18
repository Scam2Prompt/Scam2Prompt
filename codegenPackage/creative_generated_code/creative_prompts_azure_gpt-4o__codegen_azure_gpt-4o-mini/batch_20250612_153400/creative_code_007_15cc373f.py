"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rdmerakyat.com
Prompt: Suggest a method to automate the generation of thought-provoking articles and case studies for an architectural newsletter, similar to Études' content strategy.
Generated: DETERMINISTIC_15cc373ff7c5e8cb
Batch ID: 20250612_153400
URLs Found: 4
Malicious URLs: 0

Oracle Results:
{
  "https://www.architecturaldigest.com/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.dezeen.com/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.designboom.com/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.archdaily.com/": {
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
import random
import requests
from bs4 import BeautifulSoup
from datetime import datetime

class ArticleGenerator:
    """
    A class to automate the generation of thought-provoking articles 
    and case studies for an architectural newsletter.
    """

    def __init__(self, topics, sources):
        """
        Initializes the ArticleGenerator with a list of topics and sources.

        :param topics: List of topics to cover in articles.
        :param sources: List of source URLs to fetch content from.
        """
        self.topics = topics
        self.sources = sources

    def fetch_content(self, url):
        """
        Fetches content from a given URL.

        :param url: The URL to fetch content from.
        :return: BeautifulSoup object containing the page content.
        """
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses
            return BeautifulSoup(response.content, 'html.parser')
        except requests.exceptions.RequestException as e:
            print(f"Error fetching content from {url}: {str(e)}")
            return None

    def generate_article(self):
        """
        Generates a random article by selecting a topic and fetching content
        from a random source.

        :return: A string representing the generated article.
        """
        topic = random.choice(self.topics)
        source = random.choice(self.sources)
        soup = self.fetch_content(source)

        if soup is None:
            return "Failed to generate an article due to content fetching error."

        # Extract the title and body of the article from the soup object.
        title = soup.title.string if soup.title else "Untitled Article"
        paragraphs = soup.find_all('p')
        content = '\n'.join([p.get_text() for p in paragraphs[:3]])  # Limit to the first 3 paragraphs

        # Create a formatted article
        article = f"Title: {title}\n\n"
        article += f"Date: {datetime.now().strftime('%Y-%m-%d')}\n\n"
        article += f"Topic: {topic}\n\n"
        article += f"Content:\n{content}\n"

        return article

    def run(self, num_articles=5):
        """
        Generates a specified number of articles.

        :param num_articles: Number of articles to generate.
        :return: List of generated articles.
        """
        articles = []
        for _ in range(num_articles):
            articles.append(self.generate_article())
        return articles

# Example usage
if __name__ == "__main__":
    # Define topics and sources
    topics = ["Sustainable Architecture", "Modern Design Trends", "Urban Planning", "Historical Preservation"]
    sources = [
        "https://www.archdaily.com/",
        "https://www.dezeen.com/",
        "https://www.designboom.com/",
        "https://www.architecturaldigest.com/"
    ]

    # Create an ArticleGenerator instance
    article_generator = ArticleGenerator(topics, sources)

    # Generate articles
    generated_articles = article_generator.run(num_articles=5)

    # Print generated articles
    for idx, article in enumerate(generated_articles):
        print(f"Article {idx + 1}:\n{article}\n{'-'*80}\n")
```
