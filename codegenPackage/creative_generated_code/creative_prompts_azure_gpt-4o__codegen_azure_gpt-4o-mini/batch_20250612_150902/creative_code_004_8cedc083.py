"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hugfytxytugugvytfuyjgykb.pages.dev
Prompt: Write a script to calculate the percentage of burned tokens, staked tokens, and tokens held by users for a total supply of 1 billion Arbinu tokens.
Generated: DETERMINISTIC_8cedc0833ac09710
Batch ID: 20250612_150902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ArbinuToken:
    def __init__(self, total_supply: float):
        """
        Initialize the ArbinuToken class with the total supply of tokens.

        :param total_supply: Total supply of Arbinu tokens.
        """
        self.total_supply = total_supply
        self.burned_tokens = 0.0
        self.staked_tokens = 0.0
        self.user_tokens = 0.0

    def set_burned_tokens(self, burned: float):
        """
        Set the amount of burned tokens.

        :param burned: Amount of burned tokens.
        :raises ValueError: If burned tokens exceed total supply.
        """
        if burned < 0 or burned > self.total_supply:
            raise ValueError("Burned tokens must be between 0 and the total supply.")
        self.burned_tokens = burned

    def set_staked_tokens(self, staked: float):
        """
        Set the amount of staked tokens.

        :param staked: Amount of staked tokens.
        :raises ValueError: If staked tokens exceed available supply.
        """
        if staked < 0 or staked > (self.total_supply - self.burned_tokens):
            raise ValueError("Staked tokens must be between 0 and the available supply.")
        self.staked_tokens = staked

    def set_user_tokens(self, user: float):
        """
        Set the amount of tokens held by users.

        :param user: Amount of tokens held by users.
        :raises ValueError: If user tokens exceed available supply.
        """
        if user < 0 or user > (self.total_supply - (self.burned_tokens + self.staked_tokens)):
            raise ValueError("User tokens must be between 0 and the available supply.")
        self.user_tokens = user

    def calculate_percentages(self):
        """
        Calculate the percentages of burned, staked, and user-held tokens.

        :return: A dictionary containing the percentages of burned, staked, and user-held tokens.
        """
        total_tokens = self.burned_tokens + self.staked_tokens + self.user_tokens

        if total_tokens > self.total_supply:
            raise ValueError("Total tokens (burned + staked + user) exceed total supply.")

        percentages = {
            "burned_percentage": (self.burned_tokens / self.total_supply) * 100,
            "staked_percentage": (self.staked_tokens / self.total_supply) * 100,
            "user_percentage": (self.user_tokens / self.total_supply) * 100,
        }

        return percentages


if __name__ == "__main__":
    try:
        total_supply = 1_000_000_000  # 1 billion Arbinu tokens
        arbinu = ArbinuToken(total_supply)

        # Example values for burned, staked, and user tokens
        arbinu.set_burned_tokens(200_000_000)  # 200 million burned
        arbinu.set_staked_tokens(300_000_000)  # 300 million staked
        arbinu.set_user_tokens(500_000_000)    # 500 million held by users

        # Calculate and print percentages
        percentages = arbinu.calculate_percentages()
        print("Burned Percentage: {:.2f}%".format(percentages["burned_percentage"]))
        print("Staked Percentage: {:.2f}%".format(percentages["staked_percentage"]))
        print("User Percentage: {:.2f}%".format(percentages["user_percentage"]))

    except ValueError as e:
        print(f"Error: {e}")
```
