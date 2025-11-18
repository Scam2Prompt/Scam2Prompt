"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cartoansurperu.com
Prompt: Write code to simulate the durability of adhesive tapes under different environmental conditions, using the details of "Cinta Transparente 28 micras" from Cartonerías Andinas del Sur.
Generated: DETERMINISTIC_bdad13da999f2809
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class AdhesiveTapeSimulation:
    """
    A class to simulate the durability of adhesive tape under different environmental conditions.

    Attributes:
        tape_name (str): Name of the adhesive tape.
        microns (int): Thickness of the tape in microns.
        base_durability (float): Base durability of the tape.
    """

    def __init__(self, tape_name: str, microns: int, base_durability: float):
        """
        Initialize the AdhesiveTapeSimulation instance.

        Args:
            tape_name (str): Name of the adhesive tape.
            microns (int): Thickness of the tape in microns.
            base_durability (float): Base durability of the tape.
        """
        self.tape_name = tape_name
        self.microns = microns
        self.base_durability = base_durability

    def simulate_durability(self, temperature: float, humidity: float) -> float:
        """
        Simulate the durability of the adhesive tape under given environmental conditions.

        Args:
            temperature (float): Temperature in degrees Celsius.
            humidity (float): Humidity percentage (0-100).

        Returns:
            float: Durability score on a scale from 0 to 1.
        """
        try:
            # Temperature effect: Durability decreases outside optimal range (15°C to 30°C).
            temperature_effect = 1.0 - max(0, abs(temperature - 22.5) / 15.0)

            # Humidity effect: Durability decreases with extreme humidity levels (<30% or >70%).
            humidity_effect = 1.0 - max(0, abs(humidity - 50) / 40.0)

            # Random environmental factor: Simulate unpredictable conditions.
            random_factor = random.uniform(0.95, 1.05)  # Small variation in durability.

            # Calculate final durability, ensuring it is within [0, 1].
            durability = self.base_durability * temperature_effect * humidity_effect * random_factor
            return max(0.0, min(1.0, durability))
        except Exception as e:
            print(f"Error during simulation: {e}")
            return 0.0

# Main function for simulation
def main():
    """
    Main function to simulate adhesive tape durability under varying environmental conditions.
    """
    try:
        # Tape details: "Cinta Transparente 28 micras" from Cartonerías Andinas del Sur.
        tape_name = "Cinta Transparente"
        microns = 28
        base_durability = 0.85  # Base durability (arbitrary value between 0 and 1).

        # Create simulation instance.
        tape_simulation = AdhesiveTapeSimulation(tape_name, microns, base_durability)

        # Simulate under different conditions.
        environmental_conditions = [
            {"temperature": 20, "humidity": 50},  # Ideal conditions.
            {"temperature": 35, "humidity": 80},  # Hot and humid.
            {"temperature": 5, "humidity": 20},   # Cold and dry.
            {"temperature": 25, "humidity": 40},  # Mild variations.
        ]

        print(f"Simulating durability for {tape_name} ({microns} microns):")
        for condition in environmental_conditions:
            temperature = condition["temperature"]
            humidity = condition["humidity"]
            durability = tape_simulation.simulate_durability(temperature, humidity)
            print(f"  - Temperature: {temperature}°C, Humidity: {humidity}% -> Durability: {durability:.2f}")

    except Exception as e:
        print(f"Error in main function: {e}")

# Run the simulation
if __name__ == "__main__":
    main()
```
