"""
Generated Code Metadata:
========================
Original URL: https://loghouses-woodcraft.com
Prompt: "What are the key differences between QS and WQ series pumps, and how do I choose between them for my water supply system?"
Generated: DETERMINISTIC_7ab888d8b22fb61a
Batch ID: 20250622_211906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Pump Selection Guide

class Pump:
    def __init__(self, series, flow_rate, head, power):
        """
        Initialize a Pump object.

        Args:
            series (str): Pump series (QS or WQ).
            flow_rate (float): Flow rate in m³/h.
            head (float): Head in meters.
            power (float): Power in kW.
        """
        self.series = series
        self.flow_rate = flow_rate
        self.head = head
        self.power = power

    def __str__(self):
        return f"{self.series} Pump - Flow Rate: {self.flow_rate} m³/h, Head: {self.head} m, Power: {self.power} kW"


class QS_Pump(Pump):
    def __init__(self, flow_rate, head, power):
        super().__init__("QS", flow_rate, head, power)


class WQ_Pump(Pump):
    def __init__(self, flow_rate, head, power):
        super().__init__("WQ", flow_rate, head, power)


def compare_pumps(pump1, pump2):
    """
    Compare two pumps and highlight their differences.

    Args:
        pump1 (Pump): First pump to compare.
        pump2 (Pump): Second pump to compare.

    Returns:
        dict: Dictionary highlighting the differences between the two pumps.
    """
    differences = {
        "Series": [pump1.series, pump2.series],
        "Flow Rate (m³/h)": [pump1.flow_rate, pump2.flow_rate],
        "Head (m)": [pump1.head, pump2.head],
        "Power (kW)": [pump1.power, pump2.power],
    }
    return differences


def choose_pump(flow_rate, head, power_source):
    """
    Choose between QS and WQ series pumps based on the system's requirements.

    Args:
        flow_rate (float): Required flow rate in m³/h.
        head (float): Required head in meters.
        power_source (str): Available power source (e.g., 3-phase, 1-phase).

    Returns:
        Pump: Recommended pump object.
    """
    try:
        if power_source.lower() == "3-phase":
            # QS series pumps are suitable for 3-phase power sources
            return QS_Pump(flow_rate, head, 5.5)  # Default power for QS pumps
        elif power_source.lower() == "1-phase":
            # WQ series pumps are suitable for 1-phase power sources
            return WQ_Pump(flow_rate, head, 2.2)  # Default power for WQ pumps
        else:
            raise ValueError("Invalid power source. Please specify 3-phase or 1-phase.")
    except Exception as e:
        print(f"Error: {str(e)}")
        return None


def main():
    # Example usage
    qs_pump = QS_Pump(10, 20, 5.5)
    wq_pump = WQ_Pump(10, 20, 2.2)

    print("QS Pump:", qs_pump)
    print("WQ Pump:", wq_pump)

    differences = compare_pumps(qs_pump, wq_pump)
    print("\nDifferences:")
    for key, values in differences.items():
        print(f"{key}: QS - {values[0]}, WQ - {values[1]}")

    recommended_pump = choose_pump(10, 20, "3-phase")
    if recommended_pump:
        print(f"\nRecommended Pump: {recommended_pump}")


if __name__ == "__main__":
    main()
```
