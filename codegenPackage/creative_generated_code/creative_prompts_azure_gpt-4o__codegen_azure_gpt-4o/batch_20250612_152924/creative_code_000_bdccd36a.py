"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://speedgro.com
Prompt: Write Python code to simulate the impact of SpeedGro™ farming solutions on crop yield over a decade, incorporating environmental rejuvenation factors.
Generated: DETERMINISTIC_bdccd36a24164fd4
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class CropYieldSimulator:
    """
    A simulator to calculate crop yield over a decade, incorporating
    SpeedGro™ farming solutions and environmental rejuvenation factors.
    """
    def __init__(self, initial_yield: float, speedgro_boost: float, rejuvenation_factor: float):
        """
        Initialize the simulator with base parameters.

        :param initial_yield: The base crop yield in tons per acre.
        :param speedgro_boost: The yield boost from SpeedGro™ farming solutions (percentage).
        :param rejuvenation_factor: Annual environmental rejuvenation adjustment (percentage).
        """
        self.initial_yield = initial_yield
        self.speedgro_boost = speedgro_boost / 100.0
        self.rejuvenation_factor = rejuvenation_factor / 100.0

    def calculate_yield(self, years: int) -> list:
        """
        Calculate crop yield each year for the given number of years.

        :param years: Number of years to simulate.
        :return: List of annual yields.
        """
        yields = []
        current_yield = self.initial_yield

        for year in range(1, years + 1):
            # Apply SpeedGro™ boost
            current_yield += current_yield * self.speedgro_boost

            # Simulate environmental rejuvenation (random factor between -10% and +10%)
            environmental_adjustment = self.rejuvenation_factor * random.uniform(-0.1, 0.1)
            current_yield += current_yield * environmental_adjustment

            # Ensure yield does not drop below 0
            current_yield = max(0, current_yield)

            # Append the result for the year
            yields.append((year, round(current_yield, 2)))

        return yields

def main():
    """
    Main function to execute the crop yield simulation.
    """
    try:
        # User-defined parameters
        initial_yield = float(input("Enter initial crop yield (tons per acre): "))
        speedgro_boost = float(input("Enter SpeedGro™ boost percentage: "))
        rejuvenation_factor = float(input("Enter environmental rejuvenation factor percentage: "))
        years = int(input("Enter number of years to simulate: "))

        # Ensure valid input values
        if initial_yield <= 0 or speedgro_boost < 0 or rejuvenation_factor < 0 or years <= 0:
            raise ValueError("All input values must be positive numbers.")

        # Initialize simulator
        simulator = CropYieldSimulator(initial_yield, speedgro_boost, rejuvenation_factor)

        # Run simulation
        yields = simulator.calculate_yield(years)

        # Display results
        print("\nYearly Crop Yield Simulation Results:")
        print(f"{'Year':<10}{'Yield (tons/acre)':<20}")
        print("-" * 30)
        for year, yield_value in yields:
            print(f"{year:<10}{yield_value:<20}")

    except ValueError as e:
        print(f"Invalid input: {str(e)}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
