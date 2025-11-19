"""
Generated Code Metadata:
========================
Original URL: https://refund-me.net
Prompt: Write a Python script to calculate the total amount recovered by Refund-me if they have helped 4000+ customers with an average refund of £10,000.
Generated: DETERMINISTIC_5a8b70d8e4911f63
Batch ID: 20250622_212208
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Refund-me Total Recovery Calculator

Calculates the total amount recovered by Refund-me given the number of customers
and the average refund amount.

Author: [Your Name]
Date: [Today's Date]
"""

def calculate_total_recovery(num_customers: int, avg_refund: float) -> float:
    """
    Calculates the total amount recovered.

    Args:
        num_customers (int): The number of customers.
        avg_refund (float): The average refund amount.

    Returns:
        float: The total amount recovered.

    Raises:
        ValueError: If num_customers or avg_refund is negative.
    """
    if num_customers < 0 or avg_refund < 0:
        raise ValueError("Number of customers and average refund must be non-negative.")

    total_recovery = num_customers * avg_refund
    return total_recovery


def main():
    try:
        num_customers = 4000
        avg_refund = 10000.0  # in pounds

        total_recovery = calculate_total_recovery(num_customers, avg_refund)
        print(f"Total amount recovered by Refund-me: £{total_recovery:,.2f}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
