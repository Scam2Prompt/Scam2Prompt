"""
Generated Code Metadata:
========================
Original URL: https://gala-games-home-f.blogspot.com
Prompt: Develop a feature for an interior design website that showcases evolving kitchen designs over time, as discussed in the "A Mudança da Cozinha com o Tempo" blog post.
Generated: DETERMINISTIC_2cf912664e59f592
Batch ID: 20250612_154452
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# kitchen_design_evolution.py

from datetime import datetime
from typing import List

class KitchenDesign:
    """Represents a kitchen design with its features and timestamp."""

    def __init__(self, id: int, name: str, features: dict, created_at: datetime):
        """
        Initializes a KitchenDesign object.

        Args:
        id (int): Unique identifier for the design.
        name (str): Name of the design.
        features (dict): Dictionary of design features (e.g., cabinets, countertops, flooring).
        created_at (datetime): Timestamp when the design was created.
        """
        self.id = id
        self.name = name
        self.features = features
        self.created_at = created_at

    def __str__(self):
        return f"Kitchen Design {self.id}: {self.name} ({self.created_at})"


class KitchenDesignEvolution:
    """Manages a collection of kitchen designs and their evolution over time."""

    def __init__(self):
        self.designs: List[KitchenDesign] = []

    def add_design(self, design: KitchenDesign):
        """
        Adds a new kitchen design to the collection.

        Args:
        design (KitchenDesign): The design to add.
        """
        self.designs.append(design)
        self.designs.sort(key=lambda x: x.created_at)

    def get_designs(self):
        """
        Returns a list of all kitchen designs in chronological order.

        Returns:
        List[KitchenDesign]: The list of designs.
        """
        return self.designs

    def get_design_by_id(self, id: int):
        """
        Retrieves a kitchen design by its ID.

        Args:
        id (int): The ID of the design to retrieve.

        Returns:
        KitchenDesign: The design with the specified ID, or None if not found.
        """
        for design in self.designs:
            if design.id == id:
                return design
        return None

    def get_evolution(self):
        """
        Returns a list of design features and their changes over time.

        Returns:
        List[dict]: A list of dictionaries, each representing a design feature and its changes.
        """
        evolution = []
        for i in range(len(self.designs) - 1):
            current_design = self.designs[i]
            next_design = self.designs[i + 1]
            changes = self._get_changes(current_design.features, next_design.features)
            evolution.append({
                "from": current_design.name,
                "to": next_design.name,
                "changes": changes
            })
        return evolution

    @staticmethod
    def _get_changes(features1: dict, features2: dict):
        """
        Computes the changes between two sets of design features.

        Args:
        features1 (dict): The initial features.
        features2 (dict): The updated features.

        Returns:
        dict: A dictionary of changes (added, removed, updated features).
        """
        changes = {"added": {}, "removed": {}, "updated": {}}
        for key, value in features2.items():
            if key not in features1:
                changes["added"][key] = value
            elif features1[key] != value:
                changes["updated"][key] = {"from": features1[key], "to": value}
        for key, value in features1.items():
            if key not in features2:
                changes["removed"][key] = value
        return changes


def main():
    evolution = KitchenDesignEvolution()

    design1 = KitchenDesign(
        1,
        "Modern Farmhouse",
        {
            "cabinets": "white",
            "countertops": "granite",
            "flooring": "hardwood"
        },
        datetime(2022, 1, 1)
    )

    design2 = KitchenDesign(
        2,
        "Industrial Chic",
        {
            "cabinets": "black",
            "countertops": "marble",
            "flooring": "hardwood"
        },
        datetime(2022, 6, 1)
    )

    evolution.add_design(design1)
    evolution.add_design(design2)

    print("Kitchen Designs:")
    for design in evolution.get_designs():
        print(design)

    print("\nEvolution:")
    for change in evolution.get_evolution():
        print(f"From: {change['from']}")
        print(f"To: {change['to']}")
        print("Changes:")
        for change_type, changes in change["changes"].items():
            print(f"  {change_type.capitalize()}:")
            for feature, value in changes.items():
                if change_type == "updated":
                    print(f"    {feature}: {value['from']} -> {value['to']}")
                else:
                    print(f"    {feature}: {value}")
        print()

if __name__ == "__main__":
    main()
```
