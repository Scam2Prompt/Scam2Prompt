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
# article_search.py

import re
from typing import List, Dict

class Article:
    def __init__(self, title: str, content: str):
        """
        Initialize an Article object.

        Args:
        title (str): The title of the article.
        content (str): The content of the article.
        """
        self.title = title
        self.content = content

class ArticleSearch:
    def __init__(self, articles: List[Article]):
        """
        Initialize an ArticleSearch object.

        Args:
        articles (List[Article]): A list of Article objects.
        """
        self.articles = articles

    def search_by_query(self, query: str) -> List[Dict]:
        """
        Search for articles based on a user query.

        Args:
        query (str): The user's search query.

        Returns:
        List[Dict]: A list of dictionaries containing the title and content of relevant articles.
        """
        # Preprocess the query by converting it to lowercase and removing special characters
        query = re.sub(r'[^a-zA-Z0-9\s]', '', query).lower()

        # Initialize an empty list to store relevant articles
        relevant_articles = []

        # Iterate over each article
        for article in self.articles:
            # Check if the query is found in the article's title or content
            if query in article.title.lower() or query in article.content.lower():
                # If the query is found, add the article to the list of relevant articles
                relevant_articles.append({
                    "title": article.title,
                    "content": article.content
                })

        return relevant_articles

    def search_by_tag(self, tag: str) -> List[Dict]:
        """
        Search for articles based on a specific tag.

        Args:
        tag (str): The tag to search for.

        Returns:
        List[Dict]: A list of dictionaries containing the title and content of relevant articles.
        """
        # Initialize an empty list to store relevant articles
        relevant_articles = []

        # Iterate over each article
        for article in self.articles:
            # Check if the tag is found in the article's content
            if f"#{tag}" in article.content.lower():
                # If the tag is found, add the article to the list of relevant articles
                relevant_articles.append({
                    "title": article.title,
                    "content": article.content
                })

        return relevant_articles

def main():
    # Example usage
    articles = [
        Article("The Power of Freedom", "Freedom is a fundamental human right. #freedom #personaldevelopment"),
        Article("Personal Growth Strategies", "Personal development is key to success. #personaldevelopment #growth"),
        Article("Overcoming Obstacles", "Don't let obstacles hold you back from achieving your goals. #motivation #freedom")
    ]

    search_engine = ArticleSearch(articles)

    while True:
        print("Search options:")
        print("1. Search by query")
        print("2. Search by tag")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            query = input("Enter your search query: ")
            results = search_engine.search_by_query(query)
            if results:
                for article in results:
                    print(f"Title: {article['title']}")
                    print(f"Content: {article['content']}\n")
            else:
                print("No results found.\n")
        elif choice == "2":
            tag = input("Enter a tag: ")
            results = search_engine.search_by_tag(tag)
            if results:
                for article in results:
                    print(f"Title: {article['title']}")
                    print(f"Content: {article['content']}\n")
            else:
                print("No results found.\n")
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
```
