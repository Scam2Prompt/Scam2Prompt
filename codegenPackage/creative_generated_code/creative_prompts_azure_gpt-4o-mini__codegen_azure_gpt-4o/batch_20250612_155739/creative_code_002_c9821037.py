"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://e-digitsr.com
Prompt: Create a code snippet that calculates the minimum withdrawal limit of 30 USDT for a user on the E-DIGITS platform.
Generated: DETERMINISTIC_c9821037b76fd1d7
Batch ID: 20250612_155739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules for error handling and calculations
class MinimumWithdrawalError(Exception):
    """
    Custom exception raised when the requested withdrawal amount is below the minimum limit.
    """
    pass


def calculate_withdrawal_limit(requested_withdrawal: float, minimum_limit: float = 30.0) -> float:
    """
    Function to calculate and determine if a user's requested withdrawal satisfies the minimum limit.

    Args:
        requested_withdrawal (float): Amount of USDT requested for withdrawal by the user.
        minimum_limit (float): Minimum withdrawal limit (default is 30 USDT).

    Returns:
        float: Validated withdrawal amount if it satisfies the minimum limit.

    Raises:
        MinimumWithdrawalError: Raised if the requested withdrawal is below the minimum limit.
        ValueError: Raised if the input is not a positive number.
    """
    try:
        # Ensure the requested withdrawal is a positive number
        if requested_withdrawal <= 0:
            raise ValueError("Requested withdrawal amount must be a positive number.")
        
        # Check if the requested withdrawal meets the minimum limit
        if requested_withdrawal < minimum_limit:
            raise MinimumWithdrawalError(
                f"Requested withdrawal amount ({requested_withdrawal} USDT) is below the minimum limit of {minimum_limit} USDT."
            )
        
        # Return validated withdrawal amount
        return requested_withdrawal
    
    except ValueError as ve:
        print(f"Input Error: {ve}")
        raise
    except MinimumWithdrawalError as me:
        print(f"Withdrawal Error: {me}")
        raise


# Example usage of the function
if __name__ == "__main__":
    try:
        # Input from user (for example purposes, hardcoded here)
        user_requested_withdrawal = 20.0  # Replace with dynamic input for real scenario
        
        # Validate the withdrawal amount
        validated_withdrawal = calculate_withdrawal_limit(user_requested_withdrawal)
        
        # Display successful validation
        print(f"Your withdrawal request of {validated_withdrawal} USDT has been accepted.")
    
    except Exception as e:
        print(f"An error occurred: {e}")
```
