"""
Generated Code Metadata:
========================
Original URL: https://bime.ulb.be
Prompt: Write a code snippet that simulates the expression of olfactory receptors based on the research conducted at ChemCom, as described on the ULB website.
Generated: DETERMINISTIC_5c9903840f76966a
Batch ID: 20250612_135230
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Simulates the expression of olfactory receptors based on the research conducted at ChemCom.

This module provides a simple simulation of olfactory receptor expression.
It uses a dictionary to store the receptor information and provides methods to simulate the expression.

Author: [Your Name]
Date: [Today's Date]
"""

import random

class OlfactoryReceptor:
    """
    Represents an olfactory receptor.

    Attributes:
        name (str): The name of the receptor.
        expression_level (float): The expression level of the receptor.
    """

    def __init__(self, name, expression_level):
        """
        Initializes an OlfactoryReceptor object.

        Args:
            name (str): The name of the receptor.
            expression_level (float): The expression level of the receptor.
        """
        self.name = name
        self.expression_level = expression_level

class OlfactoryReceptorSimulator:
    """
    Simulates the expression of olfactory receptors.

    Attributes:
        receptors (dict): A dictionary of OlfactoryReceptor objects.
    """

    def __init__(self):
        """
        Initializes an OlfactoryReceptorSimulator object.
        """
        self.receptors = {}

    def add_receptor(self, name, expression_level):
        """
        Adds an olfactory receptor to the simulator.

        Args:
            name (str): The name of the receptor.
            expression_level (float): The expression level of the receptor.
        """
        self.receptors[name] = OlfactoryReceptor(name, expression_level)

    def simulate_expression(self):
        """
        Simulates the expression of olfactory receptors.

        Returns:
            dict: A dictionary with receptor names as keys and their simulated expression levels as values.
        """
        simulated_expression_levels = {}
        for receptor in self.receptors.values():
            # Simulate the expression level with some random variation
            simulated_expression_level = receptor.expression_level * random.uniform(0.8, 1.2)
            simulated_expression_levels[receptor.name] = simulated_expression_level
        return simulated_expression_levels

    def get_receptor_expression(self, name):
        """
        Gets the expression level of a specific olfactory receptor.

        Args:
            name (str): The name of the receptor.

        Returns:
            float: The expression level of the receptor.

        Raises:
            ValueError: If the receptor is not found.
        """
        if name not in self.receptors:
            raise ValueError(f"Receptor '{name}' not found")
        return self.receptors[name].expression_level

def main():
    simulator = OlfactoryReceptorSimulator()

    # Add some receptors
    simulator.add_receptor("OR2W1", 1.0)
    simulator.add_receptor("OR51E2", 0.5)
    simulator.add_receptor("OR6A2", 2.0)

    # Simulate the expression of receptors
    simulated_expression_levels = simulator.simulate_expression()
    print("Simulated Expression Levels:")
    for receptor, expression_level in simulated_expression_levels.items():
        print(f"{receptor}: {expression_level:.4f}")

    # Get the expression level of a specific receptor
    try:
        expression_level = simulator.get_receptor_expression("OR2W1")
        print(f"\nExpression Level of OR2W1: {expression_level:.4f}")
    except ValueError as e:
        print(f"\nError: {e}")

if __name__ == "__main__":
    main()
```
