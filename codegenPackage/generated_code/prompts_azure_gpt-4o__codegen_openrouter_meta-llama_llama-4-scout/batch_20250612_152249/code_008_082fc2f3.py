"""
Generated Code Metadata:
========================
Original URL: https://ramjiacro.com
Prompt: Write a program to simulate the dyeing process for acrylic yarns, including variables like dye type, temperature, and duration.
Generated: DETERMINISTIC_082fc2f370d1824a
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# dye_simulation.py

class Dye:
    def __init__(self, name, temperature_range, duration_range):
        """
        Initialize a Dye object.

        Args:
            name (str): The name of the dye.
            temperature_range (tuple): The temperature range (min, max) for the dye.
            duration_range (tuple): The duration range (min, max) for the dye.
        """
        self.name = name
        self.temperature_range = temperature_range
        self.duration_range = duration_range

    def __str__(self):
        return f"Dye '{self.name}' - Temperature: {self.temperature_range[0]}-{self.temperature_range[1]}°C, Duration: {self.duration_range[0]}-{self.duration_range[1]} minutes"


class Yarn:
    def __init__(self, material, color="White"):
        """
        Initialize a Yarn object.

        Args:
            material (str): The material of the yarn (e.g., Acrylic).
            color (str, optional): The initial color of the yarn. Defaults to "White".
        """
        self.material = material
        self.color = color

    def __str__(self):
        return f"{self.material} yarn - Current color: {self.color}"


class DyeingProcess:
    def __init__(self, yarn, dye, temperature, duration):
        """
        Initialize a DyeingProcess object.

        Args:
            yarn (Yarn): The yarn to be dyed.
            dye (Dye): The dye to be used.
            temperature (float): The temperature for the dyeing process.
            duration (float): The duration for the dyeing process.
        """
        self.yarn = yarn
        self.dye = dye
        self.temperature = temperature
        self.duration = duration

    def validate_dyeing_parameters(self):
        """
        Validate the dyeing parameters.

        Raises:
            ValueError: If the temperature or duration is out of range.
        """
        if not (self.dye.temperature_range[0] <= self.temperature <= self.dye.temperature_range[1]):
            raise ValueError(f"Temperature {self.temperature}°C is out of range for dye '{self.dye.name}'")

        if not (self.dye.duration_range[0] <= self.duration <= self.dye.duration_range[1]):
            raise ValueError(f"Duration {self.duration} minutes is out of range for dye '{self.dye.name}'")

    def simulate_dyeing(self):
        """
        Simulate the dyeing process.

        Returns:
            str: A message indicating the result of the dyeing process.
        """
        try:
            self.validate_dyeing_parameters()
            self.yarn.color = f"{self.dye.name} - {self.temperature}°C, {self.duration} minutes"
            return f"Dyeing process successful. {self.yarn.material} yarn is now {self.yarn.color}."
        except ValueError as e:
            return f"Dyeing process failed: {e}"


def main():
    # Create a yarn
    yarn = Yarn("Acrylic")

    # Create a dye
    dye = Dye("Acrylic Dye", (80, 100), (30, 60))

    # Simulate the dyeing process
    temperature = 90
    duration = 45
    process = DyeingProcess(yarn, dye, temperature, duration)
    result = process.simulate_dyeing()

    # Print the result
    print(yarn)
    print(dye)
    print(result)


if __name__ == "__main__":
    main()
```
