"""
Generated Code Metadata:
========================
Original URL: https://technicalpower.us
Prompt: Develop a library that helps data center managers assess the efficiency of their cooling and electrical strategies, inspired by the assessment services provided by Technical Power Service, Inc.
Generated: DETERMINISTIC_7cf144cffc6b40fc
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Library: DataCenterEfficiency
Purpose: Assess the efficiency of cooling and electrical strategies in data centers.
Author: [Your Name]
Date: [Today's Date]
"""

import math

class DataCenterEfficiency:
    """
    A library to assess the efficiency of cooling and electrical strategies in data centers.
    """

    def __init__(self, power_usage, cooling_capacity, server_load):
        """
        Initialize the DataCenterEfficiency object.

        :param power_usage: Total power usage in kilowatts (kW).
        :param cooling_capacity: Cooling capacity in kilowatts (kW).
        :param server_load: Server load in kilowatts (kW).
        """
        if power_usage <= 0 or cooling_capacity <= 0 or server_load <= 0:
            raise ValueError("All input values must be positive numbers.")
        
        self.power_usage = power_usage
        self.cooling_capacity = cooling_capacity
        self.server_load = server_load

    def calculate_pue(self):
        """
        Calculate Power Usage Effectiveness (PUE).

        PUE = Total Facility Power / IT Equipment Power

        :return: PUE value (float).
        """
        try:
            pue = self.power_usage / self.server_load
            return round(pue, 2)
        except ZeroDivisionError:
            raise ValueError("Server load cannot be zero.")

    def calculate_cooling_efficiency(self):
        """
        Calculate Cooling Efficiency Ratio (CER).

        CER = Cooling Capacity / Total Facility Power

        :return: CER value (float).
        """
        try:
            cer = self.cooling_capacity / self.power_usage
            return round(cer, 2)
        except ZeroDivisionError:
            raise ValueError("Power usage cannot be zero.")

    def assess_efficiency(self):
        """
        Assess the overall efficiency of the data center.

        :return: Dictionary containing PUE and CER values with efficiency ratings.
        """
        pue = self.calculate_pue()
        cer = self.calculate_cooling_efficiency()

        pue_rating = self._rate_pue(pue)
        cer_rating = self._rate_cer(cer)

        return {
            "PUE": {"value": pue, "rating": pue_rating},
            "CER": {"value": cer, "rating": cer_rating}
        }

    @staticmethod
    def _rate_pue(pue):
        """
        Rate the PUE value.

        :param pue: PUE value (float).
        :return: Rating as a string.
        """
        if pue < 1.5:
            return "Excellent"
        elif 1.5 <= pue < 2.0:
            return "Good"
        else:
            return "Needs Improvement"

    @staticmethod
    def _rate_cer(cer):
        """
        Rate the CER value.

        :param cer: CER value (float).
        :return: Rating as a string.
        """
        if cer > 0.5:
            return "Excellent"
        elif 0.3 <= cer <= 0.5:
            return "Good"
        else:
            return "Needs Improvement"

# Example usage:
if __name__ == "__main__":
    try:
        # Initialize the library with sample data
        data_center = DataCenterEfficiency(power_usage=1000, cooling_capacity=400, server_load=800)

        # Assess efficiency
        efficiency_report = data_center.assess_efficiency()

        # Print the report
        print("Data Center Efficiency Report:")
        print(f"PUE: {efficiency_report['PUE']['value']} ({efficiency_report['PUE']['rating']})")
        print(f"CER: {efficiency_report['CER']['value']} ({efficiency_report['CER']['rating']})")
    except ValueError as e:
        print(f"Error: {e}")
```
