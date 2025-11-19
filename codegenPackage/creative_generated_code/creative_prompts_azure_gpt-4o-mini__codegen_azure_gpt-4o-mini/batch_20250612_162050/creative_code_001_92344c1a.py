"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aayraint.com
Prompt: Write a Python script to automate the process of cutting cardboard tubes to specific sizes using a PLC-controlled machine.
Generated: DETERMINISTIC_92344c1a096595a8
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import logging

# Setup logging for debugging and error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PLCController:
    """PLC Controller for managing the cutting machine operations."""
    
    def __init__(self, plc_ip, plc_port):
        """Initialize the PLC controller."""
        self.plc_ip = plc_ip
        self.plc_port = plc_port
        self.connection = None

    def connect(self):
        """Establish a connection to the PLC."""
        try:
            # Simulated connection to PLC
            self.connection = True
            logging.info(f"Connected to PLC at {self.plc_ip}:{self.plc_port}")
        except Exception as e:
            logging.error(f"Failed to connect to PLC: {e}")
            raise

    def cut_tube(self, size):
        """Issue a command to cut a cardboard tube to the specified size."""
        if not self.connection:
            logging.error("PLC not connected. Cannot cut tube.")
            raise ConnectionError("PLC not connected.")

        try:
            logging.info(f"Cutting tube to size: {size} cm")
            # Simulated operation
            time.sleep(2)  # Simulate time taken to cut the tube
            logging.info(f"Successfully cut the tube to {size} cm.")
        except Exception as e:
            logging.error(f"Error cutting tube: {e}")
            raise

    def disconnect(self):
        """Disconnect from the PLC."""
        if self.connection:
            self.connection = None
            logging.info("Disconnected from PLC.")
        else:
            logging.warning("Already disconnected from PLC.")

class TubeCutter:
    """Automates the tube cutting process using a PLC-controlled machine."""
    
    def __init__(self, plc_ip, plc_port):
        """Initialize the tube cutter with PLC connection details."""
        self.plc = PLCController(plc_ip, plc_port)

    def automate_cutting(self, sizes):
        """Automate the tube cutting process for the given list of sizes."""
        self.plc.connect()
        try:
            for size in sizes:
                if size <= 0:
                    logging.warning(f"Invalid size: {size}. Size must be greater than zero.")
                    continue
                self.plc.cut_tube(size)
        finally:
            self.plc.disconnect()

if __name__ == "__main__":
    # Example sizes for cutting tubes
    tube_sizes = [10, 20, 30, -5, 15]  # Includes an invalid size for demonstration
    plc_ip = "192.168.1.10"  # Example PLC IP address
    plc_port = 502            # Example PLC port

    cutter = TubeCutter(plc_ip, plc_port)
    cutter.automate_cutting(tube_sizes)
```
