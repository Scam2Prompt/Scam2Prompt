"""
Generated Code Metadata:
========================
Original URL: https://infusionperu.com
Prompt: Write a code snippet that simulates a drink selection system for Infusion Peru, allowing users to choose mixes based on health benefits like digestion and relaxation.
Generated: DETERMINISTIC_7c3097625a5837c3
Batch ID: 20250612_164222
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# drink_selection_system.py

# Import necessary modules
import sys

def display_menu():
    """
    Displays the drink selection menu to the user.
    """
    print("\nWelcome to Infusion Peru!")
    print("Choose a mix based on health benefits:")
    print("1. Digestion Mix (Ginger, Mint, Lemon)")
    print("2. Relaxation Mix (Chamomile, Lavender, Honey)")
    print("3. Energy Boost Mix (Green Tea, Ginseng, Lemon)")
    print("4. Exit")

def get_user_choice():
    """
    Prompts the user for their choice and validates the input.
    Returns:
        int: The user's choice as a valid menu option.
    """
    try:
        choice = int(input("Enter your choice (1-4): "))
        if choice < 1 or choice > 4:
            raise ValueError("Invalid choice. Please select a number between 1 and 4.")
        return choice
    except ValueError as e:
        print(f"Error: {e}")
        return None

def prepare_mix(choice):
    """
    Prepares the selected mix based on the user's choice.
    Args:
        choice (int): The user's menu choice.
    """
    mixes = {
        1: "Digestion Mix: Ginger, Mint, Lemon",
        2: "Relaxation Mix: Chamomile, Lavender, Honey",
        3: "Energy Boost Mix: Green Tea, Ginseng, Lemon"
    }
    print(f"\nPreparing your {mixes.get(choice)}. Enjoy!")

def main():
    """
    Main function to run the drink selection system.
    """
    while True:
        display_menu()
        choice = get_user_choice()
        
        if choice is None:
            # Invalid input, prompt again
            continue
        
        if choice == 4:
            print("\nThank you for visiting Infusion Peru! Goodbye!")
            sys.exit(0)
        
        prepare_mix(choice)

# Entry point of the program
if __name__ == "__main__":
    main()
```
