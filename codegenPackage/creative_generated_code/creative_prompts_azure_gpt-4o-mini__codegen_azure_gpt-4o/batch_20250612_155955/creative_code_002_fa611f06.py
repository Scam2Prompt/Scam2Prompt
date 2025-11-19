"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://minerinde.com
Prompt: Write a function in Python that calculates the total earnings based on the number of taps and the multiplier effect mentioned on minerinde.com.
Generated: DETERMINISTIC_fa611f06d6371a2c
Batch ID: 20250612_155955
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_total_earnings(taps, multiplier):
    """
    Calculates the total earnings based on the number of taps and the multiplier effect.

    Args:
        taps (int): The number of taps performed by the user.
        multiplier (float): The multiplier effect applied to the taps.

    Returns:
        float: The total earnings calculated based on taps and multiplier.

    Raises:
        ValueError: If taps is not a positive integer or multiplier is not a positive float.
    """

    # Validate inputs
    if not isinstance(taps, int) or taps < 0:
        raise ValueError("Taps must be a positive integer.")
    if not isinstance(multiplier, (int, float)) or multiplier <= 0:
        raise ValueError("Multiplier must be a positive number.")

    # Calculate total earnings
    total_earnings = taps * multiplier

    return round(total_earnings, 2)  # Return rounded value for cleaner presentation


# Example usage
if __name__ == "__main__":
    try:
        # Example values
        user_taps = 500
        user_multiplier = 1.5

        # Calculate earnings
        earnings = calculate_total_earnings(user_taps, user_multiplier)
        print(f"Total earnings: ${earnings}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
