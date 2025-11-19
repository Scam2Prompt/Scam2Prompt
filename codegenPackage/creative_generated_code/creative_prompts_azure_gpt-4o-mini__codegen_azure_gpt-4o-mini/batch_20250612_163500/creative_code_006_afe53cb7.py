"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wienerdogai-en.pages.dev
Prompt: Describe the tokenomics of WienerAI and how it impacts the presale and staking rewards for $WAI holders.
Generated: DETERMINISTIC_afe53cb74628455f
Batch ID: 20250612_163500
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
    A class to describe the tokenomics of WienerAI including presale and staking rewards.
    """

    def __init__(self, total_supply: int, presale_percentage: float, staking_rewards_percentage: float):
        """
        Initializes the Tokenomics class with specified parameters.

        Args:
            total_supply (int): Total supply of the $WAI token.
            presale_percentage (float): Percentage of tokens allocated for presale.
            staking_rewards_percentage (float): Percentage of tokens allocated for staking rewards.

        Raises:
            ValueError: If the percentages do not sum up to 100% or are negative.
        """
        if not (0 <= presale_percentage <= 100) or not (0 <= staking_rewards_percentage <= 100):
            raise ValueError("Presale and staking rewards percentages must be between 0 and 100.")
        if presale_percentage + staking_rewards_percentage > 100:
            raise ValueError("Total allocation percentages cannot exceed 100%.")
        
        self.total_supply = total_supply
        self.presale_percentage = presale_percentage
        self.staking_rewards_percentage = staking_rewards_percentage

    def calculate_presale_tokens(self) -> int:
        """
        Calculate the number of tokens allocated for presale.

        Returns:
            int: Number of tokens allocated for presale.
        """
        return int(self.total_supply * (self.presale_percentage / 100))

    def calculate_staking_rewards_tokens(self) -> int:
        """
        Calculate the number of tokens allocated for staking rewards.

        Returns:
            int: Number of tokens allocated for staking rewards.
        """
        return int(self.total_supply * (self.staking_rewards_percentage / 100))

    def describe_tokenomics(self) -> str:
        """
        Generates a descriptive summary of the tokenomics.

        Returns:
            str: A summary of the tokenomics including presale and staking rewards.
        """
        presale_tokens = self.calculate_presale_tokens()
        staking_tokens = self.calculate_staking_rewards_tokens()
        
        return (
            f"WienerAI Tokenomics:\n"
            f"Total Supply: {self.total_supply}\n"
            f"Tokens allocated for Presale: {presale_tokens}\n"
            f"Tokens allocated for Staking Rewards: {staking_tokens}\n"
            f"Presale Percentage: {self.presale_percentage}%\n"
            f"Staking Rewards Percentage: {self.staking_rewards_percentage}%"
        )

def main():
    """
    Main function to demonstrate the Tokenomics class.
    """
    try:
        # Define total supply and percentages
        total_supply = 1_000_000_000  # Example total supply
        presale_percentage = 20.0       # 20% for presale
        staking_rewards_percentage = 10.0  # 10% for staking rewards
        
        # Create Tokenomics instance
        tokenomics = Tokenomics(total_supply, presale_percentage, staking_rewards_percentage)

        # Print the tokenomics description
        print(tokenomics.describe_tokenomics())

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
