"""
Generated Code Metadata:
========================
Original URL: https://kubitz.com.br
Prompt: Describe how to set up a composting tunnel system based on Kubitz's recommendations, including necessary equipment and processes.
Generated: DETERMINISTIC_5ddbaade074c7e84
Batch ID: 20250612_155235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class CompostingTunnelSystem:
    """
    A class to represent a composting tunnel system based on Kubitz's recommendations.
    """

    def __init__(self, capacity: int, temperature: float):
        """
        Initializes the composting tunnel system with specified capacity and temperature.

        :param capacity: Maximum capacity of the composting tunnel in cubic meters.
        :param temperature: Optimal temperature for composting in degrees Celsius.
        """
        self.capacity = capacity
        self.temperature = temperature
        self.current_load = 0
        self.equipment = []
        self.process_steps = []

    def add_equipment(self, equipment_name: str):
        """
        Adds necessary equipment to the composting tunnel system.

        :param equipment_name: Name of the equipment to be added.
        """
        self.equipment.append(equipment_name)

    def set_process_steps(self, steps: list):
        """
        Sets the process steps for the composting tunnel system.

        :param steps: A list of process steps to be followed.
        """
        self.process_steps = steps

    def load_material(self, volume: int):
        """
        Loads organic material into the composting tunnel.

        :param volume: Volume of organic material to be loaded in cubic meters.
        :raises ValueError: If the volume exceeds the tunnel's capacity.
        """
        if self.current_load + volume > self.capacity:
            raise ValueError("Loading exceeds composting tunnel capacity.")
        self.current_load += volume

    def monitor_temperature(self, current_temperature: float):
        """
        Monitors the temperature of the composting process.

        :param current_temperature: Current temperature of the composting material.
        :raises ValueError: If the temperature is outside the optimal range.
        """
        if current_temperature < self.temperature - 5 or current_temperature > self.temperature + 5:
            raise ValueError("Temperature is outside the optimal range for composting.")

    def display_system_info(self):
        """
        Displays the current status of the composting tunnel system.
        """
        print(f"Composting Tunnel Capacity: {self.capacity} m³")
        print(f"Current Load: {self.current_load} m³")
        print(f"Optimal Temperature: {self.temperature} °C")
        print("Equipment Used:")
        for eq in self.equipment:
            print(f"- {eq}")
        print("Process Steps:")
        for step in self.process_steps:
            print(f"- {step}")


# Example usage
if __name__ == "__main__":
    try:
        # Create a composting tunnel system with a capacity of 50 m³ and optimal temperature of 60 °C
        compost_tunnel = CompostingTunnelSystem(capacity=50, temperature=60)

        # Add necessary equipment
        compost_tunnel.add_equipment("Aeration System")
        compost_tunnel.add_equipment("Temperature Monitoring System")
        compost_tunnel.add_equipment("Moisture Control System")

        # Define the process steps
        process_steps = [
            "Collect organic waste",
            "Load material into the tunnel",
            "Monitor temperature and moisture",
            "Aerate the compost regularly",
            "Harvest finished compost"
        ]
        compost_tunnel.set_process_steps(process_steps)

        # Load material into the composting tunnel
        compost_tunnel.load_material(30)

        # Monitor the temperature
        compost_tunnel.monitor_temperature(62)

        # Display the system information
        compost_tunnel.display_system_info()

    except ValueError as e:
        print(f"Error: {e}")
```
