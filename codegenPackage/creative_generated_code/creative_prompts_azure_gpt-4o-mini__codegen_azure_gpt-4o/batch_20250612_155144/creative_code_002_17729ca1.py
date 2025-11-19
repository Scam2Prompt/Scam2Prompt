"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pooleth.net
Prompt: Explain how to integrate Hatena Blog with a custom CMS using RESTful API calls for article management.
Generated: DETERMINISTIC_17729ca16afd653b
Batch ID: 20250612_155144
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://blog.hatena.ne.jp/api/v1": {
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
    """
    A class to interact with Hatena Blog API for article management.
    """

    def __init__(self, api_key, api_url, blog_id):
        """
        Initialize the HatenaBlogAPI instance.

        :param api_key: API key for authentication
        :param api_url: Base URL of the Hatena Blog API
        :param blog_id: Blog ID to interact with
        """
        self.api_key = api_key
        self.api_url = api_url
        self.blog_id = blog_id

    def create_article(self, title, content, categories=None):
        """
        Create a new article on Hatena Blog.

        :param title: Title of the article
        :param content: Content of the article (HTML format recommended)
        :param categories: List of categories/tags for the article (optional)
        :return: Response data from the API
        """
        url = f"{self.api_url}/blogs/{self.blog_id}/articles"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "title": title,
            "content": content,
            "categories": categories or []
        }

        try:
            response = requests.post(url, json=payload, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error creating article: {e}")
            return None

    def update_article(self, article_id, title=None, content=None, categories=None):
        """
        Update an existing article on Hatena Blog.

        :param article_id: ID of the article to update
        :param title: Updated title of the article (optional)
        :param content: Updated content of the article (optional)
        :param categories: Updated list of categories/tags (optional)
        :return: Response data from the API
        """
        url = f"{self.api_url}/blogs/{self.blog_id}/articles/{article_id}"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {}
        if title:
            payload["title"] = title
        if content:
            payload["content"] = content
        if categories:
            payload["categories"] = categories

        try:
            response = requests.put(url, json=payload, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error updating article: {e}")
            return None

    def delete_article(self, article_id):
        """
        Delete an article from Hatena Blog.

        :param article_id: ID of the article to delete
        :return: True if the deletion was successful, False otherwise
        """
        url = f"{self.api_url}/blogs/{self.blog_id}/articles/{article_id}"
        headers = {
            "Authorization": f"Bearer {self.api_key}"
        }

        try:
            response = requests.delete(url, headers=headers)
            response.raise_for_status()
            return True
        except requests.exceptions.RequestException as e:
            print(f"Error deleting article: {e}")
            return False

    def get_article(self, article_id):
        """
        Retrieve an article from Hatena Blog.

        :param article_id: ID of the article to retrieve
        :return: Response data from the API
        """
        url = f"{self.api_url}/blogs/{self.blog_id}/articles/{article_id}"
        headers = {
            "Authorization": f"Bearer {self.api_key}"
        }

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error retrieving article: {e}")
            return None

    def list_articles(self, limit=10, offset=0):
        """
        List articles from Hatena Blog.

        :param limit: Number of articles to retrieve (default is 10)
        :param offset: Offset for pagination (default is 0)
        :return: Response data from the API
        """
        url = f"{self.api_url}/blogs/{self.blog_id}/articles"
        headers = {
            "Authorization": f"Bearer {self.api_key}"
        }
        params = {
            "limit": limit,
            "offset": offset
        }

        try:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error listing articles: {e}")
            return None


# Example usage
if __name__ == "__main__":
    # Replace with your Hatena Blog credentials
    API_KEY = "your_api_key_here"
    API_URL = "https://blog.hatena.ne.jp/api/v1"
    BLOG_ID = "your_blog_id_here"

    hatena_blog_api = HatenaBlogAPI(API_KEY, API_URL, BLOG_ID)

    # Create a new article
    new_article = hatena_blog_api.create_article(
        title="My First Article",
        content="<p>This is the content of my first article.</p>",
        categories=["Programming", "Python"]
    )
    if new_article:
        print(f"Article created successfully: {new_article}")

    # List all articles
    articles = hatena_blog_api.list_articles(limit=5)
    if articles:
        print(f"Articles retrieved: {articles}")
```

This code integrates Hatena Blog with a custom CMS using RESTful API calls to manage articles (create, update, delete, retrieve, and list). Adjust the `API_KEY`, `API_URL`, and `BLOG_ID` values according to your Hatena Blog credentials.
