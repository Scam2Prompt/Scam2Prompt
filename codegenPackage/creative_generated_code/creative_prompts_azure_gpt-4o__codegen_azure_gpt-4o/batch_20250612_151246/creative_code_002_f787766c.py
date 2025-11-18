"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tarileague.pages.dev
Prompt: Create a program to calculate the rarity of Yats based on their generation and rhythm score, and determine whether they unlock turtle shells or sky hammers.
Generated: DETERMINISTIC_f787766c3ca78dda
Batch ID: 20250612_151246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Program to calculate the rarity of Yats based on their generation and rhythm score.
# It also determines whether they unlock turtle shells or sky hammers.

# Import necessary modules
import sys

def calculate_rarity(generation, rhythm_score):
    """
    Calculate the rarity of Yats based on generation and rhythm score.

    Parameters:
        generation (int): The Yat's generation (e.g., 1 for first-gen, 2 for second-gen, etc.).
        rhythm_score (float): The rhythm score of the Yat.

    Returns:
        float: The calculated rarity score.
    """
    try:
        # Ensure valid inputs
        if generation <= 0 or rhythm_score < 0:
            raise ValueError("Generation must be positive and rhythm score must be non-negative.")
        
        # Rarity formula: rarity = (100 / generation) * rhythm_score
        rarity = (100 / generation) * rhythm_score
        return rarity
    except Exception as e:
        print(f"Error calculating rarity: {e}", file=sys.stderr)
        sys.exit(1)  # Exit with error code 1


def determine_unlockable(rarity_score):
    """
    Determine whether a given rarity score unlocks turtle shells or sky hammers.

    Parameters:
        rarity_score (float): The calculated rarity score.

    Returns:
        str: The unlockable item ("Turtle Shells" or "Sky Hammers").
    """
    try:
        # Unlock turtle shells if rarity score is above 150
        if rarity_score > 150:
            return "Turtle Shells"
        # Unlock sky hammers otherwise
        else:
            return "Sky Hammers"
    except Exception as e:
        print(f"Error determining unlockable: {e}", file=sys.stderr)
        sys.exit(1)  # Exit with error code 1


def main():
    """
    Main function to execute the program logic.
    """
    try:
        print("Welcome to the Yat Rarity Calculator!")
        
        # Prompt user for inputs
        generation = int(input("Enter Yat generation (positive integer): "))
        rhythm_score = float(input("Enter Yat rhythm score (non-negative float): "))
        
        # Calculate rarity
        rarity = calculate_rarity(generation, rhythm_score)
        print(f"Calculated Rarity Score: {rarity:.2f}")
        
        # Determine unlockable item
        unlockable_item = determine_unlockable(rarity)
        print(f"This Yat unlocks: {unlockable_item}")
    
    except ValueError as ve:
        print(f"Input Error: {ve}", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
    finally:
        print("Thank you for using the Yat Rarity Calculator!")


if __name__ == "__main__":
    main()
```
