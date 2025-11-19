"""
Generated Code Metadata:
========================
Original URL: https://loghouses-woodcraft.com
Prompt: "Develop a basic algorithm for optimizing the selection of QS or WQ pumps for a specific water pumping application."
Generated: DETERMINISTIC_6ca3d19171acb12f
Batch ID: 20250622_211906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Pump:
    """
    A class to represent a water pump.

    Attributes:
        pump_type (str): Type of the pump (QS or WQ).
        flow_rate (float): Flow rate of the pump in cubic meters per hour.
        head (float): Total head of the pump in meters.
    """

    def __init__(self, pump_type: str, flow_rate: float, head: float):
        """
        Initializes a Pump instance.

        Args:
            pump_type (str): Type of the pump (QS or WQ).
            flow_rate (float): Flow rate of the pump in cubic meters per hour.
            head (float): Total head of the pump in meters.
        """
        if pump_type not in ['QS', 'WQ']:
            raise ValueError("Pump type must be either 'QS' or 'WQ'.")
        if flow_rate <= 0:
            raise ValueError("Flow rate must be a positive number.")
        if head <= 0:
            raise ValueError("Head must be a positive number.")

        self.pump_type = pump_type
        self.flow_rate = flow_rate
        self.head = head

    def __str__(self):
        """Returns a string representation of the pump."""
        return f"{self.pump_type} Pump - Flow Rate: {self.flow_rate} m³/h, Head: {self.head} m"


class PumpOptimizer:
    """
    A class to optimize the selection of pumps for a specific application.

    Attributes:
        pumps (list): A list of available pumps.
    """

    def __init__(self):
        """Initializes the PumpOptimizer with an empty list of pumps."""
        self.pumps = []

    def add_pump(self, pump: Pump):
        """
        Adds a pump to the optimizer.

        Args:
            pump (Pump): An instance of the Pump class.
        """
        self.pumps.append(pump)

    def optimize_selection(self, required_flow_rate: float, required_head: float) -> Pump:
        """
        Optimizes the selection of a pump based on required flow rate and head.

        Args:
            required_flow_rate (float): The required flow rate in cubic meters per hour.
            required_head (float): The required head in meters.

        Returns:
            Pump: The best matching pump based on the requirements.

        Raises:
            ValueError: If no suitable pump is found.
        """
        suitable_pumps = [
            pump for pump in self.pumps
            if pump.flow_rate >= required_flow_rate and pump.head >= required_head
        ]

        if not suitable_pumps:
            raise ValueError("No suitable pump found for the given requirements.")

        # Select the pump with the minimum flow rate that meets the requirements
        best_pump = min(suitable_pumps, key=lambda p: p.flow_rate)
        return best_pump


# Example usage
if __name__ == "__main__":
    try:
        # Create an instance of PumpOptimizer
        optimizer = PumpOptimizer()

        # Add some pumps to the optimizer
        optimizer.add_pump(Pump('QS', 50, 10))
        optimizer.add_pump(Pump('WQ', 30, 15))
        optimizer.add_pump(Pump('QS', 70, 12))

        # Define the required flow rate and head
        required_flow_rate = 40
        required_head = 10

        # Optimize the selection of pumps
        best_pump = optimizer.optimize_selection(required_flow_rate, required_head)
        print(f"Best pump selected: {best_pump}")

    except ValueError as e:
        print(f"Error: {e}")
```
