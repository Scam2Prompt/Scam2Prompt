"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apponyx-org.pages.dev
Prompt: Create a function that calculates the daily emission based on the total staked amount in the Onyx Protocol.
Generated: DETERMINISTIC_1a8ce4d2425ce218
Batch ID: 20250612_160127
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_daily_emission(total_staked: float, emission_rate: float) -> float:
    """
    Calculate the daily emission based on the total staked amount in the Onyx Protocol.

    Parameters:
    total_staked (float): The total amount staked in the protocol.
    emission_rate (float): The emission rate per unit staked per day.

    Returns:
    float: The total daily emission.

    Raises:
    ValueError: If total_staked or emission_rate is negative.
    TypeError: If total_staked or emission_rate are not of type float or int.
    """

    # Validate input types
    if not isinstance(total_staked, (float, int)):
        raise TypeError("total_staked must be a float or an int.")
    if not isinstance(emission_rate, (float, int)):
        raise TypeError("emission_rate must be a float or an int.")

    # Validate input values
    if total_staked < 0:
        raise ValueError("total_staked must be non-negative.")
    if emission_rate < 0:
        raise ValueError("emission_rate must be non-negative.")

    # Calculate daily emission
    daily_emission = total_staked * emission_rate

    return daily_emission

# Example usage:
if __name__ == "__main__":
    try:
        total_staked_amount = 1000.0  # Example total staked amount
        daily_emission_rate = 0.05     # Example emission rate (5%)
        
        daily_emission = calculate_daily_emission(total_staked_amount, daily_emission_rate)
        print(f"Daily Emission: {daily_emission}")
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")
```
