"""
Generated Code Metadata:
========================
Original URL: https://avasconcelos.adv.br
Prompt: "Write a code snippet in Python to calculate the reduction of 75% of IRPJ tax for a company in the Northeast region of Brazil, considering the MP 2.199-14/2001 law."
Generated: DETERMINISTIC_1d9658cca7d41be2
Batch ID: 20250622_210655
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

def calculate_irpj_reduction(original_tax_amount):
    """
    Calculate the 75% reduction of IRPJ tax for companies in the Northeast region of Brazil
    under the MP 2.199-14/2001 law.

    Args:
        original_tax_amount (float): The original IRPJ tax amount.

    Returns:
        float: The reduced IRPJ tax amount.
    """
    try:
        # Validate input
        if original_tax_amount < 0:
            raise ValueError("Tax amount cannot be negative.")

        # Calculate the reduction (75% off)
        reduction_percentage = 0.75
        reduced_tax_amount = original_tax_amount * (1 - reduction_percentage)

        return reduced_tax_amount

    except ValueError as ve:
        # Handle invalid input
        print(f"Error: {ve}", file=sys.stderr)
        return None
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        return None


# Example usage
if __name__ == "__main__":
    try:
        # Input: Original IRPJ tax amount
        original_tax_amount = float(input("Enter the original IRPJ tax amount: "))

        # Calculate the reduced tax amount
        reduced_tax = calculate_irpj_reduction(original_tax_amount)

        if reduced_tax is not None:
            print(f"The reduced IRPJ tax amount is: {reduced_tax:.2f}")
        else:
            print("Failed to calculate the reduced tax amount.")

    except ValueError:
        print("Invalid input. Please enter a valid number.", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
```
