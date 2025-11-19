"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wahedabdelmajed.com
Prompt: Generate a code snippet that implements a search function for articles on a personal website similar to Dr. Wahed Abdel Majid's, focusing on user queries about freedom and personal development.
Generated: DETERMINISTIC_a48954e6fdce3d1b
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

class Article:
    """
    Represents an Article with a title and content.
    """
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content

class ArticleSearchEngine:
    """
    Search engine for querying articles based on user input.
    """
    def __init__(self, articles: list[Article]):
        self.articles = articles

    def search(self, query: str) -> list[Article]:
        """
        Searches for articles that match the query in their title or content.

        Args:
            query (str): The search query.

        Returns:
            list[Article]: List of articles matching the query.
        """
        if not query:
            raise ValueError("Query cannot be empty.")
        
        # Normalize query by stripping whitespace and converting to lowercase
        normalized_query = query.strip().lower()
        
        # Compile regex for partial word matches (case-insensitive)
        query_regex = re.compile(r'\b' + re.escape(normalized_query) + r'\b', re.IGNORECASE)
        
        # Filter articles based on regex match in title or content
        matching_articles = [
            article for article in self.articles
            if query_regex.search(article.title) or query_regex.search(article.content)
        ]
        
        return matching_articles

# Example usage
if __name__ == "__main__":
    # Articles on the website
    articles = [
        Article("The Essence of Freedom", "Freedom is a core aspect of human life."),
        Article("Personal Development Tips", "Steps to improve yourself and achieve your goals."),
        Article("Exploring the Concept of Freedom", "Philosophical insights into freedom."),
        Article("Daily Habits for Growth", "Develop habits that foster personal development."),
    ]

    # Instantiate search engine
    search_engine = ArticleSearchEngine(articles)

    # Ask user for search query
    try:
        user_query = input("Enter your search query: ").strip()
        results = search_engine.search(user_query)
        
        if results:
            print(f"\nFound {len(results)} article(s) related to '{user_query}':")
            for i, article in enumerate(results, 1):
                print(f"{i}. {article.title}")
        else:
            print(f"\nNo articles found for query: '{user_query}'")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
