"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kayen.pages.dev
Prompt: Create a function to calculate bonus points for liquidity supply in the USDT-CHZ pool on KAYEN League, including the +100% bonus multiplier.
Generated: DETERMINISTIC_6c691d6a66ecf9ee
Batch ID: 20250612_152906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_bonus_points(base_points: float, is_bonus_multiplier_active: bool) -> float:
    """
    Calculate bonus points for liquidity supply in the USDT-CHZ pool on KAYEN League.

    Args:
        base_points (float): The initial points earned from liquidity supply.
        is_bonus_multiplier_active (bool): Whether the +100% bonus multiplier is active.

    Returns:
        float: The total bonus points including the multiplier if applicable.

    Raises:
        ValueError: If base_points is negative.
    """
    # Validate input
    if base_points < 0:
        raise ValueError("Base points cannot be negative.")

    try:
        # Apply the +100% bonus multiplier if active
        if is_bonus_multiplier_active:
            total_points = base_points * 2  # +100% bonus multiplier doubles the points
        else:
            total_points = base_points
        
        return total_points
    
    except Exception as e:
        # Catch unexpected errors
        print(f"An error occurred while calculating bonus points: {e}")
        raise

# Example usage:
if __name__ == "__main__":
    try:
        base_points = 150.0  # Example base points amount
        is_active = True     # Example multiplier status
        result = calculate_bonus_points(base_points, is_active)
        print(f"Total points earned: {result}")
    except ValueError as ve:
        print(f"Input Error: {ve}")
```
