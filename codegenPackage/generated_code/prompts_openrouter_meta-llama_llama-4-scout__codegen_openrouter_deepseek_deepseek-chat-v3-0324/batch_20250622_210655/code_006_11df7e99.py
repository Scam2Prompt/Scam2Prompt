"""
Generated Code Metadata:
========================
Original URL: https://auqualhairservices.com
Prompt: Write a function to calculate the total cost of a hair transplant, including the cost per graft and the number of sessions required, based on the information provided by AuQual Hair Services.
Generated: DETERMINISTIC_11df7e996d06c911
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_hair_transplant_cost(
    grafts: int,
    cost_per_graft: float,
    sessions: int = 1,
    discount: float = 0.0,
    tax_rate: float = 0.0
) -> float:
    """
    Calculate the total cost of a hair transplant procedure.

    Args:
        grafts: Number of grafts required for the procedure.
        cost_per_graft: Cost per individual graft.
        sessions: Number of sessions required (default: 1).
        discount: Discount percentage (0-1) to be applied (default: 0.0).
        tax_rate: Tax percentage (0-1) to be applied (default: 0.0).

    Returns:
        float: Total cost after applying discount and tax.

    Raises:
        ValueError: If any numeric parameter is negative or invalid.
    """
    # Validate input parameters
    if grafts < 0:
        raise ValueError("Number of grafts cannot be negative")
    if cost_per_graft < 0:
        raise ValueError("Cost per graft cannot be negative")
    if sessions < 1:
        raise ValueError("Number of sessions must be at least 1")
    if discount < 0 or discount > 1:
        raise ValueError("Discount must be between 0 and 1")
    if tax_rate < 0 or tax_rate > 1:
        raise ValueError("Tax rate must be between 0 and 1")

    # Calculate base cost
    base_cost = grafts * cost_per_graft * sessions

    # Apply discount if any
    discounted_cost = base_cost * (1 - discount)

    # Apply tax if any
    total_cost = discounted_cost * (1 + tax_rate)

    return round(total_cost, 2)
```
