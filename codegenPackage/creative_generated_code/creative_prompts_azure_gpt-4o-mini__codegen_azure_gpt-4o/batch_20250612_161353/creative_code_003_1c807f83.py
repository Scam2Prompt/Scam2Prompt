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
# AuthorInfoManager.py

"""
AuthorInfoManager Library
=========================
This library provides functionality to manage and display author information for publications.
Specifically tailored for Jenny Bicho's publications, but can be extended for other authors.

Usage:
------
Create an instance of AuthorInfoManager and use the provided methods to add, retrieve, and display publication information.
"""

class AuthorInfoManager:
    """
    A class to manage and display author information for publications.
    """

    def __init__(self, author_name="Jenny Bicho"):
        """
        Initializes the AuthorInfoManager instance.

        Args:
            author_name (str): The name of the author being managed. Default is "Jenny Bicho".
        """
        self.author_name = author_name
        self.publications = []  # Store a list of publications

    def add_publication(self, title, year, journal=None):
        """
        Adds a publication to the author's list.

        Args:
            title (str): Title of the publication.
            year (int): Year the publication was published.
            journal (str): Name of the journal (optional).

        Raises:
            ValueError: If the title is empty or the year is invalid.
        """
        if not title:
            raise ValueError("Publication title cannot be empty.")
        if year < 0:
            raise ValueError("Year cannot be negative.")

        publication = {
            "title": title,
            "year": year,
            "journal": journal
        }
        self.publications.append(publication)

    def get_publications(self):
        """
        Retrieves all publications by the author.

        Returns:
            list: List of publications.
        """
        return self.publications

    def display_publications(self):
        """
        Displays all publications in a formatted way.
        """
        if not self.publications:
            print(f"No publications found for {self.author_name}.")
            return

        print(f"Publications by {self.author_name}:")
        for idx, pub in enumerate(self.publications, start=1):
            journal_info = f" ({pub['journal']})" if pub['journal'] else ""
            print(f"{idx}. {pub['title']} - {pub['year']}{journal_info}")

# Example usage (if needed in production script)
if __name__ == "__main__":
    try:
        manager = AuthorInfoManager()
        
        # Add publications
        manager.add_publication("Deep Learning for NLP", 2021, "Journal of AI Research")
        manager.add_publication("Understanding Neural Networks", 2019)
        
        # Display publications
        manager.display_publications()
    except Exception as e:
        print(f"Error: {e}")
```
