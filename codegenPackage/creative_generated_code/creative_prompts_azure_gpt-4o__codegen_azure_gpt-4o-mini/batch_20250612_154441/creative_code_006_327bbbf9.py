"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rubberflooringindonesia.com
Prompt: Write a script to simulate the durability of rubber flooring materials (e.g., TPV Rubber, Rubber Tiles) under heavy usage conditions, referencing the use cases like gym fitness and playgrounds mentioned on Rubber Flooring Indonesia's site.
Generated: DETERMINISTIC_327bbbf9848668e4
Batch ID: 20250612_154441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import matplotlib.pyplot as plt

class RubberFlooring:
    """
    A class to simulate the durability of rubber flooring materials under heavy usage conditions.
    """

    def __init__(self, material_name, initial_durability):
        """
        Initializes the RubberFlooring instance.

        :param material_name: Name of the rubber flooring material (e.g., "TPV Rubber", "Rubber Tiles")
        :param initial_durability: Initial durability rating of the material (1 to 100 scale)
        """
        self.material_name = material_name
        self.durability = initial_durability

    def simulate_wear(self, usage_hours):
        """
        Simulates wear on the rubber flooring material over a period of usage hours.

        :param usage_hours: Number of hours the flooring will be used
        :raises ValueError: If usage_hours is not a positive integer
        """
        if not isinstance(usage_hours, int) or usage_hours <= 0:
            raise ValueError("usage_hours must be a positive integer.")

        # Wear factor, simulating wear per hour (randomized for variability)
        wear_factor = random.uniform(0.1, 0.5)

        # Calculate wear based on usage hours
        wear = usage_hours * wear_factor
        self.durability -= wear

        # Ensure durability does not fall below zero
        if self.durability < 0:
            self.durability = 0

        return self.durability

    def evaluate_durability(self):
        """
        Evaluates the durability status of the rubber flooring material.

        :return: A string indicating the durability status
        """
        if self.durability > 75:
            return f"{self.material_name} is in excellent condition."
        elif self.durability > 50:
            return f"{self.material_name} is in good condition."
        elif self.durability > 25:
            return f"{self.material_name} is in fair condition."
        else:
            return f"{self.material_name} is in poor condition and needs replacement."

def simulate_flooring_durability(materials, usage_hours_list):
    """
    Simulates the durability of different rubber flooring materials over a range of usage hours.

    :param materials: List of tuples containing material name and initial durability
    :param usage_hours_list: List of hours for simulation
    """
    results = {}

    for material_name, initial_durability in materials:
        flooring = RubberFlooring(material_name, initial_durability)
        durability_over_time = []

        for hours in usage_hours_list:
            durability = flooring.simulate_wear(hours)
            durability_over_time.append(durability)

        results[material_name] = durability_over_time

    # Plot results
    plt.figure(figsize=(10, 6))
    for material_name, durability_over_time in results.items():
        plt.plot(usage_hours_list, durability_over_time, label=material_name)

    plt.title('Durability of Rubber Flooring Materials Under Heavy Usage')
    plt.xlabel('Usage Hours')
    plt.ylabel('Durability Rating')
    plt.legend()
    plt.grid(True)
    plt.ylim(0, 100)
    plt.show()

# Example usage
if __name__ == "__main__":
    try:
        materials = [
            ("TPV Rubber", 100),  # Initial durability of TPV Rubber
            ("Rubber Tiles", 100)  # Initial durability of Rubber Tiles
        ]
        usage_hours_list = list(range(1, 101, 10))  # Simulate for 1 to 100 hours in 10-hour increments
        simulate_flooring_durability(materials, usage_hours_list)
    except ValueError as e:
        print(f"Error: {e}")
```
