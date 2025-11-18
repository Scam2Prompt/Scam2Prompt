"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ecoswap.us
Prompt: Write a Python script to calculate the resale value of an Apple device based on its model, year, and condition, referencing EcoSwap's inventory pricing structure.
Generated: DETERMINISTIC_0305888414279f65
Batch ID: 20250612_154322
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def get_resale_value(model, year, condition):
    """
    Calculate the resale value of an Apple device based on model, year, and condition.
    
    Args:
        model (str): The model of the Apple device (e.g., "iPhone X", "MacBook Pro").
        year (int): The year of manufacture.
        condition (str): The condition of the device, one of ["Excellent", "Good", "Fair", "Poor"].
    
    Returns:
        float: The resale value of the device in USD, or None if invalid input.
    """
    # Pricing structure from EcoSwap inventory
    base_prices = {
        "iPhone X": 600,
        "iPhone 12": 800,
        "MacBook Pro": 1500,
        "MacBook Air": 1000,
        "iPad Pro": 900,
        "iPad Air": 700
    }

    # Depreciation rates per year (%)
    yearly_depreciation = 0.2  # 20% decrease per year

    # Condition multipliers
    condition_multipliers = {
        "Excellent": 1.0,   # Full value
        "Good": 0.8,        # 80% of value
        "Fair": 0.5,        # 50% of value
        "Poor": 0.3         # 30% of value
    }

    # Validate inputs
    if model not in base_prices:
        print(f"Error: Unknown model '{model}'. Please check EcoSwap's inventory.")
        return None
    if condition not in condition_multipliers:
        print(f"Error: Invalid condition '{condition}'. Must be one of ['Excellent', 'Good', 'Fair', 'Poor'].")
        return None
    if year < 2000 or year > 2023:  # Adjust the range as needed
        print(f"Error: Invalid year '{year}'. Please enter a year between 2000 and 2023.")
        return None

    # Calculate years of depreciation
    current_year = 2023  # Update to dynamic year if needed
    age = current_year - year
    if age < 0:
        print("Error: Year of manufacture cannot be in the future.")
        return None

    # Calculate resale value
    base_price = base_prices[model]
    depreciation_factor = max(0, 1 - age * yearly_depreciation)  # Ensure non-negative value
    condition_factor = condition_multipliers[condition]
    resale_value = base_price * depreciation_factor * condition_factor

    return round(resale_value, 2)


if __name__ == "__main__":
    # Command-line interface for the script
    try:
        # Collect user inputs
        model = input("Enter the Apple device model (e.g., 'iPhone X', 'MacBook Pro'): ").strip()
        year = int(input("Enter the year of manufacture (e.g., 2018): ").strip())
        condition = input("Enter the condition ['Excellent', 'Good', 'Fair', 'Poor']: ").strip()

        # Calculate resale value
        value = get_resale_value(model, year, condition)
        if value is not None:
            print(f"The estimated resale value of your {model} ({year}, {condition}) is ${value:.2f}.")
    except ValueError:
        print("Error: Invalid input. Please ensure year is a number and other fields are correctly formatted.")
    except Exception as e:
        print(f"Unexpected error occurred: {e}")
        sys.exit(1)
```
