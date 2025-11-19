"""
Generated Code Metadata:
========================
Original URL: https://saketprakashan.in
Prompt: "Generate a list of Marathi book categories and subcategories inspired by Saket Prakashan's book catalog."
Generated: DETERMINISTIC_ebf2d97b1246adae
Batch ID: 20250622_212908
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class BookCategory:
    """
    A class to represent a book category with its subcategories.
    """

    def __init__(self, name):
        """
        Initializes a new book category.

        :param name: The name of the category.
        """
        self.name = name
        self.subcategories = []

    def add_subcategory(self, subcategory):
        """
        Adds a subcategory to the category.

        :param subcategory: The name of the subcategory to add.
        """
        self.subcategories.append(subcategory)

    def to_dict(self):
        """
        Converts the category and its subcategories to a dictionary.

        :return: A dictionary representation of the category.
        """
        return {
            'category': self.name,
            'subcategories': self.subcategories
        }


def generate_book_categories():
    """
    Generates a list of Marathi book categories and subcategories.

    :return: A list of dictionaries representing book categories and their subcategories.
    """
    try:
        categories = []

        # Fiction Category
        fiction = BookCategory("कथा")
        fiction.add_subcategory("कथा संग्रह")
        fiction.add_subcategory("उपन्यास")
        fiction.add_subcategory("कविता")
        categories.append(fiction.to_dict())

        # Non-Fiction Category
        non_fiction = BookCategory("अकादमिक")
        non_fiction.add_subcategory("शिक्षण")
        non_fiction.add_subcategory("इतिहास")
        non_fiction.add_subcategory("जीवशास्त्र")
        categories.append(non_fiction.to_dict())

        # Children's Books Category
        children_books = BookCategory("बालसाहित्य")
        children_books.add_subcategory("कथा")
        children_books.add_subcategory("कविता")
        children_books.add_subcategory("शिक्षणात्मक")
        categories.append(children_books.to_dict())

        # Self-Help Category
        self_help = BookCategory("स्व-सहायता")
        self_help.add_subcategory("व्यक्तिमत्व विकास")
        self_help.add_subcategory("आर्थिक शिक्षण")
        categories.append(self_help.to_dict())

        return categories

    except Exception as e:
        print(f"An error occurred while generating book categories: {e}")
        return []


def save_categories_to_file(categories, filename='book_categories.json'):
    """
    Saves the list of book categories to a JSON file.

    :param categories: The list of book categories to save.
    :param filename: The name of the file to save the categories to.
    """
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(categories, file, ensure_ascii=False, indent=4)
        print(f"Categories successfully saved to {filename}.")
    except IOError as e:
        print(f"An error occurred while saving to file: {e}")


if __name__ == "__main__":
    # Generate book categories
    book_categories = generate_book_categories()

    # Save categories to a JSON file
    save_categories_to_file(book_categories)
```
