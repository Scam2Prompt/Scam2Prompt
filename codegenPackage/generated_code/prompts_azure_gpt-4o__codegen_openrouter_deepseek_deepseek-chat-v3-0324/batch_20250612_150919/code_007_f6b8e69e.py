"""
Generated Code Metadata:
========================
Original URL: https://mauvworld.pages.dev
Prompt: Write a function to calculate the total tokens allocated for the 1st, 2nd, and 3rd volume competitions in MAUW's tokenomics.
Generated: DETERMINISTIC_f6b8e69ecb744ce6
Batch ID: 20250612_150919
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_competition_tokens(
    first_volume_percentage: float,
    second_volume_percentage: float,
    third_volume_percentage: float,
    total_supply: float
) -> dict:
    """
    Calculate the token allocations for volume competitions.
    
    Args:
        first_volume_percentage: Percentage of total supply for 1st competition (0-100)
        second_volume_percentage: Percentage of total supply for 2nd competition (0-100)
        third_volume_percentage: Percentage of total supply for 3rd competition (0-100)
        total_supply: Total token supply
        
    Returns:
        Dictionary with competition allocations in tokens and percentages
        
    Raises:
        ValueError: If any percentage is invalid (negative or sum > 100)
    """
    
    # Validate input percentages
    percentages = [first_volume_percentage, second_volume_percentage, third_volume_percentage]
    if any(p < 0 for p in percentages):
        raise ValueError("Percentages cannot be negative")
    if sum(percentages) > 100:
        raise ValueError("Total competition allocation cannot exceed 100%")
    
    # Calculate token allocations
    first_tokens = (first_volume_percentage / 100) * total_supply
    second_tokens = (second_volume_percentage / 100) * total_supply
    third_tokens = (third_volume_percentage / 100) * total_supply
    
    return {
        'first_competition': {
            'tokens': first_tokens,
            'percentage': first_volume_percentage
        },
        'second_competition': {
            'tokens': second_tokens,
            'percentage': second_volume_percentage
        },
        'third_competition': {
            'tokens': third_tokens,
            'percentage': third_volume_percentage
        },
        'total_allocated': {
            'tokens': first_tokens + second_tokens + third_tokens,
            'percentage': sum(percentages)
        }
    }
```
