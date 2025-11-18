"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://landing-jackpotcow.pages.dev
Prompt: Write code to implement a loyalty rewards system for an online casino, including free spins and exclusive perks for players, as highlighted in Jackpot Cow Casino's promotions.
Generated: DETERMINISTIC_9968ac25eea8e0bd
Batch ID: 20250612_154542
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class LoyaltyRewardsSystem:
    def __init__(self):
        """Initialize the Loyalty Rewards System with a user database."""
        self.players = {}  # Dictionary to store player data

    class Player:
        """A class representing a player in the loyalty rewards system."""
        def __init__(self, player_id, name):
            self.player_id = player_id
            self.name = name
            self.points = 0  # Loyalty points for the player
            self.free_spins = 0  # Number of free spins
            self.exclusive_perks = []  # List to store exclusive perks

        def add_points(self, points):
            """Add loyalty points to the player's account."""
            if points < 0:
                raise ValueError("Cannot add negative points.")
            self.points += points

        def redeem_free_spins(self, spins):
            """Redeem free spins for the player."""
            if spins < 0:
                raise ValueError("Cannot redeem negative spins.")
            if self.free_spins >= spins:
                self.free_spins -= spins
                return spins
            else:
                raise ValueError("Not enough free spins available.")

        def add_exclusive_perk(self, perk):
            """Add an exclusive perk to the player's account."""
            self.exclusive_perks.append(perk)

    def register_player(self, player_id, name):
        """Register a new player in the loyalty rewards system."""
        if player_id in self.players:
            raise ValueError("Player with this ID already exists.")
        self.players[player_id] = self.Player(player_id, name)

    def add_loyalty_points(self, player_id, points):
        """Add loyalty points to a specified player's account."""
        if player_id not in self.players:
            raise ValueError("Player not found.")
        self.players[player_id].add_points(points)

    def award_free_spins(self, player_id, spins):
        """Award free spins to a specified player's account."""
        if player_id not in self.players:
            raise ValueError("Player not found.")
        self.players[player_id].free_spins += spins

    def grant_exclusive_perk(self, player_id, perk):
        """Grant exclusive perks to a specified player's account."""
        if player_id not in self.players:
            raise ValueError("Player not found.")
        self.players[player_id].add_exclusive_perk(perk)

    def get_player_info(self, player_id):
        """Retrieve information about a specified player."""
        if player_id not in self.players:
            raise ValueError("Player not found.")
        player = self.players[player_id]
        return {
            "id": player.player_id,
            "name": player.name,
            "points": player.points,
            "free_spins": player.free_spins,
            "exclusive_perks": player.exclusive_perks
        }

# Example usage
if __name__ == "__main__":
    loyalty_system = LoyaltyRewardsSystem()

    try:
        # Register players
        loyalty_system.register_player(1, "Alice")
        loyalty_system.register_player(2, "Bob")

        # Add loyalty points
        loyalty_system.add_loyalty_points(1, 100)
        loyalty_system.add_loyalty_points(2, 150)

        # Award free spins
        loyalty_system.award_free_spins(1, 5)

        # Grant exclusive perks
        loyalty_system.grant_exclusive_perk(1, "VIP Access")
        loyalty_system.grant_exclusive_perk(2, "Birthday Bonus")

        # Get player info
        alice_info = loyalty_system.get_player_info(1)
        bob_info = loyalty_system.get_player_info(2)
        
        print("Alice's Info:", alice_info)
        print("Bob's Info:", bob_info)

    except ValueError as e:
        print(f"Error: {e}")
```
