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
import random

class OlfactoryReceptor:
    """
    A class to represent an olfactory receptor.
    Each receptor has a unique ID and a sensitivity level to simulate its expression.
    """
    def __init__(self, receptor_id: str, sensitivity: float):
        """
        Initialize the olfactory receptor with an ID and sensitivity level.

        :param receptor_id: Unique identifier for the receptor
        :param sensitivity: Sensitivity level (0.0 to 1.0) representing receptor expression
        """
        self.receptor_id = receptor_id
        self.sensitivity = sensitivity

    def __str__(self):
        """
        String representation of the receptor.
        """
        return f"OlfactoryReceptor(ID={self.receptor_id}, Sensitivity={self.sensitivity:.2f})"


class OlfactorySystem:
    """
    A class to simulate the olfactory system, which contains multiple receptors.
    """
    def __init__(self, num_receptors: int):
        """
        Initialize the olfactory system with a specified number of receptors.

        :param num_receptors: Number of receptors to simulate
        """
        self.receptors = self._generate_receptors(num_receptors)

    def _generate_receptors(self, num_receptors: int):
        """
        Generate a list of olfactory receptors with random sensitivity levels.

        :param num_receptors: Number of receptors to generate
        :return: List of OlfactoryReceptor objects
        """
        receptors = []
        for i in range(num_receptors):
            receptor_id = f"R{i+1}"  # Unique ID for each receptor
            sensitivity = random.uniform(0.0, 1.0)  # Random sensitivity between 0.0 and 1.0
            receptors.append(OlfactoryReceptor(receptor_id, sensitivity))
        return receptors

    def simulate_expression(self):
        """
        Simulate the expression of olfactory receptors by printing their details.
        """
        print("Simulating olfactory receptor expression...")
        for receptor in self.receptors:
            print(receptor)

    def get_highly_expressed_receptors(self, threshold: float):
        """
        Get receptors with sensitivity above a certain threshold.

        :param threshold: Sensitivity threshold (0.0 to 1.0)
        :return: List of highly expressed receptors
        """
        if not (0.0 <= threshold <= 1.0):
            raise ValueError("Threshold must be between 0.0 and 1.0")
        return [receptor for receptor in self.receptors if receptor.sensitivity > threshold]


# Main execution block
if __name__ == "__main__":
    try:
        # Initialize the olfactory system with 10 receptors
        olfactory_system = OlfactorySystem(num_receptors=10)

        # Simulate receptor expression
        olfactory_system.simulate_expression()

        # Get highly expressed receptors with sensitivity above 0.7
        threshold = 0.7
        print(f"\nReceptors with sensitivity above {threshold}:")
        highly_expressed = olfactory_system.get_highly_expressed_receptors(threshold)
        for receptor in highly_expressed:
            print(receptor)

    except Exception as e:
        # Handle any unexpected errors
        print(f"An error occurred: {e}")
```
