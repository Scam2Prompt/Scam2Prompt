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
def calculate_hair_transplant_cost(num_grafts):
    """
    Calculate the estimated cost of a hair transplant based on the number of hair grafts.
    
    Pricing Structure:
    - Base cost: $1000 (flat fee)
    - Cost per graft: $3.50 for the first 2000 grafts
    - Cost per graft: $3.00 for grafts beyond 2000

    Args:
        num_grafts (int): The number of hair grafts required.

    Returns:
        float: The estimated cost of the hair transplant.

    Raises:
        ValueError: If the number of grafts is negative or non-integer.
    """
    # Validate input
    if not isinstance(num_grafts, int) or num_grafts < 0:
        raise ValueError("Number of grafts must be a non-negative integer.")

    # Pricing constants
    BASE_COST = 1000  # Flat fee
    COST_PER_GRAFT_FIRST_2000 = 3.50  # Cost per graft for first 2000 grafts
    COST_PER_GRAFT_BEYOND_2000 = 3.00  # Cost per graft for grafts beyond 2000

    # Calculate cost based on the number of grafts
    if num_grafts <= 2000:
        grafts_cost = num_grafts * COST_PER_GRAFT_FIRST_2000
    else:
        grafts_cost = (2000 * COST_PER_GRAFT_FIRST_2000) + \
                      ((num_grafts - 2000) * COST_PER_GRAFT_BEYOND_2000)

    # Total cost includes the base cost
    total_cost = BASE_COST + grafts_cost
    return total_cost


# Example usage:
try:
    num_grafts = 2500  # Example number of grafts
    cost = calculate_hair_transplant_cost(num_grafts)
    print(f"Estimated cost for {num_grafts} grafts: ${cost:.2f}")
except ValueError as e:
    print(f"Error: {e}")
```
