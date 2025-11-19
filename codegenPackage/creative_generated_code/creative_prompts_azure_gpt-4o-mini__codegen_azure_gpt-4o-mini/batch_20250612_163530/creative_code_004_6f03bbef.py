"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solbank-finances.pages.dev
Prompt: Explain how to calculate APY for a staking protocol similar to Solbank, considering factors like total value deposited and percentage of supply staked.
Generated: DETERMINISTIC_6f03bbef6714232f
Batch ID: 20250612_163530
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class StakingProtocol:
    """
    A class to represent a staking protocol for calculating Annual Percentage Yield (APY).
    """

    def __init__(self, total_value_deposited: float, total_supply: float, staked_percentage: float):
        """
        Initializes the StakingProtocol with the given parameters.

        :param total_value_deposited: Total value deposited in the staking protocol.
        :param total_supply: Total supply of the token.
        :param staked_percentage: Percentage of the total supply that is staked (as a decimal).
        """
        if total_value_deposited <= 0:
            raise ValueError("Total value deposited must be greater than zero.")
        if total_supply <= 0:
            raise ValueError("Total supply must be greater than zero.")
        if not (0 <= staked_percentage <= 1):
            raise ValueError("Staked percentage must be between 0 and 1.")

        self.total_value_deposited = total_value_deposited
        self.total_supply = total_supply
        self.staked_percentage = staked_percentage

    def calculate_apy(self) -> float:
        """
        Calculates the Annual Percentage Yield (APY) based on the deposited value and staked supply.

        :return: The calculated APY as a percentage.
        """
        try:
            # Calculate the total value staked
            total_value_staked = self.total_supply * self.staked_percentage

            if total_value_staked == 0:
                raise ValueError("Total value staked cannot be zero.")

            # Calculate APY using the formula: APY = (Total Value Deposited / Total Value Staked) * 100
            apy = (self.total_value_deposited / total_value_staked) * 100

            return apy
        except ZeroDivisionError:
            raise ValueError("Error in calculation: Division by zero encountered.")
        except Exception as e:
            raise RuntimeError(f"An error occurred during APY calculation: {e}")

# Example usage:
if __name__ == "__main__":
    try:
        # Create an instance of the StakingProtocol with example values
        staking_protocol = StakingProtocol(total_value_deposited=1000000, total_supply=5000000, staked_percentage=0.4)
        
        # Calculate and print the APY
        apy = staking_protocol.calculate_apy()
        print(f"The calculated APY is: {apy:.2f}%")
    except ValueError as ve:
        print(f"Value Error: {ve}")
    except RuntimeError as re:
        print(f"Runtime Error: {re}")
```
