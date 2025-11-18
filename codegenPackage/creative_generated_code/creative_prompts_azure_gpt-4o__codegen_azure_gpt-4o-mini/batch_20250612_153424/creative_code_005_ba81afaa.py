"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fehurunes.app
Prompt: Develop a Python script to simulate the evolution of digital entities based on ordinal numbers, as described in the NEO-Sentient collection.
Generated: DETERMINISTIC_ba81afaa302f7c2f
Batch ID: 20250612_153424
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import json

class DigitalEntity:
    """
    Represents a digital entity with an ordinal number and a set of traits.
    """

    def __init__(self, ordinal_number: int):
        """
        Initializes a DigitalEntity with an ordinal number and random traits.
        
        Args:
            ordinal_number (int): The unique ordinal number for the entity.
        """
        self.ordinal_number = ordinal_number
        self.traits = self.generate_traits()

    def generate_traits(self):
        """
        Generates random traits for the digital entity.
        
        Returns:
            dict: A dictionary containing the traits of the entity.
        """
        return {
            'intelligence': random.uniform(0, 1),
            'creativity': random.uniform(0, 1),
            'adaptability': random.uniform(0, 1)
        }

    def evolve(self):
        """
        Evolves the entity's traits through a mutation process.
        """
        mutation_rate = 0.1
        for trait in self.traits:
            if random.random() < mutation_rate:
                mutation_amount = random.uniform(-0.1, 0.1)
                self.traits[trait] = max(0, min(1, self.traits[trait] + mutation_amount))

    def to_dict(self) -> dict:
        """
        Converts the entity to a dictionary format.
        
        Returns:
            dict: A dictionary representation of the entity.
        """
        return {
            'ordinal_number': self.ordinal_number,
            'traits': self.traits
        }

def simulate_evolution(generations: int, population_size: int):
    """
    Simulates the evolution of digital entities over a specified number of generations.
    
    Args:
        generations (int): The number of generations to simulate.
        population_size (int): The initial population size of digital entities.
    
    Returns:
        list: A list of digital entities at the end of the simulation.
    """
    # Initialize population with unique ordinal numbers
    population = [DigitalEntity(i) for i in range(population_size)]

    for generation in range(generations):
        print(f"Generation {generation + 1}:")
        for entity in population:
            entity.evolve()
            print(json.dumps(entity.to_dict(), indent=2))  # Output the state of each entity
            
    return population

if __name__ == "__main__":
    try:
        # Set parameters for simulation
        generations = 5      # Number of generations to simulate
        population_size = 10 # Initial population size

        # Run the evolution simulation
        final_population = simulate_evolution(generations, population_size)

    except Exception as e:
        print(f"An error occurred during simulation: {e}")
```
