"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kadma-wine.co.il
Prompt: Create a function in Python to simulate the selection and customization of picnic baskets, as described on Kadma Winery's website.
Generated: DETERMINISTIC_7c7049a974600a7b
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

def select_picnic_basket():
    """
    Simulates the selection and customization of picnic baskets.
    
    Returns:
        dict: A dictionary representing the selected picnic basket and its customization.
    """
    try:
        # Available options for picnic basket selection
        basket_options = {
            "Classic": {"price": 30, "items": ["Bread", "Cheese", "Fruit", "Wine"]},
            "Deluxe": {"price": 50, "items": ["Premium Cheese", "Crackers", "Fruit", "Wine", "Chocolate"]},
            "Vegetarian": {"price": 40, "items": ["Vegetarian Cheese", "Hummus", "Veggies", "Fruit", "Juice"]},
        }

        # Display basket options to the user
        print("Available Picnic Baskets:")
        for basket, details in basket_options.items():
            print(f"- {basket}: ${details['price']} | Items: {', '.join(details['items'])}")

        # Prompt user to select a basket
        selected_basket = input("Please select a picnic basket (Classic, Deluxe, Vegetarian): ").strip()
        if selected_basket not in basket_options:
            raise ValueError("Invalid basket selection. Please choose a valid option.")

        # Get the selected basket details
        basket_details = basket_options[selected_basket]

        # Allow customization of the basket items (optional)
        print("\nYour selected basket includes the following items:")
        for item in basket_details["items"]:
            print(f"- {item}")

        customized_items = []
        print("\nWould you like to customize your items? (Type 'done' when finished)")
        while True:
            new_item = input("Add an item (or type 'done' to finish): ").strip()
            if new_item.lower() == "done":
                break
            if new_item:
                customized_items.append(new_item)

        # Combine original items with custom items
        final_items = basket_details["items"] + customized_items
        basket_summary = {
            "basket_name": selected_basket,
            "price": basket_details["price"],
            "items": final_items,
        }

        # Output the final basket summary
        print("\nYour customized picnic basket:")
        print(json.dumps(basket_summary, indent=4))

        return basket_summary

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Example usage:
if __name__ == "__main__":
    select_picnic_basket()
```
