"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://buylibracoins.com
Prompt: Provide a code example for a bonus system that rewards players using wallet payments in an online slot game.
Generated: DETERMINISTIC_4266c99363040f5d
Batch ID: 20250612_164000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Player:
    def __init__(self, player_id, wallet_balance=0.0):
        """
        Initializes a new player with a unique ID and an optional wallet balance.

        :param player_id: Unique identifier for the player
        :param wallet_balance: Initial balance in the player's wallet
        """
        self.player_id = player_id
        self.wallet_balance = wallet_balance

    def add_funds(self, amount):
        """
        Adds funds to the player's wallet.

        :param amount: Amount to be added to the wallet
        :raises ValueError: If amount is negative
        """
        if amount < 0:
            raise ValueError("Amount must be non-negative")
        self.wallet_balance += amount

    def deduct_funds(self, amount):
        """
        Deducts funds from the player's wallet if sufficient balance is available.

        :param amount: Amount to be deducted from the wallet
        :raises ValueError: If amount is negative or exceeds wallet balance
        """
        if amount < 0:
            raise ValueError("Amount must be non-negative")
        if amount > self.wallet_balance:
            raise ValueError("Insufficient funds in wallet")
        self.wallet_balance -= amount


class BonusSystem:
    def __init__(self):
        """
        Initializes the bonus system with a predefined set of bonuses.
        """
        self.bonuses = {
            'small_win': 5.0,   # Small win bonus
            'medium_win': 10.0, # Medium win bonus
            'big_win': 20.0      # Big win bonus
        }

    def reward_player(self, player, win_type):
        """
        Rewards the player based on the type of win.

        :param player: Instance of Player class
        :param win_type: Type of win ('small_win', 'medium_win', 'big_win')
        :raises ValueError: If win_type is not recognized
        """
        if win_type not in self.bonuses:
            raise ValueError("Invalid win type specified")

        bonus_amount = self.bonuses[win_type]
        player.add_funds(bonus_amount)
        print(f"Player {player.player_id} rewarded with {bonus_amount} for {win_type}!")

    def check_wallet_balance(self, player):
        """
        Checks and returns the wallet balance of the player.

        :param player: Instance of Player class
        :return: Current wallet balance
        """
        return player.wallet_balance


# Example Usage:
if __name__ == "__main__":
    # Create a new player with an initial balance
    player1 = Player(player_id='player1', wallet_balance=100.0)

    # Create a bonus system instance
    bonus_system = BonusSystem()

    # Reward player for a small win
    try:
        bonus_system.reward_player(player1, 'small_win')
    except ValueError as e:
        print(e)

    # Check current wallet balance
    print(f"Current wallet balance for {player1.player_id}: {bonus_system.check_wallet_balance(player1)}")
    
    # Attempt to deduct funds
    try:
        player1.deduct_funds(50.0)
        print(f"Balance after deduction: {player1.wallet_balance}")
    except ValueError as e:
        print(e)
```
