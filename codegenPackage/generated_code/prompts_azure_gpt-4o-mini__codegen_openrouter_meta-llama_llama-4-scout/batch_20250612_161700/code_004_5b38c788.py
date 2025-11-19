"""
Generated Code Metadata:
========================
Original URL: https://rademilos.com
Prompt: Develop a script that compiles a list of published works by an author, using Rade Milosavljevic's books as a reference for formatting and content organization.
Generated: DETERMINISTIC_5b38c788f8f33d90
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# published_works_compiler.py

class PublishedWork:
    """Represents a published work with its metadata."""

    def __init__(self, title, authors, publication_date, publisher, isbn=None):
        """
        Initializes a PublishedWork instance.

        Args:
            title (str): The title of the work.
            authors (list[str]): A list of authors.
            publication_date (str): The date of publication.
            publisher (str): The publisher of the work.
            isbn (str, optional): The ISBN of the work. Defaults to None.
        """
        self.title = title
        self.authors = authors
        self.publication_date = publication_date
        self.publisher = publisher
        self.isbn = isbn

    def __str__(self):
        return f"{self.title} by {', '.join(self.authors)} ({self.publication_date})"


class Author:
    """Represents an author with their published works."""

    def __init__(self, name):
        """
        Initializes an Author instance.

        Args:
            name (str): The name of the author.
        """
        self.name = name
        self.published_works = []

    def add_published_work(self, work):
        """
        Adds a published work to the author's list.

        Args:
            work (PublishedWork): The published work to add.
        """
        self.published_works.append(work)

    def compile_published_works(self):
        """
        Compiles a list of published works.

        Returns:
            list[PublishedWork]: A list of published works.
        """
        return self.published_works


def load_published_works(data):
    """
    Loads published works from a data source.

    Args:
        data (list[dict]): A list of dictionaries containing work metadata.

    Returns:
        list[PublishedWork]: A list of published works.
    """
    published_works = []
    for work_data in data:
        try:
            work = PublishedWork(
                title=work_data["title"],
                authors=work_data["authors"],
                publication_date=work_data["publication_date"],
                publisher=work_data["publisher"],
                isbn=work_data.get("isbn"),
            )
            published_works.append(work)
        except KeyError as e:
            print(f"Error loading work: {e}")
    return published_works


def main():
    # Example usage
    author = Author("Rade Milosavljevic")

    data = [
        {
            "title": "Book 1",
            "authors": ["Rade Milosavljevic", "Co-author"],
            "publication_date": "2020-01-01",
            "publisher": "Publisher 1",
            "isbn": "1234567890",
        },
        {
            "title": "Book 2",
            "authors": ["Rade Milosavljevic"],
            "publication_date": "2019-01-01",
            "publisher": "Publisher 2",
        },
    ]

    published_works = load_published_works(data)

    for work in published_works:
        author.add_published_work(work)

    compiled_works = author.compile_published_works()

    print("Published Works:")
    for i, work in enumerate(compiled_works, start=1):
        print(f"{i}. {work}")


if __name__ == "__main__":
    main()
```
