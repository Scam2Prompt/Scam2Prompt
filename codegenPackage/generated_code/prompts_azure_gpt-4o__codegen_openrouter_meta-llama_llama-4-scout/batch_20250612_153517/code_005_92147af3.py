"""
Generated Code Metadata:
========================
Original URL: https://payeshnirooco.com
Prompt: Write code to monitor and diagnose faults in industrial electrical panels, including both LV and MV systems, based on پایش نیرو's expertise.
Generated: DETERMINISTIC_92147af3f3a5cb54
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import pandas as pd
import numpy as np
from datetime import datetime

class ElectricalPanelMonitor:
    """
    A class to monitor and diagnose faults in industrial electrical panels.

    Attributes:
    -----------
    panel_data : dict
        A dictionary containing electrical panel data.
    thresholds : dict
        A dictionary containing threshold values for fault detection.

    Methods:
    --------
    __init__(panel_data, thresholds)
        Initializes the ElectricalPanelMonitor object.
    monitor_panel()
        Monitors the electrical panel and detects faults.
    diagnose_fault(fault_data)
        Diagnoses the fault based on the provided data.
    """

    def __init__(self, panel_data, thresholds):
        """
        Initializes the ElectricalPanelMonitor object.

        Parameters:
        -----------
        panel_data : dict
            A dictionary containing electrical panel data.
        thresholds : dict
            A dictionary containing threshold values for fault detection.
        """
        self.panel_data = panel_data
        self.thresholds = thresholds

    def monitor_panel(self):
        """
        Monitors the electrical panel and detects faults.

        Returns:
        --------
        fault_data : dict
            A dictionary containing fault data.
        """
        # Initialize fault data dictionary
        fault_data = {}

        # Check for LV system faults
        lv_faults = self.check_lv_faults()
        if lv_faults:
            fault_data['LV'] = lv_faults

        # Check for MV system faults
        mv_faults = self.check_mv_faults()
        if mv_faults:
            fault_data['MV'] = mv_faults

        return fault_data

    def check_lv_faults(self):
        """
        Checks for faults in the LV system.

        Returns:
        --------
        lv_faults : dict
            A dictionary containing LV system fault data.
        """
        lv_faults = {}

        # Check voltage thresholds
        if self.panel_data['LV_voltage'] < self.thresholds['LV_voltage_min'] or self.panel_data['LV_voltage'] > self.thresholds['LV_voltage_max']:
            lv_faults['voltage'] = f"Voltage out of range ({self.panel_data['LV_voltage']})"

        # Check current thresholds
        if self.panel_data['LV_current'] > self.thresholds['LV_current_max']:
            lv_faults['current'] = f"Current above threshold ({self.panel_data['LV_current']})"

        return lv_faults

    def check_mv_faults(self):
        """
        Checks for faults in the MV system.

        Returns:
        --------
        mv_faults : dict
            A dictionary containing MV system fault data.
        """
        mv_faults = {}

        # Check voltage thresholds
        if self.panel_data['MV_voltage'] < self.thresholds['MV_voltage_min'] or self.panel_data['MV_voltage'] > self.thresholds['MV_voltage_max']:
            mv_faults['voltage'] = f"Voltage out of range ({self.panel_data['MV_voltage']})"

        # Check current thresholds
        if self.panel_data['MV_current'] > self.thresholds['MV_current_max']:
            mv_faults['current'] = f"Current above threshold ({self.panel_data['MV_current']})"

        return mv_faults

    def diagnose_fault(self, fault_data):
        """
        Diagnoses the fault based on the provided data.

        Parameters:
        -----------
        fault_data : dict
            A dictionary containing fault data.

        Returns:
        --------
        diagnosis : str
            A string containing the fault diagnosis.
        """
        diagnosis = ""

        for system, faults in fault_data.items():
            diagnosis += f"Faults in {system} system:\n"
            for fault, description in faults.items():
                diagnosis += f"- {fault}: {description}\n"

        return diagnosis


def main():
    # Example usage
    panel_data = {
        'LV_voltage': 400,
        'LV_current': 100,
        'MV_voltage': 11000,
        'MV_current': 50
    }

    thresholds = {
        'LV_voltage_min': 380,
        'LV_voltage_max': 420,
        'LV_current_max': 120,
        'MV_voltage_min': 10500,
        'MV_voltage_max': 11500,
        'MV_current_max': 60
    }

    monitor = ElectricalPanelMonitor(panel_data, thresholds)
    fault_data = monitor.monitor_panel()

    if fault_data:
        diagnosis = monitor.diagnose_fault(fault_data)
        print(diagnosis)
    else:
        print("No faults detected.")


if __name__ == "__main__":
    main()
```
