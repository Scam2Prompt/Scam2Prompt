"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wolfyyy.pages.dev
Prompt: Write a Python script to simulate the breeding mechanics of Sheep in Wolf Game, ensuring WOOL production increases over time based on the rules described on the website.
Generated: DETERMINISTIC_67fb5642bab39d63
Batch ID: 20250612_151310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import random


class Sheep:
    """
    Class representing a Sheep in the Wolf Game.
    Sheep produce WOOL over time and can breed to create new Sheep.
    """

    def __init__(self, name):
        """
        Initialize a Sheep instance.
        :param name: Name of the sheep
        """
        self.name = name
        self.age = 0  # Age of the sheep in days
        self.wool_production_rate = 5  # WOOL produced per day
        self.total_wool = 0  # Total WOOL produced
        self.is_alive = True  # Sheep's living status

    def produce_wool(self):
        """
        Function to produce WOOL. WOOL production increases as sheep ages.
        """
        if self.is_alive:
            self.total_wool += self.wool_production_rate
            # Increase WOOL production rate by 10% every 10 days
            if self.age % 10 == 0 and self.age > 0:
                self.wool_production_rate = int(self.wool_production_rate * 1.1)

    def age_sheep(self):
        """
        Function to age the sheep by one day.
        """
        self.age += 1
        # Simulate natural death at age > 100
        if self.age > 100:
            self.is_alive = False

    def breed(self):
        """
        Function to breed the sheep. Returns a new Sheep instance.
        Breeding has a 25% chance of success per day.
        :return: A new Sheep instance if breeding is successful, else None
        """
        if self.is_alive and random.random() < 0.25:
            return Sheep(name=f"{self.name}'s offspring")
        return None


class WolfGame:
    """
    Class representing the Wolf Game mechanics for Sheep and WOOL production.
    """

    def __init__(self):
        """
        Initialize WolfGame instance with a list of Sheep.
        """
        self.sheep_list = []  # List of sheep in the game
        self.total_wool_produced = 0  # Total WOOL produced in the game

    def add_sheep(self, sheep):
        """
        Add a new Sheep to the game.
        :param sheep: Sheep instance to add
        """
        self.sheep_list.append(sheep)

    def simulate_day(self):
        """
        Simulate a single day in the game.
        """
        new_sheep = []
        for sheep in self.sheep_list:
            if sheep.is_alive:
                sheep.age_sheep()
                sheep.produce_wool()
                self.total_wool_produced += sheep.wool_production_rate

                # Try to breed the sheep
                offspring = sheep.breed()
                if offspring:
                    new_sheep.append(offspring)

        # Add any new sheep to the sheep list
        self.sheep_list.extend(new_sheep)

    def display_status(self):
        """
        Display the current status of the game.
        """
        print(f"Total WOOL produced: {self.total_wool_produced}")
        print(f"Number of sheep: {len(self.sheep_list)}")
        for sheep in self.sheep_list:
            status = "Alive" if sheep.is_alive else "Deceased"
            print(f"Sheep {sheep.name}: Age {sheep.age}, WOOL {sheep.total_wool}, Status {status}")


# Main script to run the simulation
if __name__ == "__main__":
    # Initialize the game
    game = WolfGame()

    # Add initial sheep
    game.add_sheep(Sheep(name="Sheep1"))
    game.add_sheep(Sheep(name="Sheep2"))

    # Simulate the game for 50 days
    for day in range(1, 51):
        print(f"--- Day {day} ---")
        game.simulate_day()
        game.display_status()
        time.sleep(0.5)  # Pause for readability; remove in production
```
