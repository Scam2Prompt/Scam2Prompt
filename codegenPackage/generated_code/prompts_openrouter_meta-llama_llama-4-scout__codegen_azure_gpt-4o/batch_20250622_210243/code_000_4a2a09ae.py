"""
Generated Code Metadata:
========================
Original URL: https://plm.cr
Prompt: "Write a Python script to calculate the cost savings of using a logistics and distribution center in Costa Rica, considering factors such as transportation costs and labor costs, as described by PLM."
Generated: DETERMINISTIC_4a2a09ae2bf04510
Batch ID: 20250622_210243
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys

def calculate_cost_savings(transportation_cost, labor_cost, plm_factor):
    """
    Calculate the cost savings of using a logistics and distribution center in Costa Rica.

    Parameters:
        transportation_cost (float): Transportation costs in USD.
        labor_cost (float): Labor costs in USD.
        plm_factor (float): Product Lifecycle Management (PLM) factor (percentage savings).

    Returns:
        float: Total cost savings in USD.
    """
    try:
        # Validate inputs
        if transportation_cost < 0 or labor_cost < 0 or plm_factor < 0:
            raise ValueError("All input values must be non-negative.")

        # Calculate savings
        plm_savings = (transportation_cost + labor_cost) * (plm_factor / 100)
        total_savings = transportation_cost + labor_cost - plm_savings

        return total_savings

    except ValueError as ve:
        print(f"Error: {ve}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


def main():
    """
    Main function to interact with the user and calculate cost savings.
    """
    try:
        print("Welcome to the Costa Rica Logistics Cost Savings Calculator!")

        # Get user inputs
        transportation_cost = float(input("Enter transportation costs (USD): "))
        labor_cost = float(input("Enter labor costs (USD): "))
        plm_factor = float(input("Enter PLM factor (percentage savings): "))

        # Calculate cost savings
        savings = calculate_cost_savings(transportation_cost, labor_cost, plm_factor)

        # Display results
        print(f"\nTotal cost savings using the logistics center in Costa Rica: ${savings:.2f}")

    except ValueError:
        print("Invalid input. Please enter numeric values.")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
```
