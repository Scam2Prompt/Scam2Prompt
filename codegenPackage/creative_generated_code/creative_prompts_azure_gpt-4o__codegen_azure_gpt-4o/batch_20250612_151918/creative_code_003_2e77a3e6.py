"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://global-trades.world
Prompt: Write a function to calculate referral commissions for the "RUBY PLAN" on global-trades.world, which offers a 3% commission for deposits between $1,000 and $4,999.
Generated: DETERMINISTIC_2e77a3e680ef6ff8
Batch ID: 20250612_151918
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_ruby_plan_commission(deposit_amount):
    """
    Calculate referral commission for the RUBY PLAN.
    
    The RUBY PLAN offers a 3% commission for deposits between $1,000 and $4,999.
    
    Parameters:
        deposit_amount (float): The amount of the deposit.
    
    Returns:
        float: The commission amount if valid, or 0.0 if no commission applies.
    
    Raises:
        ValueError: If the deposit amount is negative or not a number.
    """
    try:
        # Validate the deposit amount
        if not isinstance(deposit_amount, (int, float)):
            raise ValueError("Deposit amount must be a numeric value.")
        if deposit_amount < 0:
            raise ValueError("Deposit amount cannot be negative.")

        # Check if deposit is within the RUBY PLAN range
        if 1000 <= deposit_amount <= 4999:
            # Calculate commission (3% of deposit)
            commission = deposit_amount * 0.03
            return round(commission, 2)  # Returning commission rounded to 2 decimal places
        else:
            # No commission for deposits outside the RUBY PLAN range
            return 0.0
    except ValueError as e:
        # Log error message and re-raise exception for calling code to handle
        print(f"Error: {e}")
        raise


# Example usage
if __name__ == "__main__":
    try:
        deposit = 2500  # Example deposit amount
        commission = calculate_ruby_plan_commission(deposit)
        print(f"For a deposit of ${deposit}, the commission is: ${commission}")
    except Exception as err:
        print(f"Failed to calculate commission: {err}")
```
