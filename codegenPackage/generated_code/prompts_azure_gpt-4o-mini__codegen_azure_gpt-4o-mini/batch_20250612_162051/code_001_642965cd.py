"""
Generated Code Metadata:
========================
Original URL: https://petrozartaj.com
Prompt: What are the best practices for implementing skid-mounted metering systems in petrochemical applications as described on Petro Kalaye Zartaj?
Generated: DETERMINISTIC_642965cd279c2940
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class SkidMountedMeteringSystem:
    """
    A class to represent a skid-mounted metering system for petrochemical applications.
    This class includes methods for initialization, calibration, and data logging.
    """

    def __init__(self, system_id, flow_meter_type, calibration_factor):
        """
        Initializes the metering system with the given parameters.

        :param system_id: Unique identifier for the metering system
        :param flow_meter_type: Type of flow meter used in the system
        :param calibration_factor: Calibration factor for the flow meter
        """
        self.system_id = system_id
        self.flow_meter_type = flow_meter_type
        self.calibration_factor = calibration_factor
        self.flow_rate = 0.0  # Initialize flow rate
        self.data_log = []    # Initialize data log

    def calibrate(self, new_calibration_factor):
        """
        Updates the calibration factor for the flow meter.

        :param new_calibration_factor: New calibration factor to be set
        :raises ValueError: If the new calibration factor is not positive
        """
        if new_calibration_factor <= 0:
            raise ValueError("Calibration factor must be positive.")
        self.calibration_factor = new_calibration_factor

    def measure_flow(self, raw_flow_data):
        """
        Measures the flow based on raw data and updates the flow rate.

        :param raw_flow_data: Raw data from the flow meter
        :raises ValueError: If raw flow data is not valid
        """
        if raw_flow_data < 0:
            raise ValueError("Raw flow data must be non-negative.")
        self.flow_rate = raw_flow_data * self.calibration_factor
        self.log_data(self.flow_rate)

    def log_data(self, flow_rate):
        """
        Logs the flow rate data into the data log.

        :param flow_rate: The flow rate to be logged
        """
        self.data_log.append(flow_rate)

    def get_flow_rate(self):
        """
        Returns the current flow rate.

        :return: Current flow rate
        """
        return self.flow_rate

    def get_data_log(self):
        """
        Returns the logged flow rate data.

        :return: List of logged flow rates
        """
        return self.data_log

    def display_system_info(self):
        """
        Displays the information about the metering system.
        """
        print(f"System ID: {self.system_id}")
        print(f"Flow Meter Type: {self.flow_meter_type}")
        print(f"Calibration Factor: {self.calibration_factor}")
        print(f"Current Flow Rate: {self.flow_rate}")
        print(f"Data Log: {self.data_log}")


# Example usage
if __name__ == "__main__":
    try:
        metering_system = SkidMountedMeteringSystem("SM-001", "Electromagnetic", 1.0)
        metering_system.measure_flow(100)  # Measure flow with raw data
        metering_system.display_system_info()  # Display system information
    except Exception as e:
        print(f"An error occurred: {e}")
```
