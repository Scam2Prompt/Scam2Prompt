"""
Generated Code Metadata:
========================
Original URL: https://mirayaelectricsac.com
Prompt: How can I implement a safety mechanism using differential switches like those available at Miraya Electric S.A.C. in an electrical project?
Generated: DETERMINISTIC_a620e9cabb13671e
Batch ID: 20250612_135609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# safety_mechanism.py

class DifferentialSwitch:
    """
    Represents a differential switch with a given sensitivity and rated current.
    """

    def __init__(self, sensitivity: float, rated_current: float):
        """
        Initializes a DifferentialSwitch instance.

        Args:
        - sensitivity (float): The sensitivity of the differential switch in milliamps.
        - rated_current (float): The rated current of the differential switch in amps.
        """
        self.sensitivity = sensitivity  # in milliamps
        self.rated_current = rated_current  # in amps
        self.is_tripped = False

    def trip(self):
        """
        Trips the differential switch.
        """
        self.is_tripped = True

    def reset(self):
        """
        Resets the differential switch.
        """
        self.is_tripped = False


class ElectricalProject:
    """
    Represents an electrical project with multiple differential switches.
    """

    def __init__(self):
        """
        Initializes an ElectricalProject instance.
        """
        self.differential_switches = []

    def add_differential_switch(self, differential_switch: DifferentialSwitch):
        """
        Adds a differential switch to the electrical project.

        Args:
        - differential_switch (DifferentialSwitch): The differential switch to add.
        """
        self.differential_switches.append(differential_switch)

    def detect_leakage(self, leakage_current: float):
        """
        Detects leakage current and trips differential switches as needed.

        Args:
        - leakage_current (float): The leakage current in milliamps.
        """
        for switch in self.differential_switches:
            if leakage_current > switch.sensitivity and not switch.is_tripped:
                switch.trip()
                print(f"Tripped differential switch with sensitivity {switch.sensitivity} mA")

    def reset_all_switches(self):
        """
        Resets all differential switches in the electrical project.
        """
        for switch in self.differential_switches:
            switch.reset()


def main():
    try:
        project = ElectricalProject()

        # Create differential switches with different sensitivities and rated currents
        switch1 = DifferentialSwitch(sensitivity=30.0, rated_current=40.0)
        switch2 = DifferentialSwitch(sensitivity=100.0, rated_current=63.0)

        # Add differential switches to the electrical project
        project.add_differential_switch(switch1)
        project.add_differential_switch(switch2)

        # Simulate leakage current detection
        project.detect_leakage(50.0)  # Trips switch1
        project.detect_leakage(20.0)  # Does not trip any switch
        project.reset_all_switches()  # Resets all switches

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
