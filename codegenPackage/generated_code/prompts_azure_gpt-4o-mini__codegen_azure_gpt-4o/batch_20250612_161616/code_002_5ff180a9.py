"""
Generated Code Metadata:
========================
Original URL: https://purplebr.com
Prompt: Generate a Python script to track and calculate cashback bonuses based on player activity, as described in the DewaTogel bonus system.
Generated: DETERMINISTIC_5ff180a9cdffc9a7
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import List, Dict

class Player:
    """
    Represents a player in the system.
    """
    def __init__(self, player_id: int, name: str):
        self.player_id = player_id
        self.name = name
        self.transactions = []  # List to store transaction history

    def add_transaction(self, amount: float, transaction_date: datetime.date):
        """
        Adds a transaction to the player's history.
        :param amount: The amount of the transaction (positive for bets, negative for withdrawals).
        :param transaction_date: The date of the transaction.
        """
        self.transactions.append({
            "amount": amount,
            "date": transaction_date
        })

    def get_total_bets(self, start_date: datetime.date, end_date: datetime.date) -> float:
        """
        Calculates the total bets made by the player within a date range.
        :param start_date: The start date of the range.
        :param end_date: The end date of the range.
        :return: Total bet amount.
        """
        return sum(
            t["amount"] for t in self.transactions
            if start_date <= t["date"] <= end_date and t["amount"] > 0
        )


class CashbackSystem:
    """
    System to calculate and track cashback bonuses for players.
    """
    def __init__(self, cashback_rate: float):
        """
        Initializes the cashback system.
        :param cashback_rate: The cashback rate as a percentage (e.g., 10 for 10%).
        """
        if cashback_rate < 0 or cashback_rate > 100:
            raise ValueError("Cashback rate must be between 0 and 100.")
        self.cashback_rate = cashback_rate / 100  # Convert percentage to decimal
        self.players: Dict[int, Player] = {}  # Dictionary to store players by ID

    def add_player(self, player: Player):
        """
        Adds a player to the system.
        :param player: The Player object to add.
        """
        if player.player_id in self.players:
            raise ValueError(f"Player with ID {player.player_id} already exists.")
        self.players[player.player_id] = player

    def calculate_cashback(self, player_id: int, start_date: datetime.date, end_date: datetime.date) -> float:
        """
        Calculates the cashback for a player within a date range.
        :param player_id: The ID of the player.
        :param start_date: The start date of the range.
        :param end_date: The end date of the range.
        :return: The cashback amount.
        """
        if player_id not in self.players:
            raise ValueError(f"Player with ID {player_id} not found.")
        
        player = self.players[player_id]
        total_bets = player.get_total_bets(start_date, end_date)
        cashback = total_bets * self.cashback_rate
        return round(cashback, 2)  # Round to 2 decimal places for currency

    def generate_cashback_report(self, start_date: datetime.date, end_date: datetime.date) -> List[Dict]:
        """
        Generates a cashback report for all players within a date range.
        :param start_date: The start date of the range.
        :param end_date: The end date of the range.
        :return: A list of dictionaries containing player details and cashback amounts.
        """
        report = []
        for player_id, player in self.players.items():
            cashback = self.calculate_cashback(player_id, start_date, end_date)
            report.append({
                "player_id": player_id,
                "name": player.name,
                "cashback": cashback
            })
        return report


# Example usage
if __name__ == "__main__":
    # Initialize the cashback system with a 10% cashback rate
    cashback_system = CashbackSystem(cashback_rate=10)

    # Create players
    player1 = Player(player_id=1, name="Alice")
    player2 = Player(player_id=2, name="Bob")

    # Add players to the system
    cashback_system.add_player(player1)
    cashback_system.add_player(player2)

    # Add transactions for players
    today = datetime.date.today()
    player1.add_transaction(amount=100.0, transaction_date=today)
    player1.add_transaction(amount=200.0, transaction_date=today)
    player2.add_transaction(amount=50.0, transaction_date=today)

    # Calculate cashback for a specific player
    start_date = today - datetime.timedelta(days=7)  # Last 7 days
    end_date = today
    cashback = cashback_system.calculate_cashback(player_id=1, start_date=start_date, end_date=end_date)
    print(f"Cashback for Alice: ${cashback}")

    # Generate a cashback report for all players
    report = cashback_system.generate_cashback_report(start_date=start_date, end_date=end_date)
    print("Cashback Report:")
    for entry in report:
        print(f"Player: {entry['name']}, Cashback: ${entry['cashback']}")
```
