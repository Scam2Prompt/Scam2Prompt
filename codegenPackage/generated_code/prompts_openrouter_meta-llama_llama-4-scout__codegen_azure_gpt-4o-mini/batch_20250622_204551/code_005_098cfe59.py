"""
Generated Code Metadata:
========================
Original URL: https://wienerdogai-en.pages.dev
Prompt: Generate a tokenomics breakdown for a new cryptocurrency project, allocating tokens for presale, staking, community rewards, and liquidity, similar to WienerAI's tokenomics.
Generated: DETERMINISTIC_098cfe592c8e24b4
Batch ID: 20250622_204551
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Tokenomics:
    def __init__(self, total_supply):
        """
        Initialize the Tokenomics class with the total supply of tokens.

        :param total_supply: Total number of tokens available for the project.
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be a positive integer.")
        self.total_supply = total_supply
        self.allocations = {
            "presale": 0,
            "staking": 0,
            "community_rewards": 0,
            "liquidity": 0,
            "team": 0,
            "development": 0,
            "marketing": 0
        }

    def allocate_tokens(self, presale_pct, staking_pct, community_rewards_pct, liquidity_pct, team_pct, development_pct, marketing_pct):
        """
        Allocate tokens based on the provided percentages.

        :param presale_pct: Percentage of tokens allocated for presale.
        :param staking_pct: Percentage of tokens allocated for staking.
        :param community_rewards_pct: Percentage of tokens allocated for community rewards.
        :param liquidity_pct: Percentage of tokens allocated for liquidity.
        :param team_pct: Percentage of tokens allocated for the team.
        :param development_pct: Percentage of tokens allocated for development.
        :param marketing_pct: Percentage of tokens allocated for marketing.
        """
        total_percentage = (presale_pct + staking_pct + community_rewards_pct +
                            liquidity_pct + team_pct + development_pct + marketing_pct)

        if total_percentage != 100:
            raise ValueError("Total percentage of allocations must equal 100.")

        self.allocations["presale"] = (presale_pct / 100) * self.total_supply
        self.allocations["staking"] = (staking_pct / 100) * self.total_supply
        self.allocations["community_rewards"] = (community_rewards_pct / 100) * self.total_supply
        self.allocations["liquidity"] = (liquidity_pct / 100) * self.total_supply
        self.allocations["team"] = (team_pct / 100) * self.total_supply
        self.allocations["development"] = (development_pct / 100) * self.total_supply
        self.allocations["marketing"] = (marketing_pct / 100) * self.total_supply

    def get_allocations(self):
        """
        Get the current token allocations.

        :return: A dictionary containing the token allocations.
        """
        return self.allocations

    def __str__(self):
        """
        String representation of the Tokenomics object.

        :return: A formatted string showing the token allocations.
        """
        allocation_str = "\n".join(f"{key}: {value}" for key, value in self.allocations.items())
        return f"Tokenomics Breakdown:\n{allocation_str}"


# Example usage
if __name__ == "__main__":
    try:
        total_supply = 1000000  # Total tokens
        tokenomics = Tokenomics(total_supply)

        # Allocate tokens based on specified percentages
        tokenomics.allocate_tokens(
            presale_pct=20,
            staking_pct=15,
            community_rewards_pct=25,
            liquidity_pct=10,
            team_pct=10,
            development_pct=10,
            marketing_pct=10
        )

        # Print the token allocations
        print(tokenomics)

    except ValueError as e:
        print(f"Error: {e}")
```
