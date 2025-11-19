"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jobbo.com.au
Prompt: Generate a Python script that simulates the mechanics of a tractor pulling sled based on the specifications provided on Jobbo.com.au.
Generated: DETERMINISTIC_11cfdc425cbe244e
Batch ID: 20250612_155125
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math
import random
import matplotlib.pyplot as plt

class Tractor:
    def __init__(self, name, max_hp, weight, traction_coefficient):
        """
        Initialize a Tractor object.

        :param name: Name of the tractor
        :param max_hp: Maximum horsepower of the tractor
        :param weight: Weight of the tractor in kg
        :param traction_coefficient: Traction coefficient for the tractor
        """
        self.name = name
        self.max_hp = max_hp
        self.weight = weight
        self.traction_coefficient = traction_coefficient
        self.speed = 0

    def calculate_force(self):
        """
        Calculate the force exerted by the tractor based on its horsepower.

        :return: Force in Newtons
        """
        return self.max_hp * 745.7  # 1 HP = 745.7 Watts

    def accelerate(self, throttle):
        """
        Accelerate the tractor based on throttle input.

        :param throttle: Throttle input as a percentage (0 to 100)
        """
        if not (0 <= throttle <= 100):
            raise ValueError("Throttle must be between 0 and 100.")

        # Calculate acceleration based on throttle and traction
        force = self.calculate_force() * (throttle / 100)
        acceleration = force / self.weight
        self.speed += acceleration
        self.speed = max(0, self.speed)  # Ensure speed doesn't go negative

    def get_speed(self):
        """
        Get the current speed of the tractor.

        :return: Speed in m/s
        """
        return self.speed


class Sled:
    def __init__(self, name, weight):
        """
        Initialize a Sled object.

        :param name: Name of the sled
        :param weight: Weight of the sled in kg
        """
        self.name = name
        self.weight = weight
        self.distance = 0

    def move(self, force):
        """
        Move the sled based on the force applied.

        :param force: Force applied to the sled in Newtons
        """
        if force <= 0:
            raise ValueError("Force must be greater than 0.")

        acceleration = force / self.weight
        self.distance += acceleration  # Increment distance based on acceleration


def simulate_pulling(tractor, sled, pulls):
    """
    Simulate the tractor pulling the sled for a given number of pulls.

    :param tractor: The Tractor object
    :param sled: The Sled object
    :param pulls: Number of pulls to simulate
    """
    distances = []
    for i in range(pulls):
        try:
            # Randomize throttle input for simulation purposes
            throttle = random.randint(0, 100)
            tractor.accelerate(throttle)

            # Calculate total force considering traction
            force = tractor.calculate_force() * tractor.traction_coefficient

            # Move the sled
            sled.move(force)

            # Log the distance pulled and tractor speed
            distances.append(sled.distance)
            print(f"Pull {i + 1}: Tractor Speed = {tractor.get_speed():.2f} m/s, Sled Distance = {sled.distance:.2f} m")

        except Exception as e:
            print(f"Error occurred during pull {i + 1}: {e}")

    return distances


if __name__ == "__main__":
    # Create instances of Tractor and Sled
    tractor = Tractor(name="Super Trac", max_hp=200, weight=5000, traction_coefficient=0.6)
    sled = Sled(name="Heavy Sled", weight=3000)

    # Simulate pulling
    total_pulls = 10
    distances = simulate_pulling(tractor, sled, total_pulls)

    # Plotting the results
    plt.plot(range(1, total_pulls + 1), distances)
    plt.title("Sled Distance Pulled by Tractor")
    plt.xlabel("Pull Number")
    plt.ylabel("Distance (m)")
    plt.grid()
    plt.show()
```
