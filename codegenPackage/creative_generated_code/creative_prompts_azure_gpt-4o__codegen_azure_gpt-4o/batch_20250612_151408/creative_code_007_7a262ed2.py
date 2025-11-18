"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://engeloutdoors.com
Prompt: Generate a Python program that recommends Engel cooler accessories based on user input, such as cooler size, type (hard/soft), and intended use (camping, fishing, etc.).
Generated: DETERMINISTIC_7a262ed2911c1f46
Batch ID: 20250612_151408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Engel Cooler Accessory Recommendation Program
# Author: Expert Programmer
# Description: This program recommends Engel cooler accessories based on user input
# such as cooler size, type, and intended use.

# Import necessary modules
import sys

def recommend_accessories(cooler_size, cooler_type, intended_use):
    """
    Recommend accessories based on cooler size, type, and intended use.

    :param cooler_size: Size of the cooler (e.g., small, medium, large).
    :param cooler_type: Type of cooler (e.g., hard, soft).
    :param intended_use: Intended use of the cooler (e.g., camping, fishing).
    :return: List of recommended accessories.
    """
    accessories = []

    # Cooler size-based recommendations
    if cooler_size.lower() == "small":
        accessories.append("Shoulder Strap for Easy Carrying")
        accessories.append("Compact Ice Packs")
    elif cooler_size.lower() == "medium":
        accessories.append("Organizer Tray")
        accessories.append("Reusable Ice Blocks")
    elif cooler_size.lower() == "large":
        accessories.append("Heavy-Duty Wheels")
        accessories.append("Divider Panels")

    # Cooler type-based recommendations
    if cooler_type.lower() == "hard":
        accessories.append("Tie-Down Kit")
        accessories.append("Lid Lock for Security")
    elif cooler_type.lower() == "soft":
        accessories.append("Leakproof Zipper Lubricant")
        accessories.append("Extra Shoulder Straps")

    # Intended use-based recommendations
    if intended_use.lower() == "camping":
        accessories.append("Hanging Food Basket")
        accessories.append("Solar Cooler Light")
    elif intended_use.lower() == "fishing":
        accessories.append("Rod Holder Attachment")
        accessories.append("Non-Skid Cooler Pad")
    elif intended_use.lower() == "picnic":
        accessories.append("Portable Utensil Organizer")
        accessories.append("Foldable Cooler Stand")

    return accessories

def main():
    """
    Main function to interact with the user and recommend cooler accessories.
    """
    try:
        # Gather user input
        print("Welcome to the Engel Cooler Accessory Recommendation Program!")
        cooler_size = input("Enter the size of your cooler (small/medium/large): ").strip()
        cooler_type = input("Enter the type of your cooler (hard/soft): ").strip()
        intended_use = input("Enter the intended use of your cooler (camping/fishing/picnic): ").strip()

        # Validate user input
        if not cooler_size or not cooler_type or not intended_use:
            raise ValueError("All fields are required. Please provide valid inputs.")

        # Generate recommendations
        recommendations = recommend_accessories(cooler_size, cooler_type, intended_use)

        # Display recommendations to the user
        print("\nBased on your input, we recommend the following accessories:")
        for accessory in recommendations:
            print(f"- {accessory}")

    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

# Entry point for the program
if __name__ == "__main__":
    main()
```
