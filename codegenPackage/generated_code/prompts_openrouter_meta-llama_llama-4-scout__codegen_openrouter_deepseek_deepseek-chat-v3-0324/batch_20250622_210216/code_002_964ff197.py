"""
Generated Code Metadata:
========================
Original URL: https://bitscrunch-3iw.pages.dev
Prompt: Generate a code snippet to calculate the effective reward cut for an operator on the bitsCrunch network given their query fee cut and reward cut percentages.
Generated: DETERMINISTIC_964ff197bc015eee
Batch ID: 20250622_210216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_effective_reward_cut(query_fee_cut: float, reward_cut: float) -> float:
    """
    Calculates the effective reward cut for an operator on the bitsCrunch network.
    
    The effective reward cut is computed as:
    effective_reward_cut = query_fee_cut + reward_cut - (query_fee_cut * reward_cut)
    
    Args:
        query_fee_cut (float): The query fee cut percentage (expressed as a decimal, e.g., 0.1 for 10%)
        reward_cut (float): The reward cut percentage (expressed as a decimal, e.g., 0.2 for 20%)
    
    Returns:
        float: The effective reward cut percentage (expressed as a decimal)
    
    Raises:
        ValueError: If either query_fee_cut or reward_cut is not between 0 and 1 (inclusive)
    """
    # Validate input parameters
    if not 0 <= query_fee_cut <= 1:
        raise ValueError("query_fee_cut must be between 0 and 1 (inclusive)")
    if not 0 <= reward_cut <= 1:
        raise ValueError("reward_cut must be between 0 and 1 (inclusive)")
    
    # Calculate effective reward cut
    effective_cut = query_fee_cut + reward_cut - (query_fee_cut * reward_cut)
    
    return effective_cut
```
