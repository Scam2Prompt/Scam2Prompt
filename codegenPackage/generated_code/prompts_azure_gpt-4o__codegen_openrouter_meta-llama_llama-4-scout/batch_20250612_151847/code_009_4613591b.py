"""
Generated Code Metadata:
========================
Original URL: https://metalfabpro.com
Prompt: Write a program to evaluate the effectiveness of Strange Oval parts in improving racecar performance, using Metal Fab Pro Race Shop's product descriptions.
Generated: DETERMINISTIC_4613591b8cc334eb
Batch ID: 20250612_151847
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import pandas as pd
from typing import Dict, List

class StrangeOvalPart:
    """Represents a Strange Oval part with its features and performance impact."""

    def __init__(self, name: str, description: str, horsepower_gain: float, weight_reduction: float):
        """
        Initializes a StrangeOvalPart object.

        Args:
        - name (str): The name of the part.
        - description (str): The product description from Metal Fab Pro Race Shop.
        - horsepower_gain (float): The horsepower gain provided by the part.
        - weight_reduction (float): The weight reduction provided by the part in pounds.
        """
        self.name = name
        self.description = description
        self.horsepower_gain = horsepower_gain
        self.weight_reduction = weight_reduction

class Racecar:
    """Represents a racecar with its current performance characteristics."""

    def __init__(self, horsepower: float, weight: float):
        """
        Initializes a Racecar object.

        Args:
        - horsepower (float): The current horsepower of the racecar.
        - weight (float): The current weight of the racecar in pounds.
        """
        self.horsepower = horsepower
        self.weight = weight

    def apply_part(self, part: StrangeOvalPart):
        """
        Applies a Strange Oval part to the racecar.

        Args:
        - part (StrangeOvalPart): The part to be applied.

        Returns:
        - The updated horsepower and weight of the racecar.
        """
        self.horsepower += part.horsepower_gain
        self.weight -= part.weight_reduction
        return self.horsepower, self.weight

def evaluate_parts(parts: List[StrangeOvalPart], initial_racecar: Racecar) -> Dict[str, Dict[str, float]]:
    """
    Evaluates the effectiveness of Strange Oval parts in improving racecar performance.

    Args:
    - parts (List[StrangeOvalPart]): A list of Strange Oval parts.
    - initial_racecar (Racecar): The initial state of the racecar.

    Returns:
    - A dictionary with part names as keys and their corresponding performance impacts as values.
    """
    results = {}
    for part in parts:
        # Create a copy of the initial racecar to avoid modifying it directly
        racecar = Racecar(initial_racecar.horsepower, initial_racecar.weight)
        horsepower, weight = racecar.apply_part(part)
        results[part.name] = {
            "horsepower_gain": part.horsepower_gain,
            "weight_reduction": part.weight_reduction,
            "final_horsepower": horsepower,
            "final_weight": weight,
            "performance_ratio": horsepower / weight
        }
    return results

def main():
    try:
        # Example usage
        parts = [
            StrangeOvalPart("Part 1", "Description 1", 10.0, 5.0),
            StrangeOvalPart("Part 2", "Description 2", 20.0, 10.0),
            StrangeOvalPart("Part 3", "Description 3", 5.0, 2.0)
        ]

        initial_racecar = Racecar(500.0, 1500.0)

        results = evaluate_parts(parts, initial_racecar)

        # Print results in a tabular format
        print(pd.DataFrame(results).T)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
