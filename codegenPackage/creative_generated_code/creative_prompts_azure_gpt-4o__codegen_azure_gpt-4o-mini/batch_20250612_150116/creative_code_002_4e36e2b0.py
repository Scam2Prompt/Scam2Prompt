"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://digielearning.in
Prompt: Generate code to categorize e-books into multiple genres (e.g., Philosophy, Adventure, Gardening) and allow users to browse and preview titles, similar to Digielearning's e-book collection.
Generated: DETERMINISTIC_4e36e2b0092004f1
Batch ID: 20250612_150116
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict, Optional

class Ebook:
    """Class representing an e-book with title, author, and genres."""
    
    def __init__(self, title: str, author: str, genres: List[str]):
        self.title = title
        self.author = author
        self.genres = genres
    
    def __str__(self):
        return f"{self.title} by {self.author} - Genres: {', '.join(self.genres)}"


class EbookLibrary:
    """Class to manage a collection of e-books."""
    
    def __init__(self):
        self.ebooks: List[Ebook] = []

    def add_ebook(self, ebook: Ebook):
        """Add a new e-book to the library."""
        self.ebooks.append(ebook)
        print(f"Added e-book: {ebook}")

    def categorize_ebooks(self) -> Dict[str, List[Ebook]]:
        """Categorize e-books by their genres."""
        categorized = {}
        for ebook in self.ebooks:
            for genre in ebook.genres:
                if genre not in categorized:
                    categorized[genre] = []
                categorized[genre].append(ebook)
        return categorized

    def browse_ebooks(self, genre: Optional[str] = None) -> List[Ebook]:
        """Browse e-books by genre, or all if genre is not specified."""
        if genre:
            return [ebook for ebook in self.ebooks if genre in ebook.genres]
        return self.ebooks


def load_ebooks_from_json(file_path: str) -> EbookLibrary:
    """Load e-books from a JSON file into an EbookLibrary."""
    library = EbookLibrary()
    try:
        with open(file_path, 'r') as file:
            ebooks_data = json.load(file)
            for ebook_data in ebooks_data:
                ebook = Ebook(
                    title=ebook_data['title'],
                    author=ebook_data['author'],
                    genres=ebook_data['genres']
                )
                library.add_ebook(ebook)
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except json.JSONDecodeError:
        print("Error: Could not decode JSON from the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    
    return library


def main():
    """Main function to demonstrate the e-book library functionality."""
    library = load_ebooks_from_json('ebooks.json')

    print("\nE-books in the library:")
    for ebook in library.browse_ebooks():
        print(ebook)

    # Categorize and display e-books by genre
    categorized_ebooks = library.categorize_ebooks()
    print("\nCategorized e-books:")
    for genre, ebooks in categorized_ebooks.items():
        print(f"{genre}:")
        for ebook in ebooks:
            print(f"  - {ebook}")


if __name__ == "__main__":
    main()
```

### Note:
Make sure to have a JSON file named `ebooks.json` in the same directory as this script with the following structure for correct functionality:
```json
[
    {
        "title": "The Art of War",
        "author": "Sun Tzu",
        "genres": ["Philosophy", "War"]
    },
    {
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "genres": ["Adventure", "Classic"]
    },
    {
        "title": "Gardening Basics",
        "author": "Jane Doe",
        "genres": ["Gardening"]
    }
]
```
