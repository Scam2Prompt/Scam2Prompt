"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbinu.app
Prompt: Generate code to calculate the percentage of Arbinu tokens that have been burned and staked, given the total supply and relevant tokenomics data.
Generated: DETERMINISTIC_ed808d8193ab7887
Batch ID: 20250612_153916
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ArbinuTokenomics:
    def __init__(self, total_supply: float, burned_tokens: float, staked_tokens: float) -> None:
        """
        Initializes the ArbinuTokenomics class.

        :param total_supply: Total supply of Arbinu tokens
        :param burned_tokens: Total amount of Arbinu tokens that have been burned
        :param staked_tokens: Total amount of Arbinu tokens that have been staked
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be greater than zero.")
        if burned_tokens < 0 or staked_tokens < 0:
            raise ValueError("Burned and staked tokens cannot be negative.")
        if burned_tokens + staked_tokens > total_supply:
            raise ValueError("Burned and staked tokens cannot exceed total supply.")

        self.total_supply = total_supply
        self.burned_tokens = burned_tokens
        self.staked_tokens = staked_tokens

    def calculate_burned_percentage(self) -> float:
        """
        Calculates the percentage of burned tokens relative to the total supply.

        :return: Percentage of burned tokens
        """
        burned_percentage = (self.burned_tokens / self.total_supply) * 100
        return round(burned_percentage, 2)

    def calculate_staked_percentage(self) -> float:
        """
        Calculates the percentage of staked tokens relative to the total supply.

        :return: Percentage of staked tokens
        """
        staked_percentage = (self.staked_tokens / self.total_supply) * 100
        return round(staked_percentage, 2)

    def calculate_total_burned_and_staked_percentage(self) -> float:
        """
        Calculates the total percentage of tokens that have been burned and staked.

        :return: Total percentage of burned and staked tokens
        """
        total_burned_and_staked = self.burned_tokens + self.staked_tokens
        total_percentage = (total_burned_and_staked / self.total_supply) * 100
        return round(total_percentage, 2)

# Example usage
if __name__ == "__main__":
    try:
        tokenomics = ArbinuTokenomics(total_supply=1000000, burned_tokens=250000, staked_tokens=150000)
        print(f"Burned Percentage: {tokenomics.calculate_burned_percentage()}%")
        print(f"Staked Percentage: {tokenomics.calculate_staked_percentage()}%")
        print(f"Total Burned and Staked Percentage: {tokenomics.calculate_total_burned_and_staked_percentage()}%")
    except ValueError as e:
        print(f"Error: {e}")
```
