"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meatmaster.pe
Prompt: Implement a search feature that allows users to find "Parrillas" based on specific criteria like capacity and material, as highlighted on the Meat Master webpage.
Generated: DETERMINISTIC_5efc48a6b1a66937
Batch ID: 20250612_160804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from typing import List, Dict, Optional

class Parrilla:
    """Class to represent a Parrilla with specific attributes."""
    
    def __init__(self, name: str, capacity: int, material: str):
        """
        Initialize a new Parrilla instance.

        :param name: Name of the Parrilla
        :param capacity: Capacity of the Parrilla
        :param material: Material of the Parrilla
        """
        self.name = name
        self.capacity = capacity
        self.material = material

    def __repr__(self):
        """Provide a string representation of the Parrilla."""
        return f"Parrilla(name={self.name}, capacity={self.capacity}, material={self.material})"


class ParrillaSearch:
    """Class to handle searching for Parrillas based on specific criteria."""
    
    def __init__(self, parrillas: List[Parrilla]):
        """
        Initialize the search with a list of Parrillas.

        :param parrillas: List of Parrilla objects
        """
        self.parrillas = parrillas

    def search(self, capacity: Optional[int] = None, material: Optional[str] = None) -> List[Parrilla]:
        """
        Search for Parrillas based on capacity and/or material.

        :param capacity: Capacity to filter by
        :param material: Material to filter by
        :return: List of matching Parrillas
        """
        results = self.parrillas
        
        # Filter by capacity if provided
        if capacity is not None:
            results = [p for p in results if p.capacity >= capacity]

        # Filter by material if provided
        if material is not None:
            results = [p for p in results if p.material.lower() == material.lower()]

        return results


# Example usage
if __name__ == "__main__":
    # Sample data for Parrillas
    parrilla_list = [
        Parrilla("Parrilla A", 4, "Steel"),
        Parrilla("Parrilla B", 8, "Cast Iron"),
        Parrilla("Parrilla C", 6, "Stainless Steel"),
        Parrilla("Parrilla D", 10, "Steel"),
    ]

    # Create a ParrillaSearch instance with sample data
    searcher = ParrillaSearch(parrilla_list)

    # Perform search operations (example search queries)
    try:
        # Search for Parrillas with a minimum capacity of 6 and made of Steel
        search_results = searcher.search(capacity=6, material="Steel")
        print("Search Results:", search_results)

        # Search for Parrillas with a minimum capacity of 5 without material specified
        search_results = searcher.search(capacity=5)
        print("Search Results:", search_results)

        # Search for Parrillas made of Cast Iron without capacity specified
        search_results = searcher.search(material="Cast Iron")
        print("Search Results:", search_results)

    except Exception as e:
        print("An error occurred during the search:", str(e))
```
