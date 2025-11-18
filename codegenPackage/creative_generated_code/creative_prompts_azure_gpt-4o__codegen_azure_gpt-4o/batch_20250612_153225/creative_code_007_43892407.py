"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vgtindia.in
Prompt: Write code to simulate the operation of a "Seed Drill" machine, including seed distribution and soil depth control, as described on the Vinglob Greentech website.
Generated: DETERMINISTIC_43892407a436e2f7
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class SeedDrill:
    """
    A class to simulate the operation of a Seed Drill machine.

    Attributes:
        hopper_capacity (int): Maximum capacity of the seed hopper in units.
        seed_rate (int): Number of seeds to drop per second.
        soil_depth (float): Target soil depth for seed placement in cm.
    """
    def __init__(self, hopper_capacity, seed_rate, soil_depth):
        """
        Initialize the Seed Drill machine with hopper capacity, seed rate, and soil depth.
        """
        self.hopper_capacity = hopper_capacity  # Maximum seed storage capacity
        self.seed_rate = seed_rate  # Seeds dispersed per second
        self.soil_depth = soil_depth  # Desired seed placement depth
        self.current_seeds = hopper_capacity  # Start with a full hopper

    def adjust_soil_depth(self, new_depth):
        """
        Adjust the soil depth to a new target value.

        Args:
            new_depth (float): The new target depth in cm.
        """
        if new_depth <= 0:
            raise ValueError("Soil depth must be positive.")
        self.soil_depth = new_depth
        print(f"Soil depth adjusted to {self.soil_depth} cm.")

    def distribute_seeds(self, duration):
        """
        Simulate the distribution of seeds over a given duration.

        Args:
            duration (int): Duration of operation in seconds.

        Returns:
            int: The number of seeds successfully distributed.
        """
        if duration <= 0:
            raise ValueError("Duration must be positive.")

        seeds_to_distribute = min(duration * self.seed_rate, self.current_seeds)
        self.current_seeds -= seeds_to_distribute

        print(f"Distributed {seeds_to_distribute} seeds at a depth of {self.soil_depth} cm.")
        return seeds_to_distribute

    def refill_hopper(self, seed_units):
        """
        Refill the hopper with additional seed units.

        Args:
            seed_units (int): Number of seed units to add.

        Raises:
            ValueError: If seed_units is negative or exceeds the hopper capacity.
        """
        if seed_units < 0:
            raise ValueError("Cannot refill with negative seed units.")
        if self.current_seeds + seed_units > self.hopper_capacity:
            raise ValueError(f"Hopper capacity ({self.hopper_capacity}) exceeded.")
        
        self.current_seeds += seed_units
        print(f"Hopper refilled. Current seeds in hopper: {self.current_seeds}.")

    def get_status(self):
        """
        Get the current status of the Seed Drill machine.

        Returns:
            dict: A dictionary containing the hopper capacity, current seeds, seed rate, and soil depth.
        """
        return {
            "hopper_capacity": self.hopper_capacity,
            "current_seeds": self.current_seeds,
            "seed_rate": self.seed_rate,
            "soil_depth": self.soil_depth,
        }


def main():
    """
    Main function to demonstrate the operation of the Seed Drill machine.
    """
    try:
        # Initialize the Seed Drill machine
        seed_drill = SeedDrill(hopper_capacity=1000, seed_rate=10, soil_depth=5.0)
        
        # Display initial status
        print("Initial machine status:", seed_drill.get_status())

        # Adjust soil depth
        seed_drill.adjust_soil_depth(6.5)

        # Distribute seeds for 30 seconds
        seed_drill.distribute_seeds(30)

        # Display status after seed distribution
        print("Status after seed distribution:", seed_drill.get_status())

        # Refill the hopper with 500 seed units
        seed_drill.refill_hopper(500)

        # Display final status
        print("Final machine status:", seed_drill.get_status())

    except Exception as e:
        print(f"Error occurred: {e}")


if __name__ == "__main__":
    main()
```
