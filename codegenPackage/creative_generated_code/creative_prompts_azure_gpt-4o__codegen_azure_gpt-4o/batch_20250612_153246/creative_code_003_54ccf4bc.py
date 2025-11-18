"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nodoitalia.com
Prompt: Write a program that simulates a custom furniture design tool, allowing users to select materials (e.g., Olyna), colors, and shapes for outdoor furniture, inspired by Nodo Italia's customization options.
Generated: DETERMINISTIC_54ccf4bc3d0f6f1c
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

# Define constants for available options
MATERIALS = ["Olyna", "Teak", "Metal", "Plastic"]
COLORS = ["Red", "Blue", "Green", "Black", "White"]
SHAPES = ["Round", "Square", "Rectangular", "Hexagonal"]

def display_options(options, option_type):
    """
    Displays a list of options for the user to select from.

    Args:
        options (list): The available options to display.
        option_type (str): The type of options (e.g., Material, Color).
    """
    print(f"\nAvailable {option_type}:")
    for idx, option in enumerate(options, start=1):
        print(f"{idx}. {option}")

def get_user_choice(options, option_type):
    """
    Gets the user's selection from the available options.

    Args:
        options (list): The available options to choose from.
        option_type (str): The type of options (e.g., Material, Color).

    Returns:
        str: The selected option.
    """
    while True:
        try:
            display_options(options, option_type)
            choice = int(input(f"Select a {option_type} (Enter the number): "))
            if 1 <= choice <= len(options):
                return options[choice - 1]
            else:
                print(f"Invalid choice. Please select a number between 1 and {len(options)}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    """
    Main function to run the furniture customization tool.
    """
    print("Welcome to the Custom Furniture Design Tool!")
    print("Customize your outdoor furniture by selecting materials, colors, and shapes.\n")

    try:
        # Get user selections
        material = get_user_choice(MATERIALS, "Material")
        color = get_user_choice(COLORS, "Color")
        shape = get_user_choice(SHAPES, "Shape")

        # Display the final customization summary
        print("\nYour custom furniture design:")
        print(f"Material: {material}")
        print(f"Color: {color}")
        print(f"Shape: {shape}")
    except KeyboardInterrupt:
        print("\nCustomization process interrupted. Exiting...")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
