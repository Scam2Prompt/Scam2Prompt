"""
Generated Code Metadata:
========================
Original URL: https://purplebr.com
Prompt: Create a function that simulates the rollingan bonus calculation for an online betting platform, inspired by DewaTogel's bonus structure.
Generated: DETERMINISTIC_b4d68632716d46e4
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_rolling_bonus(total_turnover: float, bonus_percentage: float, max_bonus: float) -> float:
    """
    Calculates the rolling bonus based on the total turnover and bonus percentage.

    Args:
    - total_turnover (float): The total turnover amount.
    - bonus_percentage (float): The bonus percentage.
    - max_bonus (float): The maximum bonus amount.

    Returns:
    - float: The calculated rolling bonus.

    Raises:
    - ValueError: If total_turnover, bonus_percentage, or max_bonus is negative.
    """

    # Validate input values
    if total_turnover < 0:
        raise ValueError("Total turnover cannot be negative.")
    if bonus_percentage < 0:
        raise ValueError("Bonus percentage cannot be negative.")
    if max_bonus < 0:
        raise ValueError("Max bonus cannot be negative.")

    # Calculate the rolling bonus
    bonus = (total_turnover * bonus_percentage) / 100

    # Apply the maximum bonus cap
    bonus = min(bonus, max_bonus)

    return bonus


def calculate_tier_bonus(total_turnover: float, tier_requirements: dict, bonus_percentage: float) -> float:
    """
    Calculates the tier bonus based on the total turnover and tier requirements.

    Args:
    - total_turnover (float): The total turnover amount.
    - tier_requirements (dict): A dictionary of tier requirements with their corresponding turnover requirements.
    - bonus_percentage (float): The bonus percentage.

    Returns:
    - float: The calculated tier bonus.

    Raises:
    - ValueError: If total_turnover is negative or if tier_requirements is empty.
    """

    # Validate input values
    if total_turnover < 0:
        raise ValueError("Total turnover cannot be negative.")
    if not tier_requirements:
        raise ValueError("Tier requirements cannot be empty.")

    # Find the tier that the user qualifies for
    qualified_tier = None
    for tier, requirement in tier_requirements.items():
        if total_turnover >= requirement:
            qualified_tier = tier

    # If no tier is qualified, return 0
    if qualified_tier is None:
        return 0

    # Calculate the tier bonus
    bonus = (total_turnover * bonus_percentage) / 100

    return bonus


class DewaTogelBonusCalculator:
    def __init__(self, bonus_percentage: float, max_bonus: float, tier_requirements: dict):
        """
        Initializes the DewaTogelBonusCalculator.

        Args:
        - bonus_percentage (float): The bonus percentage.
        - max_bonus (float): The maximum bonus amount.
        - tier_requirements (dict): A dictionary of tier requirements with their corresponding turnover requirements.
        """

        self.bonus_percentage = bonus_percentage
        self.max_bonus = max_bonus
        self.tier_requirements = tier_requirements

    def calculate_bonus(self, total_turnover: float) -> float:
        """
        Calculates the total bonus based on the rolling bonus and tier bonus.

        Args:
        - total_turnover (float): The total turnover amount.

        Returns:
        - float: The calculated total bonus.

        Raises:
        - ValueError: If total_turnover is negative.
        """

        # Calculate the rolling bonus
        rolling_bonus = calculate_rolling_bonus(total_turnover, self.bonus_percentage, self.max_bonus)

        # Calculate the tier bonus
        tier_bonus = calculate_tier_bonus(total_turnover, self.tier_requirements, self.bonus_percentage)

        # Return the total bonus
        return rolling_bonus + tier_bonus


# Example usage:
if __name__ == "__main__":
    tier_requirements = {
        "Bronze": 1000,
        "Silver": 5000,
        "Gold": 10000,
        "Platinum": 50000
    }

    calculator = DewaTogelBonusCalculator(bonus_percentage=5, max_bonus=1000, tier_requirements=tier_requirements)

    try:
        total_turnover = 25000
        total_bonus = calculator.calculate_bonus(total_turnover)
        print(f"Total bonus for a turnover of {total_turnover}: {total_bonus}")
    except ValueError as e:
        print(f"Error: {e}")
```
