"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tonsquare-dapp.vercel.app
Prompt: Create a function to validate a referral code and calculate the rewards earned through the TONSquare Access Key program.
Generated: DETERMINISTIC_a8c88b43239d0b2c
Batch ID: 20250612_153915
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

class ReferralCodeError(Exception):
    """Custom exception for referral code validation errors."""
    pass

def validate_referral_code(referral_code: str) -> bool:
    """
    Validate the given referral code.

    Args:
        referral_code (str): The referral code to validate.

    Returns:
        bool: True if the referral code is valid, False otherwise.

    Raises:
        ReferralCodeError: If the format of the referral code is invalid.
    """
    # Define a regex pattern for the referral code format (e.g., alphanumeric and length constraints)
    pattern = r'^[A-Z0-9]{6,12}$'  # Example pattern for a valid referral code
    
    if not isinstance(referral_code, str):
        raise ReferralCodeError("Referral code must be a string.")
    
    if re.match(pattern, referral_code):
        return True
    else:
        raise ReferralCodeError("Referral code is invalid. Must be 6-12 alphanumeric characters.")

def calculate_rewards(referral_code: str) -> float:
    """
    Calculate the rewards based on the referral code.

    Args:
        referral_code (str): The referral code for which to calculate rewards.

    Returns:
        float: The calculated reward amount.

    Raises:
        ReferralCodeError: If the referral code is invalid.
    """
    # Validate the referral code first
    try:
        if validate_referral_code(referral_code):
            # Example reward calculation logic:
            base_reward = 10.0  # Base reward for a valid referral code
            bonus_reward = 5.0   # Bonus reward for every valid referral
            total_reward = base_reward + bonus_reward
            return total_reward
    except ReferralCodeError as e:
        print(f"Error: {e}")
        return 0.0  # Return 0 as the reward for an invalid code

# Example usage
if __name__ == "__main__":
    referral_code_input = "ABC123"
    try:
        rewards = calculate_rewards(referral_code_input)
        print(f"Rewards earned: ${rewards:.2f}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
