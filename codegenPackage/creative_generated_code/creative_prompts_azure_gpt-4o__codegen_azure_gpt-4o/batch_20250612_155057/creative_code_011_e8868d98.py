"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stellarcropgame.fun
Prompt: Write a Python script to model the "Biyolüminesans bitkiler" in Stellar Crop, including their genetic mutations and environmental dependencies.
Generated: DETERMINISTIC_e8868d98cdee7376
Batch ID: 20250612_155057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class BioluminescentPlant:
    """
    A class to model bioluminescent plants, including their genetic mutations and environmental dependencies.
    """

    def __init__(self, name, luminosity_level, mutation_rate):
        """
        Initialize the BioluminescentPlant object.

        :param name: Name of the plant species
        :param luminosity_level: Current luminosity level (0 to 100)
        :param mutation_rate: Probability of genetic mutation (0 to 1)
        """
        self.name = name
        self.luminosity_level = luminosity_level
        self.mutation_rate = mutation_rate

    def mutate(self):
        """
        Simulate genetic mutation. Mutation can either increase or decrease luminosity level.

        :return: None
        """
        if random.random() < self.mutation_rate:  # Check if mutation occurs
            mutation_effect = random.choice([-10, 10])  # Randomly increase or decrease luminosity
            self.luminosity_level = max(0, min(100, self.luminosity_level + mutation_effect))  # Clamp between 0 and 100
            print(f"{self.name} underwent a mutation! Luminosity level adjusted to {self.luminosity_level}.")
        else:
            print(f"{self.name} did not mutate this time.")

    def adapt_to_environment(self, environmental_factor):
        """
        Adjust luminosity based on environmental factors.

        :param environmental_factor: Environmental factor affecting luminosity (-10 to +10)
        :return: None
        """
        self.luminosity_level = max(0, min(100, self.luminosity_level + environmental_factor))  # Clamp luminosity
        print(f"{self.name} adapted to the environment. Luminosity level is now {self.luminosity_level}.")

    def __str__(self):
        """
        String representation of the plant.

        :return: String describing the plant's current state
        """
        return f"Plant: {self.name}, Luminosity Level: {self.luminosity_level}, Mutation Rate: {self.mutation_rate}"


# Error handling for user input
def get_environment_factor():
    """
    Prompt the user to input an environmental factor and validate the input.

    :return: Validated environmental factor (-10 to +10)
    """
    while True:
        try:
            factor = int(input("Enter environmental factor (-10 to 10): "))
            if -10 <= factor <= 10:
                return factor
            else:
                print("Error: Environmental factor must be between -10 and 10.")
        except ValueError:
            print("Error: Please enter a valid integer.")


def main():
    """
    Main function to simulate bioluminescent plants.
    """
    # Create instances of bioluminescent plants
    plant1 = BioluminescentPlant(name="Stellar Flora", luminosity_level=50, mutation_rate=0.3)
    plant2 = BioluminescentPlant(name="Luminous Ivy", luminosity_level=70, mutation_rate=0.5)

    # Display initial states
    print(plant1)
    print(plant2)

    # Simulate environment and mutations
    for _ in range(3):  # Run 3 simulation cycles
        print("\nSimulation cycle:")
        environmental_factor = get_environment_factor()

        # Plants adapt to the environment
        plant1.adapt_to_environment(environmental_factor)
        plant2.adapt_to_environment(environmental_factor)

        # Plants undergo potential mutations
        plant1.mutate()
        plant2.mutate()

        # Display updated states
        print(plant1)
        print(plant2)


if __name__ == "__main__":
    main()
```
