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
class Ancestor:
    """Class representing an ancestor with first name and surname."""
    
    def __init__(self, first_name: str, surname: str):
        self.first_name = first_name
        self.surname = surname

    def __repr__(self):
        return f"{self.first_name} {self.surname}"


class Genealogy:
    """Class to manage a list of ancestors and provide search functionality."""
    
    def __init__(self):
        self.ancestors = []

    def add_ancestor(self, first_name: str, surname: str):
        """Add a new ancestor to the genealogy."""
        if not first_name or not surname:
            raise ValueError("First name and surname cannot be empty.")
        self.ancestors.append(Ancestor(first_name, surname))

    def search_ancestors(self, first_name: str = None, surname: str = None):
        """Search for ancestors by first name and/or surname.
        
        Args:
            first_name (str): The first name to search for.
            surname (str): The surname to search for.
        
        Returns:
            list: A list of matching ancestors.
        """
        if first_name is None and surname is None:
            raise ValueError("At least one search parameter (first name or surname) must be provided.")

        results = []
        for ancestor in self.ancestors:
            if (first_name is None or ancestor.first_name.lower() == first_name.lower()) and \
               (surname is None or ancestor.surname.lower() == surname.lower()):
                results.append(ancestor)
        
        return results


# Example usage
if __name__ == "__main__":
    genealogy = Genealogy()
    
    # Adding ancestors
    genealogy.add_ancestor("John", "Doe")
    genealogy.add_ancestor("Jane", "Smith")
    genealogy.add_ancestor("Alice", "Johnson")
    
    # Searching for ancestors
    try:
        search_results = genealogy.search_ancestors(first_name="Jane")
        print("Search Results:", search_results)
    except ValueError as e:
        print("Error:", e)
```
