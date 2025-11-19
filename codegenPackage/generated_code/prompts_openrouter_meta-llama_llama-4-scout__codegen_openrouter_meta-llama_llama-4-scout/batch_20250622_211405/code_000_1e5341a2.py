"""
Generated Code Metadata:
========================
Original URL: https://clearpool.pages.dev
Prompt: Write a Python script to calculate the APR for staking CPOOL tokens with different oracles on Clearpool, considering the oracle size and relative voting power.
Generated: DETERMINISTIC_1e5341a2b23ce329
Batch ID: 20250622_211405
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Clearpool APR Calculator for CPOOL Token Staking

Calculates the APR for staking CPOOL tokens with different oracles on Clearpool,
considering the oracle size and relative voting power.

Usage:
    python clearpool_apr_calculator.py
"""

import math

class Oracle:
    """Represents an oracle with its size and relative voting power."""

    def __init__(self, name: str, size: int, voting_power: float):
        """
        Initializes an Oracle instance.

        Args:
            name (str): The name of the oracle.
            size (int): The size of the oracle.
            voting_power (float): The relative voting power of the oracle.
        """
        self.name = name
        self.size = size
        self.voting_power = voting_power

class ClearpoolAPRCalculator:
    """Calculates the APR for staking CPOOL tokens on Clearpool."""

    def __init__(self, cpool_staking_rate: float, oracle_rewards: dict):
        """
        Initializes a ClearpoolAPRCalculator instance.

        Args:
            cpool_staking_rate (float): The base staking rate for CPOOL tokens.
            oracle_rewards (dict): A dictionary of oracle names to their reward multipliers.
        """
        self.cpool_staking_rate = cpool_staking_rate
        self.oracle_rewards = oracle_rewards

    def calculate_apr(self, oracle: Oracle) -> float:
        """
        Calculates the APR for staking CPOOL tokens with the given oracle.

        Args:
            oracle (Oracle): The oracle to calculate the APR for.

        Returns:
            float: The calculated APR.
        """
        # Calculate the oracle reward multiplier
        oracle_reward_multiplier = self.oracle_rewards.get(oracle.name, 1.0)

        # Calculate the relative voting power factor
        relative_voting_power_factor = oracle.voting_power / sum(o.voting_power for o in self.get_oracles())

        # Calculate the oracle size factor
        oracle_size_factor = oracle.size / sum(o.size for o in self.get_oracles())

        # Calculate the APR
        apr = self.cpool_staking_rate * oracle_reward_multiplier * relative_voting_power_factor * oracle_size_factor

        return apr

    def get_oracles(self) -> list:
        """
        Returns a list of oracles.

        This method should be overridden to provide the actual list of oracles.

        Returns:
            list: A list of Oracle instances.
        """
        # For demonstration purposes, return a hardcoded list of oracles
        return [
            Oracle("Oracle 1", 100, 0.3),
            Oracle("Oracle 2", 200, 0.5),
            Oracle("Oracle 3", 50, 0.2),
        ]

def main():
    try:
        # Define the base staking rate for CPOOL tokens
        cpool_staking_rate = 0.05  # 5%

        # Define the oracle rewards
        oracle_rewards = {
            "Oracle 1": 1.2,
            "Oracle 2": 1.5,
            "Oracle 3": 1.0,
        }

        # Create a ClearpoolAPRCalculator instance
        calculator = ClearpoolAPRCalculator(cpool_staking_rate, oracle_rewards)

        # Get the list of oracles
        oracles = calculator.get_oracles()

        # Calculate and print the APR for each oracle
        for oracle in oracles:
            apr = calculator.calculate_apr(oracle)
            print(f"Oracle: {oracle.name}, APR: {apr * 100:.2f}%")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
