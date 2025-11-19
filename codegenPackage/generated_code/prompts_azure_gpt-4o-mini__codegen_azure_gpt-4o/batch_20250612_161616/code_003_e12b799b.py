"""
Generated Code Metadata:
========================
Original URL: https://divinecollections.net
Prompt: Develop a script that displays unique gift items from Divine Collections, such as bags and wall hangings, based on user-selected categories.
Generated: DETERMINISTIC_e12b799be17b1e44
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys

def display_gift_items(category, gift_items):
    """
    Displays unique gift items based on the selected category.

    Parameters:
    category (str): The category selected by the user.
    gift_items (dict): Dictionary containing categories and their respective items.

    Returns:
    None
    """
    try:
        # Check if the category exists in the gift items dictionary
        if category not in gift_items:
            print(f"Error: '{category}' is not a valid category. Please select a valid category.")
            return

        # Retrieve and display unique items for the selected category
        unique_items = set(gift_items[category])
        print(f"Unique gift items in the '{category}' category:")
        for item in unique_items:
            print(f"- {item}")

    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


def main():
    """
    Main function to run the script.
    """
    # Predefined gift items categorized by type
    gift_items = {
        "bags": ["Leather Bag", "Canvas Tote", "Leather Bag", "Backpack"],
        "wall hangings": ["Abstract Painting", "Wooden Frame", "Abstract Painting", "Metal Art"],
        "decor": ["Vase", "Candle Holder", "Vase", "Lamp"],
    }

    # Prompt the user to select a category
    print("Available categories: bags, wall hangings, decor")
    category = input("Please enter a category to view unique gift items: ").strip().lower()

    # Display gift items for the selected category
    display_gift_items(category, gift_items)


if __name__ == "__main__":
    # Entry point of the script
    main()
```
