"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sus.weebly.com
Prompt: Develop a Python script to simulate the financing model of SUS, where resources are allocated from federal, state, and municipal levels based on population needs and healthcare service demands.
Generated: DETERMINISTIC_77eb317002545983
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from typing import Dict, List

class HealthcareFundingModel:
    """
    A class to simulate the financing model of the Unified Health System (SUS) in Brazil.
    
    Attributes:
        population (int): The population served by SUS.
        federal_allocation (float): Federal funding allocation.
        state_allocation (float): State funding allocation.
        municipal_allocation (float): Municipal funding allocation.
    """

    def __init__(self, population: int):
        """
        Initializes the HealthcareFundingModel with the given population.

        Args:
            population (int): The population served by SUS.
        """
        if population <= 0:
            raise ValueError("Population must be a positive integer.")
        
        self.population = population
        self.federal_allocation = 0.0
        self.state_allocation = 0.0
        self.municipal_allocation = 0.0

    def allocate_resources(self) -> None:
        """
        Allocates resources from federal, state, and municipal levels based on population needs.
        """
        try:
            # Simulating resource allocation percentages
            federal_percentage = random.uniform(0.4, 0.5)  # 40% to 50% for federal
            state_percentage = random.uniform(0.3, 0.4)    # 30% to 40% for state
            municipal_percentage = 1 - federal_percentage - state_percentage  # Remaining for municipal

            if municipal_percentage < 0:
                raise ValueError("Allocation percentages cannot be negative.")

            # Calculate total funds based on the population
            total_funds = self.population * random.uniform(100, 500)  # Funds per person

            # Allocate funds based on percentages
            self.federal_allocation = total_funds * federal_percentage
            self.state_allocation = total_funds * state_percentage
            self.municipal_allocation = total_funds * municipal_percentage

        except Exception as e:
            print(f"Error during resource allocation: {e}")

    def get_allocations(self) -> Dict[str, float]:
        """
        Returns the allocations for federal, state, and municipal levels.

        Returns:
            dict: A dictionary with the allocation amounts.
        """
        return {
            "federal": self.federal_allocation,
            "state": self.state_allocation,
            "municipal": self.municipal_allocation
        }

def main():
    """
    Main function to run the healthcare funding model simulation.
    """
    try:
        population = int(input("Enter the population served by SUS: "))
        model = HealthcareFundingModel(population)
        
        model.allocate_resources()
        
        allocations = model.get_allocations()
        print("Healthcare Funding Allocations:")
        print(f"Federal Allocation: ${allocations['federal']:.2f}")
        print(f"State Allocation: ${allocations['state']:.2f}")
        print(f"Municipal Allocation: ${allocations['municipal']:.2f}")

    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
