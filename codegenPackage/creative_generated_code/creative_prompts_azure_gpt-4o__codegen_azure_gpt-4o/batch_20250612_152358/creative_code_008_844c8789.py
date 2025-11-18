"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://runecoin-6px.pages.dev
Prompt: Create a Python script to calculate the remaining allocated supply of Runecoin based on the surplus supply and total allocated supply metrics.
Generated: DETERMINISTIC_844c8789a575541e
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Python Script to Calculate the Remaining Allocated Supply of Runecoin.

This script calculates the remaining allocated supply of Runecoin 
based on the surplus supply and total allocated supply provided by the user.

Usage:
    Run the script and input the required metrics when prompted.

Author: Expert Programmer
"""

def calculate_remaining_supply(total_allocated_supply, surplus_supply):
    """
    Calculate the remaining allocated supply of Runecoin.

    Parameters:
        total_allocated_supply (float): Total allocated supply of Runecoin.
        surplus_supply (float): Surplus supply of Runecoin.

    Returns:
        float: Remaining allocated supply of Runecoin.
    """
    try:
        # Ensure inputs are valid numbers
        if total_allocated_supply < 0 or surplus_supply < 0:
            raise ValueError("Supply values cannot be negative.")

        # Calculate remaining allocated supply
        remaining_supply = total_allocated_supply - surplus_supply

        # Ensure the remaining supply is not negative
        if remaining_supply < 0:
            raise ValueError("Surplus supply exceeds total allocated supply.")
        
        return remaining_supply

    except ValueError as ve:
        # Handle invalid input gracefully
        print(f"Error: {ve}")
        return None
    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"An unexpected error occurred: {e}")
        return None

def main():
    """
    Main function to execute the Runecoin supply calculation script.
    """
    try:
        # Prompt user for inputs
        print("Welcome to the Runecoin Remaining Supply Calculator!")
        total_allocated_supply = float(input("Enter the total allocated supply of Runecoin: "))
        surplus_supply = float(input("Enter the surplus supply of Runecoin: "))

        # Perform calculation
        remaining_supply = calculate_remaining_supply(total_allocated_supply, surplus_supply)

        if remaining_supply is not None:
            # Display the result
            print(f"The remaining allocated supply of Runecoin is: {remaining_supply:.2f}")
        else:
            print("Calculation failed due to invalid inputs.")
    
    except ValueError:
        # Handle invalid numeric input
        print("Error: Please provide a valid numeric input.")
    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"An unexpected error occurred: {e}")

# Entry point for the script
if __name__ == "__main__":
    main()
```
