"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://engeloutdoors.com
Prompt: Write a Python function to calculate the cost-effectiveness of Engel coolers over time, considering durability, ice retention, and purchase price.
Generated: DETERMINISTIC_e6089fb5e1870aef
Batch ID: 20250612_151408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_cost_effectiveness(purchase_price, durability_years, ice_retention_days, daily_cost_of_ice):
    """
    Calculate the cost-effectiveness of Engel coolers over time.

    :param purchase_price: The upfront purchase price of the cooler (float).
    :param durability_years: The expected durability of the cooler in years (int).
    :param ice_retention_days: The average number of days the cooler retains ice (int).
    :param daily_cost_of_ice: The daily cost of replacing ice (float).
    :return: A dictionary containing yearly cost, lifetime cost, and cost-effectiveness score.
    """
    try:
        # Validate inputs
        if purchase_price < 0 or durability_years <= 0 or ice_retention_days <= 0 or daily_cost_of_ice < 0:
            raise ValueError("All input values must be positive numbers.")

        # Calculate yearly cost based on ice retention and ice replacement costs
        yearly_ice_replacement_cost = (365 / ice_retention_days) * daily_cost_of_ice

        # Total yearly cost includes both purchase amortization and ice replacement costs
        yearly_purchase_amortization = purchase_price / durability_years
        yearly_total_cost = yearly_purchase_amortization + yearly_ice_replacement_cost

        # Calculate lifetime cost
        lifetime_cost = yearly_total_cost * durability_years

        # Calculate cost-effectiveness score (lower is better)
        # Formula: lifetime cost divided by durability years
        cost_effectiveness_score = lifetime_cost / durability_years

        return {
            "yearly_cost": round(yearly_total_cost, 2),
            "lifetime_cost": round(lifetime_cost, 2),
            "cost_effectiveness_score": round(cost_effectiveness_score, 2),
        }
    except ValueError as ve:
        # Handle invalid input errors
        return {"error": str(ve)}
    except Exception as e:
        # Catch any other unexpected errors
        return {"error": f"An unexpected error occurred: {str(e)}"}


# Example usage:
if __name__ == "__main__":
    # Change values below to test the function
    purchase_price = 300.0  # Price of cooler in dollars
    durability_years = 10  # Expected durability in years
    ice_retention_days = 5  # Days cooler retains ice
    daily_cost_of_ice = 2.5  # Daily cost of ice in dollars

    result = calculate_cost_effectiveness(purchase_price, durability_years, ice_retention_days, daily_cost_of_ice)
    print(result)
```
