"""
Generated Code Metadata:
========================
Original URL: https://clearpool.pages.dev
Prompt: Generate code to calculate the total voting power percentage for each Clearpool oracle based on the provided CPOOL staking data.
Generated: DETERMINISTIC_ef84c655d9a4712d
Batch ID: 20250612_151003
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import Dict, List

class ClearpoolOracle:
    def __init__(self, name: str, total_stake: float, total_cpool_supply: float):
        """
        Initialize a Clearpool Oracle object.

        Args:
        - name (str): The name of the oracle.
        - total_stake (float): The total stake of the oracle.
        - total_cpool_supply (float): The total CPOOL supply.
        """
        self.name = name
        self.total_stake = total_stake
        self.total_cpool_supply = total_cpool_supply

    def calculate_voting_power_percentage(self) -> float:
        """
        Calculate the voting power percentage of the oracle.

        Returns:
        - float: The voting power percentage.
        """
        if self.total_cpool_supply == 0:
            raise ZeroDivisionError("Total CPOOL supply cannot be zero")

        voting_power_percentage = (self.total_stake / self.total_cpool_supply) * 100
        return voting_power_percentage


def calculate_oracle_voting_powers(oracles_data: List[Dict]) -> Dict[str, float]:
    """
    Calculate the total voting power percentage for each Clearpool oracle.

    Args:
    - oracles_data (List[Dict]): A list of dictionaries containing oracle data.
        Each dictionary should have the following keys:
            - name (str): The name of the oracle.
            - total_stake (float): The total stake of the oracle.
        The total CPOOL supply is assumed to be the same for all oracles.

    Returns:
    - Dict[str, float]: A dictionary with oracle names as keys and their voting power percentages as values.
    """
    if not oracles_data:
        return {}

    total_cpool_supply = oracles_data[0].get('total_cpool_supply')
    if total_cpool_supply is None:
        raise ValueError("Total CPOOL supply is required")

    oracles_voting_powers = {}
    for oracle_data in oracles_data:
        name = oracle_data['name']
        total_stake = oracle_data['total_stake']

        oracle = ClearpoolOracle(name, total_stake, total_cpool_supply)
        try:
            voting_power_percentage = oracle.calculate_voting_power_percentage()
        except ZeroDivisionError as e:
            print(f"Error calculating voting power for {name}: {str(e)}")
            continue

        oracles_voting_powers[name] = voting_power_percentage

    return oracles_voting_powers


# Example usage:
if __name__ == "__main__":
    oracles_data = [
        {'name': 'Oracle1', 'total_stake': 1000, 'total_cpool_supply': 10000},
        {'name': 'Oracle2', 'total_stake': 2000, 'total_cpool_supply': 10000},
        {'name': 'Oracle3', 'total_stake': 3000, 'total_cpool_supply': 10000},
    ]

    oracles_voting_powers = calculate_oracle_voting_powers(oracles_data)
    for oracle, voting_power in oracles_voting_powers.items():
        print(f"Oracle: {oracle}, Voting Power: {voting_power}%")
```
