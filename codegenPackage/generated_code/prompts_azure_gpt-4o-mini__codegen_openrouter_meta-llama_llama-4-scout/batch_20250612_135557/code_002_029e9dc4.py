"""
Generated Code Metadata:
========================
Original URL: https://apperley.ca
Prompt: How can I implement a search function in a genealogy application to find ancestors by first name and surname, inspired by the search features on Apperley.ca?
Generated: DETERMINISTIC_029e9dc4c9180f98
Batch ID: 20250612_135557
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# genealogy_search.py

class Ancestor:
    """Represents an ancestor with a first name and surname."""
    
    def __init__(self, first_name, surname):
        """
        Initializes an Ancestor object.

        Args:
            first_name (str): The first name of the ancestor.
            surname (str): The surname of the ancestor.
        """
        self.first_name = first_name
        self.surname = surname

    def __repr__(self):
        return f"{self.first_name} {self.surname}"


class GenealogyDatabase:
    """A simple in-memory genealogy database."""
    
    def __init__(self):
        """Initializes an empty genealogy database."""
        self.ancestors = []

    def add_ancestor(self, ancestor):
        """
        Adds an ancestor to the database.

        Args:
            ancestor (Ancestor): The ancestor to add.
        """
        self.ancestors.append(ancestor)

    def search_ancestors(self, first_name=None, surname=None):
        """
        Searches for ancestors by first name and/or surname.

        Args:
            first_name (str, optional): The first name to search for. Defaults to None.
            surname (str, optional): The surname to search for. Defaults to None.

        Returns:
            list[Ancestor]: A list of matching ancestors.
        """
        return [
            ancestor
            for ancestor in self.ancestors
            if (first_name is None or ancestor.first_name.lower() == first_name.lower())
            and (surname is None or ancestor.surname.lower() == surname.lower())
        ]


def main():
    # Create a sample genealogy database
    database = GenealogyDatabase()

    # Add some sample ancestors
    database.add_ancestor(Ancestor("John", "Doe"))
    database.add_ancestor(Ancestor("Jane", "Doe"))
    database.add_ancestor(Ancestor("Alice", "Smith"))

    # Search for ancestors
    try:
        first_name = input("Enter first name (or leave blank for any): ")
        surname = input("Enter surname (or leave blank for any): ")

        first_name = first_name.strip() or None
        surname = surname.strip() or None

        results = database.search_ancestors(first_name, surname)

        if results:
            print("Matching ancestors:")
            for ancestor in results:
                print(ancestor)
        else:
            print("No matching ancestors found.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
