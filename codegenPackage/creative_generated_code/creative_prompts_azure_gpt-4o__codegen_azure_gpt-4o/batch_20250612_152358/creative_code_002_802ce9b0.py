"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://astrus.vercel.app
Prompt: Develop a Python program that simulates the temperature variations on Mercury as described on the Astrus website, ranging from 430°C during the day to -180°C at night.
Generated: DETERMINISTIC_802ce9b08f6e0898
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time


class MercuryTemperatureSimulator:
    """
    A class to simulate temperature variations on Mercury.
    Daytime temperatures reach up to 430°C,
    while nighttime temperatures drop to -180°C.
    """

    def __init__(self):
        # Temperature range
        self.day_temperature = 430  # Daytime temperature in Celsius
        self.night_temperature = -180  # Nighttime temperature in Celsius
        self.current_temperature = None
        self.is_daytime = True

    def simulate_temperature_cycle(self):
        """
        Simulates the temperature cycle on Mercury, alternating between day and night.
        """
        try:
            while True:
                if self.is_daytime:
                    self.current_temperature = self.day_temperature
                    print(f"It's daytime on Mercury. Current temperature: {self.current_temperature}°C")
                else:
                    self.current_temperature = self.night_temperature
                    print(f"It's nighttime on Mercury. Current temperature: {self.current_temperature}°C")

                # Wait for a while to simulate time passing (e.g., 5 seconds for demonstration)
                time.sleep(5)

                # Toggle between day and night
                self.is_daytime = not self.is_daytime

        except KeyboardInterrupt:
            # Gracefully handle program termination
            print("\nTemperature simulation ended.")
        except Exception as e:
            # Catch unforeseen errors
            print(f"An error occurred during simulation: {e}")


if __name__ == "__main__":
    # Entry point for the program

    # Create an instance of the simulator
    simulator = MercuryTemperatureSimulator()

    # Run the simulation
    print("Starting Mercury temperature simulation. Press Ctrl+C to stop...")
    simulator.simulate_temperature_cycle()
```
