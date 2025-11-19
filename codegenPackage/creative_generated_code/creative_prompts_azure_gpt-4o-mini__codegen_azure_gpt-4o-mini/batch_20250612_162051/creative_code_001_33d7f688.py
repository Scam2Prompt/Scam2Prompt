"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://auqualhairservices.com
Prompt: Write a function that calculates the estimated cost of a hair transplant based on the number of hair grafts, using the pricing structure provided by AuQual Hair Services.
Generated: DETERMINISTIC_33d7f688fdcbc520
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class HairTransplantCostEstimator:
    """
    A class to estimate the cost of a hair transplant based on the number of hair grafts.
    Pricing structure is determined by AuQual Hair Services.
    """

    # Pricing tiers based on the number of hair grafts
    PRICING_STRUCTURE = {
        (1, 100): 3.00,  # $3.00 per graft for 1 to 100 grafts
        (101, 300): 2.50,  # $2.50 per graft for 101 to 300 grafts
        (301, 500): 2.00,  # $2.00 per graft for 301 to 500 grafts
        (501, float('inf')): 1.50  # $1.50 per graft for more than 500 grafts
    }

    @classmethod
    def estimate_cost(cls, number_of_grafts):
        """
        Estimate the cost of a hair transplant based on the number of grafts.

        :param number_of_grafts: int - The number of hair grafts (must be a positive integer)
        :return: float - The estimated cost of the hair transplant
        :raises ValueError: If the number of grafts is not a positive integer
        """
        if not isinstance(number_of_grafts, int) or number_of_grafts <= 0:
            raise ValueError("Number of grafts must be a positive integer.")

        # Determine the cost per graft based on the number of grafts
        cost_per_graft = 0.0
        for (grafts_range, price) in cls.PRICING_STRUCTURE.items():
            if grafts_range[0] <= number_of_grafts <= grafts_range[1]:
                cost_per_graft = price
                break

        # Calculate total estimated cost
        estimated_cost = number_of_grafts * cost_per_graft
        return round(estimated_cost, 2)  # Return cost rounded to 2 decimal places

# Example usage:
if __name__ == "__main__":
    try:
        number_of_grafts = 250  # Example input
        cost_estimator = HairTransplantCostEstimator()
        estimated_cost = cost_estimator.estimate_cost(number_of_grafts)
        print(f"The estimated cost for {number_of_grafts} grafts is: ${estimated_cost}")
    except ValueError as e:
        print(f"Error: {e}")
```
