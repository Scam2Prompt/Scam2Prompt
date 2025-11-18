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
import logging

# Set up logging for monitoring the simulation
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DigitalEntity:
    """
    Represents a digital entity with traits, ordinal number (generation), and fitness level.
    """
    def __init__(self, generation: int):
        self.generation = generation  # Ordinal number representing the entity's generation
        self.traits = self._generate_traits()  # Randomly generated traits
        self.fitness = self._evaluate_fitness()  # Fitness score based on traits

    def _generate_traits(self) -> dict:
        """
        Generates a set of random traits for the entity.
        Traits are represented as a dictionary with numerical values.
        """
        return {
            'strength': random.randint(1, 100),
            'agility': random.randint(1, 100),
            'intelligence': random.randint(1, 100),
            'resilience': random.randint(1, 100)
        }

    def _evaluate_fitness(self) -> int:
        """
        Calculates a fitness score based on the entity's traits.
        Higher fitness indicates better adaptation.
        """
        # Example formula: weighted sum of traits
        return (self.traits['strength'] * 0.4 +
                self.traits['agility'] * 0.3 +
                self.traits['intelligence'] * 0.2 +
                self.traits['resilience'] * 0.1)

    def mutate(self):
        """
        Introduces random mutations to the entity's traits.
        Simulates evolution through small changes.
        """
        mutation_rate = 0.1  # Probability of mutation per trait
        for trait in self.traits:
            if random.random() < mutation_rate:
                self.traits[trait] += random.randint(-10, 10)  # Random adjustment
                self.traits[trait] = max(1, min(self.traits[trait], 100))  # Keep traits within bounds
        self.fitness = self._evaluate_fitness()  # Recalculate fitness after mutation


class EvolutionSimulator:
    """
    Simulates the evolution of digital entities over multiple generations.
    """
    def __init__(self, initial_population_size: int, generations: int):
        self.initial_population_size = initial_population_size
        self.generations = generations
        self.population = []  # List to store the population of entities

    def _create_initial_population(self):
        """
        Creates the initial population of digital entities.
        """
        logging.info("Creating initial population...")
        self.population = [DigitalEntity(generation=1) for _ in range(self.initial_population_size)]

    def _select_fittest(self) -> list:
        """
        Selects the top 50% of entities based on fitness.
        Simulates natural selection.
        """
        sorted_population = sorted(self.population, key=lambda x: x.fitness, reverse=True)
        return sorted_population[:len(sorted_population) // 2]

    def _reproduce(self, parents: list) -> list:
        """
        Reproduces a new generation of entities based on the fittest parents.
        """
        logging.info("Reproducing new generation...")
        new_generation = []
        for parent in parents:
            # Each parent produces two offspring
            for _ in range(2):
                offspring = DigitalEntity(generation=parent.generation + 1)
                offspring.traits = parent.traits.copy()  # Inherit traits from parent
                offspring.mutate()  # Apply mutation to traits
                new_generation.append(offspring)
        return new_generation

    def run_simulation(self):
        """
        Runs the evolution simulation for the specified number of generations.
        """
        self._create_initial_population()
        for generation_number in range(1, self.generations + 1):
            logging.info(f"Simulating generation {generation_number}...")
            self.population = self._select_fittest()  # Select the fittest entities
            self.population = self._reproduce(self.population)  # Generate offspring
        logging.info("Simulation complete.")

    def get_top_entities(self, top_n: int = 5) -> list:
        """
        Returns the top N entities based on fitness.
        """
        return sorted(self.population, key=lambda x: x.fitness, reverse=True)[:top_n]


if __name__ == "__main__":
    try:
        # Parameters
        initial_population_size = 100
        generations = 10
        top_n = 5

        # Run the simulation
        simulator = EvolutionSimulator(initial_population_size, generations)
        simulator.run_simulation()

        # Display the top entities
        logging.info("Top entities after simulation:")
        top_entities = simulator.get_top_entities(top_n)
        for idx, entity in enumerate(top_entities, start=1):
            logging.info(f"Rank {idx}: Generation {entity.generation}, Fitness {entity.fitness}, Traits {entity.traits}")
    except Exception as e:
        logging.error(f"An error occurred during simulation: {str(e)}")
```
