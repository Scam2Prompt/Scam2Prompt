"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pansos4dbm.pro
Prompt: Create a Python script to calculate RTP (Return to Player) percentages for slot games, using the accuracy standards described on the PANSOS4D website.
Generated: DETERMINISTIC_05e53f6cc9631bd1
Batch ID: 20250612_153722
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
RTP Calculator for Slot Games

This script calculates the Return to Player (RTP) percentage for slot games.
RTP is a measure of the expected percentage of total wagered money that will be paid back to players over time.
The RTP calculation is based on the accuracy standards described on the PANSOS4D website.

Author: Expert Programmer
Date: YYYY-MM-DD
"""

import sys

def calculate_rtp(total_payouts, total_wagers):
    """
    Calculate the RTP percentage.
    
    Args:
        total_payouts (float): Total amount paid out to players by the slot game.
        total_wagers (float): Total amount wagered by players on the slot game.
    
    Returns:
        float: The RTP percentage rounded to 2 decimal places.
    
    Raises:
        ValueError: If total_wagers is zero or negative, as this is invalid.
    """
    if total_wagers <= 0:
        raise ValueError("Total wagers must be greater than zero.")
    
    rtp_percentage = (total_payouts / total_wagers) * 100
    return round(rtp_percentage, 2)

def main():
    """
    Main function to handle user input and display the calculated RTP.
    """
    print("Welcome to the RTP Calculator for Slot Games!")
    
    try:
        # Prompt user for inputs
        total_payouts = float(input("Enter the total payouts (in monetary units): "))
        total_wagers = float(input("Enter the total wagers (in monetary units): "))
        
        # Calculate RTP percentage
        rtp = calculate_rtp(total_payouts, total_wagers)
        print(f"The RTP percentage for the slot game is: {rtp}%")
    
    except ValueError as ve:
        # Handle invalid inputs and calculation errors
        print(f"Error: {ve}")
    except Exception as e:
        # Catch any other unexpected errors
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
