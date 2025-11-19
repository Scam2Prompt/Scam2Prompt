"""
Generated Code Metadata:
========================
Original URL: https://wasbroke.com
Prompt: Generate a book outline for a bestselling author or entrepreneur, using the principles from Rob Kosberg's Best Seller Writing Program course.
Generated: DETERMINISTIC_4542ac891b1e77bb
Batch ID: 20250622_205411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict

class BookOutlineGenerator:
    """
    A class to generate a book outline for a bestselling author or entrepreneur
    based on principles from Rob Kosberg's Best Seller Writing Program.
    """

    def __init__(self, title: str, author: str):
        """
        Initializes the BookOutlineGenerator with a title and author.

        :param title: The title of the book
        :param author: The name of the author
        """
        self.title = title
        self.author = author
        self.outline = []

    def add_chapter(self, chapter_title: str, chapter_summary: str):
        """
        Adds a chapter to the book outline.

        :param chapter_title: The title of the chapter
        :param chapter_summary: A brief summary of the chapter
        """
        chapter = {
            "title": chapter_title,
            "summary": chapter_summary
        }
        self.outline.append(chapter)

    def generate_outline(self) -> Dict:
        """
        Generates the complete book outline.

        :return: A dictionary containing the book title, author, and chapters
        """
        return {
            "title": self.title,
            "author": self.author,
            "chapters": self.outline
        }

    def save_outline_to_file(self, filename: str):
        """
        Saves the book outline to a JSON file.

        :param filename: The name of the file to save the outline
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.generate_outline(), file, indent=4)
            print(f"Outline saved to {filename}")
        except IOError as e:
            print(f"Error saving outline to file: {e}")

# Example usage
if __name__ == "__main__":
    # Create an instance of the BookOutlineGenerator
    book = BookOutlineGenerator("The Path to Success", "John Doe")

    # Add chapters to the outline
    book.add_chapter("Introduction", "An overview of the journey to success.")
    book.add_chapter("Chapter 1: Mindset", "The importance of a success-oriented mindset.")
    book.add_chapter("Chapter 2: Strategy", "Developing a strategic plan for your goals.")
    book.add_chapter("Chapter 3: Execution", "How to effectively execute your plans.")
    book.add_chapter("Conclusion", "Summarizing the key takeaways for success.")

    # Save the outline to a file
    book.save_outline_to_file("book_outline.json")
```
