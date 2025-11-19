"""
Generated Code Metadata:
========================
Original URL: https://coinex-tradings.ltd
Prompt: Write a script to simulate the referral bonus system described in Coinex Tradings' investment plans, including calculations for 5% bonuses.
Generated: DETERMINISTIC_9d7b3f80d1c039fd
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# referral_bonus_system.py

def calculate_referral_bonus(investment_amount, referral_level):
    """
    Calculates the referral bonus based on the investment amount and referral level.

    Args:
        investment_amount (float): The amount invested by the user.
        referral_level (int): The level of the referral (1-5).

    Returns:
        float: The referral bonus amount.

    Raises:
        ValueError: If the referral level is not between 1 and 5.
    """
    if not 1 <= referral_level <= 5:
        raise ValueError("Referral level must be between 1 and 5")

    # Define the bonus percentages for each referral level
    bonus_percentages = {
        1: 0.05,  # 5% bonus for level 1 referrals
        2: 0.04,  # 4% bonus for level 2 referrals
        3: 0.03,  # 3% bonus for level 3 referrals
        4: 0.02,  # 2% bonus for level 4 referrals
        5: 0.01   # 1% bonus for level 5 referrals
    }

    bonus_percentage = bonus_percentages[referral_level]
    referral_bonus = investment_amount * bonus_percentage

    return referral_bonus


def simulate_referral_bonus_system(investments):
    """
    Simulates the referral bonus system for a list of investments.

    Args:
        investments (list): A list of dictionaries containing the investment amount and referral level.

    Returns:
        list: A list of dictionaries containing the investment amount, referral level, and referral bonus.

    Raises:
        ValueError: If the investment amount or referral level is invalid.
    """
    results = []

    for investment in investments:
        try:
            investment_amount = float(investment["amount"])
            referral_level = int(investment["referral_level"])

            if investment_amount <= 0:
                raise ValueError("Investment amount must be greater than zero")

            referral_bonus = calculate_referral_bonus(investment_amount, referral_level)

            results.append({
                "investment_amount": investment_amount,
                "referral_level": referral_level,
                "referral_bonus": referral_bonus
            })

        except (KeyError, ValueError) as e:
            print(f"Error processing investment: {e}")

    return results


# Example usage
if __name__ == "__main__":
    investments = [
        {"amount": 1000, "referral_level": 1},
        {"amount": 500, "referral_level": 2},
        {"amount": 2000, "referral_level": 3},
        {"amount": 1500, "referral_level": 4},
        {"amount": 2500, "referral_level": 5}
    ]

    results = simulate_referral_bonus_system(investments)

    for result in results:
        print(f"Investment Amount: {result['investment_amount']}, Referral Level: {result['referral_level']}, Referral Bonus: {result['referral_bonus']}")
```
