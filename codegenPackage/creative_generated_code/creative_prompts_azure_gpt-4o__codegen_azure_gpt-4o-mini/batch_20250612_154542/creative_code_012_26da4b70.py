"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://landing-jackpotcow.pages.dev
Prompt: Write a script to calculate and distribute jackpot winnings among players, ensuring half goes to the winner and the rest to top contributors, as described in Jackpot Cow Casino's jackpot system.
Generated: DETERMINISTIC_26da4b703d5546e3
Batch ID: 20250612_154542
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Jackpot:
    def __init__(self, total_amount):
        """
        Initialize the Jackpot with a total amount.
        
        :param total_amount: Total amount available for distribution.
        """
        if total_amount <= 0:
            raise ValueError("Total amount must be greater than zero.")
        self.total_amount = total_amount
        self.winner_share = total_amount / 2
        self.contributors_share = total_amount / 2
        self.contributors = []

    def add_contributor(self, player_name, contribution):
        """
        Add a player's contribution to the jackpot.
        
        :param player_name: Name of the player.
        :param contribution: Contribution amount from the player.
        """
        if contribution <= 0:
            raise ValueError("Contribution must be greater than zero.")
        self.contributors.append((player_name, contribution))

    def distribute_winnings(self):
        """
        Distribute the jackpot winnings to the winner and contributors.
        
        :return: Dictionary containing the winner's share and each contributor's share.
        """
        if not self.contributors:
            raise RuntimeError("No contributors available to distribute winnings.")

        # Calculate total contributions
        total_contributions = sum(contribution for _, contribution in self.contributors)

        if total_contributions <= 0:
            raise RuntimeError("Total contributions must be greater than zero.")

        # Calculate each contributor's share based on their contribution percentage
        contributor_distribution = {}
        for player_name, contribution in self.contributors:
            share = (contribution / total_contributions) * self.contributors_share
            contributor_distribution[player_name] = share

        return {
            "winner_share": self.winner_share,
            "contributor_distribution": contributor_distribution
        }


def main():
    try:
        # Example total jackpot amount
        total_jackpot_amount = 1000
        jackpot = Jackpot(total_jackpot_amount)

        # Adding contributors
        jackpot.add_contributor("Alice", 200)
        jackpot.add_contributor("Bob", 300)
        jackpot.add_contributor("Charlie", 500)

        # Distributing winnings
        winnings = jackpot.distribute_winnings()
        
        # Displaying results
        print("Jackpot Distribution:")
        print(f"Winner's Share: ${winnings['winner_share']:.2f}")
        print("Contributors' Shares:")
        for player, share in winnings['contributor_distribution'].items():
            print(f"{player}: ${share:.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
