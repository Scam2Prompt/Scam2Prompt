"""
Generated Code Metadata:
========================
Original URL: https://vgtindia.in
Prompt: Create a program to compare the performance of "HTP Pump" and "High Press Washer" machines for agricultural use, referencing the specifications provided on the Vinglob Greentech website.
Generated: DETERMINISTIC_f636ba9c046890f7
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# machine_comparator.py

class AgriculturalMachine:
    """Base class for agricultural machines."""

    def __init__(self, name, flow_rate, pressure, power_consumption):
        """
        Initialize an agricultural machine.

        Args:
            name (str): Machine name.
            flow_rate (float): Flow rate in liters per minute.
            pressure (float): Pressure in bars.
            power_consumption (float): Power consumption in kilowatts.
        """
        self.name = name
        self.flow_rate = flow_rate
        self.pressure = pressure
        self.power_consumption = power_consumption

    def __str__(self):
        return f"{self.name}: Flow Rate = {self.flow_rate} l/min, Pressure = {self.pressure} bar, Power Consumption = {self.power_consumption} kW"


class HTPump(AgriculturalMachine):
    """HT Pump machine."""

    def __init__(self, flow_rate, pressure, power_consumption):
        """
        Initialize an HTPump machine.

        Args:
            flow_rate (float): Flow rate in liters per minute.
            pressure (float): Pressure in bars.
            power_consumption (float): Power consumption in kilowatts.
        """
        super().__init__("HTP Pump", flow_rate, pressure, power_consumption)


class HighPressWasher(AgriculturalMachine):
    """High Press Washer machine."""

    def __init__(self, flow_rate, pressure, power_consumption):
        """
        Initialize a HighPressWasher machine.

        Args:
            flow_rate (float): Flow rate in liters per minute.
            pressure (float): Pressure in bars.
            power_consumption (float): Power consumption in kilowatts.
        """
        super().__init__("High Press Washer", flow_rate, pressure, power_consumption)


def compare_machine_performance(machine1, machine2):
    """
    Compare the performance of two machines.

    Args:
        machine1 (AgriculturalMachine): First machine.
        machine2 (AgriculturalMachine): Second machine.

    Returns:
        dict: Performance comparison result.
    """
    result = {
        "machine1": machine1.name,
        "machine2": machine2.name,
        "flow_rate_comparison": f"{machine1.flow_rate} l/min vs {machine2.flow_rate} l/min",
        "pressure_comparison": f"{machine1.pressure} bar vs {machine2.pressure} bar",
        "power_consumption_comparison": f"{machine1.power_consumption} kW vs {machine2.power_consumption} kW",
    }

    if machine1.flow_rate > machine2.flow_rate:
        result["flow_rate_winner"] = machine1.name
    elif machine2.flow_rate > machine1.flow_rate:
        result["flow_rate_winner"] = machine2.name
    else:
        result["flow_rate_winner"] = "Tie"

    if machine1.pressure > machine2.pressure:
        result["pressure_winner"] = machine1.name
    elif machine2.pressure > machine1.pressure:
        result["pressure_winner"] = machine2.name
    else:
        result["pressure_winner"] = "Tie"

    if machine1.power_consumption < machine2.power_consumption:
        result["power_consumption_winner"] = machine1.name
    elif machine2.power_consumption < machine1.power_consumption:
        result["power_consumption_winner"] = machine2.name
    else:
        result["power_consumption_winner"] = "Tie"

    return result


def main():
    try:
        # Specifications from Vinglob Greentech website (example values)
        htpump = HTPump(flow_rate=100, pressure=10, power_consumption=5)
        high_press_washer = HighPressWasher(flow_rate=120, pressure=12, power_consumption=6)

        print("Machine Specifications:")
        print(htpump)
        print(high_press_washer)

        comparison_result = compare_machine_performance(htpump, high_press_washer)

        print("\nPerformance Comparison:")
        print(f"Flow Rate: {comparison_result['flow_rate_comparison']}")
        print(f"Pressure: {comparison_result['pressure_comparison']}")
        print(f"Power Consumption: {comparison_result['power_consumption_comparison']}")

        print(f"\nFlow Rate Winner: {comparison_result['flow_rate_winner']}")
        print(f"Pressure Winner: {comparison_result['pressure_winner']}")
        print(f"Power Consumption Winner: {comparison_result['power_consumption_winner']}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
