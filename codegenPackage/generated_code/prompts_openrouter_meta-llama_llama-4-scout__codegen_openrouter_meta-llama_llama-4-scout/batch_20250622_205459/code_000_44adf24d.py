"""
Generated Code Metadata:
========================
Original URL: https://servim.ch
Prompt: What are the key factors to consider when claiming a 400% bonus in online casinos, and how do I ensure I'm meeting the wagering requirements?
Generated: DETERMINISTIC_44adf24def967aee
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re

class CasinoBonus:
    def __init__(self, bonus_amount, wagering_requirement):
        """
        Initialize a CasinoBonus object.

        Args:
            bonus_amount (float): The amount of the bonus.
            wagering_requirement (int): The wagering requirement for the bonus.
        """
        self.bonus_amount = bonus_amount
        self.wagering_requirement = wagering_requirement

    def calculate_wagering_target(self):
        """
        Calculate the target amount that needs to be wagered.

        Returns:
            float: The target amount.
        """
        return self.bonus_amount * self.wagering_requirement


class OnlineCasino:
    def __init__(self, name, bonus_terms):
        """
        Initialize an OnlineCasino object.

        Args:
            name (str): The name of the casino.
            bonus_terms (str): The terms of the bonus.
        """
        self.name = name
        self.bonus_terms = bonus_terms

    def extract_wagering_requirement(self):
        """
        Extract the wagering requirement from the bonus terms.

        Returns:
            int: The wagering requirement.

        Raises:
            ValueError: If the wagering requirement cannot be found.
        """
        pattern = r"(\d+)x"
        match = re.search(pattern, self.bonus_terms)
        if match:
            return int(match.group(1))
        else:
            raise ValueError("Wagering requirement not found")

    def check_eligibility(self, bonus):
        """
        Check if a player is eligible for a bonus.

        Args:
            bonus (CasinoBonus): The bonus to check.

        Returns:
            bool: True if the player is eligible, False otherwise.
        """
        try:
            wagering_requirement = self.extract_wagering_requirement()
            return wagering_requirement > 0
        except ValueError:
            return False


def main():
    # Example usage
    casino = OnlineCasino("Example Casino", "400% bonus with 30x wagering requirement")
    bonus = CasinoBonus(400, 30)

    try:
        wagering_target = bonus.calculate_wagering_target()
        print(f"The wagering target is: {wagering_target}")
        eligible = casino.check_eligibility(bonus)
        print(f"Eligible for bonus: {eligible}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
