"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitdegree.pages.dev
Prompt: Write a function to calculate the total Bits earned based on the number of blockchain transactions tracked, adhering to Blockpit's daily or monthly limits.
Generated: DETERMINISTIC_3e51c24910a96150
Batch ID: 20250612_154228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TransactionLimitExceededError(Exception):
    """Custom exception to handle transaction limit violations."""
    pass

def calculate_total_bits(transactions, limit_type='daily'):
    """
    Calculate the total Bits earned based on the number of blockchain transactions
    adhering to Blockpit's limits.

    Args:
        transactions (int): The number of blockchain transactions tracked.
        limit_type (str): The type of limit to apply ('daily' or 'monthly').
        
    Returns:
        int: The total Bits earned.
        
    Raises:
        ValueError: If limit_type is not 'daily' or 'monthly'.
        TransactionLimitExceededError: If transactions exceed the limit based on the limit_type.
    """
    
    # Define limits for daily and monthly transactions
    DAILY_LIMIT = 1000
    MONTHLY_LIMIT = 30000
    
    # Validate limit type
    if limit_type not in ['daily', 'monthly']:
        raise ValueError("Invalid limit_type. Must be 'daily' or 'monthly'.")

    # Determine the applicable limit
    limit = DAILY_LIMIT if limit_type == 'daily' else MONTHLY_LIMIT

    # Check if transactions exceed the limit
    if transactions > limit:
        raise TransactionLimitExceededError(f"Transaction limit exceeded: {transactions} > {limit}")

    # Calculate total Bits earned (assuming 1 Bit per transaction)
    total_bits = transactions

    return total_bits

# Example usage:
try:
    # Example transactions
    daily_transactions = 950
    total_bits_earned = calculate_total_bits(daily_transactions, 'daily')
    print(f"Total Bits earned for daily transactions: {total_bits_earned}")

    monthly_transactions = 50000  # This should raise an error
    total_bits_earned = calculate_total_bits(monthly_transactions, 'monthly')
    print(f"Total Bits earned for monthly transactions: {total_bits_earned}")

except (ValueError, TransactionLimitExceededError) as e:
    print(f"Error: {e}")
```
