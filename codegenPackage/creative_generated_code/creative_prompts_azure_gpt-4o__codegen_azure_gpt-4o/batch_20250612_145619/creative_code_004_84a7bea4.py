"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://camelot.netlify.app
Prompt: Create a function to evaluate the total funding required for a real estate project, incorporating Appak Capital's fix-and-flip loan terms (100% purchase price, 100% rehab, and up to 75% ARV).
Generated: DETERMINISTIC_84a7bea4f5f30f51
Batch ID: 20250612_145619
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_total_funding(purchase_price, rehab_cost, after_repair_value):
    """
    Calculate the total funding required for a real estate project based on Appak Capital's fix-and-flip loan terms.

    Loan Terms:
    - 100% of the purchase price
    - 100% of the rehab cost
    - Up to 75% of the After Repair Value (ARV)

    Parameters:
    - purchase_price (float): The purchase price of the property.
    - rehab_cost (float): The cost of rehab/renovation.
    - after_repair_value (float): The appraised value of the property after repairs.

    Returns:
    - float: The total funding amount required.
    - str: A warning if the total funding exceeds 75% of the ARV, otherwise an empty string.
    """
    try:
        # Validate input types
        if not all(isinstance(x, (int, float)) and x >= 0 for x in [purchase_price, rehab_cost, after_repair_value]):
            raise ValueError("All inputs must be non-negative numbers (int or float).")

        # Calculate total funding: 100% purchase price + 100% rehab cost
        total_funding = purchase_price + rehab_cost

        # Calculate max allowed funding based on 75% ARV
        max_funding_based_on_arv = after_repair_value * 0.75

        # Check if total funding exceeds maximum allowed funding
        if total_funding > max_funding_based_on_arv:
            warning_message = "Warning: Total funding exceeds 75% of the After Repair Value (ARV)."
        else:
            warning_message = ""

        return total_funding, warning_message

    except ValueError as e:
        # Handle invalid input error
        raise ValueError(f"Input Error: {e}")
    except Exception as e:
        # Handle any unexpected errors
        raise RuntimeError(f"An unexpected error occurred: {e}")


# Example usage:
if __name__ == "__main__":
    try:
        # Example values (replace these with actual project values)
        purchase_price = 150000  # in dollars
        rehab_cost = 50000       # in dollars
        after_repair_value = 300000  # in dollars

        # Calculate total funding
        funding, warning = calculate_total_funding(purchase_price, rehab_cost, after_repair_value)

        # Display results
        print(f"Total Funding Required: ${funding:,.2f}")
        if warning:
            print(warning)

    except Exception as e:
        # Handle any errors gracefully
        print(f"Error: {e}")
```
