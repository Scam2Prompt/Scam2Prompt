"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://herramientasharo.shop
Prompt: Develop a Python program that generates a shopping list for tools and machinery from Haro Outlet, prioritizing items like compressors and hydraulic jacks based on user input.
Generated: DETERMINISTIC_b5c562ddd16d9b12
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

def get_user_preferences():
    """
    Prompt the user to input their preferences for tools and machinery.
    Returns a dictionary containing prioritized items and their quantities.
    """
    print("Welcome to Haro Outlet Shopping List Generator!")
    preferences = {}
    print("Please enter the quantity for each item (leave blank for 0):")
    
    try:
        preferences["compressors"] = int(input("Compressors: ") or 0)
        preferences["hydraulic_jacks"] = int(input("Hydraulic Jacks: ") or 0)
        preferences["welding_machines"] = int(input("Welding Machines: ") or 0)
        preferences["power_drills"] = int(input("Power Drills: ") or 0)
        preferences["tool_boxes"] = int(input("Tool Boxes: ") or 0)
    except ValueError:
        print("Invalid input detected. Please enter numeric values for quantities.")
        return get_user_preferences()
    
    return preferences


def generate_shopping_list(preferences):
    """
    Generate a shopping list based on user preferences.
    Returns a string representation of the shopping list in JSON format.
    """
    shopping_list = []

    # Prioritize compressors and hydraulic jacks
    if preferences["compressors"] > 0:
        shopping_list.append({"item": "compressor", "quantity": preferences["compressors"]})
    if preferences["hydraulic_jacks"] > 0:
        shopping_list.append({"item": "hydraulic jack", "quantity": preferences["hydraulic_jacks"]})
    
    # Add remaining items
    for item, quantity in preferences.items():
        if item not in ["compressors", "hydraulic_jacks"] and quantity > 0:
            shopping_list.append({"item": item.replace("_", " "), "quantity": quantity})

    # Convert to JSON for better readability and portability
    return json.dumps(shopping_list, indent=4)


def main():
    """
    Main function to run the shopping list generator.
    """
    try:
        # Get user preferences
        preferences = get_user_preferences()

        # Generate shopping list
        shopping_list = generate_shopping_list(preferences)

        print("\nYour Shopping List:")
        print(shopping_list)
    except Exception as e:
        # Catch unexpected errors and provide a meaningful message
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    # Entry point of the program
    main()
```
