"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://divinecollections.net
Prompt: Develop a script that displays unique gift items from Divine Collections, such as bags and wall hangings, based on user-selected categories.
Generated: DETERMINISTIC_e12b799be17b1e44
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

# Define a dictionary to store gift items categorized by type
GIFT_ITEMS = {
    "bags": ["Leather Tote Bag", "Canvas Backpack", "Handmade Clutch"],
    "wall_hangings": ["Decorative Tapestry", "Metal Art Wall Hanging", "Wooden Plaque"]
}

def display_categories():
    """
    Display the available categories to the user.
    """
    print("\nAvailable Gift Categories:")
    for category in GIFT_ITEMS.keys():
        print(f"- {category.capitalize()}")

def display_items_by_category(category):
    """
    Display unique gift items for the selected category.
    :param category: The category selected by the user.
    """
    if category in GIFT_ITEMS:
        print(f"\nUnique items in '{category.capitalize()}' category:")
        for item in GIFT_ITEMS[category]:
            print(f"- {item}")
    else:
        print("\nError: Invalid category selected. Please choose a valid category.")

def main():
    """
    Main function to execute the script logic.
    """
    try:
        print("Welcome to Divine Collections!")
        display_categories()

        # Ask the user to select a category
        user_input = input("\nEnter the category you want to explore: ").strip().lower()

        # Display items based on the selected category
        display_items_by_category(user_input)

    except Exception as e:
        print(f"\nAn unexpected error occurred: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
