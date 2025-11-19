"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jphs.snru.ac.th
Prompt: How can I access the archives of the PHUPHAN SARN Journal of Humanities and Social Sciences for research purposes?
Generated: DETERMINISTIC_4d3ed203f56a1545
Batch ID: 20250612_160853
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.phuphanjournal.com/archive": {
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

class PHUPHANJournalScraper:
    """
    A class to scrape archives of the PHUPHAN SARN Journal of Humanities and Social Sciences for research purposes.
    """

    BASE_URL = 'https://www.phuphanjournal.com/archive'  # Base URL for the journal's archive

    def __init__(self):
        """
        Initializes the scraper with the base URL.
        """
        self.session = requests.Session()  # Create a session for making HTTP requests

    def get_archive_links(self):
        """
        Fetches archive links from the journal's archive page.

        Returns:
            list: A list of archive links.
        """
        try:
            response = self.session.get(self.BASE_URL)
            response.raise_for_status()  # Raise an error for bad responses
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find all archive links in the soup object
            archive_links = [
                a['href'] for a in soup.find_all('a', href=True) 
                if 'archive' in a['href']
            ]
            return archive_links
        except requests.RequestException as e:
            print(f"Error fetching archive links: {e}")
            return []

    def fetch_article(self, article_url):
        """
        Fetches the content of a specific article given its URL.

        Args:
            article_url (str): URL of the article to fetch.

        Returns:
            str: The content of the article, or an error message.
        """
        try:
            response = self.session.get(article_url)
            response.raise_for_status()  # Raise an error for bad responses
            soup = BeautifulSoup(response.text, 'html.parser')

            # Extract the title and content of the article
            title = soup.find('h1').text  # Assuming the title is in an <h1> tag
            content = soup.find('div', class_='article-content').text  # Assuming article content has this class
            return title, content
        except requests.RequestException as e:
            return f"Error fetching article: {e}"

    def close(self):
        """
        Closes the session.
        """
        self.session.close()

if __name__ == "__main__":
    scraper = PHUPHANJournalScraper()

    # Get archive links
    archives = scraper.get_archive_links()
    print("Archive Links:")
    for link in archives:
        print(link)

    # Example: Fetch an article from the first archive link (if available)
    if archives:
        title, content = scraper.fetch_article(archives[0])  # Fetching the first article as an example
        print("\nArticle Title:", title)
        print("Article Content:", content)

    # Clean up the session
    scraper.close()
```
