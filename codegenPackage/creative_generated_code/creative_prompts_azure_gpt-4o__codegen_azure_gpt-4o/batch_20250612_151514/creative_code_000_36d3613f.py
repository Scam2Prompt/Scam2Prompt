"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coastalboatrentals.co.za
Prompt: Write a Python script to create a boat rental booking system that includes options for selecting boats like "Panache Charlie" or "Infanta Bravo" and watersports accessories such as wakeboards or life jackets.
Generated: DETERMINISTIC_36d3613faa1321ec
Batch ID: 20250612_151514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Boat Rental Booking System

This Python script allows users to book boats and optional watersports accessories.
It includes:
- Boat selection
- Accessory selection
- Booking summary
- Error handling and validation

Author: Professional Developer
"""

# Import necessary library
import sys

def display_boats():
    """
    Display available boats for selection.
    """
    print("\nAvailable Boats:")
    print("1. Panache Charlie")
    print("2. Infanta Bravo")

def display_accessories():
    """
    Display available watersports accessories for selection.
    """
    print("\nAvailable Accessories:")
    print("1. Wakeboard")
    print("2. Life Jacket")
    print("3. None")

def get_user_choice(prompt, valid_choices):
    """
    Prompt the user for a valid choice.
    
    :param prompt: The prompt to display to the user.
    :param valid_choices: A list of valid choices.
    :return: The user's selected choice.
    """
    while True:
        try:
            choice = int(input(prompt))
            if choice in valid_choices:
                return choice
            else:
                print(f"Invalid choice. Please select from {valid_choices}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    """
    Main function for the boat rental booking system.
    """
    print("Welcome to the Boat Rental Booking System!")

    # Step 1: Select a boat
    display_boats()
    boat_choice = get_user_choice("Please select a boat (1-2): ", [1, 2])
    
    if boat_choice == 1:
        selected_boat = "Panache Charlie"
    else:
        selected_boat = "Infanta Bravo"

    # Step 2: Select accessories
    display_accessories()
    accessory_choice = get_user_choice("Please select an accessory (1-3): ", [1, 2, 3])
    
    if accessory_choice == 1:
        selected_accessory = "Wakeboard"
    elif accessory_choice == 2:
        selected_accessory = "Life Jacket"
    else:
        selected_accessory = "None"

    # Display booking summary
    print("\nBooking Summary:")
    print(f"Boat Selected: {selected_boat}")
    print(f"Accessory Selected: {selected_accessory}")
    print("Thank you for booking with us!")

# Entry point of the script
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
        sys.exit(1)
```
