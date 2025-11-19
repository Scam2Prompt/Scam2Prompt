"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trialsonicsolutions.com
Prompt: Can you provide a code snippet for calculating potential savings from using ultrasonic cleaning services for automotive parts?
Generated: DETERMINISTIC_3bd99ba06abd2ab8
Batch ID: 20250612_140414
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_potential_savings(current_cleaning_cost, ultrasonic_cleaning_cost, parts_cleaned_per_month):
    """
    Calculate potential savings from using ultrasonic cleaning services for automotive parts.

    Args:
        current_cleaning_cost (float): Current cost per part for cleaning using traditional methods.
        ultrasonic_cleaning_cost (float): Proposed cost per part using ultrasonic cleaning services.
        parts_cleaned_per_month (int): Number of parts cleaned per month.

    Returns:
        float: Monthly savings when switching to ultrasonic cleaning.
    """
    try:
        # Validate inputs
        if current_cleaning_cost < 0 or ultrasonic_cleaning_cost < 0 or parts_cleaned_per_month < 0:
            raise ValueError("All input values must be non-negative.")
        
        # Calculate the savings
        savings_per_part = current_cleaning_cost - ultrasonic_cleaning_cost
        total_savings = savings_per_part * parts_cleaned_per_month
        
        return total_savings
    except ValueError as ve:
        print(f"Input Error: {ve}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        return None

def main():
    """
    Main function to interact with the user and calculate savings based on their input.
    """
    try:
        print("Ultrasonic Cleaning Savings Calculator")
        
        # Get user input
        current_cleaning_cost = float(input("Enter the current cleaning cost per part (in USD): "))
        ultrasonic_cleaning_cost = float(input("Enter the ultrasonic cleaning cost per part (in USD): "))
        parts_cleaned_per_month = int(input("Enter the number of parts cleaned per month: "))
        
        # Calculate savings
        savings = calculate_potential_savings(current_cleaning_cost, ultrasonic_cleaning_cost, parts_cleaned_per_month)
        
        # Display the result
        if savings is not None:
            print(f"Potential monthly savings: ${savings:.2f}")
        else:
            print("Unable to calculate savings due to input errors.")
    except ValueError:
        print("Invalid input. Please enter numeric values where applicable.", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)

# Run the script
if __name__ == "__main__":
    main()
```
