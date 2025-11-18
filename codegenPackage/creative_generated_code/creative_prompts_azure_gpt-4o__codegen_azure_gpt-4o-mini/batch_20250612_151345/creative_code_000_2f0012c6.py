"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://foodandwine.one
Prompt: Write a Python script to simulate a betting system for sports, including features like odds calculation, bet placement, and payout computation, inspired by the offerings of Hi88.
Generated: DETERMINISTIC_2f0012c6e9c0e2ea
Batch ID: 20250612_151345
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class BettingSystem:
    def __init__(self):
        # Initialize an empty dictionary to store bets
        self.bets = {}
        self.odds = self.generate_odds()
    
    def generate_odds(self):
        """
        Generate random odds for different outcomes in a sporting event.
        For simplicity, we will create odds for three different outcomes.
        """
        return {
            "Team A": round(random.uniform(1.5, 3.0), 2),
            "Team B": round(random.uniform(1.5, 3.0), 2),
            "Draw": round(random.uniform(2.0, 4.0), 2)
        }

    def place_bet(self, user_id, team, amount):
        """
        Place a bet for a specific user on a given team.
        
        Parameters:
            user_id (str): Unique identifier for the user
            team (str): The team on which the bet is placed
            amount (float): The amount of money being bet

        Raises:
            ValueError: If the bet amount is not positive or team is invalid
        """
        if amount <= 0:
            raise ValueError("Bet amount must be positive.")
        
        if team not in self.odds:
            raise ValueError("Invalid team selected for betting.")

        if user_id not in self.bets:
            self.bets[user_id] = []
        
        # Store the bet details
        self.bets[user_id].append({"team": team, "amount": amount})
        print(f"User {user_id} placed a bet of ${amount} on {team}.")

    def calculate_payout(self, user_id):
        """
        Calculate the total payout for a user based on their bets and the current odds.
        
        Parameters:
            user_id (str): Unique identifier for the user
            
        Returns:
            float: Total payout amount for the user
        """
        if user_id not in self.bets:
            return 0.0  # No bets placed by this user

        total_payout = 0.0
        for bet in self.bets[user_id]:
            team = bet["team"]
            amount = bet["amount"]
            payout = amount * self.odds[team]
            total_payout += payout
            print(f"Bet on {team}: Bet amount ${amount}, Payout ${payout:.2f}")

        return total_payout

    def show_odds(self):
        """
        Display the current odds for each outcome.
        """
        print("Current Odds:")
        for team, odds in self.odds.items():
            print(f"{team}: {odds}")

def main():
    # Create an instance of the Betting System
    betting_system = BettingSystem()
    
    # Show current odds
    betting_system.show_odds()

    # Sample user interaction
    try:
        betting_system.place_bet("user123", "Team A", 100)
        betting_system.place_bet("user123", "Draw", 50)

        # Calculate and display payout for the user
        payout = betting_system.calculate_payout("user123")
        print(f"Total payout for user123: ${payout:.2f}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
