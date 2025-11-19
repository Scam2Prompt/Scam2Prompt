"""
Generated Code Metadata:
========================
Original URL: https://fehurunes.app
Prompt: Develop a Python script to simulate the evolution of digital entities based on ordinal numbers, as described in the NEO-Sentient collection.
Generated: DETERMINISTIC_ba81afaa302f7c2f
Batch ID: 20250612_153424
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import numpy as np
from typing import List, Dict, Tuple, Optional

class DigitalEntity:
    """
    Represents a digital entity with attributes based on ordinal numbers.
    """
    def __init__(self, id: int, ordinal: int):
        """
        Initialize a digital entity with given ID and ordinal number.
        
        Args:
            id: Unique identifier for the entity
            ordinal: Ordinal number representing the entity's position in evolution
        """
        self.id = id
        self.ordinal = ordinal
        self.traits = self._generate_traits()
        self.fitness = 0.0
        
    def _generate_traits(self) -> Dict[str, float]:
        """
        Generate random traits based on the ordinal number.
        
        Returns:
            Dictionary of trait names and their values
        """
        random.seed(self.ordinal)
        return {
            'intelligence': random.uniform(0, 1) * (self.ordinal / 10),
            'adaptability': random.uniform(0, 1) * (self.ordinal / 5),
            'resilience': random.uniform(0, 1) * (self.ordinal / 8),
            'creativity': random.uniform(0, 1) * (self.ordinal / 12)
        }
    
    def calculate_fitness(self, environment: Dict[str, float]) -> None:
        """
        Calculate fitness based on how well traits match environment requirements.
        
        Args:
            environment: Dictionary of environment requirements
        """
        self.fitness = sum(
            self.traits[trait] * environment.get(trait, 0)
            for trait in self.traits
        )
    
    def mutate(self, mutation_rate: float = 0.1) -> None:
        """
        Mutate the entity's traits based on mutation rate.
        
        Args:
            mutation_rate: Probability of mutation (0 to 1)
        """
        for trait in self.traits:
            if random.random() < mutation_rate:
                self.traits[trait] = np.clip(
                    self.traits[trait] + random.uniform(-0.2, 0.2),
                    0, 1
                )
        self.ordinal += 1  # Increment ordinal after mutation

class EvolutionSimulator:
    """
    Simulates the evolution of digital entities.
    """
    def __init__(self, population_size: int = 100, initial_ordinal: int = 1):
        """
        Initialize the simulator with a population of entities.
        
        Args:
            population_size: Number of entities in the population
            initial_ordinal: Starting ordinal number for first generation
        """
        self.population = [
            DigitalEntity(id=i, ordinal=initial_ordinal)
            for i in range(population_size)
        ]
        self.generation = 0
        self.environment = {
            'intelligence': 0.6,
            'adaptability': 0.8,
            'resilience': 0.5,
            'creativity': 0.3
        }
    
    def evaluate_population(self) -> None:
        """
        Calculate fitness for all entities in the population.
        """
        for entity in self.population:
            entity.calculate_fitness(self.environment)
    
    def select_parents(self, num_parents: int = 20) -> List[DigitalEntity]:
        """
        Select top-performing entities as parents for next generation.
        
        Args:
            num_parents: Number of parents to select
            
        Returns:
            List of selected parent entities
        """
        sorted_pop = sorted(
            self.population,
            key=lambda x: x.fitness,
            reverse=True
        )
        return sorted_pop[:num_parents]
    
    def reproduce(self, parents: List[DigitalEntity], offspring_size: int) -> List[DigitalEntity]:
        """
        Create new generation through crossover and mutation.
        
        Args:
            parents: List of parent entities
            offspring_size: Number of offspring to produce
            
        Returns:
            List of new offspring entities
        """
        offspring = []
        for i in range(offspring_size):
            parent1, parent2 = random.sample(parents, 2)
            new_ordinal = max(parent1.ordinal, parent2.ordinal) + 1
            offspring.append(DigitalEntity(id=i, ordinal=new_ordinal))
            
            # Blend traits from both parents
            for trait in offspring[-1].traits:
                offspring[-1].traits[trait] = np.mean([
                    parent1.traits[trait],
                    parent2.traits[trait]
                ])
            
            # Apply mutation
            offspring[-1].mutate()
        return offspring
    
    def evolve(self, generations: int = 10) -> None:
        """
        Run the evolution simulation for specified number of generations.
        
        Args:
            generations: Number of generations to simulate
        """
        for _ in range(generations):
            self.generation += 1
            self.evaluate_population()
            parents = self.select_parents()
            self.population = self.reproduce(parents, len(self.population))
            
            # Optional: Print generation statistics
            avg_fitness = sum(e.fitness for e in self.population) / len(self.population)
            max_fitness = max(e.fitness for e in self.population)
            print(f"Generation {self.generation}: Avg Fitness = {avg_fitness:.2f}, Max Fitness = {max_fitness:.2f}")
    
    def get_best_entity(self) -> Optional[DigitalEntity]:
        """
        Get the entity with highest fitness in current population.
        
        Returns:
            The best performing entity or None if population is empty
        """
        if not self.population:
            return None
        return max(self.population, key=lambda x: x.fitness)

def main():
    """Run the evolution simulation."""
    try:
        simulator = EvolutionSimulator(population_size=50)
        simulator.evolve(generations=20)
        
        best_entity = simulator.get_best_entity()
        if best_entity:
            print("\nBest Entity:")
            print(f"ID: {best_entity.id}")
            print(f"Ordinal: {best_entity.ordinal}")
            print(f"Fitness: {best_entity.fitness:.2f}")
            print("Traits:", best_entity.traits)
    except Exception as e:
        print(f"Error during simulation: {str(e)}")

if __name__ == "__main__":
    main()
```
