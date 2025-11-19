"""
Generated Code Metadata:
========================
Original URL: https://coindoor.trade
Prompt: "Design a referral program with 5 levels of income, similar to Coindoor's program, and calculate the bonuses for each level based on minimum investment and team investment requirements."
Generated: DETERMINISTIC_cb670cb2dc382a5a
Batch ID: 20250622_212046
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# referral_program.py

class ReferralProgram:
    """
    A referral program with 5 levels of income.
    """

    def __init__(self):
        # Define the referral levels with their minimum investment and team investment requirements
        self.levels = [
            {"level": 1, "min_investment": 100, "team_investment": 0, "bonus_percentage": 5},
            {"level": 2, "min_investment": 500, "team_investment": 2000, "bonus_percentage": 3},
            {"level": 3, "min_investment": 2000, "team_investment": 10000, "bonus_percentage": 2},
            {"level": 4, "min_investment": 5000, "team_investment": 25000, "bonus_percentage": 1.5},
            {"level": 5, "min_investment": 10000, "team_investment": 50000, "bonus_percentage": 1},
        ]

    def calculate_bonus(self, level, investment_amount):
        """
        Calculate the bonus for a given level and investment amount.

        Args:
            level (int): The level of the referral program.
            investment_amount (float): The investment amount.

        Returns:
            float: The calculated bonus.

        Raises:
            ValueError: If the level is not found.
        """
        level_config = next((level_config for level_config in self.levels if level_config["level"] == level), None)
        if level_config is None:
            raise ValueError("Invalid level")

        bonus_percentage = level_config["bonus_percentage"]
        bonus = investment_amount * (bonus_percentage / 100)
        return bonus

    def check_eligibility(self, level, investment_amount, team_investment):
        """
        Check if a user is eligible for a given level.

        Args:
            level (int): The level of the referral program.
            investment_amount (float): The investment amount.
            team_investment (float): The team investment.

        Returns:
            bool: True if the user is eligible, False otherwise.

        Raises:
            ValueError: If the level is not found.
        """
        level_config = next((level_config for level_config in self.levels if level_config["level"] == level), None)
        if level_config is None:
            raise ValueError("Invalid level")

        return investment_amount >= level_config["min_investment"] and team_investment >= level_config["team_investment"]

    def get_referral_bonuses(self, investment_amount, team_investment):
        """
        Get the referral bonuses for each level.

        Args:
            investment_amount (float): The investment amount.
            team_investment (float): The team investment.

        Returns:
            dict: A dictionary with the level as key and the bonus as value.
        """
        bonuses = {}
        for level_config in self.levels:
            if self.check_eligibility(level_config["level"], investment_amount, team_investment):
                bonus = self.calculate_bonus(level_config["level"], investment_amount)
                bonuses[level_config["level"]] = bonus
        return bonuses


def main():
    referral_program = ReferralProgram()

    # Example usage:
    investment_amount = 10000
    team_investment = 50000

    print("Referral Bonuses:")
    bonuses = referral_program.get_referral_bonuses(investment_amount, team_investment)
    for level, bonus in bonuses.items():
        print(f"Level {level}: ${bonus:.2f}")

    try:
        invalid_level = 6
        referral_program.calculate_bonus(invalid_level, investment_amount)
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
