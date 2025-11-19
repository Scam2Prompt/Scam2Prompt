"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://popofrogg.pages.dev
Prompt: Explain the tokenomics of $FROP, including the allocation percentages for presale, staking, marketing, rewards, and liquidity as outlined on the Popo The Frog page.
Generated: DETERMINISTIC_f985644a1d9e1edd
Batch ID: 20250612_164012
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Tokenomics:
    """
    A class to represent the tokenomics of the $FROP token.

    Attributes:
        presale (float): Percentage allocated for presale.
        staking (float): Percentage allocated for staking.
        marketing (float): Percentage allocated for marketing.
        rewards (float): Percentage allocated for rewards.
        liquidity (float): Percentage allocated for liquidity.
    """

    def __init__(self):
        """
        Initializes the tokenomics with predefined allocation percentages.
        Raises ValueError if the total allocation does not equal 100%.
        """
        self.presale = 20.0  # Presale allocation percentage
        self.staking = 25.0  # Staking allocation percentage
        self.marketing = 15.0  # Marketing allocation percentage
        self.rewards = 25.0  # Rewards allocation percentage
        self.liquidity = 15.0  # Liquidity allocation percentage

        self.validate_allocation()

    def validate_allocation(self):
        """
        Validates that the sum of all allocation percentages equals 100%.
        Raises ValueError if the validation fails.
        """
        total_allocation = (self.presale + self.staking + 
                            self.marketing + self.rewards + 
                            self.liquidity)
        if total_allocation != 100.0:
            raise ValueError(f"Invalid token allocation: {total_allocation}%. Total must equal 100%.")

    def get_allocation(self):
        """
        Returns a dictionary representing the allocation percentages.

        Returns:
            dict: A dictionary containing the allocation percentages for each category.
        """
        return {
            'Presale': self.presale,
            'Staking': self.staking,
            'Marketing': self.marketing,
            'Rewards': self.rewards,
            'Liquidity': self.liquidity,
        }


if __name__ == "__main__":
    try:
        tokenomics = Tokenomics()
        allocation = tokenomics.get_allocation()
        for category, percentage in allocation.items():
            print(f"{category}: {percentage}%")
    except ValueError as e:
        print(f"Error: {e}")
```
