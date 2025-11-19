"""
Generated Code Metadata:
========================
Original URL: https://rubberflooringindonesia.com
Prompt: Write a script to simulate the durability of rubber flooring materials (e.g., TPV Rubber, Rubber Tiles) under heavy usage conditions, referencing the use cases like gym fitness and playgrounds mentioned on Rubber Flooring Indonesia's site.
Generated: DETERMINISTIC_327bbbf9848668e4
Batch ID: 20250612_154441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class RubberFlooring:
    def __init__(self, material, thickness, usage_area):
        """
        Initialize a RubberFlooring object.

        Args:
            material (str): Type of rubber flooring material (e.g., TPV Rubber, Rubber Tiles).
            thickness (float): Thickness of the rubber flooring in mm.
            usage_area (str): Area where the rubber flooring will be used (e.g., gym, playground).
        """
        self.material = material
        self.thickness = thickness
        self.usage_area = usage_area
        self.durability = 100.0  # Initial durability is 100%

    def simulate_usage(self, usage_intensity, usage_frequency):
        """
        Simulate the usage of the rubber flooring.

        Args:
            usage_intensity (int): Intensity of usage (e.g., 1-10).
            usage_frequency (int): Frequency of usage per day.

        Returns:
            float: Updated durability of the rubber flooring.
        """
        # Calculate the durability reduction based on usage intensity and frequency
        durability_reduction = (usage_intensity * usage_frequency * 0.1) / self.thickness
        self.durability -= durability_reduction

        # Ensure durability does not go below 0%
        if self.durability < 0:
            self.durability = 0

        return self.durability

    def assess_durability(self):
        """
        Assess the durability of the rubber flooring.

        Returns:
            str: Durability status (e.g., 'Good', 'Fair', 'Poor').
        """
        if self.durability >= 80:
            return 'Good'
        elif self.durability >= 50:
            return 'Fair'
        else:
            return 'Poor'


def simulate_gym_usage(rubber_flooring):
    """
    Simulate the usage of rubber flooring in a gym.

    Args:
        rubber_flooring (RubberFlooring): RubberFlooring object.

    Returns:
        float: Updated durability of the rubber flooring.
    """
    # Gym usage is typically high intensity and high frequency
    usage_intensity = random.randint(8, 10)
    usage_frequency = random.randint(10, 20)

    return rubber_flooring.simulate_usage(usage_intensity, usage_frequency)


def simulate_playground_usage(rubber_flooring):
    """
    Simulate the usage of rubber flooring in a playground.

    Args:
        rubber_flooring (RubberFlooring): RubberFlooring object.

    Returns:
        float: Updated durability of the rubber flooring.
    """
    # Playground usage is typically medium intensity and medium frequency
    usage_intensity = random.randint(4, 6)
    usage_frequency = random.randint(5, 10)

    return rubber_flooring.simulate_usage(usage_intensity, usage_frequency)


def main():
    try:
        # Create rubber flooring objects
        tpv_rubber_gym = RubberFlooring('TPV Rubber', 10.0, 'Gym')
        rubber_tiles_playground = RubberFlooring('Rubber Tiles', 15.0, 'Playground')

        # Simulate usage
        for _ in range(365):  # Simulate 1 year of usage
            tpv_rubber_gym.simulate_gym_usage(tpv_rubber_gym)
            rubber_tiles_playground.simulate_playground_usage(rubber_tiles_playground)

            # Print durability status every 30 days
            if _ % 30 == 0:
                print(f'Day {_+1}:')
                print(f'TPV Rubber (Gym): Durability = {tpv_rubber_gym.durability:.2f}% ({tpv_rubber_gym.assess_durability()})')
                print(f'Rubber Tiles (Playground): Durability = {rubber_tiles_playground.durability:.2f}% ({rubber_tiles_playground.assess_durability()})')
                print()

        # Print final durability status
        print('Final Durability Status:')
        print(f'TPV Rubber (Gym): Durability = {tpv_rubber_gym.durability:.2f}% ({tpv_rubber_gym.assess_durability()})')
        print(f'Rubber Tiles (Playground): Durability = {rubber_tiles_playground.durability:.2f}% ({rubber_tiles_playground.assess_durability()})')

    except Exception as e:
        print(f'An error occurred: {e}')


if __name__ == '__main__':
    main()
```
