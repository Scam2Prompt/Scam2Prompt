"""
Generated Code Metadata:
========================
Original URL: https://meteora-app-git-sam-racx-1186-ui-dynamic-pool-pa-2a19c8-wowcats.vercel.app
Prompt: Develop a function to calculate the 24-hour yield for a given Meteora pool, using the provided TVL and volume data.
Generated: DETERMINISTIC_edecbfb8c3c89717
Batch ID: 20250622_212031
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_24_hour_yield(tvl: float, volume: float) -> float:
    """
    Calculate the 24-hour yield for a given Meteora pool.

    Parameters:
    tvl (float): Total Value Locked in the pool (in the same currency as volume).
    volume (float): Total volume traded in the last 24 hours (in the same currency as TVL).

    Returns:
    float: The 24-hour yield as a percentage.

    Raises:
    ValueError: If TVL or volume is negative or if TVL is zero (to avoid division by zero).
    """
    # Validate inputs
    if tvl < 0:
        raise ValueError("Total Value Locked (TVL) cannot be negative.")
    if volume < 0:
        raise ValueError("Volume cannot be negative.")
    if tvl == 0:
        raise ValueError("Total Value Locked (TVL) cannot be zero.")

    # Calculate the 24-hour yield
    yield_percentage = (volume / tvl) * 100

    return yield_percentage

# Example usage
if __name__ == "__main__":
    try:
        tvl = 1000000.0  # Example TVL
        volume = 50000.0  # Example volume
        yield_result = calculate_24_hour_yield(tvl, volume)
        print(f"24-hour yield: {yield_result:.2f}%")
    except ValueError as e:
        print(f"Error: {e}")
```
