"""
Generated Code Metadata:
========================
Original URL: https://hugfytxytugugvytfuyjgykb.pages.dev
Prompt: Write a script to calculate the percentage of burned tokens, staked tokens, and tokens held by users for a total supply of 1 billion Arbinu tokens.
Generated: DETERMINISTIC_8cedc0833ac09710
Batch ID: 20250612_150902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class ArbinuTokenDistribution:
    def __init__(self, total_supply: float):
        """
        Initialize the ArbinuTokenDistribution with the total supply of tokens.

        :param total_supply: Total supply of Arbinu tokens.
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be a positive number.")
        self.total_supply = total_supply
        self.burned_tokens = 0.0
        self.staked_tokens = 0.0
        self.user_tokens = 0.0

    def set_burned_tokens(self, amount: float):
        """
        Set the amount of burned tokens.

        :param amount: Amount of tokens to be burned.
        """
        if amount < 0:
            raise ValueError("Burned tokens cannot be negative.")
        self.burned_tokens = amount

    def set_staked_tokens(self, amount: float):
        """
        Set the amount of staked tokens.

        :param amount: Amount of tokens to be staked.
        """
        if amount < 0:
            raise ValueError("Staked tokens cannot be negative.")
        self.staked_tokens = amount

    def set_user_tokens(self, amount: float):
        """
        Set the amount of tokens held by users.

        :param amount: Amount of tokens held by users.
        """
        if amount < 0:
            raise ValueError("User tokens cannot be negative.")
        self.user_tokens = amount

    def calculate_percentages(self):
        """
        Calculate the percentages of burned, staked, and user-held tokens.

        :return: A dictionary containing the percentages of burned, staked, and user-held tokens.
        """
        if self.burned_tokens + self.staked_tokens + self.user_tokens > self.total_supply:
            raise ValueError("The sum of burned, staked, and user-held tokens exceeds total supply.")

        percentages = {
            "burned_percentage": (self.burned_tokens / self.total_supply) * 100,
            "staked_percentage": (self.staked_tokens / self.total_supply) * 100,
            "user_percentage": (self.user_tokens / self.total_supply) * 100
        }
        return percentages


def main():
    # Total supply of Arbinu tokens
    total_supply = 1_000_000_000.0  # 1 billion tokens

    # Create an instance of ArbinuTokenDistribution
    arbinu_distribution = ArbinuTokenDistribution(total_supply)

    # Set the amounts for burned, staked, and user-held tokens
    arbinu_distribution.set_burned_tokens(200_000_000.0)  # Example: 200 million burned
    arbinu_distribution.set_staked_tokens(300_000_000.0)  # Example: 300 million staked
    arbinu_distribution.set_user_tokens(500_000_000.0)    # Example: 500 million held by users

    # Calculate and print the percentages
    try:
        percentages = arbinu_distribution.calculate_percentages()
        print("Token Distribution Percentages:")
        print(f"Burned Tokens: {percentages['burned_percentage']:.2f}%")
        print(f"Staked Tokens: {percentages['staked_percentage']:.2f}%")
        print(f"User Held Tokens: {percentages['user_percentage']:.2f}%")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
