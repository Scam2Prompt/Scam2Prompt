"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cabinet-customs.com.ua
Prompt: Generate a program to calculate the import costs of a passenger car using the "Automobile Calculator" feature described on the Single Window Portal.
Generated: DETERMINISTIC_473a0c9cadb697c0
Batch ID: 20250612_151429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Program to calculate the import costs of a passenger car
# using the "Automobile Calculator" feature.

import sys

def get_float_input(prompt):
    """
    Utility function to get valid float input from the user.
    Re-prompts the user in case of invalid input.
    """
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                raise ValueError("Value cannot be negative.")
            return value
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a valid number.")

def calculate_import_costs(car_value, import_tax_rate, customs_fee, other_fees):
    """
    Calculate the total import cost of the automobile.
    
    Parameters:
    - car_value (float): The declared value of the car (in USD).
    - import_tax_rate (float): The import tax rate (percentage, e.g., 20 for 20%).
    - customs_fee (float): Fixed customs fee (in USD).
    - other_fees (float): Fixed other fees (inspection, licensing, etc.) in USD.
    
    Returns:
    - total_cost (float): The total import cost of the automobile.
    """
    try:
        import_tax = (import_tax_rate / 100) * car_value
        total_cost = car_value + import_tax + customs_fee + other_fees
        return total_cost
    except Exception as e:
        print(f"Error occurred during cost calculation: {e}")
        sys.exit(1)

def main():
    """
    Main function to run the automobile import cost calculator.
    """
    print("Welcome to the Automobile Import Cost Calculator!\n")
    
    # Step 1: Get inputs from the user
    car_value = get_float_input("Enter the declared value of the car (in USD): ")
    import_tax_rate = get_float_input("Enter the import tax rate (percentage): ")
    customs_fee = get_float_input("Enter the customs fee (in USD): ")
    other_fees = get_float_input("Enter other fees (inspection, licensing, etc. in USD): ")
    
    # Step 2: Calculate the import costs
    total_cost = calculate_import_costs(car_value, import_tax_rate, customs_fee, other_fees)

    # Step 3: Display the total import cost
    print("\n=== Calculation Results ===")
    print(f"Declared Car Value: ${car_value:.2f}")
    print(f"Import Tax Rate: {import_tax_rate:.2f}%")
    print(f"Customs Fee: ${customs_fee:.2f}")
    print(f"Other Fees: ${other_fees:.2f}")
    print(f"Total Import Cost: ${total_cost:.2f}")

if __name__ == "__main__":
    main()
```
