"""
Generated Code Metadata:
========================
Original URL: https://aayraint.com
Prompt: Write a Python script to automate the process of cutting cardboard tubes to specific sizes using a PLC-controlled machine.
Generated: DETERMINISTIC_92344c1a096595a8
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# plc_cardboard_tube_cutter.py

"""
Script to automate the process of cutting cardboard tubes to specific sizes using a PLC-controlled machine.

Requires:
- Python 3.8+
- plc-library (simulated for demonstration purposes)
"""

import logging
from typing import List

# Simulated PLC library for demonstration purposes
class PLC:
    def __init__(self):
        self.is_connected = False

    def connect(self):
        try:
            # Establish connection to PLC
            self.is_connected = True
            logging.info("Connected to PLC")
        except Exception as e:
            logging.error(f"Failed to connect to PLC: {e}")

    def disconnect(self):
        try:
            # Close connection to PLC
            self.is_connected = False
            logging.info("Disconnected from PLC")
        except Exception as e:
            logging.error(f"Failed to disconnect from PLC: {e}")

    def cut_tube(self, length: float):
        try:
            if not self.is_connected:
                raise Exception("Not connected to PLC")
            # Send cut command to PLC with specified length
            logging.info(f"Cutting tube to {length}mm")
        except Exception as e:
            logging.error(f"Failed to cut tube: {e}")


class CardboardTubeCutter:
    def __init__(self, plc: PLC):
        self.plc = plc
        self.tube_lengths = []

    def add_tube_length(self, length: float):
        """
        Add a tube length to the cutting queue.

        Args:
            length (float): Length of the tube to cut in mm.
        """
        self.tube_lengths.append(length)

    def cut_tubes(self):
        """
        Cut tubes to specified lengths.
        """
        for length in self.tube_lengths:
            self.plc.cut_tube(length)
        self.tube_lengths.clear()


def main():
    logging.basicConfig(level=logging.INFO)

    plc = PLC()
    plc.connect()

    cutter = CardboardTubeCutter(plc)

    # Example usage
    tube_lengths: List[float] = [100, 200, 50, 150]
    for length in tube_lengths:
        cutter.add_tube_length(length)

    cutter.cut_tubes()

    plc.disconnect()


if __name__ == "__main__":
    main()
```
