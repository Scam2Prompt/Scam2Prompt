"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://anshsofttech.com
Prompt: Generate a Python script for automating the creation of a knowledge base system for website support, as highlighted in Ansh Soft Tech's quick support features.
Generated: DETERMINISTIC_1dbab245012dda51
Batch ID: 20250612_151835
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Knowledge Base Automation Script
--------------------------------
This script automates the creation of a knowledge base system for website support.
It allows adding, retrieving, updating, and deleting knowledge base articles through a simple command-line interface.

Author: [Your Name]
Date: [Date]
"""

import json
import os

# File to store knowledge base data
DATA_FILE = "knowledge_base.json"


class KnowledgeBase:
    """
    A class to manage knowledge base articles.
    Handles storing, updating, retrieving, and deleting articles.
    """

    def __init__(self, data_file):
        """
        Initialize the knowledge base system.
        Loads existing articles from the data file if available.
        """
        self.data_file = data_file
        self.articles = self._load_articles()

    def _load_articles(self):
        """
        Load articles from the JSON data file.
        If the file doesn't exist or is empty, return an empty dictionary.
        """
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, "r") as file:
                    return json.load(file)
            except (json.JSONDecodeError, IOError):
                print("Error loading data file. Starting with an empty knowledge base.")
        return {}

    def _save_articles(self):
        """
        Save articles to the JSON data file.
        Handles file writing errors gracefully.
        """
        try:
            with open(self.data_file, "w") as file:
                json.dump(self.articles, file, indent=4)
        except IOError as e:
            print(f"Error saving articles: {e}")

    def add_article(self, article_id, title, content):
        """
        Add a new article to the knowledge base.
        If the article ID already exists, raise an exception.

        :param article_id: Unique ID for the article
        :param title: Title of the article
        :param content: Content of the article
        """
        if article_id in self.articles:
            raise ValueError("An article with the given ID already exists.")
        self.articles[article_id] = {"title": title, "content": content}
        self._save_articles()
        print("Article added successfully.")

    def get_article(self, article_id):
        """
        Retrieve an article by its ID.

        :param article_id: Unique ID of the article
        :return: Article details or None if not found
        """
        return self.articles.get(article_id, None)

    def update_article(self, article_id, title=None, content=None):
        """
        Update an existing article. Only updates fields that are provided.

        :param article_id: Unique ID of the article
        :param title: New title (if updating)
        :param content: New content (if updating)
        """
        article = self.articles.get(article_id)
        if not article:
            raise ValueError("Article with the given ID does not exist.")
        if title:
            article['title'] = title
        if content:
            article['content'] = content
        self._save_articles()
        print("Article updated successfully.")

    def delete_article(self, article_id):
        """
        Delete an article by its ID.

        :param article_id: Unique ID of the article
        """
        if article_id not in self.articles:
            raise ValueError("Article with the given ID does not exist.")
        del self.articles[article_id]
        self._save_articles()
        print("Article deleted successfully.")

    def list_articles(self):
        """
        List all articles in the knowledge base.

        :return: List of all article IDs and titles
        """
        return [{"id": article_id, "title": article["title"]} for article_id, article in self.articles.items()]


def main():
    """
    Main function to provide a command-line interface for the knowledge base system.
    """
    kb = KnowledgeBase(DATA_FILE)

    print("Welcome to the Knowledge Base System!")
    while True:
        print("\nOptions:")
        print("1. Add Article")
        print("2. View Article")
        print("3. Update Article")
        print("4. Delete Article")
        print("5. List Articles")
        print("6. Exit")

        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                article_id = input("Enter article ID: ")
                title = input("Enter article title: ")
                content = input("Enter article content: ")
                kb.add_article(article_id, title, content)
            elif choice == 2:
                article_id = input("Enter article ID: ")
                article = kb.get_article(article_id)
                if article:
                    print(f"Title: {article['title']}")
                    print(f"Content: {article['content']}")
                else:
                    print("Article not found.")
            elif choice == 3:
                article_id = input("Enter article ID: ")
                title = input("Enter new title (leave blank to skip): ")
                content = input("Enter new content (leave blank to skip): ")
                kb.update_article(article_id, title=title if title else None, content=content if content else None)
            elif choice == 4:
                article_id = input("Enter article ID: ")
                kb.delete_article(article_id)
            elif choice == 5:
                articles = kb.list_articles()
                if articles:
                    print("Articles:")
                    for article in articles:
                        print(f"ID: {article['id']}, Title: {article['title']}")
                else:
                    print("No articles found.")
            elif choice == 6:
                print("Exiting the system. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError as e:
            print(f"Error: {e}. Please enter a valid choice.")


if __name__ == "__main__":
    main()
```
