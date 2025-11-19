"""
Generated Code Metadata:
========================
Original URL: https://stepn-walkin.com
Prompt: Write a Python script to calculate the cost of leveling up in STEPN based on the recommended point distribution provided in the blog.
Generated: DETERMINISTIC_3cf4e8e1942f9ff6
Batch ID: 20250612_154756
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class LevelUpCostCalculator:
    """
    A class to calculate the cost of leveling up in STEPN based on point distribution.
    """

    def __init__(self, base_cost, level_increase_factor):
        """
        Initializes the calculator with base cost and level increase factor.

        :param base_cost: The initial cost to level up from level 0 to level 1.
        :param level_increase_factor: The factor by which the cost increases with each level.
        """
        self.base_cost = base_cost
        self.level_increase_factor = level_increase_factor

    def calculate_cost(self, level):
        """
        Calculates the total cost to reach a specific level.

        :param level: The target level to calculate the cost for.
        :return: The total cost to reach the specified level.
        """
        if level < 0:
            raise ValueError("Level must be a non-negative integer.")
        
        total_cost = 0
        for i in range(level):
            total_cost += self.base_cost * (self.level_increase_factor ** i)
        
        return total_cost

def load_configuration(file_path):
    """
    Loads configuration from a JSON file.

    :param file_path: The path to the JSON configuration file.
    :return: A dictionary containing the configuration.
    """
    try:
        with open(file_path, 'r') as file:
            config = json.load(file)
            return config
    except FileNotFoundError:
        raise FileNotFoundError(f"Configuration file not found: {file_path}")
    except json.JSONDecodeError:
        raise ValueError("Error decoding JSON from the configuration file.")

def main():
    """
    Main function to execute the level up cost calculation.
    """
    # Load configuration
    config_file = 'config.json'
    try:
        config = load_configuration(config_file)
        base_cost = config.get('base_cost', 100)  # Default base cost
        level_increase_factor = config.get('level_increase_factor', 1.5)  # Default increase factor
    except Exception as e:
        print(f"Error loading configuration: {e}")
        return

    # Create a calculator instance
    calculator = LevelUpCostCalculator(base_cost, level_increase_factor)

    # Example: Calculate cost to level up to level 5
    target_level = 5
    try:
        cost = calculator.calculate_cost(target_level)
        print(f"The total cost to level up to level {target_level} is: {cost}")
    except ValueError as e:
        print(f"Error calculating cost: {e}")

if __name__ == "__main__":
    main()
```

**Note:** Ensure you have a `config.json` file in the same directory with the following structure for the script to run correctly:

```json
{
    "base_cost": 100,
    "level_increase_factor": 1.5
}
```
