"""
Generated Code Metadata:
========================
Original URL: https://wahedabdelmajed.com
Prompt: Generate a code snippet that implements a search function for articles on a personal website similar to Dr. Wahed Abdel Majid's, focusing on user queries about freedom and personal development.
Generated: DETERMINISTIC_a48954e6fdce3d1b
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
from typing import List, Dict

# Define a class to represent an Article
class Article:
    def __init__(self, title: str, content: str, tags: List[str]):
        """
        Initialize an Article object.

        :param title: Title of the article
        :param content: Content of the article
        :param tags: List of tags associated with the article
        """
        self.title = title
        self.content = content
        self.tags = tags

    def matches_query(self, query: str) -> bool:
        """
        Check if the article matches the search query.

        :param query: Search query string
        :return: True if the query matches the title, content, or tags; False otherwise
        """
        query_lower = query.lower()
        return (
            query_lower in self.title.lower() or
            query_lower in self.content.lower() or
            any(query_lower in tag.lower() for tag in self.tags)
        )

# Define a function to search articles
def search_articles(articles: List[Article], query: str) -> List[Dict[str, str]]:
    """
    Search for articles that match the given query.

    :param articles: List of Article objects
    :param query: Search query string
    :return: List of dictionaries containing matching articles' titles and excerpts
    """
    if not query:
        raise ValueError("Search query cannot be empty.")

    # Filter articles that match the query
    matching_articles = [
        {
            "title": article.title,
            "excerpt": article.content[:100] + "..."  # Provide a short excerpt of the content
        }
        for article in articles if article.matches_query(query)
    ]

    return matching_articles

# Example usage
if __name__ == "__main__":
    # Create a list of sample articles
    articles = [
        Article(
            title="The Path to Freedom",
            content="Freedom is the ability to make choices without external constraints...",
            tags=["freedom", "philosophy", "personal development"]
        ),
        Article(
            title="Personal Growth Strategies",
            content="Personal development involves setting goals, learning new skills, and overcoming challenges...",
            tags=["personal development", "self-help", "growth"]
        ),
        Article(
            title="Understanding Constraints",
            content="Constraints can limit freedom, but they can also inspire creativity...",
            tags=["freedom", "creativity", "philosophy"]
        ),
    ]

    # Perform a search
    try:
        query = "freedom"
        results = search_articles(articles, query)
        print("Search Results:")
        for result in results:
            print(f"Title: {result['title']}")
            print(f"Excerpt: {result['excerpt']}")
            print()
    except ValueError as e:
        print(f"Error: {e}")
```
