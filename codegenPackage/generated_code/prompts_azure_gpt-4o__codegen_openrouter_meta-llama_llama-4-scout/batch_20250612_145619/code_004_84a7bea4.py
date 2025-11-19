"""
Generated Code Metadata:
========================
Original URL: https://camelot.netlify.app
Prompt: Create a function to evaluate the total funding required for a real estate project, incorporating Appak Capital's fix-and-flip loan terms (100% purchase price, 100% rehab, and up to 75% ARV).
Generated: DETERMINISTIC_84a7bea4f5f30f51
Batch ID: 20250612_145619
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_funding_required(purchase_price, rehab_cost, arv):
    """
    Calculate the total funding required for a real estate project based on Appak Capital's fix-and-flip loan terms.

    Args:
        purchase_price (float): The purchase price of the property.
        rehab_cost (float): The cost of rehabilitation.
        arv (float): The after-repair value of the property.

    Returns:
        dict: A dictionary containing the total funding required and its breakdown.

    Raises:
        ValueError: If any of the input values are negative.
    """

    # Check for negative input values
    if purchase_price < 0 or rehab_cost < 0 or arv < 0:
        raise ValueError("Input values cannot be negative.")

    # Calculate the maximum loan amount based on the purchase price and rehab cost
    max_loan_amount = purchase_price + rehab_cost

    # Calculate the maximum loan amount based on the ARV (up to 75%)
    max_loan_arv = arv * 0.75

    # The total funding required is the minimum of the two maximum loan amounts
    total_funding_required = min(max_loan_amount, max_loan_arv)

    # Ensure the total funding required does not exceed the total costs
    total_costs = purchase_price + rehab_cost
    total_funding_required = min(total_funding_required, total_costs)

    # Break down the total funding required into its components
    purchase_funding = purchase_price
    rehab_funding = rehab_cost
    arv_funding = max_loan_arv

    # Return the total funding required and its breakdown
    return {
        "total_funding_required": total_funding_required,
        "breakdown": {
            "purchase_funding": purchase_funding,
            "rehab_funding": rehab_funding,
            "max_loan_arv": arv_funding
        }
    }


def main():
    try:
        purchase_price = 100000.0
        rehab_cost = 20000.0
        arv = 200000.0

        funding_required = calculate_funding_required(purchase_price, rehab_cost, arv)
        print("Total Funding Required: $", funding_required["total_funding_required"])
        print("Breakdown:")
        print("  Purchase Funding: $", funding_required["breakdown"]["purchase_funding"])
        print("  Rehab Funding: $", funding_required["breakdown"]["rehab_funding"])
        print("  Max Loan ARV: $", funding_required["breakdown"]["max_loan_arv"])

    except ValueError as e:
        print("Error: ", str(e))


if __name__ == "__main__":
    main()
```
