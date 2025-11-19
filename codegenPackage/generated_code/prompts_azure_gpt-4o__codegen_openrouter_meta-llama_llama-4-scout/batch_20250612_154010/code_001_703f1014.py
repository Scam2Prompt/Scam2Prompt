"""
Generated Code Metadata:
========================
Original URL: https://batteryaustralia.com.au
Prompt: Generate code to simulate battery health testing for lithium-ion batteries, incorporating details about Battery Australia's AC-DC 24V 20A Lithium Battery Charger.
Generated: DETERMINISTIC_703f10144214f353
Batch ID: 20250612_154010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# battery_health_tester.py

class LithiumIonBattery:
    def __init__(self, capacity, max_charge_current, max_discharge_current):
        """
        Initialize a lithium-ion battery.

        Args:
            capacity (float): Battery capacity in Ah.
            max_charge_current (float): Maximum charge current in A.
            max_discharge_current (float): Maximum discharge current in A.
        """
        self.capacity = capacity
        self.max_charge_current = max_charge_current
        self.max_discharge_current = max_discharge_current
        self.state_of_charge = 1.0  # Initialize to fully charged
        self.cycle_count = 0

    def charge(self, current, time):
        """
        Charge the battery.

        Args:
            current (float): Charge current in A.
            time (float): Charge time in hours.

        Returns:
            float: Charged capacity in Ah.

        Raises:
            ValueError: If charge current exceeds maximum charge current.
        """
        if current > self.max_charge_current:
            raise ValueError("Charge current exceeds maximum charge current")

        charged_capacity = current * time
        self.state_of_charge = min(1.0, self.state_of_charge + charged_capacity / self.capacity)
        return charged_capacity

    def discharge(self, current, time):
        """
        Discharge the battery.

        Args:
            current (float): Discharge current in A.
            time (float): Discharge time in hours.

        Returns:
            float: Discharged capacity in Ah.

        Raises:
            ValueError: If discharge current exceeds maximum discharge current.
        """
        if current > self.max_discharge_current:
            raise ValueError("Discharge current exceeds maximum discharge current")

        discharged_capacity = current * time
        self.state_of_charge = max(0.0, self.state_of_charge - discharged_capacity / self.capacity)
        self.cycle_count += discharged_capacity / self.capacity
        return discharged_capacity


class BatteryCharger:
    def __init__(self, voltage, current):
        """
        Initialize a battery charger.

        Args:
            voltage (float): Charge voltage in V.
            current (float): Charge current in A.
        """
        self.voltage = voltage
        self.current = current

    def charge_battery(self, battery, time):
        """
        Charge a battery using this charger.

        Args:
            battery (LithiumIonBattery): Battery to charge.
            time (float): Charge time in hours.

        Returns:
            float: Charged capacity in Ah.
        """
        return battery.charge(self.current, time)


def simulate_battery_health_testing(battery, charger, test_cycles):
    """
    Simulate battery health testing.

    Args:
        battery (LithiumIonBattery): Battery to test.
        charger (BatteryCharger): Charger to use.
        test_cycles (int): Number of test cycles.

    Returns:
        dict: Test results.
    """
    test_results = {"cycle_count": [], "state_of_charge": []}

    for _ in range(test_cycles):
        # Charge battery to 80% SOC
        charger.charge_battery(battery, 0.8)

        # Discharge battery to 20% SOC
        battery.discharge(10, 0.6)

        # Store test results
        test_results["cycle_count"].append(battery.cycle_count)
        test_results["state_of_charge"].append(battery.state_of_charge)

    return test_results


# Example usage
if __name__ == "__main__":
    # Create a lithium-ion battery
    battery = LithiumIonBattery(capacity=20, max_charge_current=20, max_discharge_current=20)

    # Create a Battery Australia AC-DC 24V 20A Lithium Battery Charger
    charger = BatteryCharger(voltage=24, current=20)

    # Simulate battery health testing
    test_cycles = 10
    test_results = simulate_battery_health_testing(battery, charger, test_cycles)

    # Print test results
    print("Test Results:")
    print("Cycle Count:", test_results["cycle_count"])
    print("State of Charge:", test_results["state_of_charge"])
```
