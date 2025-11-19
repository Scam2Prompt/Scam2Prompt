"""
Generated Code Metadata:
========================
Original URL: https://itamarationlinebraz.blogspot.com
Prompt: "Write a Python code to calculate the total cost of purchasing 4 tires with the specifications P 185/65r14 86 T and P 205/50r17 Run Flat 89 V from Itamarati Online, considering a 12x installment plan with no interest."
Generated: DETERMINISTIC_3ac3c39555c740c1
Batch ID: 20250622_212850
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
import sys

def calculate_total_cost(tire_prices, installment_plan):
    """
    Calculate the total cost of purchasing tires and the monthly installment amount.

    Parameters:
        tire_prices (list): List of tire prices.
        installment_plan (int): Number of installments.

    Returns:
        tuple: Total cost and monthly installment amount.
    """
    try:
        # Calculate the total cost
        total_cost = sum(tire_prices)
        
        # Calculate the monthly installment amount
        monthly_installment = total_cost / installment_plan
        
        return total_cost, monthly_installment
    except Exception as e:
        # Handle unexpected errors
        print(f"An error occurred: {e}", file=sys.stderr)
        return None, None

def main():
    """
    Main function to calculate the total cost of purchasing tires.
    """
    # Tire specifications and prices (example prices in USD)
    tire_specs = {
        "P 185/65r14 86 T": 75.00,  # Price per tire
        "P 205/50r17 Run Flat 89 V": 150.00  # Price per tire
    }
    
    # Number of tires to purchase
    num_tires = 4
    
    # Installment plan (12x with no interest)
    installment_plan = 12
    
    try:
        # Calculate the total price for each type of tire
        tire_prices = [
            tire_specs["P 185/65r14 86 T"] * num_tires,
            tire_specs["P 205/50r17 Run Flat 89 V"] * num_tires
        ]
        
        # Calculate the total cost and monthly installment
        total_cost, monthly_installment = calculate_total_cost(tire_prices, installment_plan)
        
        if total_cost is not None and monthly_installment is not None:
            # Display the results
            print(f"Total cost of purchasing the tires: ${total_cost:.2f}")
            print(f"Monthly installment amount (12x no interest): ${monthly_installment:.2f}")
        else:
            print("Failed to calculate the total cost.")
    except KeyError as e:
        # Handle missing tire specifications
        print(f"Error: Missing tire specification - {e}", file=sys.stderr)
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}", file=sys.stderr)

# Entry point of the program
if __name__ == "__main__":
    main()
```
