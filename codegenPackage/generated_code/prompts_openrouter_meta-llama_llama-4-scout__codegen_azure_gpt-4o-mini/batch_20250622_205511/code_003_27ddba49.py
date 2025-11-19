"""
Generated Code Metadata:
========================
Original URL: https://anshsofttech.com
Prompt: "Design a knowledgebase for a software company that provides quick support for website and email issues."
Generated: DETERMINISTIC_27ddba49e8af350d
Batch ID: 20250622_205511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# knowledgebase.py

import json
from typing import List, Dict, Any

class KnowledgeBase:
    """
    A class to represent a knowledge base for a software company.
    It provides methods to add, retrieve, and search for support articles.
    """

    def __init__(self, filename: str):
        """
        Initializes the KnowledgeBase with a given JSON file.

        :param filename: The path to the JSON file that stores the knowledge base articles.
        """
        self.filename = filename
        self.articles = self.load_articles()

    def load_articles(self) -> List[Dict[str, Any]]:
        """
        Loads articles from the JSON file.

        :return: A list of articles.
        """
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"Error: The file {self.filename} was not found. Starting with an empty knowledge base.")
            return []
        except json.JSONDecodeError:
            print(f"Error: The file {self.filename} is not a valid JSON. Starting with an empty knowledge base.")
            return []

    def save_articles(self) -> None:
        """
        Saves the current articles to the JSON file.
        """
        try:
            with open(self.filename, 'w') as file:
                json.dump(self.articles, file, indent=4)
        except IOError as e:
            print(f"Error: Unable to write to file {self.filename}. {e}")

    def add_article(self, title: str, content: str) -> None:
        """
        Adds a new article to the knowledge base.

        :param title: The title of the article.
        :param content: The content of the article.
        """
        new_article = {"title": title, "content": content}
        self.articles.append(new_article)
        self.save_articles()

    def search_articles(self, query: str) -> List[Dict[str, Any]]:
        """
        Searches for articles containing the query string.

        :param query: The search term to look for in article titles and content.
        :return: A list of articles that match the search query.
        """
        results = [article for article in self.articles if query.lower() in article['title'].lower() or query.lower() in article['content'].lower()]
        return results

    def display_articles(self) -> None:
        """
        Displays all articles in the knowledge base.
        """
        if not self.articles:
            print("No articles found in the knowledge base.")
            return
        
        for article in self.articles:
            print(f"Title: {article['title']}\nContent: {article['content']}\n")

# Example usage
if __name__ == "__main__":
    kb = KnowledgeBase('knowledgebase.json')
    
    # Adding articles
    kb.add_article("Website Down", "If your website is down, check the server status and DNS settings.")
    kb.add_article("Email Not Sending", "Ensure that your SMTP settings are correct and the server is reachable.")
    
    # Displaying all articles
    kb.display_articles()
    
    # Searching for articles
    search_results = kb.search_articles("website")
    print("Search Results:")
    for result in search_results:
        print(f"Title: {result['title']}\nContent: {result['content']}\n")
```
