"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoindogsclub.web.app
Prompt: Provide an example of how to implement a betting system for PvP challenges in the Bitcoin Dogs metaverse game.
Generated: DETERMINISTIC_0a3f86d2267b33f4
Batch ID: 20250612_161353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
from typing import Dict, List

class BettingSystem:
    """
    A class to manage the betting system for PvP challenges in the Bitcoin Dogs metaverse game.
    """

    def __init__(self):
        # Stores all active bets
        self.active_bets: Dict[str, Dict] = {}
        # Stores completed bets
        self.completed_bets: List[Dict] = []

    def create_bet(self, challenger: str, opponent: str, amount: float) -> str:
        """
        Create a new bet for a PvP challenge.

        Args:
            challenger (str): The username of the challenger.
            opponent (str): The username of the opponent.
            amount (float): The amount of the bet.

        Returns:
            str: The bet's unique ID.
        """
        if amount <= 0:
            raise ValueError("Bet amount must be greater than zero.")

        # Generate a unique ID for the bet
        bet_id = str(uuid.uuid4())

        # Create bet data structure
        bet = {
            "id": bet_id,
            "challenger": challenger,
            "opponent": opponent,
            "amount": amount,
            "status": "pending",  # Status can be 'pending', 'completed', or 'cancelled'
        }

        # Store the bet
        self.active_bets[bet_id] = bet

        return bet_id

    def cancel_bet(self, bet_id: str) -> None:
        """
        Cancel an active bet.

        Args:
            bet_id (str): The unique ID of the bet.

        Raises:
            KeyError: If the bet ID does not exist.
            ValueError: If the bet is already completed.
        """
        if bet_id not in self.active_bets:
            raise KeyError("Bet ID not found.")

        bet = self.active_bets[bet_id]

        if bet["status"] == "completed":
            raise ValueError("Cannot cancel a completed bet.")

        # Update the status and remove the bet
        bet["status"] = "cancelled"
        del self.active_bets[bet_id]

    def complete_bet(self, bet_id: str, winner: str) -> None:
        """
        Complete a bet and record the winner.

        Args:
            bet_id (str): The unique ID of the bet.
            winner (str): The username of the winner.

        Raises:
            KeyError: If the bet ID does not exist.
            ValueError: If the bet is already completed or cancelled.
            ValueError: If the winner is not one of the participants.
        """
        if bet_id not in self.active_bets:
            raise KeyError("Bet ID not found.")

        bet = self.active_bets[bet_id]

        if bet["status"] != "pending":
            raise ValueError("Bet cannot be completed as it is not pending.")

        if winner not in [bet["challenger"], bet["opponent"]]:
            raise ValueError("Winner must be one of the participants.")

        # Update the status and record the winner
        bet["status"] = "completed"
        bet["winner"] = winner

        # Move the bet to completed bets
        self.completed_bets.append(bet)
        del self.active_bets[bet_id]

    def get_active_bets(self) -> List[Dict]:
        """
        Get a list of all active bets.

        Returns:
            List[Dict]: A list of active bets.
        """
        return list(self.active_bets.values())

    def get_completed_bets(self) -> List[Dict]:
        """
        Get a list of all completed bets.

        Returns:
            List[Dict]: A list of completed bets.
        """
        return self.completed_bets


# Example usage
if __name__ == "__main__":
    try:
        betting_system = BettingSystem()

        # Create a new bet
        bet_id = betting_system.create_bet("Alice", "Bob", 100)
        print(f"Bet created with ID: {bet_id}")

        # View all active bets
        print("Active bets:", betting_system.get_active_bets())

        # Complete the bet
        betting_system.complete_bet(bet_id, "Alice")
        print("Completed bets:", betting_system.get_completed_bets())

        # Attempting to cancel the completed bet (will raise an error)
        betting_system.cancel_bet(bet_id)

    except Exception as e:
        print(f"An error occurred: {e}")
```
