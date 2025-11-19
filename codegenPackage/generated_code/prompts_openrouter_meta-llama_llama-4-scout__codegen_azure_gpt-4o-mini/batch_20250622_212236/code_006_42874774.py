"""
Generated Code Metadata:
========================
Original URL: https://master-brain.com
Prompt: "Write a code to implement a business strategy planning tool for SMEs."
Generated: DETERMINISTIC_428747741976c156
Batch ID: 20250622_212236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Any

class BusinessStrategy:
    """
    A class to represent a business strategy for SMEs.
    """

    def __init__(self, name: str, objectives: List[str], actions: List[str]):
        """
        Initializes a new BusinessStrategy instance.

        :param name: The name of the business strategy.
        :param objectives: A list of objectives for the strategy.
        :param actions: A list of actions to achieve the objectives.
        """
        self.name = name
        self.objectives = objectives
        self.actions = actions

    def to_dict(self) -> Dict[str, Any]:
        """
        Converts the BusinessStrategy instance to a dictionary.

        :return: A dictionary representation of the business strategy.
        """
        return {
            'name': self.name,
            'objectives': self.objectives,
            'actions': self.actions
        }

class StrategyPlanner:
    """
    A class to manage business strategies for SMEs.
    """

    def __init__(self):
        """
        Initializes a new StrategyPlanner instance with an empty strategy list.
        """
        self.strategies = []

    def add_strategy(self, strategy: BusinessStrategy) -> None:
        """
        Adds a new business strategy to the planner.

        :param strategy: An instance of BusinessStrategy to add.
        """
        self.strategies.append(strategy)

    def save_strategies(self, filename: str) -> None:
        """
        Saves the list of strategies to a JSON file.

        :param filename: The name of the file to save the strategies to.
        """
        try:
            with open(filename, 'w') as file:
                json.dump([strategy.to_dict() for strategy in self.strategies], file, indent=4)
            print(f"Strategies saved to {filename}.")
        except IOError as e:
            print(f"Error saving strategies to file: {e}")

    def load_strategies(self, filename: str) -> None:
        """
        Loads strategies from a JSON file.

        :param filename: The name of the file to load strategies from.
        """
        try:
            with open(filename, 'r') as file:
                strategies_data = json.load(file)
                for strategy_data in strategies_data:
                    strategy = BusinessStrategy(
                        name=strategy_data['name'],
                        objectives=strategy_data['objectives'],
                        actions=strategy_data['actions']
                    )
                    self.add_strategy(strategy)
            print(f"Strategies loaded from {filename}.")
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading strategies from file: {e}")

    def display_strategies(self) -> None:
        """
        Displays all the strategies in the planner.
        """
        if not self.strategies:
            print("No strategies available.")
            return
        
        for strategy in self.strategies:
            print(f"Strategy Name: {strategy.name}")
            print("Objectives:")
            for objective in strategy.objectives:
                print(f" - {objective}")
            print("Actions:")
            for action in strategy.actions:
                print(f" - {action}")
            print("\n")

# Example usage
if __name__ == "__main__":
    planner = StrategyPlanner()

    # Create a sample strategy
    strategy1 = BusinessStrategy(
        name="Market Expansion",
        objectives=["Increase market share", "Enhance brand awareness"],
        actions=["Launch social media campaign", "Participate in trade shows"]
    )

    planner.add_strategy(strategy1)

    # Save strategies to a file
    planner.save_strategies("strategies.json")

    # Load strategies from a file
    planner.load_strategies("strategies.json")

    # Display all strategies
    planner.display_strategies()
```
