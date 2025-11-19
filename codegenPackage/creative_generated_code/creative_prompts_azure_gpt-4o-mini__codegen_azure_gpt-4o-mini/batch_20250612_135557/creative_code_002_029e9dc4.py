"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apperley.ca
Prompt: How can I implement a search function in a genealogy application to find ancestors by first name and surname, inspired by the search features on Apperley.ca?
Generated: DETERMINISTIC_029e9dc4c9180f98
Batch ID: 20250612_135557
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import List, Dict, Optional

class Ancestor:
    """Class representing an ancestor with a first name and surname."""
    
    def __init__(self, first_name: str, surname: str):
        self.first_name = first_name
        self.surname = surname

    def __repr__(self):
        return f"{self.first_name} {self.surname}"

class Genealogy:
    """Class handling genealogy data and search functionality."""
    
    def __init__(self):
        # Initialize an empty list to hold ancestors
        self.ancestors: List[Ancestor] = []

    def add_ancestor(self, first_name: str, surname: str):
        """Add a new ancestor to the genealogy."""
        if not first_name or not surname:
            raise ValueError("First name and surname cannot be empty.")
        ancestor = Ancestor(first_name, surname)
        self.ancestors.append(ancestor)

    def search_ancestors(self, first_name: Optional[str] = None, surname: Optional[str] = None) -> List[Ancestor]:
        """
        Search for ancestors by first name and/or surname.

        :param first_name: The first name to search for (optional).
        :param surname: The surname to search for (optional).
        :return: A list of matching ancestors.
        """
        if first_name is None and surname is None:
            raise ValueError("At least one search parameter (first name or surname) must be provided.")
        
        # Filter ancestors based on provided search criteria
        results = [
            ancestor for ancestor in self.ancestors
            if (first_name is None or ancestor.first_name.lower() == first_name.lower()) and
               (surname is None or ancestor.surname.lower() == surname.lower())
        ]
        
        return results

# Example usage of the Genealogy class
if __name__ == "__main__":
    try:
        genealogy = Genealogy()
        genealogy.add_ancestor("John", "Doe")
        genealogy.add_ancestor("Jane", "Smith")
        genealogy.add_ancestor("Alice", "Doe")

        # Search for ancestors
        search_results = genealogy.search_ancestors(first_name="John")
        print("Search Results for first name 'John':", search_results)

        search_results = genealogy.search_ancestors(surname="Doe")
        print("Search Results for surname 'Doe':", search_results)

        search_results = genealogy.search_ancestors(first_name="Alice", surname="Doe")
        print("Search Results for 'Alice Doe':", search_results)
    
    except ValueError as e:
        print("Error:", e)
```
