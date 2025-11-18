"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://collectiblemarkethub.com
Prompt: Create a Python function to calculate the total bid amount for an NFT on Collectible Market Hub, factoring in the service fee and user balance.
Generated: DETERMINISTIC_29f3d267ce1b681a
Batch ID: 20250612_145616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class InsufficientBalanceError(Exception):
    """Custom exception for handling insufficient user balance."""
    pass

def calculate_total_bid_amount(bid_amount: float, service_fee_percentage: float, user_balance: float) -> float:
    """
    Calculate the total bid amount for an NFT on Collectible Market Hub.

    Args:
        bid_amount (float): The base amount of the bid.
        service_fee_percentage (float): The percentage of the service fee (e.g., 5 for 5%).
        user_balance (float): The available balance of the user.

    Returns:
        float: The total bid amount including the service fee.

    Raises:
        InsufficientBalanceError: If the total bid amount exceeds the user's balance.
    """
    if bid_amount < 0:
        raise ValueError("Bid amount cannot be negative.")
    if service_fee_percentage < 0:
        raise ValueError("Service fee percentage cannot be negative.")
    if user_balance < 0:
        raise ValueError("User balance cannot be negative.")

    # Calculate the service fee
    service_fee = (service_fee_percentage / 100) * bid_amount
    
    # Calculate the total bid amount
    total_bid_amount = bid_amount + service_fee
    
    # Check if the user balance is sufficient
    if total_bid_amount > user_balance:
        raise InsufficientBalanceError("Total bid amount exceeds user balance.")
    
    return total_bid_amount

# Example usage (uncomment to test):
# try:
#     total = calculate_total_bid_amount(100.0, 5.0, 110.0)
#     print(f"Total bid amount: {total}")
# except Exception as e:
#     print(f"Error: {e}")
```
