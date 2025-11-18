"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stellarcropgame.fun
Prompt: Create a Python program to simulate the "Yerçekimsiz Deneyler" in Stellar Crop, modeling crop growth in zero-gravity conditions with adjustable parameters for environmental factors.
Generated: DETERMINISTIC_465debd28bd1ffeb
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

class ZeroGravityCropGrowthSimulator:
    """
    Simulates crop growth in a zero-gravity environment with adjustable environmental factors.
    """

    def __init__(self, crop_type, initial_health=100, growth_rate=1.0, water_level=50, light_level=50):
        """
        Initialize the crop simulator.

        :param crop_type: String, the type of crop being simulated (e.g., "Wheat", "Corn").
        :param initial_health: Integer, initial health of the crop (default is 100).
        :param growth_rate: Float, rate at which the crop grows (default is 1.0).
        :param water_level: Integer, initial water level (default is 50).
        :param light_level: Integer, initial light level (default is 50).
        """
        self.crop_type = crop_type
        self.health = initial_health
        self.growth_rate = growth_rate
        self.water_level = water_level
        self.light_level = light_level
        self.growth_stage = 0  # Represents the stage of crop growth, starts at 0
        self.is_alive = True  # Indicates whether the crop is alive

    def adjust_environment(self, water_change=0, light_change=0):
        """
        Adjust the environmental parameters: water and light levels.

        :param water_change: Integer, change to water level (can be positive or negative).
        :param light_change: Integer, change to light level (can be positive or negative).
        """
        self.water_level += water_change
        self.light_level += light_change
        self.water_level = max(0, min(100, self.water_level))  # Ensure water level stays within bounds
        self.light_level = max(0, min(100, self.light_level))  # Ensure light level stays within bounds

    def simulate_growth(self):
        """
        Simulate one cycle of crop growth in zero-gravity conditions.
        """
        if not self.is_alive:
            print(f"The {self.crop_type} crop has died.")
            return

        # Random environmental effects in zero-gravity
        random_effect = random.uniform(-0.1, 0.1)
        self.growth_rate += random_effect
        self.growth_rate = max(0.1, min(2.0, self.growth_rate))  # Keep growth rate within reasonable bounds

        # Adjust crop health based on environmental conditions
        if self.water_level < 30 or self.light_level < 30:
            self.health -= 10  # Decrease health if water/light levels are insufficient
        elif self.water_level > 70 or self.light_level > 70:
            self.health += 5  # Slightly increase health if water/light levels are optimal

        # Crop health cannot exceed 100 or fall below 0
        self.health = max(0, min(100, self.health))

        # Check if the crop is alive
        if self.health <= 0:
            self.is_alive = False
            print(f"The {self.crop_type} crop has died.")
            return

        # Update growth stage based on health and growth rate
        self.growth_stage += self.growth_rate * (self.health / 100.0)
        print(f"{self.crop_type} Growth Stage: {self.growth_stage:.1f}, Health: {self.health}, Water: {self.water_level}, Light: {self.light_level}")

    def get_status(self):
        """
        Get the current status of the crop.
        
        :return: Dictionary containing crop status.
        """
        return {
            "Crop Type": self.crop_type,
            "Health": self.health,
            "Growth Stage": self.growth_stage,
            "Water Level": self.water_level,
            "Light Level": self.light_level,
            "Alive": self.is_alive
        }


if __name__ == "__main__":
    # Example usage of the simulator
    crop = ZeroGravityCropGrowthSimulator(crop_type="Stellar Wheat", growth_rate=1.2)

    # Simulate multiple cycles of growth
    for day in range(1, 11):  # Simulate 10 days
        print(f"Day {day}")
        crop.simulate_growth()
        crop.adjust_environment(water_change=random.randint(-5, 5), light_change=random.randint(-5, 5))

    # Final status of the crop
    status = crop.get_status()
    print("\nFinal Crop Status:")
    for key, value in status.items():
        print(f"{key}: {value}")
```
