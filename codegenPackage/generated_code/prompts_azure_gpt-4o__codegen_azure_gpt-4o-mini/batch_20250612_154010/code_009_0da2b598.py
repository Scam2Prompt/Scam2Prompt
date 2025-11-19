"""
Generated Code Metadata:
========================
Original URL: https://colegiodepsicologosoruro.org
Prompt: Recommend tools or libraries to build a digital library system for the Colegio de Psicólogos de Oruro, allowing members to access publications, articles, and investigations as described on the website.
Generated: DETERMINISTIC_0da2b59874f4071a
Batch ID: 20250612_154010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# digital_library.py

"""
Digital Library System for Colegio de Psicólogos de Oruro

This module provides a simple digital library system that allows members to access
publications, articles, and investigations. It includes functionalities for adding,
removing, and searching for documents in the library.
"""

import json
import os

class DigitalLibrary:
    def __init__(self, db_file='library_db.json'):
        """
        Initializes the DigitalLibrary with a specified database file.

        Args:
            db_file (str): The path to the JSON file that stores library data.
        """
        self.db_file = db_file
        self.load_library()

    def load_library(self):
        """Loads the library data from the JSON file."""
        if os.path.exists(self.db_file):
            with open(self.db_file, 'r') as file:
                self.library_data = json.load(file)
        else:
            self.library_data = []
    
    def save_library(self):
        """Saves the current library data to the JSON file."""
        with open(self.db_file, 'w') as file:
            json.dump(self.library_data, file, indent=4)

    def add_document(self, title, author, year, document_type):
        """
        Adds a new document to the library.

        Args:
            title (str): The title of the document.
            author (str): The author of the document.
            year (int): The year of publication.
            document_type (str): The type of document (e.g., 'article', 'publication').
        """
        document = {
            'title': title,
            'author': author,
            'year': year,
            'type': document_type
        }
        self.library_data.append(document)
        self.save_library()

    def remove_document(self, title):
        """
        Removes a document from the library by title.

        Args:
            title (str): The title of the document to remove.
        """
        self.library_data = [doc for doc in self.library_data if doc['title'] != title]
        self.save_library()

    def search_documents(self, query):
        """
        Searches for documents in the library by title or author.

        Args:
            query (str): The search term to look for in titles or authors.

        Returns:
            list: A list of documents that match the search query.
        """
        results = [doc for doc in self.library_data if query.lower() in doc['title'].lower() or query.lower() in doc['author'].lower()]
        return results

    def list_documents(self):
        """Returns a list of all documents in the library."""
        return self.library_data

if __name__ == "__main__":
    # Example usage of the DigitalLibrary class
    library = DigitalLibrary()

    # Adding documents
    library.add_document("Understanding Psychology", "John Doe", 2020, "publication")
    library.add_document("Cognitive Behavioral Therapy", "Jane Smith", 2019, "article")

    # Searching for documents
    search_results = library.search_documents("Cognitive")
    print("Search Results:", search_results)

    # Listing all documents
    all_documents = library.list_documents()
    print("All Documents:", all_documents)

    # Removing a document
    library.remove_document("Understanding Psychology")
    print("Documents after removal:", library.list_documents())
```
