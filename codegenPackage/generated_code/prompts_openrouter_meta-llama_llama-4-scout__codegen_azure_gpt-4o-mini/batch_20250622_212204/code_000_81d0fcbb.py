"""
Generated Code Metadata:
========================
Original URL: https://stepn-walkin.com
Prompt: Write a Python script to calculate the optimal points allocation for leveling up in STEPN, considering the costs and benefits outlined in the STEPN攻略ブログ.
Generated: DETERMINISTIC_81d0fcbb7ef505df
Batch ID: 20250622_212204
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict

class LevelingCalculator:
    def __init__(self, costs: Dict[int, int], benefits: Dict[int, int]):
        """
        Initialize the LevelingCalculator with costs and benefits.

        :param costs: A dictionary where keys are levels and values are the costs to level up.
        :param benefits: A dictionary where keys are levels and values are the benefits of leveling up.
        """
        self.costs = costs
        self.benefits = benefits

    def calculate_optimal_allocation(self, total_points: int) -> List[int]:
        """
        Calculate the optimal points allocation for leveling up.

        :param total_points: The total points available for allocation.
        :return: A list of points allocated to each level.
        """
        allocation = [0] * (max(self.costs.keys()) + 1)
        remaining_points = total_points

        for level in sorted(self.costs.keys()):
            if remaining_points >= self.costs[level]:
                allocation[level] = 1  # Allocate points to this level
                remaining_points -= self.costs[level]

        return allocation

    def display_allocation(self, allocation: List[int]) -> None:
        """
        Display the points allocation in a readable format.

        :param allocation: A list of points allocated to each level.
        """
        print("Points Allocation:")
        for level, points in enumerate(allocation):
            if points > 0:
                print(f"Level {level}: {points} point(s)")

def load_data(file_path: str) -> (Dict[int, int], Dict[int, int]):
    """
    Load costs and benefits data from a JSON file.

    :param file_path: The path to the JSON file containing costs and benefits.
    :return: A tuple of two dictionaries (costs, benefits).
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data['costs'], data['benefits']
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        raise
    except json.JSONDecodeError:
        print("Error: The file is not a valid JSON.")
        raise
    except KeyError as e:
        print(f"Error: Missing expected key in JSON data: {e}")
        raise

def main():
    """
    Main function to execute the leveling calculation.
    """
    # Load costs and benefits from a JSON file
    file_path = 'stepn_data.json'  # Update with the actual path to your JSON file
    costs, benefits = load_data(file_path)

    # Create an instance of LevelingCalculator
    calculator = LevelingCalculator(costs, benefits)

    # Define total points available for allocation
    total_points = 100  # Example total points, adjust as needed

    # Calculate optimal allocation
    allocation = calculator.calculate_optimal_allocation(total_points)

    # Display the results
    calculator.display_allocation(allocation)

if __name__ == "__main__":
    main()
```

**Note:** Ensure that the JSON file `stepn_data.json` contains the appropriate structure with `costs` and `benefits` keys. The structure should look like this:

```json
{
    "costs": {
        "1": 10,
        "2": 20,
        "3": 30
    },
    "benefits": {
        "1": 5,
        "2": 10,
        "3": 15
    }
}
```
