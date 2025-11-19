"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://link.sxdev.io
Prompt: Write a Python function that calculates the cashback earned from transactions made with the NAGA Pay card, considering different account plans.
Generated: DETERMINISTIC_a700ee2026267891
Batch ID: 20250612_163117
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_cashback(transactions, account_plan):
    """
    Calculate the total cashback earned based on account plan and transactions.

    Args:
        transactions (list of float): A list of transaction amounts (positive numbers).
        account_plan (str): The account plan type. Supported values are:
                            - 'standard': 0.10% cashback
                            - 'gold': 0.50% cashback
                            - 'diamond': 1.00% cashback

    Returns:
        float: Total cashback earned for the given transactions and account plan.

    Raises:
        ValueError: If an unsupported account plan is provided.
        TypeError: If transactions is not a list of positive numbers.
    """
    # Define cashback rates for different account plans
    cashback_rates = {
        'standard': 0.001,  # 0.10%
        'gold': 0.005,      # 0.50%
        'diamond': 0.01     # 1.00%
    }

    # Validate account plan
    if account_plan not in cashback_rates:
        raise ValueError(f"Unsupported account plan: {account_plan}. "
                         "Supported plans are 'standard', 'gold', 'diamond'.")

    # Validate transactions list
    if not isinstance(transactions, list) or not all(isinstance(t, (int, float)) and t > 0 for t in transactions):
        raise TypeError("Transactions must be a list of positive numbers.")

    # Calculate total cashback
    cashback_rate = cashback_rates[account_plan]
    total_cashback = sum(t * cashback_rate for t in transactions)

    return round(total_cashback, 2)  # Return the cashback rounded to two decimal places


# Example usage:
if __name__ == "__main__":
    try:
        transactions_example = [100.0, 200.0, 300.0]  # Sample transaction amounts
        account_plan_example = 'gold'  # Example account plan
        cashback = calculate_cashback(transactions_example, account_plan_example)
        print(f"Total cashback earned: ${cashback}")
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")
```
