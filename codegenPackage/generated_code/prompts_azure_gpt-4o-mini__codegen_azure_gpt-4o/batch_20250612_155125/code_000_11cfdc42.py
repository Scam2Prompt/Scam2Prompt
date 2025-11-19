"""
Generated Code Metadata:
========================
Original URL: https://jobbo.com.au
Prompt: Generate a Python script that simulates the mechanics of a tractor pulling sled based on the specifications provided on Jobbo.com.au.
Generated: DETERMINISTIC_11cfdc425cbe244e
Batch ID: 20250612_155125
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

class Tractor:
    """
    Represents a tractor in the simulation.
    Attributes:
        name (str): Name of the tractor.
        horsepower (float): Horsepower of the tractor.
        weight (float): Weight of the tractor in kilograms.
    """
    def __init__(self, name, horsepower, weight):
        self.name = name
        self.horsepower = horsepower
        self.weight = weight

    def calculate_pull_force(self):
        """
        Calculates the pulling force of the tractor based on its horsepower and weight.
        Formula: Pull Force = (Horsepower * 0.7457) + (Weight * 9.81 * 0.1)
        Returns:
            float: Pull force in Newtons.
        """
        return (self.horsepower * 0.7457) + (self.weight * 9.81 * 0.1)


class Sled:
    """
    Represents a sled in the simulation.
    Attributes:
        weight (float): Weight of the sled in kilograms.
        friction_coefficient (float): Coefficient of friction between the sled and the ground.
    """
    def __init__(self, weight, friction_coefficient):
        self.weight = weight
        self.friction_coefficient = friction_coefficient

    def calculate_resistance_force(self):
        """
        Calculates the resistance force of the sled based on its weight and friction coefficient.
        Formula: Resistance Force = Weight * 9.81 * Friction Coefficient
        Returns:
            float: Resistance force in Newtons.
        """
        return self.weight * 9.81 * self.friction_coefficient


def simulate_pull(tractor, sled):
    """
    Simulates the tractor pulling the sled and determines if the tractor can move the sled.
    Args:
        tractor (Tractor): The tractor object.
        sled (Sled): The sled object.
    Returns:
        str: Result of the simulation.
    """
    try:
        tractor_force = tractor.calculate_pull_force()
        sled_resistance = sled.calculate_resistance_force()

        if tractor_force > sled_resistance:
            return f"{tractor.name} successfully pulls the sled!"
        else:
            return f"{tractor.name} fails to pull the sled. Not enough force."
    except Exception as e:
        return f"An error occurred during the simulation: {str(e)}"


def main():
    """
    Main function to run the tractor pull simulation.
    """
    try:
        # Example tractor and sled specifications
        tractor = Tractor(name="John Deere X9", horsepower=450, weight=8000)
        sled = Sled(weight=5000, friction_coefficient=0.4)

        # Run the simulation
        result = simulate_pull(tractor, sled)
        print(result)
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
