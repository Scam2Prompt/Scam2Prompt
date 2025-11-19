"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bime.ulb.be
Prompt: Write a code snippet that simulates the expression of olfactory receptors based on the research conducted at ChemCom, as described on the ULB website.
Generated: DETERMINISTIC_5c9903840f76966a
Batch ID: 20250612_135230
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import logging

# Configure logging for error handling and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class OlfactoryReceptor:
    """
    Class representing an olfactory receptor.
    Each receptor has a name and an expression level.
    """
    def __init__(self, name, expression_level=0.0):
        """
        Initialize an olfactory receptor instance.
        
        :param name: Name of the receptor (string)
        :param expression_level: Initial expression level (float, default 0.0)
        """
        self.name = name
        self.expression_level = expression_level

    def simulate_expression(self):
        """
        Simulate the expression level of the receptor.
        Expression level is a random float between 0 and 1.
        """
        self.expression_level = round(random.uniform(0, 1), 4)
        logging.info(f"Receptor {self.name} simulated expression level: {self.expression_level}")

    def __str__(self):
        """
        String representation of the receptor.
        """
        return f"{self.name}: Expression Level = {self.expression_level}"


class OlfactorySystem:
    """
    Class representing the olfactory system, containing multiple olfactory receptors.
    """
    def __init__(self):
        """
        Initialize the olfactory system with an empty list of receptors.
        """
        self.receptors = []

    def add_receptor(self, receptor_name):
        """
        Add a new receptor to the system.
        
        :param receptor_name: Name of the receptor (string)
        """
        if not receptor_name:
            logging.error("Receptor name cannot be empty.")
            raise ValueError("Receptor name cannot be empty.")
        receptor = OlfactoryReceptor(receptor_name)
        self.receptors.append(receptor)
        logging.info(f"Receptor '{receptor_name}' added to the system.")

    def simulate_all_expressions(self):
        """
        Simulate the expression levels for all receptors in the system.
        """
        if not self.receptors:
            logging.warning("No receptors found in the system. Add receptors before simulating.")
            return

        for receptor in self.receptors:
            receptor.simulate_expression()

    def display_expressions(self):
        """
        Display the expression levels of all receptors.
        """
        if not self.receptors:
            logging.info("No receptors to display.")
            return

        logging.info("Displaying all receptor expressions:")
        for receptor in self.receptors:
            print(receptor)


# Example usage:

if __name__ == "__main__":
    try:
        # Initialize the olfactory system
        olfactory_system = OlfactorySystem()
        
        # Add receptors to the system (based on research data or hypothetical receptors)
        olfactory_system.add_receptor("OR1A1")
        olfactory_system.add_receptor("OR2W3")
        olfactory_system.add_receptor("OR5K1")
        
        # Simulate expression for all receptors
        olfactory_system.simulate_all_expressions()
        
        # Display the receptor expressions
        olfactory_system.display_expressions()
    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
