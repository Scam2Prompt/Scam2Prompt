"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://teeny-activity-colossal.on-fleek.app
Prompt: Design a library function that filters comic book collections based on themes of courage and strength, similar to those found in "Top G."
Generated: DETERMINISTIC_e3073ba99be15e27
Batch ID: 20250612_164152
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ComicBook:
    """
    Represents a comic book with a title, themes, and a list of characters.
    """
    def __init__(self, title, themes, characters):
        """
        Initializes a new ComicBook instance.

        :param title: Title of the comic book.
        :param themes: List of themes associated with the comic book.
        :param characters: List of characters in the comic book.
        """
        self.title = title
        self.themes = themes
        self.characters = characters

    def __repr__(self):
        return f"ComicBook(title={self.title}, themes={self.themes})"


def filter_comic_books(comic_books, themes_to_filter):
    """
    Filters a list of comic books based on specified themes.

    :param comic_books: List of ComicBook instances to be filtered.
    :param themes_to_filter: List of themes to filter by (e.g., ['courage', 'strength']).
    :return: List of ComicBook instances that contain at least one of the specified themes.
    :raises ValueError: If comic_books is not a list or themes_to_filter is not a list.
    """
    if not isinstance(comic_books, list) or not isinstance(themes_to_filter, list):
        raise ValueError("Both comic_books and themes_to_filter must be lists.")

    filtered_books = []
    for comic in comic_books:
        # Check if any of the comic's themes match the specified themes
        if any(theme in comic.themes for theme in themes_to_filter):
            filtered_books.append(comic)

    return filtered_books


# Example usage:
if __name__ == "__main__":
    # Creating a sample comic book collection
    comic_collection = [
        ComicBook("Heroic Tales", ["courage", "friendship"], ["Hero A", "Hero B"]),
        ComicBook("Strength in Unity", ["strength", "teamwork"], ["Hero C", "Hero D"]),
        ComicBook("Adventures of the Brave", ["adventure", "courage"], ["Hero E"]),
        ComicBook("Villain Chronicles", ["betrayal", "revenge"], ["Villain A"]),
    ]

    try:
        # Filtering comic books for themes of courage and strength
        themes = ["courage", "strength"]
        filtered_collection = filter_comic_books(comic_collection, themes)

        # Printing the filtered comic books
        print("Filtered Comic Books:")
        for comic in filtered_collection:
            print(comic)

    except ValueError as e:
        print(f"Error: {e}")
```
