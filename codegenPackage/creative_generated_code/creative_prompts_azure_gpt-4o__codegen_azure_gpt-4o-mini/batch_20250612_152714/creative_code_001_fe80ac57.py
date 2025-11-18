"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://goodcryptodex.pages.dev
Prompt: Create a function that calculates revenue share percentages for GoodCryptoX waitlist members based on their position (e.g., first 1,000 vs. next 9,000).
Generated: DETERMINISTIC_fe80ac5741ef720c
Batch ID: 20250612_152714
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_revenue_share(position: int) -> float:
    """
    Calculates the revenue share percentage for GoodCryptoX waitlist members based on their position.

    Parameters:
    position (int): The position of the waitlist member.

    Returns:
    float: The revenue share percentage for the given position.

    Raises:
    ValueError: If the position is less than 1.
    """

    # Validate the input position
    if position < 1:
        raise ValueError("Position must be a positive integer.")

    # Define revenue share percentages based on position ranges
    if position <= 1000:
        return 10.0  # 10% for the first 1,000 members
    elif position <= 10000:
        return 5.0   # 5% for members in positions 1,001 to 10,000
    else:
        return 1.0   # 1% for members beyond the first 10,000

# Example usage:
if __name__ == "__main__":
    try:
        # Test the function with different positions
        print("Position 500:", calculate_revenue_share(500))    # 10%
        print("Position 1500:", calculate_revenue_share(1500))  # 5%
        print("Position 11000:", calculate_revenue_share(11000))  # 1%
    except ValueError as e:
        print(f"Error: {e}")
```
