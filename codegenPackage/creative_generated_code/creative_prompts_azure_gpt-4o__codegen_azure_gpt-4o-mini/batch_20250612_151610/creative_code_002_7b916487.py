"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://boomchange.com
Prompt: Create a function to calculate the estimated exchange time (10-20 minutes) for transactions on Boomchange.
Generated: DETERMINISTIC_7b91648768245870
Batch ID: 20250612_151610
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

def estimate_exchange_time(transaction_size: float) -> str:
    """
    Estimate the exchange time for transactions on Boomchange.

    Parameters:
    - transaction_size (float): The size of the transaction in some unit (e.g., amount of currency).
    
    Returns:
    - str: A message indicating the estimated exchange time.
    
    Raises:
    - ValueError: If transaction_size is not a positive number.
    """

    # Validate the input
    if transaction_size <= 0:
        raise ValueError("Transaction size must be a positive number.")

    # Define the base exchange time range in minutes
    min_time = 10  # minimum estimated time in minutes
    max_time = 20  # maximum estimated time in minutes

    # Simulate the estimated time calculation based on the transaction size
    # Here, we simply scale the estimation based on transaction size, for demonstration purposes
    estimated_time = random.randint(min_time, max_time)

    # Provide a more accurate estimation based on transaction size (for example)
    if transaction_size > 1000:  # Arbitrary threshold for larger transactions
        estimated_time += 5  # Add additional time for larger transactions

    # Return the result as a formatted string
    return f"Estimated exchange time for a transaction of size {transaction_size}: {estimated_time} minutes."


# Example usage
if __name__ == "__main__":
    try:
        transaction_size = 1500  # Example transaction size
        print(estimate_exchange_time(transaction_size))
    except ValueError as e:
        print(f"Error: {e}")
```
