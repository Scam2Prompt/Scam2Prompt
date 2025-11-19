"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://karak-acq.pages.dev
Prompt: Generate a function to check if a user's deposit exceeds the cap in a restaking protocol like Karak.
Generated: DETERMINISTIC_c4c3f2adf8334dfa
Batch ID: 20250612_163530
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class DepositCapExceededError(Exception):
    """Custom exception for deposit cap exceeded errors."""
    pass

def check_deposit_cap(user_deposit: float, cap: float) -> bool:
    """
    Checks if the user's deposit exceeds the specified cap.

    Args:
        user_deposit (float): The amount the user wishes to deposit.
        cap (float): The maximum allowable deposit cap.

    Raises:
        ValueError: If user_deposit or cap is negative.
        TypeError: If user_deposit or cap is not a float or int.

    Returns:
        bool: True if the deposit is within the cap, False otherwise.
    """
    
    # Input validation
    if not isinstance(user_deposit, (int, float)):
        raise TypeError("user_deposit must be a number.")
    if not isinstance(cap, (int, float)):
        raise TypeError("cap must be a number.")
    if user_deposit < 0 or cap < 0:
        raise ValueError("user_deposit and cap must be non-negative.")

    # Check if user's deposit exceeds the cap
    if user_deposit > cap:
        raise DepositCapExceededError("User's deposit exceeds the cap.")
    
    return True  # Deposit is within the cap

# Example usage (commented out for production):
# try:
#     if check_deposit_cap(1500.00, 1000.00):
#         print("Deposit is within the cap.")
# except (DepositCapExceededError, ValueError, TypeError) as e:
#     print(f"Error: {e}")
```
