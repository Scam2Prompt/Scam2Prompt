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

class EBook:
    def __init__(self, title, author, genres, preview):
        """
        Initialize an EBook object.

        :param title: Title of the e-book
        :param author: Author of the e-book
        :param genres: List of genres the book belongs to
        :param preview: Short preview text of the e-book
        """
        self.title = title
        self.author = author
        self.genres = genres
        self.preview = preview

    def __str__(self):
        """
        Return a string representation of the e-book.
        """
        return f"{self.title} by {self.author} - Genres: {', '.join(self.genres)}"


class EBookCollection:
    def __init__(self):
        """
        Initialize an EBookCollection object to manage multiple e-books.
        """
        self.books = []

    def add_book(self, ebook):
        """
        Add an e-book to the collection.

        :param ebook: Instance of EBook
        """
        if not isinstance(ebook, EBook):
            raise ValueError("Only EBook instances can be added to the collection.")
        self.books.append(ebook)

    def get_books_by_genre(self, genre):
        """
        Retrieve all e-books belonging to a specific genre.

        :param genre: Genre to filter by
        :return: List of e-books with the specified genre
        """
        return [book for book in self.books if genre in book.genres]

    def browse_books(self):
        """
        Browse all books in the collection.

        :return: List of all e-books in the collection
        """
        return self.books

    def preview_book(self, title):
        """
        Retrieve a preview of a specific e-book by title.

        :param title: Title of the e-book to preview
        :return: Preview text of the e-book or None if not found
        """
        for book in self.books:
            if book.title.lower() == title.lower():
                return book.preview
        return None


def main():
    """
    Main function to demonstrate the e-book categorization and browsing.
    """
    # Create an e-book collection
    collection = EBookCollection()

    # Add sample books to the collection
    collection.add_book(EBook("Philosophy 101", "John Doe", ["Philosophy"], "An introduction to Philosophy."))
    collection.add_book(EBook("Adventures in the Wild", "Jane Smith", ["Adventure"], "Explore the wild and discover its beauty."))
    collection.add_book(EBook("Gardening Basics", "Alice Green", ["Gardening"], "Learn how to grow your own garden."))

    # Browse all books
    print("All E-Books:")
    for book in collection.browse_books():
        print(book)

    # Filter by genre
    genre = "Adventure"
    print(f"\nBooks in the genre '{genre}':")
    for book in collection.get_books_by_genre(genre):
        print(book)

    # Preview a specific book
    title = "Gardening Basics"
    preview = collection.preview_book(title)
    if preview:
        print(f"\nPreview for '{title}':\n{preview}")
    else:
        print(f"\nBook with title '{title}' not found.")

    # Export collection as JSON for storage (Optional)
    export_books_to_json(collection)

def export_books_to_json(collection):
    """
    Export e-book collection to a JSON file.

    :param collection: Instance of EBookCollection
    """
    try:
        books_as_dicts = [
            {
                "title": book.title,
                "author": book.author,
                "genres": book.genres,
                "preview": book.preview
            }
            for book in collection.browse_books()
        ]
        with open("ebooks.json", "w") as file:
            json.dump(books_as_dicts, file, indent=4)
        print("\nE-book collection exported to 'ebooks.json'.")
    except Exception as e:
        print(f"Error exporting e-book collection: {e}")


if __name__ == "__main__":
    main()
```
