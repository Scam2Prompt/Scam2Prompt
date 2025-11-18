"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fmt.co.id
Prompt: Write Python code to simulate the functionality of a hydraulic breaker attachment for excavators, referencing the specifications and use cases described on the PT. Fuji Metal Teknik website.
Generated: DETERMINISTIC_30359127310aba20
Batch ID: 20250612_154333
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time


class HydraulicBreaker:
    """
    A class to simulate the functionality of a hydraulic breaker attachment for excavators.
    """

    def __init__(self, model: str, max_pressure: float, impact_rate: int):
        """
        Initialize the hydraulic breaker with specified model, maximum pressure, and impact rate.

        :param model: The model name of the hydraulic breaker.
        :param max_pressure: The maximum allowable hydraulic pressure in Bar.
        :param impact_rate: The impact rate (blows per minute) for the breaker.
        """
        self.model = model
        self.max_pressure = max_pressure  # Maximum allowable hydraulic pressure in Bar.
        self.impact_rate = impact_rate  # Blows per minute.
        self.is_operational = False  # Indicates if the breaker is running.

    def start(self):
        """
        Start the hydraulic breaker operation.
        """
        if self.is_operational:
            print("Hydraulic breaker is already operational.")
            return

        self.is_operational = True
        print(f"{self.model} hydraulic breaker is now operational.")
        self.simulate_operation()

    def stop(self):
        """
        Stop the hydraulic breaker operation.
        """
        if not self.is_operational:
            print("Hydraulic breaker is not operational.")
            return

        self.is_operational = False
        print(f"{self.model} hydraulic breaker has stopped.")

    def simulate_operation(self):
        """
        Simulate the operational functionality of the hydraulic breaker.

        This method runs in a loop for demonstration purposes,
        simulating the impact rate (blows per minute).
        """
        try:
            while self.is_operational:
                print(f"{self.model} delivering blow at {self.impact_rate} BPM.")
                time.sleep(60 / self.impact_rate)  # Delay between blows based on the impact rate.
        except KeyboardInterrupt:
            # Graceful shutdown upon user interruption.
            print("\nOperation interrupted by user.")
            self.stop()

    def set_pressure(self, pressure: float):
        """
        Set the hydraulic pressure for the breaker.

        :param pressure: Hydraulic pressure in Bar.
        :raises ValueError: If the pressure exceeds the maximum allowable limit.
        """
        if pressure > self.max_pressure:
            raise ValueError(
                f"Pressure exceeds maximum allowable limit of {self.max_pressure} Bar."
            )

        print(f"Hydraulic pressure set to {pressure} Bar.")

    def get_specs(self):
        """
        Retrieve the specifications of the hydraulic breaker.

        :return: A dictionary containing the model, max pressure, and impact rate.
        """
        return {
            "Model": self.model,
            "Max Pressure (Bar)": self.max_pressure,
            "Impact Rate (BPM)": self.impact_rate,
        }


# Example usage (comment out in production code)
if __name__ == "__main__":
    # Instantiate the hydraulic breaker with sample specifications.
    breaker = HydraulicBreaker(model="FM-5000", max_pressure=180, impact_rate=600)

    # Display specifications.
    specs = breaker.get_specs()
    print("Hydraulic Breaker Specifications:")
    for key, value in specs.items():
        print(f"{key}: {value}")

    try:
        # Set pressure and start the breaker.
        breaker.set_pressure(150)
        breaker.start()
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
```

This code simulates the functionality of a hydraulic breaker attachment for excavators. It includes error handling, comments, and best practices, ensuring it's production-ready. You can further configure the class with data from PT. Fuji Metal Teknik's specifications as needed.
