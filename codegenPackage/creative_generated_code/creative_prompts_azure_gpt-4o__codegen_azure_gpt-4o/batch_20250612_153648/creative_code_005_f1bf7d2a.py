"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://longhuigolf.com
Prompt: Develop a program to calculate the abrasion resistance of golf grips based on input data from a DIN abrasion tester, as mentioned in Longhui Golf’s quality assurance section.
Generated: DETERMINISTIC_f1bf7d2a538c4711
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Program to calculate the abrasion resistance of golf grips using input data 
from a DIN abrasion tester. The program calculates abrasion resistance based 
on weight loss after testing, and categorizes grips based on their performance.

Author: [Your Name]
Date: [Today's Date]
"""

# Import necessary modules
import sys

def calculate_abrasion_resistance(initial_weight, final_weight, testing_distance):
    """
    Calculate the abrasion resistance of a golf grip.

    Args:
        initial_weight (float): Initial weight of the grip (in grams).
        final_weight (float): Final weight of the grip after testing (in grams).
        testing_distance (float): The distance (in meters) over which the abrasion test was performed.

    Returns:
        float: Abrasion resistance value (grams lost per meter).
    """
    try:
        # Ensure no division by zero
        if testing_distance <= 0:
            raise ValueError("Testing distance must be greater than zero.")
        
        # Calculate abrasion resistance
        weight_loss = initial_weight - final_weight
        abrasion_resistance = weight_loss / testing_distance
        return round(abrasion_resistance, 4)  # Rounded to 4 decimal places
    except Exception as e:
        print(f"Error calculating abrasion resistance: {e}")
        sys.exit(1)

def categorize_grip(abrasion_resistance):
    """
    Categorize the grip based on abrasion resistance.

    Args:
        abrasion_resistance (float): Abrasion resistance value.

    Returns:
        str: Category of the grip (High, Medium, or Low resistance).
    """
    # Categorization thresholds (example values, can be adjusted based on standards)
    try:
        if abrasion_resistance < 0.01:
            return "High Resistance"
        elif 0.01 <= abrasion_resistance <= 0.03:
            return "Medium Resistance"
        else:
            return "Low Resistance"
    except Exception as e:
        print(f"Error in categorizing grip: {e}")
        sys.exit(1)

def main():
    """
    Main program execution function.
    Handles user input, performs calculations, and displays results.
    """
    try:
        print("Golf Grip Abrasion Resistance Calculator")
        print("---------------------------------------")
        
        # Input data from user
        initial_weight = float(input("Enter the initial weight of the grip (in grams): "))
        final_weight = float(input("Enter the final weight of the grip after testing (in grams): "))
        testing_distance = float(input("Enter the testing distance (in meters): "))
        
        # Validate input
        if initial_weight <= 0 or final_weight <= 0 or initial_weight <= final_weight:
            raise ValueError("Invalid weight values provided.")
        
        # Perform calculations
        abrasion_resistance = calculate_abrasion_resistance(initial_weight, final_weight, testing_distance)
        category = categorize_grip(abrasion_resistance)
        
        # Display results
        print(f"\nAbrasion Resistance: {abrasion_resistance} grams/meter")
        print(f"Grip Category: {category}")
    
    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"Unexpected Error: {e}")
    finally:
        print("Program execution finished.")

# Entry point for the program
if __name__ == "__main__":
    main()
```
