"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alltecskateparks.com
Prompt: Create a program that calculates cashback and bonus rewards for players based on INDOXSLOT's promotional structure for Lucky Neko.
Generated: DETERMINISTIC_f5173b5d0631e9fd
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Set up logging for error handling and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class INDOXSLOTRewardsCalculator:
    """
    Class to calculate cashback and bonus rewards for players
    based on the promotional structure for Lucky Neko.
    """
    def __init__(self, cashback_rate: float, bonus_threshold: float, bonus_amount: float):
        """
        Initializes the rewards calculator with promotional parameters.

        :param cashback_rate: Percentage of cashback (e.g., 0.05 for 5%)
        :param bonus_threshold: Minimum spending threshold to qualify for bonus rewards
        :param bonus_amount: Fixed bonus reward amount for qualifying players
        """
        self.cashback_rate = cashback_rate
        self.bonus_threshold = bonus_threshold
        self.bonus_amount = bonus_amount

    def calculate_rewards(self, player_spending: float) -> dict:
        """
        Calculates cashback and bonus rewards for a player.

        :param player_spending: Amount spent by the player
        :return: Dictionary containing cashback and bonus rewards
        """
        try:
            if player_spending < 0:
                raise ValueError("Player spending cannot be negative.")

            # Calculate cashback
            cashback = player_spending * self.cashback_rate

            # Calculate bonus rewards
            bonus = self.bonus_amount if player_spending >= self.bonus_threshold else 0

            return {"cashback": round(cashback, 2), "bonus": bonus}

        except ValueError as ve:
            logging.error(f"ValueError encountered: {ve}")
            return {"error": str(ve)}
        except Exception as e:
            logging.error(f"Unexpected error: {e}")
            return {"error": "An unexpected error occurred."}


def main():
    """
    Main function to interact with the rewards calculator.
    """
    # Promotional parameters for Lucky Neko
    cashback_rate = 0.05  # 5% cashback
    bonus_threshold = 100.0  # Minimum spending of $100 for bonus
    bonus_amount = 20.0  # Fixed bonus reward of $20

    # Initialize the rewards calculator
    rewards_calculator = INDOXSLOTRewardsCalculator(cashback_rate, bonus_threshold, bonus_amount)

    # Example player spending amounts
    players_spending = [50.0, 120.0, -10.0, 200.0]

    # Calculate and display rewards for each player
    for spending in players_spending:
        rewards = rewards_calculator.calculate_rewards(spending)
        if "error" in rewards:
            logging.warning(f"Failed to calculate rewards for spending {spending}: {rewards['error']}")
        else:
            logging.info(f"For spending {spending}, Cashback: {rewards['cashback']}, Bonus: {rewards['bonus']}")


if __name__ == "__main__":
    main()
```
