"""
Generated Code Metadata:
========================
Original URL: https://heartofjesuscollege.com
Prompt: "Create a virtual library system for a bilingual school, incorporating e-learning resources and interactive materials, similar to the one used at Heart of Jesus College."
Generated: DETERMINISTIC_00bc99dffbe58696
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Virtual Library System for a Bilingual School
This system allows users to manage books, e-learning resources, and interactive materials.
"""

import json
import os

class VirtualLibrary:
    def __init__(self, library_file="library.json"):
        """
        Initialize the virtual library system.
        :param library_file: Path to the JSON file where library data is stored.
        """
        self.library_file = library_file
        self.library_data = self.load_library()

    def load_library(self):
        """
        Load library data from a JSON file. If the file doesn't exist, initialize an empty library.
        :return: Dictionary containing library data.
        """
        if os.path.exists(self.library_file):
            try:
                with open(self.library_file, 'r') as file:
                    return json.load(file)
            except json.JSONDecodeError:
                print("Error: Library file is corrupted. Initializing empty library.")
                return {"books": [], "e_learning_resources": [], "interactive_materials": []}
        else:
            return {"books": [], "e_learning_resources": [], "interactive_materials": []}

    def save_library(self):
        """
        Save the current library data to a JSON file.
        """
        try:
            with open(self.library_file, 'w') as file:
                json.dump(self.library_data, file, indent=4)
        except Exception as e:
            print(f"Error: Unable to save library data. {e}")

    def add_item(self, category, title, language, description):
        """
        Add a new item to the library.
        :param category: Category of the item (books, e_learning_resources, interactive_materials).
        :param title: Title of the item.
        :param language: Language of the item (e.g., English, Spanish).
        :param description: Brief description of the item.
        """
        if category not in self.library_data:
            print("Error: Invalid category. Choose from 'books', 'e_learning_resources', or 'interactive_materials'.")
            return

        item = {
            "title": title,
            "language": language,
            "description": description
        }
        self.library_data[category].append(item)
        self.save_library()
        print(f"Item '{title}' added to {category}.")

    def search_items(self, category, language=None):
        """
        Search for items in a specific category, optionally filtered by language.
        :param category: Category to search in (books, e_learning_resources, interactive_materials).
        :param language: Language filter (optional).
        :return: List of matching items.
        """
        if category not in self.library_data:
            print("Error: Invalid category. Choose from 'books', 'e_learning_resources', or 'interactive_materials'.")
            return []

        results = [
            item for item in self.library_data[category]
            if language is None or item["language"].lower() == language.lower()
        ]
        return results

    def display_items(self, items):
        """
        Display a list of items in a readable format.
        :param items: List of items to display.
        """
        if not items:
            print("No items found.")
            return

        for idx, item in enumerate(items, start=1):
            print(f"{idx}. Title: {item['title']}")
            print(f"   Language: {item['language']}")
            print(f"   Description: {item['description']}")
            print()

    def delete_item(self, category, title):
        """
        Delete an item from the library by title.
        :param category: Category of the item (books, e_learning_resources, interactive_materials).
        :param title: Title of the item to delete.
        """
        if category not in self.library_data:
            print("Error: Invalid category. Choose from 'books', 'e_learning_resources', or 'interactive_materials'.")
            return

        for item in self.library_data[category]:
            if item["title"].lower() == title.lower():
                self.library_data[category].remove(item)
                self.save_library()
                print(f"Item '{title}' deleted from {category}.")
                return

        print(f"Error: Item '{title}' not found in {category}.")

# Example usage
if __name__ == "__main__":
    library = VirtualLibrary()

    # Add items
    library.add_item("books", "Learn Python", "English", "A comprehensive guide to Python programming.")
    library.add_item("e_learning_resources", "Math Interactive", "Spanish", "Interactive math exercises for students.")
    library.add_item("interactive_materials", "Science Lab", "English", "Virtual science experiments.")

    # Search and display items
    print("\nBooks in English:")
    books_in_english = library.search_items("books", language="English")
    library.display_items(books_in_english)

    print("\nAll e-learning resources:")
    all_e_learning = library.search_items("e_learning_resources")
    library.display_items(all_e_learning)

    # Delete an item
    library.delete_item("books", "Learn Python")
```
