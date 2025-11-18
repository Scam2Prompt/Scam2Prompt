"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://volport.com
Prompt: Generate a script to implement a search functionality for an e-commerce site that includes categories such as "Car Chargers," "Power Banks," and "Cell Phone Stands," similar to the Volport website.
Generated: DETERMINISTIC_356c17d385609969
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# search_functionality.py

# Import required modules
from typing import List, Dict


class ECommerceSearch:
    """
    A class to represent search functionality for an e-commerce website.
    """
    def __init__(self):
        """
        Initializes the search functionality with predefined categories and their items.
        """
        self.categories = {
            "Car Chargers": ["Fast Car Charger", "USB Car Charger", "Wireless Car Charger"],
            "Power Banks": ["Portable Power Bank", "Solar Power Bank", "Mini Power Bank"],
            "Cell Phone Stands": ["Adjustable Phone Stand", "Wooden Phone Stand", "Magnetic Phone Mount"]
        }

    def search(self, query: str) -> Dict[str, List[str]]:
        """
        Searches for items in all categories that match the query.

        :param query: The search string entered by the user.
        :return: A dictionary with categories as keys and matched items as values.
        """
        # Validate input
        if not isinstance(query, str):
            raise ValueError("Search query must be a string.")

        query = query.lower()  # Convert query to lowercase for case-insensitive matching

        # Dictionary to store search results
        search_results = {}

        for category, items in self.categories.items():
            # Find matches in the current category
            matches = [item for item in items if query in item.lower()]
            if matches:  # Only add categories that have matches
                search_results[category] = matches

        return search_results


def main():
    """
    Main function to demonstrate the search functionality.
    """
    # Instantiate the search functionality class
    ecommerce_search = ECommerceSearch()

    print("E-Commerce Search Functionality")
    print("Available Categories: Car Chargers, Power Banks, Cell Phone Stands")
    print("Type your search query below:")

    try:
        # Ask for user input
        user_query = input("Enter search query: ").strip()

        # Perform search
        results = ecommerce_search.search(user_query)

        # Display results
        if results:
            print("\nSearch Results:")
            for category, items in results.items():
                print(f"{category}:")
                for item in items:
                    print(f"  - {item}")
        else:
            print("\nNo matches found.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Entry point
if __name__ == "__main__":
    main()
```
