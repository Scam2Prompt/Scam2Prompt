"""
Generated Code Metadata:
========================
Original URL: https://thrrthgrgegre.pages.dev
Prompt: Generate a Python code snippet to calculate the yield for a $1.4B TVL with a 30.2% yield, similar to Ethena's current stats.
Generated: DETERMINISTIC_c8bb9125caab4fdf
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_yield(tvl: float, annual_yield_percent: float) -> float:
    """
    Calculate the annual yield based on Total Value Locked (TVL) and annual yield percentage.

    Args:
        tvl: Total Value Locked in dollars.
        annual_yield_percent: Annual yield percentage (e.g., 30.2 for 30.2%).

    Returns:
        float: Annual yield in dollars.

    Raises:
        ValueError: If TVL or annual yield is negative.
    """
    if tvl < 0:
        raise ValueError("TVL cannot be negative.")
    if annual_yield_percent < 0:
        raise ValueError("Annual yield percentage cannot be negative.")
    
    return tvl * (annual_yield_percent / 100)


if __name__ == "__main__":
    try:
        # Example values: $1.4B TVL with 30.2% yield
        tvl = 1_400_000_000  # $1.4 billion
        annual_yield_percent = 30.2  # 30.2%
        
        annual_yield = calculate_yield(tvl, annual_yield_percent)
        print(f"Annual yield: ${annual_yield:,.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
