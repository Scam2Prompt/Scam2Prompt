"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://traceybaptiste.com
Prompt: Write a Python script that retrieves and displays information about the books authored by Tracey Baptiste, including "Moko Magic: Carnival Chaos" and "Boy 2.0", using a fictional API for book data.
Generated: DETERMINISTIC_2f22ba9fa692db03
Batch ID: 20250612_163526
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.fictionalbookdata.com/books": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests

class Book:
    """Class to represent a book with title and author."""

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f'"{self.title}" by {self.author}'


class BookAPI:
    """Class to interact with a fictional book API."""

    BASE_URL = "https://api.fictionalbookdata.com/books"

    @staticmethod
    def fetch_books_by_author(author_name):
        """
        Fetch books authored by a specific author from the fictional API.

        :param author_name: Name of the author to search for.
        :return: A list of Book objects.
        """
        try:
            response = requests.get(f"{BookAPI.BASE_URL}?author={author_name}")
            response.raise_for_status()  # Raise an exception for HTTP errors

            # Assuming the API returns a JSON response with a list of books
            books_data = response.json()
            books = [Book(book['title'], book['author']) for book in books_data]

            return books
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data from API: {e}")
            return []

def display_books(books):
    """
    Display a list of books in a readable format.

    :param books: A list of Book objects.
    """
    if not books:
        print("No books found.")
        return

    print("Books authored by Tracey Baptiste:")
    for book in books:
        print(book)

def main():
    """Main function to execute the script."""
    author_name = "Tracey Baptiste"
    books = BookAPI.fetch_books_by_author(author_name)
    display_books(books)

if __name__ == "__main__":
    main()
```
