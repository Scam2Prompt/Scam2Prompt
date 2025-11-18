"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://capinaeletrica.com.br
Prompt: Write Python code to simulate the effects of Capina Elétrica's high-voltage weed removal technology on urban vegetation, ensuring the simulation models both root and shoot elimination as described on the website.
Generated: DETERMINISTIC_5d8264a3becb7215
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class UrbanVegetation:
    """
    Represents urban vegetation with properties for roots and shoots.
    """
    def __init__(self, name: str, root_health: int, shoot_health: int):
        """
        Initialize the vegetation with given health values.

        :param name: Name of the vegetation (e.g., plant type).
        :param root_health: Health level of the roots (0-100).
        :param shoot_health: Health level of the shoots (0-100).
        """
        self.name = name
        self.root_health = root_health
        self.shoot_health = shoot_health

    def __str__(self):
        return f"{self.name} (Roots: {self.root_health}, Shoots: {self.shoot_health})"

    def is_completely_removed(self) -> bool:
        """
        Check if both roots and shoots are completely eliminated.

        :return: True if root_health and shoot_health are both 0, else False.
        """
        return self.root_health == 0 and self.shoot_health == 0


class HighVoltageWeedRemovalSimulator:
    """
    Simulates the effects of Capina Elétrica's high-voltage weed removal technology.
    """
    def __init__(self, efficiency: float):
        """
        Initialize the simulator with a given efficiency rate.

        :param efficiency: Effectiveness of the technology as a percentage (0-1).
        """
        if not (0 <= efficiency <= 1):
            raise ValueError("Efficiency must be between 0 and 1.")
        self.efficiency = efficiency

    def apply_high_voltage(self, vegetation: UrbanVegetation):
        """
        Simulate applying high voltage to the vegetation.

        :param vegetation: The UrbanVegetation instance to simulate effects on.
        """
        try:
            # Calculate damage based on efficiency and randomness
            root_damage = int(self.efficiency * random.randint(20, 50))
            shoot_damage = int(self.efficiency * random.randint(30, 60))

            # Apply damage to roots and shoots
            vegetation.root_health = max(0, vegetation.root_health - root_damage)
            vegetation.shoot_health = max(0, vegetation.shoot_health - shoot_damage)

            print(f"Applied high voltage to {vegetation.name}: "
                  f"Root damage={root_damage}, Shoot damage={shoot_damage}")
        except Exception as e:
            print(f"Error during simulation: {e}")


def main():
    """
    Entry point for the simulation script.
    """
    try:
        # Create sample urban vegetation instances
        vegetation_list = [
            UrbanVegetation("Grass", root_health=100, shoot_health=100),
            UrbanVegetation("Bush", root_health=80, shoot_health=90),
            UrbanVegetation("Tree", root_health=120, shoot_health=110),
        ]

        # Initialize the simulator with 80% efficiency
        simulator = HighVoltageWeedRemovalSimulator(efficiency=0.8)

        # Run simulation
        for vegetation in vegetation_list:
            print(f"Before treatment: {vegetation}")
            simulator.apply_high_voltage(vegetation)
            print(f"After treatment: {vegetation}")
            print(f"Removed: {'Yes' if vegetation.is_completely_removed() else 'No'}")
            print("-" * 40)

    except Exception as e:
        print(f"An error occurred during simulation: {e}")


if __name__ == "__main__":
    # Execute the simulation script
    main()
```
