"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://staking-shakryfi.pages.dev
Prompt: Create a function that simulates the process of locking $SHARK tokens in the Sharky staking pool and calculates the resulting total weight based on the selected duration multiplier.
Generated: DETERMINISTIC_5c04012788c27167
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python code to simulate locking $SHARK tokens in a Sharky staking pool.
# The function calculates the resulting total weight based on a selected duration multiplier.

def lock_tokens_in_pool(shark_tokens: float, lock_duration: int) -> float:
    """
    Simulates the process of locking $SHARK tokens in the Sharky staking pool.

    Parameters:
        shark_tokens (float): The amount of $SHARK tokens being locked.
        lock_duration (int): The lock duration in months. Must be within the range 1-36 (inclusive).
        
    Returns:
        float: The total weight calculated based on the lock duration multiplier.
    
    Raises:
        ValueError: If shark_tokens <= 0 or lock_duration is out of the valid range.
    """
    # Define multipliers for different lock durations
    duration_multiplier = {
        1: 1.0,   # 1-month lock = 1.0x multiplier
        3: 1.1,   # 3-month lock = 1.1x multiplier
        6: 1.25,  # 6-month lock = 1.25x multiplier
        12: 1.5,  # 12-month lock = 1.5x multiplier
        24: 2.0,  # 24-month lock = 2.0x multiplier
        36: 2.5   # 36-month lock = 2.5x multiplier
    }

    try:
        # Validate input parameters
        if shark_tokens <= 0:
            raise ValueError("The amount of $SHARK tokens must be greater than 0.")
        if lock_duration not in duration_multiplier:
            raise ValueError("Lock duration must be one of the valid durations: " + 
                             ", ".join(map(str, duration_multiplier.keys())))

        # Calculate total weight
        multiplier = duration_multiplier[lock_duration]
        total_weight = shark_tokens * multiplier

        return total_weight

    except ValueError as e:
        # Handle invalid input gracefully
        print(f"Error: {e}")
        return 0.0


# Example usage:
if __name__ == "__main__":
    # Test the function with sample inputs
    tokens = 1000.0  # Amount of $SHARK tokens
    duration = 12    # Lock duration in months

    # Call the function and display the result
    result = lock_tokens_in_pool(tokens, duration)
    if result > 0:
        print(f"Total weight for locking {tokens} $SHARK tokens for {duration} months: {result}")
```
