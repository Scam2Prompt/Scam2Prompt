"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gcbt.com
Prompt: Write a function that validates a user's bid input for purchasing gcbt.com on Sedo, ensuring it meets the seller's requirements.
Generated: DETERMINISTIC_186e7ae55b61e312
Batch ID: 20250612_160553
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class BidValidationError(Exception):
    """Custom exception for bid validation errors."""
    pass


def validate_bid(bid_amount: float, min_bid: float, max_bid: float) -> bool:
    """
    Validates a user's bid input for purchasing a domain on Sedo.
    
    Args:
        bid_amount (float): The amount of the user's bid.
        min_bid (float): The minimum bid amount set by the seller.
        max_bid (float): The maximum bid amount set by the seller.
    
    Raises:
        BidValidationError: If the bid amount is not within the required range.
    
    Returns:
        bool: True if the bid is valid, False otherwise.
    """
    try:
        # Check if the bid amount is a valid number
        if not isinstance(bid_amount, (int, float)):
            raise BidValidationError("Bid amount must be a number.")
        
        # Check if the bid amount is within the seller's required range
        if bid_amount < min_bid:
            raise BidValidationError(f"Bid must be at least {min_bid}.")
        elif bid_amount > max_bid:
            raise BidValidationError(f"Bid must not exceed {max_bid}.")
        
        # If all checks pass, the bid is valid
        return True
    
    except BidValidationError as e:
        print(f"Bid validation error: {e}")
        return False


# Example usage
if __name__ == "__main__":
    # Define the minimum and maximum bid amounts
    minimum_bid = 100.0
    maximum_bid = 10000.0

    # User's bid input
    user_bid = 150.0

    # Validate the user's bid
    if validate_bid(user_bid, minimum_bid, maximum_bid):
        print("Bid is valid.")
    else:
        print("Bid is invalid.")
```
