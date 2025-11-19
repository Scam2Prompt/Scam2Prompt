"""
Generated Code Metadata:
========================
Original URL: https://bvitravel.co.uk
Prompt: "Provide a list of the best islands to visit in the BVI for solo travelers, including information on safety and popular activities like snorkelling and diving."
Generated: DETERMINISTIC_2555957e586112f4
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import requests
from typing import List, Dict

class Island:
    """Represents an island in the BVI with information on safety and activities."""

    def __init__(self, name: str, safety_rating: int, snorkelling: bool, diving: bool):
        """
        Initializes an Island object.

        Args:
        - name (str): The name of the island.
        - safety_rating (int): A rating from 1-5 representing the island's safety for solo travelers.
        - snorkelling (bool): Whether snorkelling is a popular activity on the island.
        - diving (bool): Whether diving is a popular activity on the island.
        """
        self.name = name
        self.safety_rating = safety_rating
        self.snorkelling = snorkelling
        self.diving = diving

    def __repr__(self):
        return f"Island('{self.name}', {self.safety_rating}, {self.snorkelling}, {self.diving})"


def get_islands() -> List[Island]:
    """
    Returns a list of Island objects representing the best islands to visit in the BVI for solo travelers.

    Returns:
    - List[Island]: A list of Island objects.
    """
    # Sample data for demonstration purposes
    islands: List[Island] = [
        Island("Tortola", 5, True, True),
        Island("Jost Van Dyke", 4, True, False),
        Island("Virgin Gorda", 5, True, True),
        Island("Anegada", 4, True, False),
        Island("Peter Island", 5, False, True),
    ]

    return islands


def get_top_islands_by_safety(islands: List[Island], num_islands: int) -> List[Island]:
    """
    Returns the top N islands by safety rating.

    Args:
    - islands (List[Island]): A list of Island objects.
    - num_islands (int): The number of top islands to return.

    Returns:
    - List[Island]: A list of the top N Island objects by safety rating.
    """
    # Sort islands by safety rating in descending order
    sorted_islands = sorted(islands, key=lambda island: island.safety_rating, reverse=True)

    return sorted_islands[:num_islands]


def print_island_info(island: Island):
    """
    Prints information about an island.

    Args:
    - island (Island): An Island object.
    """
    print(f"Island: {island.name}")
    print(f"Safety Rating: {island.safety_rating}/5")
    print(f"Snorkelling: {'Yes' if island.snorkelling else 'No'}")
    print(f"Diving: {'Yes' if island.diving else 'No'}")
    print("------------------------")


def main():
    try:
        islands = get_islands()
        top_islands = get_top_islands_by_safety(islands, 3)

        print("Top 3 Islands to Visit in the BVI for Solo Travelers:")
        for island in top_islands:
            print_island_info(island)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
