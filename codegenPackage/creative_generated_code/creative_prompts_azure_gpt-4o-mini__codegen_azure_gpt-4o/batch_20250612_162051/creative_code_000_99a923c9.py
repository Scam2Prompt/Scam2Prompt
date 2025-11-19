"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://avasconcelos.adv.br
Prompt: Write a Python script that calculates the potential tax savings from the MP 2.199-14/2001 for a company in the energy sector looking to reduce its IRPJ by 75%.
Generated: DETERMINISTIC_99a923c992e6cb00
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Python script to calculate potential tax savings for a company in the energy sector
using the provisions of MP 2.199-14/2001 which allows a reduction of IRPJ by 75%.

Inputs:
- Gross Profit (Annual)
- IRPJ Tax Rate (Percentage)

Outputs:
- Initial IRPJ value
- Reduced IRPJ value
- Potential Tax Savings
"""

def calculate_tax_savings(gross_profit, irpj_rate):
    """
    Calculate the potential tax savings based on MP 2.199-14/2001.

    Parameters:
        gross_profit (float): Annual gross profit of the company.
        irpj_rate (float): IRPJ tax rate as a percentage.

    Returns:
        dict: A dictionary containing initial IRPJ value, reduced IRPJ value,
              and potential tax savings.
    """
    try:
        # Validate inputs
        if gross_profit < 0 or irpj_rate < 0:
            raise ValueError("Gross profit and IRPJ rate must be non-negative.")

        # Calculate initial IRPJ amount
        initial_irpj = gross_profit * (irpj_rate / 100)

        # Calculate reduced IRPJ amount (75% reduction)
        reduced_irpj = initial_irpj * 0.25

        # Calculate tax savings
        tax_savings = initial_irpj - reduced_irpj

        # Return results as a dictionary
        return {
            "initial_irpj": round(initial_irpj, 2),
            "reduced_irpj": round(reduced_irpj, 2),
            "tax_savings": round(tax_savings, 2)
        }

    except Exception as e:
        # Handle unexpected errors
        return {"error": f"An error occurred: {str(e)}"}

if __name__ == "__main__":
    import sys

    # Prompt user for inputs
    try:
        print("Welcome to the Tax Savings Calculator (MP 2.199-14/2001)!")
        gross_profit = float(input("Enter the annual gross profit of the company (in monetary units): "))
        irpj_rate = float(input("Enter the IRPJ tax rate (percentage): "))

        # Calculate and display tax savings
        results = calculate_tax_savings(gross_profit, irpj_rate)
        
        if "error" in results:
            print(results["error"])
        else:
            print("\nTax Savings Calculation Results:")
            print(f"Initial IRPJ Value: {results['initial_irpj']}")
            print(f"Reduced IRPJ Value (75% reduction): {results['reduced_irpj']}")
            print(f"Potential Tax Savings: {results['tax_savings']}")

    except ValueError:
        print("Invalid input. Please enter numeric values for gross profit and IRPJ rate.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
```
