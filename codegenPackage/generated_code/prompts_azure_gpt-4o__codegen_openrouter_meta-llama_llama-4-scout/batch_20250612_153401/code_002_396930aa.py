"""
Generated Code Metadata:
========================
Original URL: https://gemcaster.vercel.app
Prompt: Generate a function that calculates the earnings for the first minter and the cast creator based on Gemcaster's reward structure.
Generated: DETERMINISTIC_396930aac95a5401
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_earnings(cast_price, minter_referral_percentage, creator_referral_percentage):
    """
    Calculates the earnings for the first minter and the cast creator based on Gemcaster's reward structure.

    Args:
        cast_price (float): The price of the cast.
        minter_referral_percentage (float): The percentage of the cast price that the minter referral receives.
        creator_referral_percentage (float): The percentage of the cast price that the creator referral receives.

    Returns:
        tuple: A tuple containing the earnings for the first minter and the cast creator.

    Raises:
        ValueError: If the cast price or referral percentages are negative.
        ValueError: If the sum of referral percentages exceeds 100%.
    """

    # Validate input values
    if cast_price < 0:
        raise ValueError("Cast price cannot be negative.")
    if minter_referral_percentage < 0 or creator_referral_percentage < 0:
        raise ValueError("Referral percentages cannot be negative.")
    if minter_referral_percentage + creator_referral_percentage > 100:
        raise ValueError("Sum of referral percentages cannot exceed 100%.")

    # Calculate earnings
    minter_earnings = cast_price * (minter_referral_percentage / 100)
    creator_earnings = cast_price * (creator_referral_percentage / 100)

    return minter_earnings, creator_earnings


def main():
    try:
        cast_price = 100.0  # example cast price
        minter_referral_percentage = 10.0  # example minter referral percentage
        creator_referral_percentage = 20.0  # example creator referral percentage

        minter_earnings, creator_earnings = calculate_earnings(cast_price, minter_referral_percentage, creator_referral_percentage)

        print(f"Minter earnings: {minter_earnings}")
        print(f"Creator earnings: {creator_earnings}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
