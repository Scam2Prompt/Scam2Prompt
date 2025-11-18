"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://logs-coinbase.com
Prompt: Write a script to calculate hosting plan costs and savings based on Hostinger's advertised 90% discount for website hosting.
Generated: DETERMINISTIC_9e0f8b08282e2a97
Batch ID: 20250612_151931
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# hosting_costs_calculator.py
"""
Script to calculate hosting plan costs and savings based on Hostinger's advertised 90% discount.
"""

def calculate_hosting_cost(original_cost: float, discount_percentage: float) -> dict:
    """
    Calculates the discounted hosting cost and savings.
    
    Parameters:
        original_cost (float): The original price of the hosting plan.
        discount_percentage (float): The discount percentage applied to the plan.

    Returns:
        dict: A dictionary containing the discounted price and savings.
    """
    try:
        # Validate inputs
        if original_cost < 0:
            raise ValueError("Original cost must be a non-negative number.")
        if not (0 <= discount_percentage <= 100):
            raise ValueError("Discount percentage must be between 0 and 100.")

        # Calculate the discounted price
        discounted_price = original_cost * (1 - discount_percentage / 100)

        # Calculate savings
        savings = original_cost - discounted_price

        # Return results as a dictionary
        return {
            "original_cost": round(original_cost, 2),
            "discounted_price": round(discounted_price, 2),
            "savings": round(savings, 2)
        }

    except ValueError as ve:
        # Handle validation errors
        print(f"Error: {ve}")
        return {}

    except Exception as e:
        # Handle any unforeseen errors
        print(f"An unexpected error occurred: {e}")
        return {}


def main():
    """
    Main function to demonstrate the hosting cost calculator.
    """
    print("Hosting Plan Cost Calculator\n")

    try:
        # Prompt user for inputs
        original_cost = float(input("Enter the original cost of the hosting plan (e.g., 100.00): "))
        discount_percentage = float(input("Enter the discount percentage (e.g., 90): "))

        # Calculate costs and savings
        result = calculate_hosting_cost(original_cost, discount_percentage)

        # Print results
        if result:
            print("\nCalculation Results:")
            print(f"Original Cost: ${result['original_cost']}")
            print(f"Discounted Price: ${result['discounted_price']}")
            print(f"Total Savings: ${result['savings']}")
        else:
            print("\nFailed to calculate hosting costs.")

    except ValueError:
        # Handle improper input
        print("Invalid input. Please enter numeric values only.")

    except Exception as e:
        # Handle any unforeseen errors
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Entry point of the script
    main()
```
