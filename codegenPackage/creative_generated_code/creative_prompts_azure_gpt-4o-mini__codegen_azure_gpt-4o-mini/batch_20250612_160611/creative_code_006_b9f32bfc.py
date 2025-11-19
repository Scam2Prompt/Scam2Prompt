"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://boostrunning.com
Prompt: Develop a simple app feature that tracks a runner's mileage and suggests workouts based on the 10-mile running plan from Boost Running.
Generated: DETERMINISTIC_b9f32bfc836063cc
Batch ID: 20250612_160611
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

class Runner:
    def __init__(self, name: str):
        """
        Initialize a Runner instance with a name and an empty mileage log.
        
        :param name: Name of the runner.
        """
        self.name = name
        self.mileage_log: List[float] = []

    def add_mileage(self, miles: float) -> None:
        """
        Adds mileage to the runner's mileage log.
        
        :param miles: The number of miles run.
        :raises ValueError: If miles is negative or not a number.
        """
        if not isinstance(miles, (int, float)) or miles < 0:
            raise ValueError("Miles must be a non-negative number.")
        
        self.mileage_log.append(miles)

    def get_total_mileage(self) -> float:
        """
        Returns the total mileage recorded for the runner.
        
        :return: Total mileage as a float.
        """
        return sum(self.mileage_log)

    def suggest_workout(self) -> str:
        """
        Suggests a workout based on the 10-mile running plan from Boost Running.
        
        :return: Suggested workout as a string.
        """
        total_mileage = self.get_total_mileage()
        
        if total_mileage < 10:
            return "You are just starting! Try to reach 10 miles this week."
        elif total_mileage < 20:
            return "Consider adding interval training to build speed."
        elif total_mileage < 30:
            return "Great job! Try a long run this weekend."
        else:
            return "You're in great shape! Incorporate hill workouts."

def save_mileage(runner: Runner, file_path: str) -> None:
    """
    Saves the runner's mileage log to a JSON file.
    
    :param runner: The Runner instance to save.
    :param file_path: The path to the file where the mileage log will be saved.
    :raises IOError: If there is an issue writing to the file.
    """
    try:
        with open(file_path, 'w') as file:
            json.dump(runner.mileage_log, file)
    except IOError as e:
        raise IOError(f"Error saving mileage log to {file_path}: {e}")

def load_mileage(runner: Runner, file_path: str) -> None:
    """
    Loads the runner's mileage log from a JSON file.
    
    :param runner: The Runner instance to load mileage into.
    :param file_path: The path to the file to load the mileage log from.
    :raises IOError: If there is an issue reading the file.
    :raises ValueError: If the mileage data is not valid.
    """
    try:
        with open(file_path, 'r') as file:
            mileage_log = json.load(file)
            if all(isinstance(miles, (int, float)) and miles >= 0 for miles in mileage_log):
                runner.mileage_log = mileage_log
            else:
                raise ValueError("Invalid mileage data in the file.")
    except IOError as e:
        raise IOError(f"Error loading mileage log from {file_path}: {e}")

# Example usage
if __name__ == "__main__":
    runner = Runner("Alice")

    # Add some mileage
    runner.add_mileage(5)
    runner.add_mileage(7.5)

    # Suggest a workout
    print(runner.suggest_workout())

    # Save mileage log
    try:
        save_mileage(runner, 'mileage_log.json')
    except IOError as e:
        print(e)

    # Load mileage log
    try:
        load_mileage(runner, 'mileage_log.json')
    except (IOError, ValueError) as e:
        print(e)

    # Check total mileage
    print(f"Total mileage: {runner.get_total_mileage()} miles")
```
