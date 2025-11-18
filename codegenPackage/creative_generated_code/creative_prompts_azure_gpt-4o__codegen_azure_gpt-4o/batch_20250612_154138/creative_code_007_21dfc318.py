"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://venez888.vip
Prompt: Generate Python code to simulate a jackpot system where users can win large rewards, inspired by the "รางวัลแจ็คพอต" feature on venez888.vip.
Generated: DETERMINISTIC_21dfc318a2846f1f
Batch ID: 20250612_154138
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import time

class JackpotSystem:
    """
    A system to simulate a jackpot feature, allowing users to win large rewards.
    """

    def __init__(self, jackpot_amount):
        """
        Initialize the jackpot system with a specified jackpot amount.

        Args:
            jackpot_amount (float): The total amount of the jackpot.
        """
        self.jackpot_amount = jackpot_amount
        self.participants = {}
        self.winners = []

    def add_participant(self, user_id, contribution):
        """
        Add a participant to the jackpot system.

        Args:
            user_id (str): Unique identifier for the user.
            contribution (float): Amount contributed by the user.

        Raises:
            ValueError: If contribution is less than or equal to 0.
        """
        if contribution <= 0:
            raise ValueError("Contribution must be greater than zero.")
        
        # Add or update participant's contribution
        self.participants[user_id] = self.participants.get(user_id, 0) + contribution

    def draw_winner(self):
        """
        Simulate drawing a winner for the jackpot.

        Returns:
            tuple: Winner's user ID and the reward amount.

        Raises:
            ValueError: If no participants exist.
        """
        if not self.participants:
            raise ValueError("No participants available for the jackpot draw.")
        
        # Weighted random draw based on contributions
        user_ids = list(self.participants.keys())
        weights = list(self.participants.values())

        winner = random.choices(user_ids, weights=weights, k=1)[0]
        reward = round(self.jackpot_amount, 2)

        self.winners.append((winner, reward))
        self.participants.clear()  # Reset participants for the next round

        return winner, reward

    def show_winners(self):
        """
        Retrieve the list of winners.

        Returns:
            list: List of tuples containing winner user IDs and their rewards.
        """
        return self.winners


# Example usage
def main():
    try:
        # Create a jackpot system with a starting reward of $10,000
        jackpot = JackpotSystem(jackpot_amount=10000.00)
        
        # Add participants to the jackpot
        jackpot.add_participant("user1", 500.00)   # User 1 contributes $500
        jackpot.add_participant("user2", 1500.00)  # User 2 contributes $1500
        jackpot.add_participant("user3", 250.00)   # User 3 contributes $250
        
        # Simulate the jackpot draw
        print("Drawing the jackpot winner...")
        time.sleep(2)  # Simulate suspense
        
        winner, reward = jackpot.draw_winner()
        print(f"Congratulations! {winner} has won the jackpot of ${reward:.2f}.")
        
        # Show previous winners
        print("Previous winners:")
        for user_id, amount in jackpot.show_winners():
            print(f"- {user_id} won ${amount:.2f}")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Run the example if this script is executed directly
if __name__ == "__main__":
    main()
```
