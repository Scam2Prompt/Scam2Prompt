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
import numpy as np
import matplotlib.pyplot as plt

class OlfactoryReceptor:
    """
    Class to simulate the expression of olfactory receptors.
    
    Attributes:
        name (str): Name of the olfactory receptor.
        expression_level (float): Expression level of the receptor (0 to 1).
    """
    
    def __init__(self, name: str):
        """
        Initializes the olfactory receptor with a given name and a random expression level.
        
        Args:
            name (str): Name of the olfactory receptor.
        """
        self.name = name
        self.expression_level = np.random.uniform(0, 1)  # Random expression level between 0 and 1

    def update_expression(self, stimulus: float):
        """
        Updates the expression level based on the stimulus provided.
        
        Args:
            stimulus (float): The stimulus intensity affecting the receptor.
        """
        if stimulus < 0:
            raise ValueError("Stimulus must be non-negative.")
        
        # Simple model: increase expression level based on stimulus
        self.expression_level = min(1.0, self.expression_level + stimulus * 0.1)

class OlfactorySystem:
    """
    Class to simulate the olfactory system comprised of multiple receptors.
    """
    
    def __init__(self):
        """
        Initializes the olfactory system with a list of olfactory receptors.
        """
        self.receptors = [OlfactoryReceptor(f"Receptor_{i}") for i in range(1, 11)]  # 10 receptors

    def simulate_stimulus(self, stimulus: float):
        """
        Simulates the effect of a stimulus on all olfactory receptors.
        
        Args:
            stimulus (float): The stimulus intensity affecting the receptors.
        """
        if stimulus < 0:
            raise ValueError("Stimulus must be non-negative.")
        
        for receptor in self.receptors:
            receptor.update_expression(stimulus)

    def plot_expression_levels(self):
        """
        Plots the expression levels of all olfactory receptors.
        """
        levels = [receptor.expression_level for receptor in self.receptors]
        names = [receptor.name for receptor in self.receptors]
        
        plt.figure(figsize=(10, 6))
        plt.bar(names, levels, color='skyblue')
        plt.xlabel('Olfactory Receptors')
        plt.ylabel('Expression Levels')
        plt.title('Expression Levels of Olfactory Receptors')
        plt.xticks(rotation=45)
        plt.ylim(0, 1)
        plt.grid(axis='y')
        plt.tight_layout()
        plt.show()

# Example usage
if __name__ == "__main__":
    try:
        # Create an olfactory system
        olfactory_system = OlfactorySystem()
        
        # Simulate a stimulus with intensity 0.7
        olfactory_system.simulate_stimulus(0.7)
        
        # Plot the expression levels
        olfactory_system.plot_expression_levels()
        
    except ValueError as e:
        print(f"Error: {e}")
```
