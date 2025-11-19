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
  "https://blog.hatena.ne.jp/": {
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
    A class to interact with the Hatena Blog API for article management.
    """

    BASE_URL = "https://blog.hatena.ne.jp/"

    def __init__(self, blog_id, user_id, api_key):
        """
        Initializes the HatenaBlogAPI with the required credentials.

        :param blog_id: The unique identifier for the Hatena Blog.
        :param user_id: The user's Hatena account ID.
        :param api_key: The API key for authentication.
        """
        self.blog_id = blog_id
        self.user_id = user_id
        self.api_key = api_key

    def _make_request(self, endpoint, method='GET', data=None):
        """
        Makes a request to the Hatena Blog API.

        :param endpoint: The API endpoint to call.
        :param method: The HTTP method to use (GET or POST).
        :param data: The data to send with the request (for POST).
        :return: The response from the API.
        """
        url = f"{self.BASE_URL}{self.blog_id}/{endpoint}"
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json',
        }

        try:
            if method == 'GET':
                response = requests.get(url, headers=headers)
            elif method == 'POST':
                response = requests.post(url, headers=headers, json=data)
            else:
                raise ValueError("Unsupported HTTP method.")

            response.raise_for_status()  # Raise an error for bad status codes
            return response.json()
        
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None

    def get_articles(self):
        """
        Retrieves a list of articles from the blog.

        :return: A list of articles or None if an error occurred.
        """
        return self._make_request('atom.xml', method='GET')

    def create_article(self, title, content):
        """
        Creates a new article on the blog.

        :param title: The title of the article.
        :param content: The content of the article.
        :return: The created article's details or None if an error occurred.
        """
        data = {
            'entry': {
                'title': title,
                'content': {
                    'type': 'text/plain',
                    'body': content
                }
            }
        }
        return self._make_request('atom/entry', method='POST', data=data)

    def update_article(self, article_id, title, content):
        """
        Updates an existing article on the blog.

        :param article_id: The unique identifier for the article.
        :param title: The new title of the article.
        :param content: The new content of the article.
        :return: The updated article's details or None if an error occurred.
        """
        data = {
            'entry': {
                'id': article_id,
                'title': title,
                'content': {
                    'type': 'text/plain',
                    'body': content
                }
            }
        }
        return self._make_request(f'atom/entry/{article_id}', method='POST', data=data)

    def delete_article(self, article_id):
        """
        Deletes an article from the blog.

        :param article_id: The unique identifier for the article.
        :return: True if the deletion was successful, False otherwise.
        """
        response = self._make_request(f'atom/entry/{article_id}', method='DELETE')
        return response is not None

# Example usage:
if __name__ == "__main__":
    blog_id = "your_blog_id"
    user_id = "your_user_id"
    api_key = "your_api_key"

    hatena_blog = HatenaBlogAPI(blog_id, user_id, api_key)

    # Get articles
    articles = hatena_blog.get_articles()
    print(articles)

    # Create a new article
    new_article = hatena_blog.create_article("New Title", "This is the content of the article.")
    print(new_article)

    # Update an article
    updated_article = hatena_blog.update_article("article_id", "Updated Title", "Updated content.")
    print(updated_article)

    # Delete an article
    delete_status = hatena_blog.delete_article("article_id")
    print(f"Deletion successful: {delete_status}")
```
