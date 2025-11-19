"""
Generated Code Metadata:
========================
Original URL: https://www.oasishottubsep.com
Prompt: Generate code to implement a search functionality for hot tubs and swim spas, similar to the search feature on the Oasis Hot Tubs website.
Generated: DETERMINISTIC_1c6a8f9ed150fe3d
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# search_hot_tubs.py

import json
from typing import Dict, List

class HotTub:
    def __init__(self, id: int, name: str, description: str, price: float, features: List[str]):
        """
        Initialize a HotTub object.

        Args:
        id (int): Unique identifier for the hot tub.
        name (str): Name of the hot tub.
        description (str): Description of the hot tub.
        price (float): Price of the hot tub.
        features (List[str]): List of features of the hot tub.
        """
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.features = features

class SearchHotTubs:
    def __init__(self, hot_tubs: List[HotTub]):
        """
        Initialize a SearchHotTubs object.

        Args:
        hot_tubs (List[HotTub]): List of HotTub objects.
        """
        self.hot_tubs = hot_tubs

    def search_by_name(self, name: str) -> List[HotTub]:
        """
        Search hot tubs by name.

        Args:
        name (str): Name to search for.

        Returns:
        List[HotTub]: List of hot tubs matching the search name.
        """
        return [hot_tub for hot_tub in self.hot_tubs if name.lower() in hot_tub.name.lower()]

    def search_by_feature(self, feature: str) -> List[HotTub]:
        """
        Search hot tubs by feature.

        Args:
        feature (str): Feature to search for.

        Returns:
        List[HotTub]: List of hot tubs matching the search feature.
        """
        return [hot_tub for hot_tub in self.hot_tubs if feature.lower() in [f.lower() for f in hot_tub.features]]

    def search_by_price(self, min_price: float, max_price: float) -> List[HotTub]:
        """
        Search hot tubs by price range.

        Args:
        min_price (float): Minimum price.
        max_price (float): Maximum price.

        Returns:
        List[HotTub]: List of hot tubs matching the search price range.
        """
        return [hot_tub for hot_tub in self.hot_tubs if min_price <= hot_tub.price <= max_price]

    def advanced_search(self, name: str = None, feature: str = None, min_price: float = None, max_price: float = None) -> List[HotTub]:
        """
        Advanced search for hot tubs.

        Args:
        name (str): Name to search for.
        feature (str): Feature to search for.
        min_price (float): Minimum price.
        max_price (float): Maximum price.

        Returns:
        List[HotTub]: List of hot tubs matching the search criteria.
        """
        results = self.hot_tubs
        if name:
            results = [hot_tub for hot_tub in results if name.lower() in hot_tub.name.lower()]
        if feature:
            results = [hot_tub for hot_tub in results if feature.lower() in [f.lower() for f in hot_tub.features]]
        if min_price and max_price:
            results = [hot_tub for hot_tub in results if min_price <= hot_tub.price <= max_price]
        return results

def load_hot_tubs() -> List[HotTub]:
    """
    Load sample hot tub data.

    Returns:
    List[HotTub]: List of HotTub objects.
    """
    hot_tubs = [
        HotTub(1, "Oasis Hot Tub", "A luxurious hot tub.", 9999.99, ["Jets", "LED Lights", "Heated"]),
        HotTub(2, "Swim Spa", "A swim spa for exercise and relaxation.", 12999.99, ["Jets", "LED Lights", "Heated", "Swim Current"]),
        HotTub(3, "Bubble Bath", "A simple bubble bath.", 499.99, ["Bubbles"]),
    ]
    return hot_tubs

def main():
    hot_tubs = load_hot_tubs()
    search = SearchHotTubs(hot_tubs)

    while True:
        print("\nSearch Options:")
        print("1. Search by name")
        print("2. Search by feature")
        print("3. Search by price range")
        print("4. Advanced search")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter a name to search for: ")
            results = search.search_by_name(name)
        elif choice == "2":
            feature = input("Enter a feature to search for: ")
            results = search.search_by_feature(feature)
        elif choice == "3":
            try:
                min_price = float(input("Enter a minimum price: "))
                max_price = float(input("Enter a maximum price: "))
                results = search.search_by_price(min_price, max_price)
            except ValueError:
                print("Invalid price. Please enter a valid number.")
                continue
        elif choice == "4":
            name = input("Enter a name to search for (optional): ")
            feature = input("Enter a feature to search for (optional): ")
            try:
                min_price = float(input("Enter a minimum price (optional): ") or 0)
                max_price = float(input("Enter a maximum price (optional): ") or float('inf'))
                results = search.advanced_search(name or None, feature or None, min_price or None, max_price or None)
            except ValueError:
                print("Invalid price. Please enter a valid number.")
                continue
        elif choice == "5":
            break
        else:
            print("Invalid option. Please choose a valid option.")
            continue

        if results:
            print("\nSearch Results:")
            for hot_tub in results:
                print(f"ID: {hot_tub.id}, Name: {hot_tub.name}, Price: ${hot_tub.price:.2f}, Features: {', '.join(hot_tub.features)}")
        else:
            print("\nNo results found.")

if __name__ == "__main__":
    main()
```
