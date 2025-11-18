"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thegladiatorshoes.com
Prompt: Write Python code to create a product filter system for safety shoes based on features like "steel toe," "composite toe," and "metal-free" using the Gladiator Shoes product categories.
Generated: DETERMINISTIC_59d24fd8816606f1
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import List, Dict

class SafetyShoe:
    """Class to represent a safety shoe product with specific features."""
    
    def __init__(self, name: str, features: List[str]):
        """
        Initializes a SafetyShoe instance.

        :param name: Name of the safety shoe.
        :param features: List of features associated with the safety shoe.
        """
        self.name = name
        self.features = features

    def has_feature(self, feature: str) -> bool:
        """
        Checks if the safety shoe has a specific feature.

        :param feature: The feature to check for.
        :return: True if feature exists, False otherwise.
        """
        return feature in self.features


class GladiatorShoes:
    """Class to represent the collection of Gladiator safety shoes."""
    
    def __init__(self):
        """Initializes an empty list of safety shoes."""
        self.shoes: List[SafetyShoe] = []

    def add_shoe(self, shoe: SafetyShoe) -> None:
        """
        Adds a safety shoe to the collection.

        :param shoe: The SafetyShoe instance to add.
        """
        self.shoes.append(shoe)

    def filter_shoes(self, required_features: List[str]) -> List[SafetyShoe]:
        """
        Filters the shoes based on required features.

        :param required_features: List of features to filter the shoes by.
        :return: A list of SafetyShoe instances matching the required features.
        """
        filtered_shoes = []

        for shoe in self.shoes:
            if all(shoe.has_feature(feature) for feature in required_features):
                filtered_shoes.append(shoe)

        return filtered_shoes


def main() -> None:
    """Main function to demonstrate the functionality of the product filter system."""
    try:
        # Create an instance of GladiatorShoes collection
        gladiator_shoes = GladiatorShoes()

        # Add sample shoes to the collection
        gladiator_shoes.add_shoe(SafetyShoe("Gladiator Steel Toe", ["steel toe", "waterproof"]))
        gladiator_shoes.add_shoe(SafetyShoe("Gladiator Composite Toe", ["composite toe", "lightweight"]))
        gladiator_shoes.add_shoe(SafetyShoe("Gladiator Metal-Free", ["metal-free", "comfortable"]))

        # Define features to filter by
        features_to_filter = ["metal-free"]
        
        # Get filtered shoes
        filtered_shoes = gladiator_shoes.filter_shoes(features_to_filter)

        # Output the filtered shoes
        print("Filtered Safety Shoes:")
        for shoe in filtered_shoes:
            print(f"- {shoe.name} with features: {', '.join(shoe.features)}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
