"""
Generated Code Metadata:
========================
Original URL: https://monadday23.testnet.nfts2.me
Prompt: Create a function to calculate referral earnings based on the number of mints completed through a referral link, using the reward rate of 0.00000000666 tMON per mint.
Generated: DETERMINISTIC_7385085d160dff21
Batch ID: 20250612_155057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_referral_earnings(mints_completed: int, reward_rate: float = 0.00000000666) -> float:
    """
    Calculate referral earnings based on the number of mints completed through a referral link.

    Args:
    - mints_completed (int): The number of mints completed through the referral link.
    - reward_rate (float, optional): The reward rate per mint. Defaults to 0.00000000666.

    Returns:
    - float: The total referral earnings in tMON.

    Raises:
    - TypeError: If mints_completed is not an integer or reward_rate is not a float.
    - ValueError: If mints_completed or reward_rate is negative.
    """

    # Validate input types
    if not isinstance(mints_completed, int):
        raise TypeError("mints_completed must be an integer.")
    if not isinstance(reward_rate, (int, float)):
        raise TypeError("reward_rate must be a float.")

    # Validate input values
    if mints_completed < 0:
        raise ValueError("mints_completed cannot be negative.")
    if reward_rate < 0:
        raise ValueError("reward_rate cannot be negative.")

    # Calculate referral earnings
    try:
        referral_earnings = mints_completed * reward_rate
        return referral_earnings
    except Exception as e:
        # Log and re-raise any unexpected errors
        print(f"An unexpected error occurred: {str(e)}")
        raise


# Example usage:
if __name__ == "__main__":
    mints = 1000000
    earnings = calculate_referral_earnings(mints)
    print(f"Referral earnings for {mints} mints: {earnings} tMON")
```
