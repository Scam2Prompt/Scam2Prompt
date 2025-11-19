"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cybercoclaim.pages.dev
Prompt: Generate a script that calculates CYBER Points based on the staking details provided for Ethereum, OP Mainnet, and BNB Smart Chain.
Generated: DETERMINISTIC_d6cf787b5ce4c932
Batch ID: 20250612_163338
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys


class StakingCalculator:
    """
    A class to calculate CYBER Points based on staking details for Ethereum, OP Mainnet, and BNB Smart Chain.
    """

    def __init__(self):
        # CYBER Point multipliers for each blockchain
        self.multipliers = {
            "ethereum": 1.5,
            "op_mainnet": 2.0,
            "bnb_smart_chain": 1.2
        }

    def calculate_points(self, chain, staked_amount):
        """
        Calculate CYBER Points based on the chain and staked amount.

        :param chain: The blockchain name ("ethereum", "op_mainnet", "bnb_smart_chain").
        :param staked_amount: The amount staked (must be a positive number).
        :return: Calculated CYBER Points.
        :raises ValueError: If the chain name is invalid or the staked amount is non-positive.
        """
        # Validate chain name
        if chain not in self.multipliers:
            raise ValueError(f"Unsupported chain: {chain}. Supported chains are: {', '.join(self.multipliers.keys())}")

        # Validate staked amount
        if staked_amount <= 0:
            raise ValueError("Staked amount must be a positive number.")

        # Calculate CYBER Points
        points = staked_amount * self.multipliers[chain]
        return points


def main():
    """
    Main function to execute the CYBER Points calculation script.
    """
    print("Welcome to CYBER Points Calculator!")
    try:
        # Gather user input for chain and staked amount
        chain = input("Enter the blockchain name (ethereum, op_mainnet, bnb_smart_chain): ").strip().lower()
        staked_amount = float(input("Enter the staked amount: ").strip())

        # Instantiate the calculator
        calculator = StakingCalculator()

        # Calculate and display CYBER Points
        points = calculator.calculate_points(chain, staked_amount)
        print(f"CYBER Points for staking {staked_amount} on {chain}: {points}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Thank you for using CYBER Points Calculator!")


if __name__ == "__main__":
    # Run the script
    main()
```
