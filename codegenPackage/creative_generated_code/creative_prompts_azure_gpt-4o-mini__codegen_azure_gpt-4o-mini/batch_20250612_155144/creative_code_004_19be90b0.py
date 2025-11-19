"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pooleth.net
Prompt: Provide an example of using the Hatena Blog API to retrieve and display a list of popular articles based on user interactions.
Generated: DETERMINISTIC_19be90b07c374100
Batch ID: 20250612_155144
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://blog.hatena.ne.jp": {
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

class HatenaBlogAPI:
    BASE_URL = "https://blog.hatena.ne.jp"

    def __init__(self, blog_id):
        """
        Initializes the HatenaBlogAPI with the specified blog_id.

        :param blog_id: The ID of the Hatena blog.
        """
        self.blog_id = blog_id

    def get_popular_articles(self, count=5):
        """
        Retrieves a list of popular articles from the specified Hatena blog.

        :param count: Number of popular articles to retrieve (default is 5).
        :return: A list of popular articles.
        """
        url = f"{self.BASE_URL}/{self.blog_id}/atom/popular"
        params = {'count': count}
        
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()  # Raise an error for bad responses
        except requests.exceptions.RequestException as e:
            print(f"Error fetching popular articles: {e}")
            return []

        articles = self._parse_articles(response.content)
        return articles

    def _parse_articles(self, xml_content):
        """
        Parses the XML content to extract article information.

        :param xml_content: The XML response content from the API.
        :return: A list of dictionaries containing article details.
        """
        import xml.etree.ElementTree as ET

        articles = []
        try:
            root = ET.fromstring(xml_content)
            for entry in root.findall('.//entry'):
                title = entry.find('title').text
                link = entry.find('link').attrib['href']
                published = entry.find('published').text
                articles.append({
                    'title': title,
                    'link': link,
                    'published': published
                })
        except ET.ParseError as e:
            print(f"Error parsing XML content: {e}")

        return articles

def display_articles(articles):
    """
    Displays the list of articles.

    :param articles: A list of articles to display.
    """
    if not articles:
        print("No articles found.")
        return

    print("Popular Articles:")
    for article in articles:
        print(f"- {article['title']} (Published on: {article['published']})")
        print(f"  Link: {article['link']}\n")

if __name__ == "__main__":
    # Replace 'your_blog_id' with the actual blog ID
    blog_id = 'your_blog_id'
    api = HatenaBlogAPI(blog_id)
    
    # Fetch and display popular articles
    popular_articles = api.get_popular_articles(count=5)
    display_articles(popular_articles)
```
