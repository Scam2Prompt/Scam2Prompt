"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://infusionperu.com
Prompt: Write a code snippet that simulates a drink selection system for Infusion Peru, allowing users to choose mixes based on health benefits like digestion and relaxation.
Generated: DETERMINISTIC_7c3097625a5837c3
Batch ID: 20250612_164222
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# drink_selection_system.py

# This script simulates a drink selection system for Infusion Peru,
# allowing users to choose tea mixes based on health benefits like digestion and relaxation.

def display_menu():
    """
    Displays the drink menu with health benefits.
    """
    print("\nWelcome to Infusion Peru!")
    print("Please select your drink mix based on health benefits:")
    print("1. Digestion Boost - Ginger, Mint, and Chamomile")
    print("2. Relaxation Mix - Lavender, Lemon Balm, and Valerian Root")
    print("3. Energy Revival - Green Tea, Ginseng, and Lemon")
    print("4. Immune Support - Turmeric, Honey, and Lime")
    print("5. Exit")

def get_user_choice():
    """
    Prompts the user for their choice and validates the input.
    Returns:
        int: The selected option.
    """
    try:
        choice = int(input("\nEnter the number corresponding to your choice: "))
        if choice < 1 or choice > 5:
            raise ValueError("Invalid choice. Please select a number between 1 and 5.")
        return choice
    except ValueError as e:
        print(f"Error: {e}")
        return None

def prepare_drink(choice):
    """
    Prepares the selected drink mix based on the user's choice.
    Args:
        choice (int): The user's selected option.
    """
    drink_options = {
        1: "Digestion Boost - Ginger, Mint, and Chamomile",
        2: "Relaxation Mix - Lavender, Lemon Balm, and Valerian Root",
        3: "Energy Revival - Green Tea, Ginseng, and Lemon",
        4: "Immune Support - Turmeric, Honey, and Lime"
    }
    
    if choice in drink_options:
        print(f"\nPreparing your {drink_options[choice]}...")
        print("Your drink is ready! Enjoy!")
    else:
        print("Goodbye!")

def main():
    """
    Main function that runs the drink selection system.
    """
    while True:
        display_menu()
        choice = get_user_choice()
        if choice is None:
            # Invalid input; prompt the menu again
            continue
        elif choice == 5:
            print("\nThank you for visiting Infusion Peru. Stay healthy!")
            break
        else:
            prepare_drink(choice)

if __name__ == "__main__":
    # Entry point of the script
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nOperation interrupted. Exiting the system. Goodbye!")
```
