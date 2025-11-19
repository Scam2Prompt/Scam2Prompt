"""
Generated Code Metadata:
========================
Original URL: https://bismillahgems.com
Prompt: Using the gemstone categories from "Bismillah Gems," write a program to generate a visual catalog that organizes gemstones by type, weight, and price.
Generated: DETERMINISTIC_8090b26c066a3243
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt

# Define a class for Gemstone
class Gemstone:
    def __init__(self, name, category, weight, price):
        """
        Initialize a Gemstone object.

        Args:
            name (str): Name of the gemstone.
            category (str): Category of the gemstone.
            weight (float): Weight of the gemstone in carats.
            price (float): Price of the gemstone in dollars.
        """
        self.name = name
        self.category = category
        self.weight = weight
        self.price = price

# Define a class for GemstoneCatalog
class GemstoneCatalog:
    def __init__(self):
        """
        Initialize a GemstoneCatalog object.
        """
        self.gemstones = []

    def add_gemstone(self, gemstone):
        """
        Add a gemstone to the catalog.

        Args:
            gemstone (Gemstone): Gemstone object to add.
        """
        self.gemstones.append(gemstone)

    def organize_by_type(self):
        """
        Organize gemstones by type.

        Returns:
            dict: Dictionary with categories as keys and lists of gemstones as values.
        """
        organized_gemstones = {}
        for gemstone in self.gemstones:
            if gemstone.category not in organized_gemstones:
                organized_gemstones[gemstone.category] = []
            organized_gemstones[gemstone.category].append(gemstone)
        return organized_gemstones

    def organize_by_weight(self):
        """
        Organize gemstones by weight.

        Returns:
            dict: Dictionary with weight ranges as keys and lists of gemstones as values.
        """
        organized_gemstones = {}
        for gemstone in self.gemstones:
            if gemstone.weight < 1:
                weight_range = "Under 1 carat"
            elif gemstone.weight < 5:
                weight_range = "1-5 carats"
            else:
                weight_range = "Over 5 carats"
            if weight_range not in organized_gemstones:
                organized_gemstones[weight_range] = []
            organized_gemstones[weight_range].append(gemstone)
        return organized_gemstones

    def organize_by_price(self):
        """
        Organize gemstones by price.

        Returns:
            dict: Dictionary with price ranges as keys and lists of gemstones as values.
        """
        organized_gemstones = {}
        for gemstone in self.gemstones:
            if gemstone.price < 1000:
                price_range = "Under $1000"
            elif gemstone.price < 5000:
                price_range = "$1000-$5000"
            else:
                price_range = "Over $5000"
            if price_range not in organized_gemstones:
                organized_gemstones[price_range] = []
            organized_gemstones[price_range].append(gemstone)
        return organized_gemstones

    def visualize_catalog(self):
        """
        Visualize the gemstone catalog.
        """
        # Organize gemstones by type, weight, and price
        by_type = self.organize_by_type()
        by_weight = self.organize_by_weight()
        by_price = self.organize_by_price()

        # Create a figure with subplots
        fig, axs = plt.subplots(1, 3, figsize=(15, 5))

        # Plot gemstones by type
        type_counts = {category: len(gemstones) for category, gemstones in by_type.items()}
        axs[0].bar(type_counts.keys(), type_counts.values())
        axs[0].set_title("Gemstones by Type")
        axs[0].set_xlabel("Type")
        axs[0].set_ylabel("Count")

        # Plot gemstones by weight
        weight_counts = {weight_range: len(gemstones) for weight_range, gemstones in by_weight.items()}
        axs[1].bar(weight_counts.keys(), weight_counts.values())
        axs[1].set_title("Gemstones by Weight")
        axs[1].set_xlabel("Weight Range")
        axs[1].set_ylabel("Count")

        # Plot gemstones by price
        price_counts = {price_range: len(gemstones) for price_range, gemstones in by_price.items()}
        axs[2].bar(price_counts.keys(), price_counts.values())
        axs[2].set_title("Gemstones by Price")
        axs[2].set_xlabel("Price Range")
        axs[2].set_ylabel("Count")

        # Show the plot
        plt.tight_layout()
        plt.show()

# Define a main function
def main():
    try:
        # Create a GemstoneCatalog object
        catalog = GemstoneCatalog()

        # Add gemstones to the catalog
        gemstones = [
            Gemstone("Ruby", "Corundum", 2.5, 2000),
            Gemstone("Sapphire", "Corundum", 3.2, 3000),
            Gemstone("Emerald", "Beryl", 1.8, 1500),
            Gemstone("Diamond", "Diamond", 0.5, 500),
            Gemstone("Amethyst", "Quartz", 4.1, 100),
            Gemstone("Topaz", "Topaz", 2.1, 200),
            Gemstone("Garnet", "Garnet", 3.5, 300),
            Gemstone("Opal", "Opal", 1.2, 400),
            Gemstone("Peridot", "Olivine", 2.8, 250),
            Gemstone("Turquoise", "Turquoise", 3.8, 350),
        ]
        for gemstone in gemstones:
            catalog.add_gemstone(gemstone)

        # Visualize the catalog
        catalog.visualize_catalog()

    except Exception as e:
        print(f"An error occurred: {e}")

# Call the main function
if __name__ == "__main__":
    main()
```
