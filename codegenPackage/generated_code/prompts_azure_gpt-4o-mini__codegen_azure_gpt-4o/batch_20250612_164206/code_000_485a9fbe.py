"""
Generated Code Metadata:
========================
Original URL: https://smkn1kadipaten.sch.id
Prompt: Generate a Python script that implements a character education program based on the values of Pancasila as described on the SMKN 1 Kadipaten website.
Generated: DETERMINISTIC_485a9fbeb890a8b3
Batch ID: 20250612_164206
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Character Education Program Based on Pancasila
This script implements a character education program inspired by the values of Pancasila.
Pancasila is the foundational philosophical theory of Indonesia, consisting of five principles:
1. Belief in the One and Only God
2. Just and Civilized Humanity
3. Unity of Indonesia
4. Democracy Guided by the Inner Wisdom in the Unanimity Arising Out of Deliberation Amongst Representatives
5. Social Justice for All Indonesians

Author: [Your Name]
Date: [Insert Date]
"""

import sys

# Define the Pancasila principles
PANCASILA_VALUES = [
    "Belief in the One and Only God",
    "Just and Civilized Humanity",
    "Unity of Indonesia",
    "Democracy Guided by the Inner Wisdom in the Unanimity Arising Out of Deliberation Amongst Representatives",
    "Social Justice for All Indonesians"
]

def display_pancasila_values():
    """
    Display the values of Pancasila to the user.
    """
    print("Pancasila Values:")
    for idx, value in enumerate(PANCASILA_VALUES, start=1):
        print(f"{idx}. {value}")

def educate_character(value_index):
    """
    Provide education based on the selected Pancasila value.
    
    Args:
        value_index (int): Index of the selected Pancasila value.
    """
    try:
        # Validate the index
        if value_index < 1 or value_index > len(PANCASILA_VALUES):
            raise ValueError("Invalid selection. Please choose a number between 1 and 5.")
        
        # Display the selected value and its educational message
        selected_value = PANCASILA_VALUES[value_index - 1]
        print(f"\nYou selected: {selected_value}")
        print("Educational Message:")
        if value_index == 1:
            print("Foster a sense of spirituality and respect for religious diversity.")
        elif value_index == 2:
            print("Promote empathy, kindness, and respect for human rights.")
        elif value_index == 3:
            print("Encourage national pride and unity among all citizens.")
        elif value_index == 4:
            print("Advocate for democratic principles and active participation in decision-making.")
        elif value_index == 5:
            print("Strive for equality and fairness in society.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    """
    Main function to run the character education program.
    """
    print("Welcome to the Character Education Program Based on Pancasila!")
    display_pancasila_values()
    
    try:
        # Prompt the user to select a Pancasila value
        user_input = input("\nEnter the number corresponding to the Pancasila value you'd like to learn about (1-5): ")
        value_index = int(user_input)
        educate_character(value_index)
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 5.")
    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("\nThank you for participating in the Character Education Program!")

if __name__ == "__main__":
    # Entry point of the script
    main()
```
