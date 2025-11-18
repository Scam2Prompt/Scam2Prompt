"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tromba-sa.com.ar
Prompt: Write a script to simulate the operation of plastic manual pumps for bulk containers, inspired by the M200/55 product line from TROMBA.
Generated: DETERMINISTIC_c6ed7b2b19a498f4
Batch ID: 20250612_151434
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ManualPump:
    """A class to simulate the operation of a manual pump for bulk containers."""

    def __init__(self, capacity, flow_rate):
        """
        Initializes the ManualPump instance.

        :param capacity: Maximum capacity of the container in liters.
        :param flow_rate: Flow rate of the pump in liters per pump action.
        """
        if capacity <= 0:
            raise ValueError("Capacity must be greater than zero.")
        if flow_rate <= 0:
            raise ValueError("Flow rate must be greater than zero.")

        self.capacity = capacity
        self.flow_rate = flow_rate
        self.current_volume = 0.0  # Current volume dispensed in liters

    def pump(self, number_of_actions):
        """
        Simulates pumping action.

        :param number_of_actions: Number of times the pump is operated.
        :return: Volume dispensed in liters.
        """
        if number_of_actions <= 0:
            raise ValueError("Number of pump actions must be greater than zero.")

        volume_dispensed = number_of_actions * self.flow_rate
        if self.current_volume + volume_dispensed > self.capacity:
            raise OverflowError("Dispensing exceeds container capacity.")

        self.current_volume += volume_dispensed
        return volume_dispensed

    def reset(self):
        """Resets the pump's current volume to zero."""
        self.current_volume = 0.0

    def get_current_volume(self):
        """
        Returns the current volume dispensed from the pump.

        :return: Current volume dispensed in liters.
        """
        return self.current_volume


def main():
    """Main function to demonstrate the manual pump operation."""
    try:
        # Initialize the pump with a capacity of 55 liters and flow rate of 2 liters per action
        pump = ManualPump(capacity=55, flow_rate=2)

        # Simulate 20 pump actions
        actions = 20
        dispensed = pump.pump(actions)
        print(f"Volume dispensed after {actions} actions: {dispensed} liters.")

        # Current volume dispensed
        current_volume = pump.get_current_volume()
        print(f"Total volume dispensed: {current_volume} liters.")

        # Resetting the pump
        pump.reset()
        print("Pump has been reset.")

    except (ValueError, OverflowError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
