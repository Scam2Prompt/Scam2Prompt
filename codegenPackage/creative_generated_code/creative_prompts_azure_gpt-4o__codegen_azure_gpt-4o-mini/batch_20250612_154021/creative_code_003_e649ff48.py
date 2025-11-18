"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimhyperlane.foundation
Prompt: Create a function to verify eligibility for claiming $HYPER tokens based on fee spending thresholds ($5.00 USD notional) and activity on Hyperlane-supported chains.
Generated: DETERMINISTIC_e649ff48fc74a526
Batch ID: 20250612_154021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class EligibilityError(Exception):
    """Custom exception for eligibility verification errors."""
    pass

def verify_hyper_token_eligibility(user_activity, fee_spent):
    """
    Verify eligibility for claiming $HYPER tokens based on fee spending thresholds and activity.

    Args:
        user_activity (dict): A dictionary containing user activity data,
                              with chains as keys and activity counts as values.
        fee_spent (float): The total fees spent by the user in USD.

    Returns:
        bool: True if eligible, False otherwise.

    Raises:
        EligibilityError: If the input data is invalid.
    """
    
    # Validate the fee_spent input
    if not isinstance(fee_spent, (int, float)) or fee_spent < 0:
        raise EligibilityError("Invalid fee spent value. It should be a non-negative number.")

    # Define eligibility criteria
    REQUIRED_FEE_SPENT = 5.00  # USD
    REQUIRED_ACTIVITY_COUNT = 1  # Minimum activity in any supported chain
    
    # Check if fee spent meets the threshold
    if fee_spent < REQUIRED_FEE_SPENT:
        return False
    
    # Check user activity on Hyperlane-supported chains
    if not isinstance(user_activity, dict) or not user_activity:
        raise EligibilityError("Invalid user activity data. It should be a non-empty dictionary.")

    # Determine if the user has sufficient activity
    for chain, activity_count in user_activity.items():
        if not isinstance(activity_count, int) or activity_count < 0:
            raise EligibilityError(f"Invalid activity count for chain '{chain}'. It should be a non-negative integer.")
        
        if activity_count >= REQUIRED_ACTIVITY_COUNT:
            return True  # User is eligible
    
    return False  # No sufficient activity found

# Example usage
if __name__ == "__main__":
    user_activity = {
        "ChainA": 2,
        "ChainB": 0,
        "ChainC": 1
    }
    fee_spent = 6.00  # Example fee spent

    try:
        eligibility = verify_hyper_token_eligibility(user_activity, fee_spent)
        print(f"User is eligible for $HYPER tokens: {eligibility}")
    except EligibilityError as e:
        print(f"Eligibility verification failed: {e}")
```
