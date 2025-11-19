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
  "https://fictional-book-api.com/books": {
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

def fetch_books_by_author(author_name):
    """
    Fetches book information for a given author using a fictional API.

    :param author_name: Name of the author whose books are to be retrieved.
    :return: List of books authored by the given author, or an error message if the request fails.
    """
    # Fictional API endpoint for book data
    api_url = "https://fictional-book-api.com/books"
    try:
        # Make a GET request to the API
        response = requests.get(api_url, params={"author": author_name}, timeout=10)
        response.raise_for_status()  # Raise HTTPError if the response has a failed status code

        # Parse the response JSON
        data = response.json()

        # Check if books are returned
        if not data.get("books"):
            return f"No books found for author: {author_name}"

        # Return list of books
        return data["books"]

    except requests.exceptions.RequestException as e:
        # Handle API request exceptions
        return f"Error fetching books: {str(e)}"


def display_book_info(books):
    """
    Displays information about books in a user-friendly format.

    :param books: List of book dictionaries containing book details.
    """
    print("Books authored by Tracey Baptiste:")
    print("-" * 40)  # Divider line
    for book in books:
        # Extract book details with default fallback values
        title = book.get("title", "Unknown Title")
        genre = book.get("genre", "Unknown Genre")
        publication_year = book.get("publication_year", "Unknown Year")
        description = book.get("description", "No description available.")
        
        # Display book information
        print(f"Title: {title}")
        print(f"Genre: {genre}")
        print(f"Publication Year: {publication_year}")
        print(f"Description: {description}")
        print("-" * 40)  # Divider line


def main():
    """
    Main function to retrieve and display books authored by Tracey Baptiste.
    """
    author_name = "Tracey Baptiste"

    # Fetch books from the API
    books_or_error = fetch_books_by_author(author_name)

    # Check if the result is an error message or book list
    if isinstance(books_or_error, str):
        print(books_or_error)  # Print the error message
    else:
        # Display book information
        display_book_info(books_or_error)


if __name__ == "__main__":
    main()
```
