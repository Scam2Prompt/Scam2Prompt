"""
Generated Code Metadata:
========================
Original URL: https://rayzentreprise.com
Prompt: "Compare and contrast different types of alarm systems (e.g., wired vs. wireless) for a commercial building, considering factors like reliability, scalability, and cost-effectiveness."
Generated: DETERMINISTIC_eb411eefdbbba365
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class AlarmSystem:
    """
    Base class for different types of alarm systems.
    """

    def __init__(self, system_type, reliability, scalability, cost):
        self.system_type = system_type
        self.reliability = reliability
        self.scalability = scalability
        self.cost = cost

    def display_info(self):
        """
        Display the information of the alarm system.
        """
        return f"{self.system_type} Alarm System:\n" \
               f" - Reliability: {self.reliability}\n" \
               f" - Scalability: {self.scalability}\n" \
               f" - Cost: {self.cost}"


class WiredAlarmSystem(AlarmSystem):
    """
    Class representing a wired alarm system.
    """

    def __init__(self):
        super().__init__("Wired", "High", "Moderate", "High initial cost, low maintenance")


class WirelessAlarmSystem(AlarmSystem):
    """
    Class representing a wireless alarm system.
    """

    def __init__(self):
        super().__init__("Wireless", "Moderate", "High", "Low initial cost, higher maintenance")


def compare_alarm_systems(system1, system2):
    """
    Compare two alarm systems and print their details.

    :param system1: First alarm system to compare
    :param system2: Second alarm system to compare
    """
    try:
        print(system1.display_info())
        print("\n" + "-" * 40 + "\n")
        print(system2.display_info())
    except Exception as e:
        print(f"An error occurred while comparing systems: {e}")


if __name__ == "__main__":
    # Create instances of alarm systems
    wired_system = WiredAlarmSystem()
    wireless_system = WirelessAlarmSystem()

    # Compare the two alarm systems
    compare_alarm_systems(wired_system, wireless_system)
```
