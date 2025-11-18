"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cybercoclaim.pages.dev
Prompt: Write a function to calculate referral points based on the CYBER referral system described in the content.
Generated: DETERMINISTIC_4d72d0ae28c99aab
Batch ID: 20250612_151003
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_referral_points(referrals, base_points=10, bonus_threshold=5, bonus_points=50):
    """
    Calculate referral points based on the CYBER referral system.

    Parameters:
    - referrals (int): Number of referrals made by the user.
    - base_points (int): Points awarded per referral (default: 10).
    - bonus_threshold (int): Number of referrals required to earn bonus points (default: 5).
    - bonus_points (int): Bonus points awarded for meeting the bonus threshold (default: 50).

    Returns:
    - int: Total referral points earned by the user.
    """
    try:
        # Ensure referrals is a positive integer
        if not isinstance(referrals, int) or referrals < 0:
            raise ValueError("Referrals must be a non-negative integer.")

        # Calculate base points
        total_points = referrals * base_points

        # Add bonus points if referrals exceed the bonus threshold
        if referrals >= bonus_threshold:
            total_points += bonus_points

        return total_points

    except ValueError as e:
        # Handle invalid input
        print(f"Error: {e}")
        return 0  # Return 0 points for invalid input

# Example usage:
if __name__ == "__main__":
    # Test with valid input
    referrals = 7
    points = calculate_referral_points(referrals)
    print(f"Total points for {referrals} referrals: {points}")

    # Test with invalid input
    referrals = -3
    points = calculate_referral_points(referrals)
    print(f"Total points for {referrals} referrals: {points}")
```
