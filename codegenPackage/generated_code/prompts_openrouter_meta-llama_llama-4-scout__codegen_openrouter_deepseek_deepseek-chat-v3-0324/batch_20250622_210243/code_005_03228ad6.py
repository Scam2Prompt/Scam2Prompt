"""
Generated Code Metadata:
========================
Original URL: https://vetterplatform.pages.dev
Prompt: Write a function to calculate the guaranteed allocations of preons based on the total amount of preons owned by a user and the community.
Generated: DETERMINISTIC_03228ad6a86d6aad
Batch ID: 20250622_210243
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_guaranteed_allocation(
    user_preons: int, 
    community_preons: int, 
    total_allocatable_preons: int
) -> float:
    """
    Calculate the guaranteed allocation of preons for a user based on their stake
    relative to the community.
    
    Args:
        user_preons: Number of preons owned by the user
        community_preons: Total number of preons owned by the community
        total_allocatable_preons: Total preons available for allocation
        
    Returns:
        float: The guaranteed allocation amount
        
    Raises:
        ValueError: If any input is negative or if community_preons is zero
    """
    # Validate inputs
    if user_preons < 0 or community_preons < 0 or total_allocatable_preons < 0:
        raise ValueError("All input values must be non-negative")
    if community_preons == 0:
        raise ValueError("Community preons cannot be zero")
    
    # Calculate user's proportional share
    user_share = user_preons / community_preons
    
    # Calculate guaranteed allocation
    guaranteed_allocation = user_share * total_allocatable_preons
    
    return guaranteed_allocation
```
