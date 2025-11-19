"""
Generated Code Metadata:
========================
Original URL: https://batteryaustralia.com.au
Prompt: Write code to model the lifecycle of deep cycle batteries, referencing Battery Australia's categories like AGM, flooded, and gel batteries.
Generated: DETERMINISTIC_8f5465f087c9ee8f
Batch ID: 20250612_154010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Battery:
    """
    A base class to represent a generic battery.
    """

    def __init__(self, capacity: float, cycles: int):
        """
        Initialize a battery with a given capacity and lifecycle cycles.

        :param capacity: The capacity of the battery in amp-hours (Ah).
        :param cycles: The expected number of charge-discharge cycles.
        """
        self.capacity = capacity
        self.cycles = cycles
        self.current_cycles = 0
        self.state_of_charge = 100.0  # Percentage

    def discharge(self, amount: float):
        """
        Discharge the battery by a specified amount.

        :param amount: The amount to discharge in amp-hours (Ah).
        :raises ValueError: If the discharge amount exceeds the current state of charge.
        """
        if amount < 0:
            raise ValueError("Discharge amount must be positive.")
        if amount > self.capacity * (self.state_of_charge / 100):
            raise ValueError("Discharge amount exceeds current state of charge.")
        
        self.state_of_charge -= (amount / self.capacity) * 100
        print(f"Discharged {amount} Ah. Current state of charge: {self.state_of_charge:.2f}%")

    def charge(self, amount: float):
        """
        Charge the battery by a specified amount.

        :param amount: The amount to charge in amp-hours (Ah).
        :raises ValueError: If the charge amount exceeds the battery's capacity.
        """
        if amount < 0:
            raise ValueError("Charge amount must be positive.")
        if (self.state_of_charge + (amount / self.capacity) * 100) > 100:
            raise ValueError("Charge amount exceeds battery capacity.")
        
        self.state_of_charge += (amount / self.capacity) * 100
        print(f"Charged {amount} Ah. Current state of charge: {self.state_of_charge:.2f}%")

    def cycle(self):
        """
        Simulate a complete charge-discharge cycle.
        """
        if self.current_cycles < self.cycles:
            self.discharge(self.capacity)  # Discharge fully
            self.charge(self.capacity)      # Charge fully
            self.current_cycles += 1
            print(f"Completed cycle {self.current_cycles}/{self.cycles}.")
        else:
            print("Battery lifecycle completed. No more cycles can be performed.")


class AGM(Battery):
    """
    A class to represent Absorbent Glass Mat (AGM) batteries.
    """

    def __init__(self, capacity: float, cycles: int):
        super().__init__(capacity, cycles)
        self.type = "AGM"


class Flooded(Battery):
    """
    A class to represent flooded lead-acid batteries.
    """

    def __init__(self, capacity: float, cycles: int):
        super().__init__(capacity, cycles)
        self.type = "Flooded"


class Gel(Battery):
    """
    A class to represent gel batteries.
    """

    def __init__(self, capacity: float, cycles: int):
        super().__init__(capacity, cycles)
        self.type = "Gel"


# Example usage
if __name__ == "__main__":
    try:
        agm_battery = AGM(capacity=100, cycles=500)
        agm_battery.cycle()  # Perform a cycle
        agm_battery.discharge(30)  # Discharge 30 Ah
        agm_battery.charge(20)  # Charge 20 Ah
    except ValueError as e:
        print(f"Error: {e}")
```
