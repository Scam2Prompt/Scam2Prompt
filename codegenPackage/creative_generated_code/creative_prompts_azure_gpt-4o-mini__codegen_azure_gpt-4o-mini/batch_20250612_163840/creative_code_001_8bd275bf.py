"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://camelot.netlify.app
Prompt: Write a Python function that calculates the maximum loan amount for a Fix and Flip project based on the purchase price and ARV, as described on Appak Capital's website.
Generated: DETERMINISTIC_8bd275bf740d110b
Batch ID: 20250612_163840
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_max_loan_amount(purchase_price: float, arv: float, renovation_cost: float) -> float:
    """
    Calculate the maximum loan amount for a Fix and Flip project.
    
    Parameters:
    purchase_price (float): The purchase price of the property.
    arv (float): The After Repair Value of the property.
    renovation_cost (float): The estimated cost of renovations.

    Returns:
    float: The maximum loan amount for the project.

    Raises:
    ValueError: If any input is negative or if purchase_price is greater than arv.
    """
    
    # Validate inputs
    if purchase_price < 0 or arv < 0 or renovation_cost < 0:
        raise ValueError("Purchase price, ARV, and renovation cost must be non-negative.")
    
    if purchase_price > arv:
        raise ValueError("Purchase price cannot be greater than ARV.")

    # Calculation based on standard Fix and Flip lending practices
    max_loan_based_on_arv = arv * 0.70  # Typically lenders will finance up to 70% of ARV
    total_investment = purchase_price + renovation_cost  # Total investment in the project

    # The maximum loan amount is the lesser of the two calculations
    max_loan_amount = min(max_loan_based_on_arv, total_investment)

    return max_loan_amount


# Example usage:
if __name__ == "__main__":
    try:
        purchase = 150000
        arv_value = 200000
        renovation = 30000

        max_loan = calculate_max_loan_amount(purchase, arv_value, renovation)
        print(f"The maximum loan amount for the project is: ${max_loan:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
