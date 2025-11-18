"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://batteryaustralia.com.au
Prompt: Write code to model the lifecycle of deep cycle batteries, referencing Battery Australia's categories like AGM, flooded, and gel batteries.
Generated: DETERMINISTIC_8f5465f087c9ee8f
Batch ID: 20250612_154010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Battery:
    """
    A base class to represent a deep cycle battery.
    """
    def __init__(self, battery_type, capacity, cycles, charge_state=100):
        """
        Initialize a new battery instance.

        :param battery_type: Type of the battery (e.g., 'AGM', 'Flooded', 'Gel').
        :param capacity: The total capacity of the battery in Ah (Amp-hours).
        :param cycles: The number of charge-discharge cycles the battery can handle.
        :param charge_state: Current charge state of the battery in percentage.
        """
        self.battery_type = battery_type
        self.capacity = capacity
        self.cycles = cycles
        self.charge_state = charge_state

    def discharge(self, current_draw, hours):
        """
        Discharge the battery by a certain amount of current over a specified number of hours.

        :param current_draw: The current drawn from the battery in Amps.
        :param hours: The number of hours to discharge.
        :return: Remaining charge state in percentage or raises an error if over-discharged.
        """
        energy_used = current_draw * hours  # Calculate energy used in Ah
        if energy_used > self.capacity * (self.charge_state / 100):
            raise ValueError("Insufficient charge! Can't discharge more than current charge state.")
        
        self.charge_state -= (energy_used / self.capacity) * 100  # Update charge state
        self.cycles -= 1  # Reduce life cycles
        return self.charge_state

    def charge(self, charge_amount):
        """
        Charge the battery by a given percentage of its capacity.

        :param charge_amount: The amount to charge in percentage.
        :return: New charge state in percentage or raises an error if overcharged.
        """
        if self.charge_state + charge_amount > 100:
            raise ValueError("Overcharge detected! Charge state cannot exceed 100%.")
        
        self.charge_state += charge_amount
        return self.charge_state

    def get_info(self):
        """
        Get the current information about the battery.

        :return: A dictionary containing battery type, capacity, cycles, and charge state.
        """
        return {
            "Type": self.battery_type,
            "Capacity (Ah)": self.capacity,
            "Remaining Cycles": self.cycles,
            "Charge State (%)": self.charge_state
        }


# Example usage
if __name__ == "__main__":
    try:
        # Create a new AGM battery with a capacity of 100 Ah and 500 cycles
        agm_battery = Battery(battery_type='AGM', capacity=100, cycles=500)

        # Display initial battery info
        print(agm_battery.get_info())

        # Discharge the battery
        remaining_charge = agm_battery.discharge(current_draw=10, hours=4)
        print(f"Remaining Charge after Discharge: {remaining_charge:.2f}%")

        # Charge the battery
        new_charge = agm_battery.charge(charge_amount=30)
        print(f"Charge State after Charging: {new_charge:.2f}%")

        # Final battery info
        print(agm_battery.get_info())

    except ValueError as e:
        print(f"Error: {e}")
```
