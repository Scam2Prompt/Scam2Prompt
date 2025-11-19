"""
Generated Code Metadata:
========================
Original URL: https://tromba-sa.com.ar
Prompt: Write a script to simulate the operation of plastic manual pumps for bulk containers, inspired by the M200/55 product line from TROMBA.
Generated: DETERMINISTIC_c6ed7b2b19a498f4
Batch ID: 20250612_151434
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# plastic_pump_simulator.py

class PlasticManualPump:
    """
    Simulates the operation of plastic manual pumps for bulk containers.

    Attributes:
        container_volume (float): The volume of the bulk container in liters.
        pump_capacity (float): The volume of liquid pumped per stroke in liters.
        strokes (int): The number of pump strokes performed.
        current_volume (float): The current volume of liquid in the container.
    """

    def __init__(self, container_volume, pump_capacity):
        """
        Initializes a PlasticManualPump instance.

        Args:
            container_volume (float): The volume of the bulk container in liters.
            pump_capacity (float): The volume of liquid pumped per stroke in liters.

        Raises:
            ValueError: If container_volume or pump_capacity is not a positive number.
        """
        if container_volume <= 0 or pump_capacity <= 0:
            raise ValueError("Container volume and pump capacity must be positive numbers.")

        self.container_volume = container_volume
        self.pump_capacity = pump_capacity
        self.strokes = 0
        self.current_volume = 0.0

    def pump(self):
        """
        Simulates a single pump stroke.

        Returns:
            float: The new current volume of liquid in the container.

        Raises:
            RuntimeError: If the container is already full.
        """
        if self.current_volume >= self.container_volume:
            raise RuntimeError("Container is already full.")

        self.strokes += 1
        self.current_volume = min(self.current_volume + self.pump_capacity, self.container_volume)
        return self.current_volume

    def drain(self):
        """
        Simulates draining the container.

        Returns:
            float: The volume of liquid drained from the container.

        Raises:
            RuntimeError: If the container is already empty.
        """
        if self.current_volume <= 0:
            raise RuntimeError("Container is already empty.")

        drained_volume = self.current_volume
        self.current_volume = 0.0
        return drained_volume

    def get_status(self):
        """
        Returns the current status of the pump and container.

        Returns:
            dict: A dictionary containing the current volume, container volume, pump capacity, and number of strokes.
        """
        return {
            "current_volume": self.current_volume,
            "container_volume": self.container_volume,
            "pump_capacity": self.pump_capacity,
            "strokes": self.strokes,
        }


def main():
    try:
        # Create a PlasticManualPump instance with a 55-gallon container and 1 liter pump capacity
        pump = PlasticManualPump(container_volume=208.2, pump_capacity=1.0)

        # Pump liquid into the container
        print("Pumping liquid into the container:")
        for _ in range(100):
            current_volume = pump.pump()
            print(f"Stroke {_+1}: {current_volume:.2f} liters")

        # Get the current status of the pump and container
        status = pump.get_status()
        print("\nCurrent Status:")
        print(f"Current Volume: {status['current_volume']:.2f} liters")
        print(f"Container Volume: {status['container_volume']:.2f} liters")
        print(f"Pump Capacity: {status['pump_capacity']:.2f} liters")
        print(f"Number of Strokes: {status['strokes']}")

        # Drain the container
        print("\nDraining the container:")
        drained_volume = pump.drain()
        print(f"Drained Volume: {drained_volume:.2f} liters")

    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
```
