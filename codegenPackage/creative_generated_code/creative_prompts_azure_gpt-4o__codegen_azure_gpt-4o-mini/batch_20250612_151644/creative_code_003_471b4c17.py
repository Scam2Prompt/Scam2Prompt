"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://boomchange.io
Prompt: Create a function that calculates the estimated exchange time (10-20 minutes) for transactions on Boomchange, considering the platform’s high-speed exchange feature.
Generated: DETERMINISTIC_471b4c17b0301167
Batch ID: 20250612_151644
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import time

def estimate_exchange_time():
    """
    Estimates the exchange time for transactions on Boomchange.
    The estimated time is randomly chosen between 10 and 20 minutes.
    
    Returns:
        int: Estimated time in minutes.
    
    Raises:
        ValueError: If the estimated time is not within the expected range.
    """
    # Define the minimum and maximum exchange time in minutes
    min_time = 10
    max_time = 20
    
    try:
        # Randomly select an estimated exchange time
        estimated_time = random.randint(min_time, max_time)
        
        if estimated_time < min_time or estimated_time > max_time:
            raise ValueError("Estimated time is out of expected range.")
        
        return estimated_time
    
    except Exception as e:
        # Log exception (In production, use logging instead of print)
        print(f"Error occurred while estimating exchange time: {e}")
        return None

# Example usage
if __name__ == "__main__":
    estimated_time = estimate_exchange_time()
    if estimated_time is not None:
        print(f"Estimated exchange time: {estimated_time} minutes.")
```
