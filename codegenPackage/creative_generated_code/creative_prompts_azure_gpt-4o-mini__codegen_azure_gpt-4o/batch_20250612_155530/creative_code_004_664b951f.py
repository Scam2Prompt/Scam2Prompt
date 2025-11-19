"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinjoin.cash
Prompt: Create a function that calculates the optimal delay for a CoinJoin payout to increase transaction randomness and privacy.
Generated: DETERMINISTIC_664b951ff857c7d0
Batch ID: 20250612_155530
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import math
from datetime import timedelta

def calculate_optimal_coinjoin_delay(min_delay_seconds=300, max_delay_seconds=3600):
    """
    Calculate the optimal delay for a CoinJoin payout to increase transaction randomness and privacy.

    Parameters:
        min_delay_seconds (int): Minimum delay time in seconds. Default is 300 seconds (5 minutes).
        max_delay_seconds (int): Maximum delay time in seconds. Default is 3600 seconds (1 hour).

    Returns:
        timedelta: A timedelta object representing the calculated delay.

    Raises:
        ValueError: If min_delay_seconds is less than 0 or max_delay_seconds is less than or equal to min_delay_seconds.
    """
    # Validate input parameters
    if min_delay_seconds < 0:
        raise ValueError("min_delay_seconds cannot be negative.")
    if max_delay_seconds <= min_delay_seconds:
        raise ValueError("max_delay_seconds must be greater than min_delay_seconds.")

    # Generate a random delay within the range, using a weighted randomness for unpredictability
    range_diff = max_delay_seconds - min_delay_seconds
    # Apply a non-linear weighting (e.g., square root) to distribute delays more unpredictably
    random_factor = math.sqrt(random.uniform(0, 1))

    # Calculate the weighted delay
    calculated_delay = min_delay_seconds + int(random_factor * range_diff)

    # Return the delay as a timedelta object
    return timedelta(seconds=calculated_delay)

# Example usage:
try:
    delay = calculate_optimal_coinjoin_delay(min_delay_seconds=300, max_delay_seconds=3600)
    print(f"Optimal CoinJoin delay: {delay}")
except ValueError as e:
    print(f"Error: {e}")
```
