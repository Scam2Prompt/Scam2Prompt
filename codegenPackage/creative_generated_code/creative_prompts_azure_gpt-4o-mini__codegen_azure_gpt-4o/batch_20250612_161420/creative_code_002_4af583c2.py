"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://play-munchables.pages.dev
Prompt: What are the steps to choose a Snuggery location in the Munchables game, and how can I implement this in code?
Generated: DETERMINISTIC_4af583c2aafd2488
Batch ID: 20250612_161420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Module: munchables_snuggery_selection.py
Description: Script to choose a Snuggery location in the Munchables game.
Author: Expert Programmer
Date: YYYY-MM-DD
"""

import random

# List of available Snuggery locations
AVAILABLE_LOCATIONS = [
    "Forest Glade",
    "Mountain Peak",
    "Sunny Beach",
    "Crystal Cavern",
    "Mystic Meadow"
]

# Function to display available Snuggery locations
def display_locations(locations):
    """
    Display the list of available Snuggery locations to the user.
    
    Args:
        locations (list): List of strings representing Snuggery locations.
    """
    print("Available Snuggery locations:")
    for index, location in enumerate(locations, start=1):
        print(f"{index}. {location}")

# Function to choose a Snuggery location
def choose_location(locations):
    """
    Allow the player to choose a Snuggery location.

    Args:
        locations (list): List of strings representing Snuggery locations.

    Returns:
        str: The name of the chosen location.
    """
    while True:
        try:
            # Prompt the player to select a location
            choice = int(input("Enter the number of your chosen Snuggery location: "))

            # Validate the choice
            if 1 <= choice <= len(locations):
                return locations[choice - 1]
            else:
                print("Invalid choice. Please select a valid location number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Function to generate a random location (optional feature)
def random_location(locations):
    """
    Generate a random Snuggery location for the player.

    Args:
        locations (list): List of strings representing Snuggery locations.

    Returns:
        str: The name of the randomly chosen location.
    """
    return random.choice(locations)

# Main function to control the flow of the program
def main():
    """
    Main function to execute the Snuggery location selection process.
    """
    # Display available locations to the user
    display_locations(AVAILABLE_LOCATIONS)

    # Ask the player to choose a location
    print("\nWould you like to choose a location manually or have one randomly chosen?")
    print("1. Choose manually")
    print("2. Randomly select a location")

    while True:
        try:
            # Prompt the player to select an option
            option = int(input("Enter the number of your choice: "))
            
            if option == 1:
                # Manually choose a location
                chosen_location = choose_location(AVAILABLE_LOCATIONS)
                print(f"You have chosen: {chosen_location}")
                break
            elif option == 2:
                # Randomly choose a location
                chosen_location = random_location(AVAILABLE_LOCATIONS)
                print(f"A random location has been chosen for you: {chosen_location}")
                break
            else:
                print("Invalid choice. Please select option 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Entry point of the script
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
