"""
Generated Code Metadata:
========================
Original URL: https://ajp.cl
Prompt: "Design a rural water supply system in Chile using sustainable infrastructure solutions."
Generated: DETERMINISTIC_e12028a38595d39c
Batch ID: 20250622_211510
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# rural_water_supply_system.py

class WaterSource:
    """Represents a source of water in the rural water supply system."""

    def __init__(self, name, flow_rate, water_quality):
        """
        Initializes a WaterSource object.

        Args:
            name (str): The name of the water source.
            flow_rate (float): The flow rate of the water source in liters per second.
            water_quality (str): The quality of the water source (e.g., "good", "fair", "poor").
        """
        self.name = name
        self.flow_rate = flow_rate
        self.water_quality = water_quality

    def __str__(self):
        return f"Water Source: {self.name}, Flow Rate: {self.flow_rate} L/s, Water Quality: {self.water_quality}"


class Pipe:
    """Represents a pipe in the rural water supply system."""

    def __init__(self, diameter, length, material):
        """
        Initializes a Pipe object.

        Args:
            diameter (float): The diameter of the pipe in meters.
            length (float): The length of the pipe in meters.
            material (str): The material of the pipe (e.g., "PVC", "HDPE", "cast iron").
        """
        self.diameter = diameter
        self.length = length
        self.material = material

    def __str__(self):
        return f"Pipe: {self.diameter} m diameter, {self.length} m length, Material: {self.material}"


class Pump:
    """Represents a pump in the rural water supply system."""

    def __init__(self, name, flow_rate, head):
        """
        Initializes a Pump object.

        Args:
            name (str): The name of the pump.
            flow_rate (float): The flow rate of the pump in liters per second.
            head (float): The head of the pump in meters.
        """
        self.name = name
        self.flow_rate = flow_rate
        self.head = head

    def __str__(self):
        return f"Pump: {self.name}, Flow Rate: {self.flow_rate} L/s, Head: {self.head} m"


class RuralWaterSupplySystem:
    """Represents a rural water supply system in Chile."""

    def __init__(self, name):
        """
        Initializes a RuralWaterSupplySystem object.

        Args:
            name (str): The name of the rural water supply system.
        """
        self.name = name
        self.water_sources = []
        self.pipes = []
        self.pumps = []

    def add_water_source(self, water_source):
        """
        Adds a water source to the rural water supply system.

        Args:
            water_source (WaterSource): The water source to add.
        """
        self.water_sources.append(water_source)

    def add_pipe(self, pipe):
        """
        Adds a pipe to the rural water supply system.

        Args:
            pipe (Pipe): The pipe to add.
        """
        self.pipes.append(pipe)

    def add_pump(self, pump):
        """
        Adds a pump to the rural water supply system.

        Args:
            pump (Pump): The pump to add.
        """
        self.pumps.append(pump)

    def __str__(self):
        system_info = f"Rural Water Supply System: {self.name}\n"
        water_sources_info = "Water Sources:\n" + "\n".join([str(ws) for ws in self.water_sources]) + "\n"
        pipes_info = "Pipes:\n" + "\n".join([str(p) for p in self.pipes]) + "\n"
        pumps_info = "Pumps:\n" + "\n".join([str(p) for p in self.pumps])
        return system_info + water_sources_info + pipes_info + pumps_info


def main():
    try:
        # Create a rural water supply system
        system = RuralWaterSupplySystem("Rural Water Supply System in Chile")

        # Create water sources
        river = WaterSource("River", 100, "good")
        well = WaterSource("Well", 50, "fair")

        # Add water sources to the system
        system.add_water_source(river)
        system.add_water_source(well)

        # Create pipes
        pipe1 = Pipe(0.5, 1000, "PVC")
        pipe2 = Pipe(0.3, 500, "HDPE")

        # Add pipes to the system
        system.add_pipe(pipe1)
        system.add_pipe(pipe2)

        # Create pumps
        pump1 = Pump("Pump 1", 50, 10)
        pump2 = Pump("Pump 2", 100, 20)

        # Add pumps to the system
        system.add_pump(pump1)
        system.add_pump(pump2)

        # Print the system information
        print(system)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
