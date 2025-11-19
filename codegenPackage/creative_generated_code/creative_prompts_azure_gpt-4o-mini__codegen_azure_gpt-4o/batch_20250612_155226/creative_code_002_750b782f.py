"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://neiropump.com
Prompt: What are the key functionalities of the Neiro Pump library for managing pump operations?
Generated: DETERMINISTIC_750b782f79b2e983
Batch ID: 20250612_155226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Neiro Pump Library - Key Functionalities for Managing Pump Operations

This library provides a set of functionalities to control and monitor pump operations,
such as turning pumps on/off, setting flow rates, monitoring status, and handling errors.

Author: Your Name
Date: YYYY-MM-DD
Version: 1.0.0
"""

# Import necessary modules
import time


class PumpError(Exception):
    """Custom exception for pump-related errors."""
    pass


class NeiroPump:
    """
    Represents a pump with functionalities to control and monitor its operations.
    """

    def __init__(self, pump_id, max_flow_rate):
        """
        Initialize the pump object.

        Args:
            pump_id (str): Unique identifier for the pump.
            max_flow_rate (float): Maximum flow rate of the pump in liters per minute.

        Raises:
            ValueError: If max_flow_rate is not positive.
        """
        if max_flow_rate <= 0:
            raise ValueError("max_flow_rate must be a positive number.")
        self.pump_id = pump_id
        self.max_flow_rate = max_flow_rate
        self.is_running = False
        self.current_flow_rate = 0.0

    def start(self):
        """
        Start the pump operation.

        Raises:
            PumpError: If the pump is already running.
        """
        if self.is_running:
            raise PumpError(f"Pump {self.pump_id} is already running.")
        self.is_running = True
        print(f"Pump {self.pump_id} started.")

    def stop(self):
        """
        Stop the pump operation.

        Raises:
            PumpError: If the pump is not running.
        """
        if not self.is_running:
            raise PumpError(f"Pump {self.pump_id} is not running.")
        self.is_running = False
        self.current_flow_rate = 0.0
        print(f"Pump {self.pump_id} stopped.")

    def set_flow_rate(self, flow_rate):
        """
        Set the flow rate of the pump.

        Args:
            flow_rate (float): Desired flow rate in liters per minute.

        Raises:
            PumpError: If the pump is not running.
            ValueError: If the flow_rate is outside the valid range.
        """
        if not self.is_running:
            raise PumpError(f"Pump {self.pump_id} is not running. Cannot set flow rate.")
        if flow_rate <= 0 or flow_rate > self.max_flow_rate:
            raise ValueError(f"Flow rate must be between 0 and {self.max_flow_rate} liters per minute.")
        self.current_flow_rate = flow_rate
        print(f"Pump {self.pump_id}: Flow rate set to {flow_rate} liters per minute.")

    def get_status(self):
        """
        Get the current status of the pump.

        Returns:
            dict: Dictionary containing the pump's status.
        """
        return {
            "pump_id": self.pump_id,
            "is_running": self.is_running,
            "current_flow_rate": self.current_flow_rate,
            "max_flow_rate": self.max_flow_rate,
        }

    @staticmethod
    def monitor_pumps(pumps, interval=5):
        """
        Monitor the status of multiple pumps at regular intervals.

        Args:
            pumps (list): List of NeiroPump objects to monitor.
            interval (int): Time interval (in seconds) between status checks.

        Raises:
            ValueError: If interval is not positive.
        """
        if interval <= 0:
            raise ValueError("Interval must be a positive number.")

        try:
            while True:
                print("Monitoring pump statuses...")
                for pump in pumps:
                    status = pump.get_status()
                    print(f"Pump {status['pump_id']} status: {status}")
                time.sleep(interval)
        except KeyboardInterrupt:
            print("Monitoring stopped by user.")


# Example usage
if __name__ == "__main__":
    try:
        pump1 = NeiroPump("Pump1", max_flow_rate=100.0)
        pump2 = NeiroPump("Pump2", max_flow_rate=50.0)

        pump1.start()
        pump1.set_flow_rate(75.0)

        pump2.start()
        pump2.set_flow_rate(40.0)

        # Print status of each pump
        print(pump1.get_status())
        print(pump2.get_status())

        # Monitor pumps (Press Ctrl+C to stop monitoring)
        NeiroPump.monitor_pumps([pump1, pump2], interval=10)

    except Exception as e:
        print(f"Error: {e}")
```
