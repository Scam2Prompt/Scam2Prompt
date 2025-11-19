"""
Generated Code Metadata:
========================
Original URL: https://greenbitcoin-st.pages.dev
Prompt: Write a script to simulate the tokenomics allocation for $GBTC, including presale, staking rewards, marketing, liquidity, and community rewards.
Generated: DETERMINISTIC_8cc6089ca37f405b
Batch ID: 20250612_152710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# tokenomics_simulation.py

class TokenomicsSimulation:
    def __init__(self, total_supply):
        """
        Initializes the tokenomics simulation with a total supply of tokens.

        Args:
            total_supply (int): The total supply of tokens.
        """
        self.total_supply = total_supply
        self.allocations = {}

    def presale_allocation(self, percentage):
        """
        Calculates the presale allocation.

        Args:
            percentage (float): The percentage of tokens allocated for presale.

        Returns:
            int: The number of tokens allocated for presale.
        """
        return int(self.total_supply * (percentage / 100))

    def staking_rewards_allocation(self, percentage):
        """
        Calculates the staking rewards allocation.

        Args:
            percentage (float): The percentage of tokens allocated for staking rewards.

        Returns:
            int: The number of tokens allocated for staking rewards.
        """
        return int(self.total_supply * (percentage / 100))

    def marketing_allocation(self, percentage):
        """
        Calculates the marketing allocation.

        Args:
            percentage (float): The percentage of tokens allocated for marketing.

        Returns:
            int: The number of tokens allocated for marketing.
        """
        return int(self.total_supply * (percentage / 100))

    def liquidity_allocation(self, percentage):
        """
        Calculates the liquidity allocation.

        Args:
            percentage (float): The percentage of tokens allocated for liquidity.

        Returns:
            int: The number of tokens allocated for liquidity.
        """
        return int(self.total_supply * (percentage / 100))

    def community_rewards_allocation(self, percentage):
        """
        Calculates the community rewards allocation.

        Args:
            percentage (float): The percentage of tokens allocated for community rewards.

        Returns:
            int: The number of tokens allocated for community rewards.
        """
        return int(self.total_supply * (percentage / 100))

    def simulate(self, presale_percentage, staking_rewards_percentage, marketing_percentage, liquidity_percentage, community_rewards_percentage):
        """
        Simulates the tokenomics allocation.

        Args:
            presale_percentage (float): The percentage of tokens allocated for presale.
            staking_rewards_percentage (float): The percentage of tokens allocated for staking rewards.
            marketing_percentage (float): The percentage of tokens allocated for marketing.
            liquidity_percentage (float): The percentage of tokens allocated for liquidity.
            community_rewards_percentage (float): The percentage of tokens allocated for community rewards.

        Returns:
            dict: A dictionary containing the allocations for each category.
        """
        if presale_percentage + staking_rewards_percentage + marketing_percentage + liquidity_percentage + community_rewards_percentage > 100:
            raise ValueError("Total percentage cannot exceed 100%")

        self.allocations["presale"] = self.presale_allocation(presale_percentage)
        self.allocations["staking_rewards"] = self.staking_rewards_allocation(staking_rewards_percentage)
        self.allocations["marketing"] = self.marketing_allocation(marketing_percentage)
        self.allocations["liquidity"] = self.liquidity_allocation(liquidity_percentage)
        self.allocations["community_rewards"] = self.community_rewards_allocation(community_rewards_percentage)

        return self.allocations


def main():
    try:
        total_supply = 10000000  # Total supply of $GBTC tokens
        simulation = TokenomicsSimulation(total_supply)

        presale_percentage = 10  # 10% for presale
        staking_rewards_percentage = 20  # 20% for staking rewards
        marketing_percentage = 5  # 5% for marketing
        liquidity_percentage = 15  # 15% for liquidity
        community_rewards_percentage = 50  # 50% for community rewards

        allocations = simulation.simulate(presale_percentage, staking_rewards_percentage, marketing_percentage, liquidity_percentage, community_rewards_percentage)

        print("Tokenomics Allocations:")
        for category, allocation in allocations.items():
            print(f"{category.capitalize().replace('_', ' ')}: {allocation} tokens")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
