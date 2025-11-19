"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.bicho.se
Prompt: Create a library function to manage and display author information for Jenny Bicho's publications.
Generated: DETERMINISTIC_1c807f83d8a25260
Batch ID: 20250612_161353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Author:
    """
    A class to represent an author and manage their publication information.
    """

    def __init__(self, name: str):
        """
        Initialize an Author instance.

        :param name: The name of the author.
        :raises ValueError: If the name is empty or None.
        """
        if not name:
            raise ValueError("Author name cannot be empty.")
        self.name = name
        self.publications = []

    def add_publication(self, title: str, year: int):
        """
        Add a publication to the author's list of publications.

        :param title: The title of the publication.
        :param year: The year of publication.
        :raises ValueError: If the title is empty or year is not a positive integer.
        """
        if not title:
            raise ValueError("Publication title cannot be empty.")
        if not isinstance(year, int) or year <= 0:
            raise ValueError("Publication year must be a positive integer.")

        self.publications.append({'title': title, 'year': year})

    def display_info(self):
        """
        Display the author's information and their publications.
        """
        print(f"Author: {self.name}")
        if not self.publications:
            print("No publications available.")
        else:
            print("Publications:")
            for pub in self.publications:
                print(f" - {pub['title']} ({pub['year']})")

# Example usage
if __name__ == "__main__":
    try:
        author = Author("Jenny Bicho")
        author.add_publication("Understanding AI", 2021)
        author.add_publication("Python Best Practices", 2022)
        author.display_info()
    except ValueError as e:
        print(f"Error: {e}")
```
