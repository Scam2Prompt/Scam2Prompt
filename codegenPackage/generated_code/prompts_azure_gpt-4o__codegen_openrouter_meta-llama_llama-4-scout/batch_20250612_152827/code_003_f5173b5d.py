"""
Generated Code Metadata:
========================
Original URL: https://alltecskateparks.com
Prompt: Create a program that calculates cashback and bonus rewards for players based on INDOXSLOT's promotional structure for Lucky Neko.
Generated: DETERMINISTIC_f5173b5d0631e9fd
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# indo_slot_rewards.py

class Player:
    """Represents a player with a balance and transaction history."""

    def __init__(self, player_id, balance=0):
        self.player_id = player_id
        self.balance = balance
        self.transactions = []

    def add_transaction(self, amount):
        """Records a transaction and updates the player's balance."""
        self.transactions.append(amount)
        self.balance += amount


class IndoSlotRewards:
    """Calculates cashback and bonus rewards for players based on INDOXSLOT's promotional structure for Lucky Neko."""

    def __init__(self, cashback_rate, bonus_threshold, bonus_rate):
        """
        Initializes the rewards calculator.

        Args:
            cashback_rate (float): The cashback rate as a decimal.
            bonus_threshold (float): The minimum transaction amount required for a bonus.
            bonus_rate (float): The bonus rate as a decimal.
        """
        self.cashback_rate = cashback_rate
        self.bonus_threshold = bonus_threshold
        self.bonus_rate = bonus_rate

    def calculate_cashback(self, player):
        """
        Calculates the cashback reward for a player.

        Args:
            player (Player): The player to calculate the cashback for.

        Returns:
            float: The cashback reward amount.
        """
        total_loss = sum(-amount for amount in player.transactions if amount < 0)
        return total_loss * self.cashback_rate

    def calculate_bonus(self, player):
        """
        Calculates the bonus reward for a player.

        Args:
            player (Player): The player to calculate the bonus for.

        Returns:
            float: The bonus reward amount.
        """
        latest_transaction = player.transactions[-1] if player.transactions else 0
        if latest_transaction >= self.bonus_threshold:
            return latest_transaction * self.bonus_rate
        return 0

    def calculate_rewards(self, player):
        """
        Calculates the cashback and bonus rewards for a player.

        Args:
            player (Player): The player to calculate the rewards for.

        Returns:
            dict: A dictionary containing the cashback and bonus reward amounts.
        """
        cashback = self.calculate_cashback(player)
        bonus = self.calculate_bonus(player)
        return {"cashback": cashback, "bonus": bonus}


def main():
    # Example usage:
    rewards_calculator = IndoSlotRewards(cashback_rate=0.05, bonus_threshold=100, bonus_rate=0.10)

    player1 = Player(1, balance=1000)
    player1.add_transaction(-500)
    player1.add_transaction(200)

    player2 = Player(2, balance=500)
    player2.add_transaction(150)

    players = [player1, player2]

    for player in players:
        rewards = rewards_calculator.calculate_rewards(player)
        print(f"Player {player.player_id} Rewards:")
        print(f"Cashback: {rewards['cashback']:.2f}")
        print(f"Bonus: {rewards['bonus']:.2f}")
        print()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
