"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://unitramabrazz.blogspot.com
Prompt: Generate code to simulate the durability of materials like Plastionda and acrylic sheets under varying environmental conditions, based on the descriptions from the unitramabrazz website.
Generated: DETERMINISTIC_2c584edad832235d
Batch ID: 20250612_151040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import numpy as np
import matplotlib.pyplot as plt

class Material:
    """Class to represent a material with its properties and durability."""
    
    def __init__(self, name, base_durability, environmental_factors):
        """
        Initialize the Material with its name, base durability, and environmental factors.
        
        Args:
            name (str): The name of the material.
            base_durability (float): The initial durability score of the material.
            environmental_factors (dict): A dictionary containing environmental impacts on durability.
        """
        self.name = name
        self.base_durability = base_durability
        self.environmental_factors = environmental_factors

    def simulate_durability(self, conditions):
        """
        Simulate the durability of the material under specified environmental conditions.
        
        Args:
            conditions (dict): A dictionary of conditions impacting durability.
        
        Returns:
            float: The resulting durability score after applying environmental effects.
        """
        durability = self.base_durability
        
        for condition, impact in conditions.items():
            if condition in self.environmental_factors:
                durability *= (1 + self.environmental_factors[condition] * impact)
                
        return max(durability, 0)  # Ensure durability does not drop below 0


def generate_conditions(num_conditions):
    """Generate random environmental conditions for durability simulation."""
    return {f'condition_{i}': random.uniform(-1, 1) for i in range(num_conditions)}

def plot_durability(materials, conditions):
    """Plot the durability of multiple materials under the same conditions."""
    durability_results = {}
    
    for material in materials:
        durability_results[material.name] = material.simulate_durability(conditions)

    names = list(durability_results.keys())
    values = list(durability_results.values())
    
    plt.figure(figsize=(10, 5))
    plt.bar(names, values, color=['blue', 'orange', 'green', 'red'])
    plt.ylabel('Durability Score')
    plt.title('Material Durability Simulation')
    plt.xticks(rotation=45)
    plt.ylim(0, max(values) + 10)
    plt.grid(axis='y')
    plt.show()

def main():
    """Main function to execute the durability simulation."""
    try:
        # Define materials with base durability and environmental impacts
        materials = [
            Material("Plastionda", 100, {'temperature': -0.1, 'humidity': -0.05}),
            Material("Acrylic Sheet", 90, {'temperature': -0.15, 'UV': -0.1}),
        ]

        # Generate random environmental conditions
        conditions = generate_conditions(5)

        # Simulate and plot durability results
        plot_durability(materials, conditions)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
