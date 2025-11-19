"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://miningbase.cloud
Prompt: Create a Python script that calculates potential earnings from free mining power on Bitspeed based on hourly rates.
Generated: DETERMINISTIC_df922ddb0f3a15f6
Batch ID: 20250612_161331
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Python Script: Calculate potential earnings from free mining power on Bitspeed based on hourly rates.

This script computes potential earnings using free mining power provided by Bitspeed. 
The user inputs the hourly mining power rate and the script calculates the earnings over a specified duration.

Author: Expert Programmer
Date: October 2023
"""

# Import necessary libraries
import sys

def calculate_earnings(hourly_rate, hours):
    """
    Calculate potential earnings based on hourly rate and duration.

    Parameters:
        hourly_rate (float): Mining power earnings per hour.
        hours (int): Number of hours to compute earnings for.
    
    Returns:
        float: Total potential earnings.
    """
    try:
        # Ensure inputs are valid
        if hourly_rate < 0:
            raise ValueError("Hourly rate must be a positive number.")
        if hours < 0:
            raise ValueError("Hours must be a positive integer.")
        
        # Calculate total earnings
        return hourly_rate * hours
    except ValueError as e:
        # Handle invalid input errors
        print(f"Error: {e}")
        sys.exit(1)

def main():
    """
    Main function to execute the script.
    """
    print("Bitspeed Mining Earnings Calculator")
    print("-----------------------------------")
    
    try:
        # Prompt user for input
        hourly_rate = float(input("Enter hourly mining power rate (e.g., 0.05): "))
        hours = int(input("Enter number of hours: "))
        
        # Calculate potential earnings
        total_earnings = calculate_earnings(hourly_rate, hours)
        
        # Display the result
        print(f"\nPotential earnings for {hours} hours at an hourly rate of {hourly_rate}: {total_earnings:.2f} units")
    except ValueError:
        # Handle invalid input errors
        print("Error: Please enter valid numeric inputs for hourly rate and hours.")
        sys.exit(1)
    except Exception as e:
        # Catch any unexpected errors
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

# Entry point for the script
if __name__ == "__main__":
    main()
```
