"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starltoken.com
Prompt: Write code to create a loyalty program for a cryptocurrency casino, including tiered VIP benefits and cashback rewards, inspired by the STARL Token site.
Generated: DETERMINISTIC_a41df721c50650c0
Batch ID: 20250612_145455
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class LoyaltyProgram:
    """
    A class to manage the loyalty program for a cryptocurrency casino,
    including tiered VIP benefits and cashback rewards.
    """

    def __init__(self):
        # Initialize tiers and their respective benefits
        self.tiers = {
            "Bronze": {"min_bet": 0, "cashback_rate": 0.01, "benefits": ["Access to promotions"]},
            "Silver": {"min_bet": 1000, "cashback_rate": 0.02, "benefits": ["Monthly bonuses", "Exclusive games"]},
            "Gold": {"min_bet": 5000, "cashback_rate": 0.05, "benefits": ["Priority support", "VIP events"]},
            "Platinum": {"min_bet": 10000, "cashback_rate": 0.1, "benefits": ["Personal account manager", "High stakes tables"]}
        }
        self.players = {}

    def add_player(self, player_id, total_bet):
        """
        Add a new player to the loyalty program.
        
        :param player_id: Unique identifier for the player
        :param total_bet: Total amount the player has bet
        """
        if player_id in self.players:
            raise ValueError("Player already exists.")
        
        self.players[player_id] = {
            "total_bet": total_bet,
            "tier": self.calculate_tier(total_bet),
            "cashback": 0
        }

    def calculate_tier(self, total_bet):
        """
        Calculate the player's tier based on their total bets.
        
        :param total_bet: Total amount the player has bet
        :return: Tier level as a string
        """
        for tier, info in reversed(self.tiers.items()):
            if total_bet >= info["min_bet"]:
                return tier
        return "Bronze"

    def update_player_bet(self, player_id, bet_amount):
        """
        Update a player's total bet and tier.
        
        :param player_id: Unique identifier for the player
        :param bet_amount: Amount to add to the player's total bet
        """
        if player_id not in self.players:
            raise ValueError("Player not found.")

        self.players[player_id]["total_bet"] += bet_amount
        self.players[player_id]["tier"] = self.calculate_tier(self.players[player_id]["total_bet"])

    def calculate_cashback(self, player_id):
        """
        Calculate and apply cashback for a player based on their current tier.
        
        :param player_id: Unique identifier for the player
        :return: Amount of cashback
        """
        if player_id not in self.players:
            raise ValueError("Player not found.")
        
        tier = self.players[player_id]["tier"]
        cashback_rate = self.tiers[tier]["cashback_rate"]
        total_bet = self.players[player_id]["total_bet"]

        cashback = total_bet * cashback_rate
        self.players[player_id]["cashback"] += cashback
        return cashback

    def get_player_info(self, player_id):
        """
        Retrieve information about a player in the loyalty program.
        
        :param player_id: Unique identifier for the player
        :return: Player information as a dictionary
        """
        if player_id not in self.players:
            raise ValueError("Player not found.")
        
        return self.players[player_id]

# Example usage
if __name__ == "__main__":
    loyalty_program = LoyaltyProgram()

    try:
        loyalty_program.add_player("player1", 500)
        loyalty_program.update_player_bet("player1", 800)
        cashback = loyalty_program.calculate_cashback("player1")
        player_info = loyalty_program.get_player_info("player1")
        
        print("Player Info:", player_info)
        print("Cashback Earned:", cashback)
        
    except ValueError as e:
        print("Error:", e)
```
