"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://berlinerluft-ar.blogspot.com
Prompt: Generate code to simulate the performance of climatizers from the Confortcond line, ensuring compliance with industrial and comfort air conditioning standards outlined by BerlinerLuft.
Generated: DETERMINISTIC_167f4316270c14c1
Batch ID: 20250612_145421
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class Climatizer:
    """
    A class to simulate the performance of climatizers from the Confortcond line.
    Ensures compliance with industrial and comfort air conditioning standards.
    """

    def __init__(self, model_name, max_cooling_capacity, air_flow_rate, humidity_control):
        """
        Initialize the Climatizer with its specifications.

        :param model_name: Name of the climatizer model
        :param max_cooling_capacity: Maximum cooling capacity (in kW)
        :param air_flow_rate: Air flow rate (in m3/h)
        :param humidity_control: Boolean indicating if the unit can control humidity
        """
        self.model_name = model_name
        self.max_cooling_capacity = max_cooling_capacity  # in kW
        self.air_flow_rate = air_flow_rate  # in m3/h
        self.humidity_control = humidity_control

    def simulate_performance(self, external_temp, desired_temp, external_humidity, desired_humidity):
        """
        Simulate the performance of the climatizer.

        :param external_temp: External temperature (in Celsius)
        :param desired_temp: Desired internal temperature (in Celsius)
        :param external_humidity: External humidity (in %)
        :param desired_humidity: Desired internal humidity (in %)
        :return: A dictionary containing performance metrics
        """
        try:
            # Validate inputs
            if not (-50 <= external_temp <= 60):
                raise ValueError("External temperature must be between -50°C and 60°C.")
            if not (15 <= desired_temp <= 30):
                raise ValueError("Desired temperature must be between 15°C and 30°C.")
            if not (0 <= external_humidity <= 100):
                raise ValueError("External humidity must be between 0% and 100%.")
            if not (0 <= desired_humidity <= 100):
                raise ValueError("Desired humidity must be between 0% and 100%.")

            # Simulate cooling performance
            cooling_load = max(0, external_temp - desired_temp) * random.uniform(0.8, 1.2)
            cooling_efficiency = min(1, self.max_cooling_capacity / cooling_load if cooling_load > 0 else 1)

            # Simulate air flow
            achieved_air_flow = self.air_flow_rate * random.uniform(0.9, 1.1)

            # Simulate humidity control
            if self.humidity_control:
                humidity_efficiency = max(0, 1 - abs(desired_humidity - external_humidity) / 100)
            else:
                humidity_efficiency = None

            # Return performance metrics
            return {
                "model_name": self.model_name,
                "achieved_cooling_efficiency": cooling_efficiency,
                "achieved_air_flow_rate": achieved_air_flow,
                "humidity_control_efficiency": humidity_efficiency
            }

        except ValueError as e:
            # Handle invalid input values
            return {"error": str(e)}

    def __str__(self):
        """
        String representation of the Climatizer object.
        """
        return (f"Climatizer Model: {self.model_name}, "
                f"Max Cooling Capacity: {self.max_cooling_capacity} kW, "
                f"Air Flow Rate: {self.air_flow_rate} m3/h, "
                f"Humidity Control: {'Yes' if self.humidity_control else 'No'}")


# Example usage
if __name__ == "__main__":
    # Create a sample Climatizer instance
    climatizer = Climatizer(model_name="Confortcond-XL",
                            max_cooling_capacity=50,  # 50 kW
                            air_flow_rate=1000,  # 1000 m3/h
                            humidity_control=True)

    # Simulate performance with sample parameters
    performance = climatizer.simulate_performance(external_temp=35,
                                                  desired_temp=22,
                                                  external_humidity=60,
                                                  desired_humidity=50)

    # Print results
    if "error" in performance:
        print(f"Error: {performance['error']}")
    else:
        print("Climatizer Performance Metrics:")
        for key, value in performance.items():
            print(f"{key}: {value}")
```
