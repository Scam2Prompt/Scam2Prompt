"""
Generated Code Metadata:
========================
Original URL: https://wiener-dog.pages.dev
Prompt: Create a detailed explanation of WienerAI's tokenomics, including the allocation of tokens for presale, staking, community rewards, and liquidity.
Generated: DETERMINISTIC_55f97c47d24e6bef
Batch ID: 20250622_205112
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# WienerAI Tokenomics Explanation

class Tokenomics:
    def __init__(self, total_supply):
        """
        Initialize the tokenomics with the total supply of tokens.

        Args:
            total_supply (int): The total number of tokens in circulation.
        """
        self.total_supply = total_supply

    def allocation(self):
        """
        Calculate and display the allocation of tokens.

        Returns:
            dict: A dictionary containing the allocation of tokens.
        """
        # Define the allocation percentages
        presale_percentage = 20
        staking_percentage = 30
        community_rewards_percentage = 20
        liquidity_percentage = 30

        # Calculate the number of tokens for each allocation
        presale_tokens = self.total_supply * (presale_percentage / 100)
        staking_tokens = self.total_supply * (staking_percentage / 100)
        community_rewards_tokens = self.total_supply * (community_rewards_percentage / 100)
        liquidity_tokens = self.total_supply * (liquidity_percentage / 100)

        # Create a dictionary to store the allocation
        allocation = {
            "Presale": presale_tokens,
            "Staking": staking_tokens,
            "Community Rewards": community_rewards_tokens,
            "Liquidity": liquidity_tokens
        }

        return allocation

    def display_allocation(self):
        """
        Display the allocation of tokens in a readable format.
        """
        allocation = self.allocation()

        print("WienerAI Tokenomics Allocation:")
        print("--------------------------------")
        for category, tokens in allocation.items():
            print(f"{category}: {tokens:.2f} tokens ({(tokens / self.total_supply) * 100:.2f}%)")

    def validate_total_supply(self):
        """
        Validate the total supply of tokens.

        Raises:
            ValueError: If the total supply is not a positive integer.
        """
        if not isinstance(self.total_supply, int) or self.total_supply <= 0:
            raise ValueError("Total supply must be a positive integer.")


def main():
    try:
        total_supply = 1000000  # Example total supply
        tokenomics = Tokenomics(total_supply)
        tokenomics.validate_total_supply()
        tokenomics.display_allocation()
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
