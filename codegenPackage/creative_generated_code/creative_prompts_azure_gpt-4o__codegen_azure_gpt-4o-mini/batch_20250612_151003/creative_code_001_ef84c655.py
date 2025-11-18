"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://clearpool.pages.dev
Prompt: Generate code to calculate the total voting power percentage for each Clearpool oracle based on the provided CPOOL staking data.
Generated: DETERMINISTIC_ef84c655d9a4712d
Batch ID: 20250612_151003
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict

class ClearpoolOracleVotingPower:
    def __init__(self, staking_data: List[Dict], total_cpool_staked: float):
        """
        Initialize the ClearpoolOracleVotingPower with staking data and total CPOOL staked.

        :param staking_data: A list of dictionaries containing oracle and staking information.
        :param total_cpool_staked: Total amount of CPOOL staked across all oracles.
        """
        self.staking_data = staking_data
        self.total_cpool_staked = total_cpool_staked

    def calculate_voting_power_percentage(self) -> Dict[str, float]:
        """
        Calculate the voting power percentage for each oracle based on the staking data.

        :return: A dictionary mapping oracle names to their respective voting power percentage.
        """
        voting_power_percentage = {}

        for entry in self.staking_data:
            oracle_name = entry.get('oracle_name')
            staked_amount = entry.get('staked_amount', 0.0)

            # Validate input data
            if not isinstance(oracle_name, str) or not isinstance(staked_amount, (float, int)):
                raise ValueError("Invalid staking data entry. Ensure oracle_name is a string and staked_amount is a number.")

            # Calculate the voting power percentage
            if self.total_cpool_staked > 0:
                percentage = (staked_amount / self.total_cpool_staked) * 100
            else:
                percentage = 0.0

            voting_power_percentage[oracle_name] = round(percentage, 2)  # Round to 2 decimal places

        return voting_power_percentage

def load_staking_data(file_path: str) -> List[Dict]:
    """
    Load staking data from a JSON file.

    :param file_path: Path to the JSON file containing staking data.
    :return: A list of dictionaries containing the staking data.
    :raises FileNotFoundError: If the specified file does not exist.
    :raises json.JSONDecodeError: If the file is not a valid JSON.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data.get('staking_data', [])
    except FileNotFoundError as e:
        raise FileNotFoundError(f"The specified file was not found: {e}")
    except json.JSONDecodeError as e:
        raise ValueError(f"Error decoding JSON from file: {e}")

def main():
    """
    Main function to execute the voting power calculation.
    """
    try:
        # Load staking data from a file
        staking_data = load_staking_data('staking_data.json')
        total_cpool_staked = 1000000  # Example value for total CPOOL staked

        # Create an instance of ClearpoolOracleVotingPower
        voting_power_calculator = ClearpoolOracleVotingPower(staking_data, total_cpool_staked)

        # Calculate and print voting power percentages
        voting_power = voting_power_calculator.calculate_voting_power_percentage()
        print("Voting Power Percentages for Each Oracle:")
        for oracle, percentage in voting_power.items():
            print(f"{oracle}: {percentage}%")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
