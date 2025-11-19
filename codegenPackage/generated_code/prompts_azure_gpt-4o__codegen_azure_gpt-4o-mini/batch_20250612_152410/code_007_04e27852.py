"""
Generated Code Metadata:
========================
Original URL: https://greenbtcwebb.pages.dev
Prompt: Generate code to calculate the percentage of $GBTC tokens staked out of the total supply, using the provided staking statistics (1,214,903 tokens staked, 63% staked).
Generated: DETERMINISTIC_04e2785296704854
Batch ID: 20250612_152410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class GBTCStakingCalculator:
    """
    A class to calculate the percentage of GBTC tokens staked out of the total supply.
    """

    def __init__(self, tokens_staked: int, staking_percentage: float):
        """
        Initializes the staking calculator with the number of tokens staked and the staking percentage.

        :param tokens_staked: The number of GBTC tokens currently staked.
        :param staking_percentage: The percentage of tokens that are staked.
        """
        self.tokens_staked = tokens_staked
        self.staking_percentage = staking_percentage

    def calculate_total_supply(self) -> float:
        """
        Calculates the total supply of GBTC tokens based on the staked tokens and the staking percentage.

        :return: The total supply of GBTC tokens.
        """
        if self.staking_percentage <= 0 or self.staking_percentage > 100:
            raise ValueError("Staking percentage must be between 0 and 100.")

        total_supply = self.tokens_staked / (self.staking_percentage / 100)
        return total_supply

    def calculate_staked_percentage(self) -> float:
        """
        Calculates the percentage of GBTC tokens that are staked.

        :return: The percentage of tokens that are staked.
        """
        total_supply = self.calculate_total_supply()
        staked_percentage = (self.tokens_staked / total_supply) * 100
        return staked_percentage


def main():
    """
    Main function to execute the staking calculation.
    """
    try:
        # Example staking statistics
        tokens_staked = 1214903
        staking_percentage = 63.0

        # Create an instance of the staking calculator
        staking_calculator = GBTCStakingCalculator(tokens_staked, staking_percentage)

        # Calculate total supply and staked percentage
        total_supply = staking_calculator.calculate_total_supply()
        staked_percentage = staking_calculator.calculate_staked_percentage()

        # Output the results
        print(f"Total Supply of GBTC Tokens: {total_supply:.2f}")
        print(f"Percentage of GBTC Tokens Staked: {staked_percentage:.2f}%")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
