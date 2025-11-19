"""
Generated Code Metadata:
========================
Original URL: https://iqnetwork.io
Prompt: Create a function that calculates the total IQ tokens staked over time based on the data from the IQ Dashboard.
Generated: DETERMINISTIC_3d35b89bf8645a04
Batch ID: 20250612_163506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import List, Dict

class IqTokenStakingCalculator:
    """
    Calculates the total IQ tokens staked over time based on the data from the IQ Dashboard.
    """

    def __init__(self, staking_data: List[Dict]):
        """
        Initializes the IqTokenStakingCalculator with staking data.

        Args:
        staking_data (List[Dict]): A list of dictionaries containing staking data.
            Each dictionary should have the following keys:
                - 'timestamp' (int): The timestamp of the staking data point.
                - 'staked_tokens' (float): The number of IQ tokens staked at the given timestamp.
        """
        self.staking_data = staking_data

    def calculate_total_staked_tokens(self) -> float:
        """
        Calculates the total IQ tokens staked over time.

        Returns:
        float: The total IQ tokens staked.

        Raises:
        ValueError: If the staking data is empty.
        """
        if not self.staking_data:
            raise ValueError("Staking data is empty")

        total_staked_tokens = sum(data_point['staked_tokens'] for data_point in self.staking_data)
        return total_staked_tokens

    def calculate_staked_tokens_over_time(self) -> List[Dict]:
        """
        Calculates the total IQ tokens staked over time.

        Returns:
        List[Dict]: A list of dictionaries containing the total IQ tokens staked at each timestamp.

        Raises:
        ValueError: If the staking data is empty.
        """
        if not self.staking_data:
            raise ValueError("Staking data is empty")

        # Sort the staking data by timestamp
        self.staking_data.sort(key=lambda x: x['timestamp'])

        total_staked_tokens = 0
        staked_tokens_over_time = []

        for data_point in self.staking_data:
            total_staked_tokens += data_point['staked_tokens']
            staked_tokens_over_time.append({
                'timestamp': data_point['timestamp'],
                'total_staked_tokens': total_staked_tokens
            })

        return staked_tokens_over_time


def main():
    # Example usage
    staking_data = [
        {'timestamp': 1643723400, 'staked_tokens': 1000},
        {'timestamp': 1643723410, 'staked_tokens': 500},
        {'timestamp': 1643723420, 'staked_tokens': 2000},
    ]

    calculator = IqTokenStakingCalculator(staking_data)
    total_staked_tokens = calculator.calculate_total_staked_tokens()
    staked_tokens_over_time = calculator.calculate_staked_tokens_over_time()

    print(f"Total staked tokens: {total_staked_tokens}")
    print("Staked tokens over time:")
    for data_point in staked_tokens_over_time:
        print(f"Timestamp: {data_point['timestamp']}, Total staked tokens: {data_point['total_staked_tokens']}")


if __name__ == "__main__":
    main()
```
