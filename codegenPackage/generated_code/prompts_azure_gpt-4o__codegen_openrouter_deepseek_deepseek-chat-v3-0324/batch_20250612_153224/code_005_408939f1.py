"""
Generated Code Metadata:
========================
Original URL: https://afranaden.org
Prompt: Develop a function to calculate the number of beneficiaries for food distribution campaigns, like the Ramadan food basket initiative mentioned on the Gulf and Aden website.
Generated: DETERMINISTIC_408939f1d0ea332f
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_beneficiaries(
    total_food_baskets: int,
    basket_capacity: int,
    family_size: int = 1,
    min_family_size: int = 1,
    max_family_size: int = 10
) -> dict:
    """
    Calculate the number of beneficiaries for food distribution campaigns.
    
    Args:
        total_food_baskets (int): Total number of food baskets available
        basket_capacity (int): Number of people one basket can feed
        family_size (int, optional): Average family size. Defaults to 1.
        min_family_size (int, optional): Minimum family size considered. Defaults to 1.
        max_family_size (int, optional): Maximum family size considered. Defaults to 10.
    
    Returns:
        dict: Dictionary containing:
            - total_beneficiaries: Total number of people that can be fed
            - families_served: Number of families that can be served
            - baskets_per_family: Number of baskets needed per family
            - remaining_baskets: Baskets left after distribution
    
    Raises:
        ValueError: If any input parameter is invalid
    """
    # Validate input parameters
    if total_food_baskets <= 0:
        raise ValueError("Total food baskets must be positive")
    if basket_capacity <= 0:
        raise ValueError("Basket capacity must be positive")
    if family_size < min_family_size or family_size > max_family_size:
        raise ValueError(f"Family size must be between {min_family_size} and {max_family_size}")
    
    # Calculate baskets needed per family
    baskets_per_family = max(1, (family_size + basket_capacity - 1) // basket_capacity)
    
    # Calculate families that can be served
    families_served = total_food_baskets // baskets_per_family
    
    # Calculate remaining baskets
    remaining_baskets = total_food_baskets % baskets_per_family
    
    # Calculate total beneficiaries
    total_beneficiaries = families_served * family_size
    
    return {
        "total_beneficiaries": total_beneficiaries,
        "families_served": families_served,
        "baskets_per_family": baskets_per_family,
        "remaining_baskets": remaining_baskets
    }
```
