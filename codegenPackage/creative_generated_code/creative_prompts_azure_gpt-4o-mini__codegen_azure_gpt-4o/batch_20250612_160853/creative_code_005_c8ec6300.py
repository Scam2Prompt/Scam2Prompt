"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moonbags.pages.dev
Prompt: Create a function that calculates the total MBAG tokens earned from referrals based on the number of uses of a referral code.
Generated: DETERMINISTIC_c8ec63004783b1fb
Batch ID: 20250612_160853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Function to calculate total MBAG tokens earned from referrals
def calculate_mbag_tokens(referral_uses, tokens_per_referral=10):
    """
    Calculate the total MBAG tokens earned from referrals.

    Args:
        referral_uses (int): The number of times the referral code has been used.
        tokens_per_referral (int, optional): Number of MBAG tokens earned per referral. Default is 10.

    Returns:
        int: Total MBAG tokens earned.

    Raises:
        ValueError: If referral_uses is negative or not an integer.
    """
    try:
        # Validate input
        if not isinstance(referral_uses, int):
            raise ValueError("The referral_uses parameter must be an integer.")
        if referral_uses < 0:
            raise ValueError("The referral_uses parameter cannot be negative.")
        
        # Calculate total tokens earned
        total_tokens = referral_uses * tokens_per_referral
        return total_tokens
    except ValueError as e:
        print(f"Error: {e}")
        return 0  # Return 0 tokens in case of an error

# Example usage:
if __name__ == "__main__":
    try:
        # Input: Number of referral uses
        referral_uses = int(input("Enter number of referral uses: "))

        # Calculate tokens earned
        total_tokens = calculate_mbag_tokens(referral_uses)
        print(f"Total MBAG tokens earned: {total_tokens}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
```
