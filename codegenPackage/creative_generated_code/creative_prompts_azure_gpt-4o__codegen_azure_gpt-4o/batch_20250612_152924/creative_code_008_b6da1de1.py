"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inmobiliariacapri.com.co
Prompt: Generate a script to calculate rental profitability for property owners, incorporating insurance coverage as mentioned in Inmobiliaria Capri's services.
Generated: DETERMINISTIC_b6da1de172cfa33d
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_rental_profitability(rental_income, monthly_expenses, insurance_cost, additional_costs):
    """
    Calculate rental profitability for property owners.
    
    Parameters:
    rental_income (float): Monthly rental income from the property.
    monthly_expenses (float): Monthly expenses including maintenance, utilities, etc.
    insurance_cost (float): Monthly cost of insurance coverage.
    additional_costs (float): Any additional monthly costs associated with the property.
    
    Returns:
    float: Net monthly profit from the rental property.
    """
    try:
        # Ensure inputs are valid numbers
        for value in [rental_income, monthly_expenses, insurance_cost, additional_costs]:
            if not isinstance(value, (int, float)) or value < 0:
                raise ValueError("All input values must be non-negative numbers.")
        
        # Calculate total costs
        total_costs = monthly_expenses + insurance_cost + additional_costs

        # Calculate net profit
        net_profit = rental_income - total_costs

        return net_profit

    except Exception as e:
        print(f"Error calculating rental profitability: {e}")
        sys.exit(1)


def main():
    """
    Main function to get user input and calculate rental profitability.
    """
    try:
        # Gather input from the user
        print("Welcome to the Rental Profitability Calculator!")
        rental_income = float(input("Enter the monthly rental income (e.g., 1200): "))
        monthly_expenses = float(input("Enter the monthly expenses (e.g., 400): "))
        insurance_cost = float(input("Enter the monthly insurance cost (e.g., 150): "))
        additional_costs = float(input("Enter any additional monthly costs (e.g., 100): "))

        # Calculate rental profitability
        net_profit = calculate_rental_profitability(rental_income, monthly_expenses, insurance_cost, additional_costs)

        # Display results
        print(f"\nNet Monthly Profit: ${net_profit:.2f}")
        if net_profit > 0:
            print("Congratulations! Your property is profitable.")
        elif net_profit == 0:
            print("Your property is breaking even.")
        else:
            print("Warning: Your property is operating at a loss.")

    except ValueError as ve:
        print(f"Invalid input: {ve}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
```
