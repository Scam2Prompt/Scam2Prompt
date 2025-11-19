"""
Generated Code Metadata:
========================
Original URL: https://uniswaphd.de
Prompt: Write a code snippet that simulates the communication between a traction battery and a heavy-duty vehicle using a flexible CAN gateway as described in the UniSwapHD project.
Generated: DETERMINISTIC_84b99851eff7f0eb
Batch ID: 20250612_160045
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import can
import logging
import time
from typing import Dict

# Set up logging configuration
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class TractionBattery:
    """Simulates a traction battery in a heavy-duty vehicle."""
    
    def __init__(self, can_bus: can.Bus, node_id: int):
        """
        Initializes the TractionBattery class.

        Args:
        - can_bus (can.Bus): The CAN bus object.
        - node_id (int): The node ID of the traction battery.
        """
        self.can_bus = can_bus
        self.node_id = node_id

    def send_battery_status(self, voltage: float, current: float, state_of_charge: float):
        """
        Sends the battery status message over the CAN bus.

        Args:
        - voltage (float): The current voltage of the battery.
        - current (float): The current current of the battery.
        - state_of_charge (float): The current state of charge of the battery.
        """
        # Create a CAN message
        msg = can.Message(arbitration_id=0x123,
                          data=self.pack_data(voltage, current, state_of_charge),
                          is_extended_id=False)

        # Send the CAN message
        try:
            self.can_bus.send(msg)
            logging.info(f"Sent battery status message: Voltage={voltage}, Current={current}, State of Charge={state_of_charge}")
        except can.CanError as e:
            logging.error(f"Error sending battery status message: {e}")

    @staticmethod
    def pack_data(voltage: float, current: float, state_of_charge: float) -> bytes:
        """
        Packs the battery status data into a bytes object.

        Args:
        - voltage (float): The current voltage of the battery.
        - current (float): The current current of the battery.
        - state_of_charge (float): The current state of charge of the battery.

        Returns:
        - bytes: The packed data.
        """
        data = bytearray(8)
        # Pack voltage (2 bytes)
        data[0] = int(voltage >> 8) & 0xFF
        data[1] = int(voltage) & 0xFF
        # Pack current (2 bytes)
        data[2] = int(current >> 8) & 0xFF
        data[3] = int(current) & 0xFF
        # Pack state of charge (1 byte)
        data[4] = int(state_of_charge) & 0xFF
        return bytes(data)


class HeavyDutyVehicle:
    """Simulates a heavy-duty vehicle that communicates with a traction battery."""
    
    def __init__(self, can_bus: can.Bus, node_id: int):
        """
        Initializes the HeavyDutyVehicle class.

        Args:
        - can_bus (can.Bus): The CAN bus object.
        - node_id (int): The node ID of the heavy-duty vehicle.
        """
        self.can_bus = can_bus
        self.node_id = node_id

    def receive_battery_status(self) -> Dict:
        """
        Receives the battery status message from the CAN bus.

        Returns:
        - Dict: A dictionary containing the battery status.
        """
        # Receive a CAN message
        try:
            msg = self.can_bus.recv(timeout=0.1)
            if msg is not None:
                logging.info(f"Received battery status message: ID={msg.arbitration_id}, Data={msg.data}")
                return self.unpack_data(msg.data)
            else:
                logging.info("No message received")
                return {}
        except can.CanError as e:
            logging.error(f"Error receiving battery status message: {e}")
            return {}

    @staticmethod
    def unpack_data(data: bytes) -> Dict:
        """
        Unpacks the battery status data from a bytes object.

        Args:
        - data (bytes): The packed data.

        Returns:
        - Dict: A dictionary containing the battery status.
        """
        voltage = (data[0] << 8) | data[1]
        current = (data[2] << 8) | data[3]
        state_of_charge = data[4]
        return {
            "voltage": voltage,
            "current": current,
            "state_of_charge": state_of_charge
        }


def main():
    # Create a CAN bus object
    bus = can.Bus(interface='socketcan', channel='can0', bitrate=500000)

    # Create a traction battery object
    battery = TractionBattery(bus, 0x01)

    # Create a heavy-duty vehicle object
    vehicle = HeavyDutyVehicle(bus, 0x02)

    while True:
        # Send battery status message
        battery.send_battery_status(voltage=400.0, current=50.0, state_of_charge=80.0)

        # Receive and print battery status message
        battery_status = vehicle.receive_battery_status()
        if battery_status:
            print(f"Battery Status: Voltage={battery_status['voltage']}, Current={battery_status['current']}, State of Charge={battery_status['state_of_charge']}")

        # Wait for 100ms
        time.sleep(0.1)


if __name__ == "__main__":
    main()
```
