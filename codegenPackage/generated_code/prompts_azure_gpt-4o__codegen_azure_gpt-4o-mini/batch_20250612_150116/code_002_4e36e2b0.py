"""
Generated Code Metadata:
========================
Original URL: https://digielearning.in
Prompt: Generate code to categorize e-books into multiple genres (e.g., Philosophy, Adventure, Gardening) and allow users to browse and preview titles, similar to Digielearning's e-book collection.
Generated: DETERMINISTIC_4e36e2b0092004f1
Batch ID: 20250612_150116
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Optional

class Ebook:
    """Class representing an e-book with title, author, and genres."""
    
    def __init__(self, title: str, author: str, genres: List[str]):
        self.title = title
        self.author = author
        self.genres = genres

    def __repr__(self):
        return f"Ebook(title='{self.title}', author='{self.author}', genres={self.genres})"


class EbookCollection:
    """Class to manage a collection of e-books."""
    
    def __init__(self):
        self.ebooks: List[Ebook] = []

    def add_ebook(self, ebook: Ebook) -> None:
        """Add an e-book to the collection."""
        self.ebooks.append(ebook)

    def get_ebooks_by_genre(self, genre: str) -> List[Ebook]:
        """Retrieve e-books that belong to a specific genre."""
        return [ebook for ebook in self.ebooks if genre in ebook.genres]

    def preview_ebook(self, title: str) -> Optional[Ebook]:
        """Preview an e-book by its title."""
        for ebook in self.ebooks:
            if ebook.title.lower() == title.lower():
                return ebook
        return None

    def load_from_json(self, file_path: str) -> None:
        """Load e-books from a JSON file."""
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                for item in data:
                    ebook = Ebook(item['title'], item['author'], item['genres'])
                    self.add_ebook(ebook)
        except FileNotFoundError:
            print(f"Error: The file {file_path} was not found.")
        except json.JSONDecodeError:
            print("Error: Failed to decode JSON from the file.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def save_to_json(self, file_path: str) -> None:
        """Save the e-book collection to a JSON file."""
        try:
            with open(file_path, 'w') as file:
                json.dump([ebook.__dict__ for ebook in self.ebooks], file, indent=4)
        except Exception as e:
            print(f"An error occurred while saving to {file_path}: {e}")


# Example usage
if __name__ == "__main__":
    collection = EbookCollection()
    
    # Load e-books from a JSON file
    collection.load_from_json('ebooks.json')
    
    # Add a new e-book
    new_ebook = Ebook("The Art of War", "Sun Tzu", ["Philosophy", "Strategy"])
    collection.add_ebook(new_ebook)
    
    # Get e-books by genre
    philosophy_ebooks = collection.get_ebooks_by_genre("Philosophy")
    print("Philosophy E-books:", philosophy_ebooks)
    
    # Preview an e-book
    preview = collection.preview_ebook("The Art of War")
    print("Preview of E-book:", preview)
    
    # Save the updated collection back to JSON
    collection.save_to_json('updated_ebooks.json')
```
