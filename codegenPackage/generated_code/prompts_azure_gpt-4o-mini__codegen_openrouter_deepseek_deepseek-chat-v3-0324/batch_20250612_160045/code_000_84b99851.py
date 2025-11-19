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
import can
import time
import random
import logging
from typing import Dict, Any

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class CANGateway:
    """
    Flexible CAN Gateway for communication between traction battery and heavy-duty vehicle.
    Implements the UniSwapHD protocol for battery swapping in heavy-duty vehicles.
    """
    
    def __init__(self, channel: str, bustype: str = 'socketcan', bitrate: int = 500000):
        """
        Initialize CAN gateway with specified parameters.
        
        Args:
            channel: CAN interface channel (e.g., 'can0')
            bustype: Type of CAN bus (default: 'socketcan')
            bitrate: CAN bus bitrate in bps (default: 500000)
        """
        self.channel = channel
        self.bustype = bustype
        self.bitrate = bitrate
        self.bus = None
        self.battery_state = {
            'soc': 0.0,  # State of Charge (0-100%)
            'soh': 100.0,  # State of Health (0-100%)
            'voltage': 0.0,  # Battery voltage (V)
            'current': 0.0,  # Battery current (A)
            'temperature': 25.0,  # Battery temperature (°C)
            'status': 'disconnected'  # Battery connection status
        }
        
    def connect(self) -> bool:
        """
        Connect to the CAN bus.
        
        Returns:
            bool: True if connection successful, False otherwise
        """
        try:
            self.bus = can.interface.Bus(
                channel=self.channel,
                bustype=self.bustype,
                bitrate=self.bitrate
            )
            logger.info(f"Connected to CAN bus on {self.channel}")
            return True
        except Exception as e:
            logger.error(f"Failed to connect to CAN bus: {e}")
            return False
    
    def disconnect(self) -> None:
        """Disconnect from the CAN bus."""
        if self.bus:
            self.bus.shutdown()
            logger.info("Disconnected from CAN bus")
    
    def send_battery_data(self) -> None:
        """
        Send battery data to the vehicle via CAN bus.
        Implements the UniSwapHD protocol for battery status communication.
        """
        if not self.bus:
            logger.error("CAN bus not connected")
            return
            
        # Simulate battery data updates
        self._update_battery_state()
        
        # Prepare CAN message (UniSwapHD protocol format)
        msg_data = self._pack_battery_data()
        
        try:
            message = can.Message(
                arbitration_id=0x18FFA001,  # Standard battery status message ID
                data=msg_data,
                is_extended_id=True
            )
            self.bus.send(message)
            logger.debug(f"Sent battery data: {msg_data.hex()}")
        except can.CanError as e:
            logger.error(f"Failed to send CAN message: {e}")
    
    def receive_vehicle_commands(self) -> Dict[str, Any]:
        """
        Receive and process commands from the vehicle.
        
        Returns:
            dict: Parsed vehicle commands or empty dict if no message received
        """
        if not self.bus:
            logger.error("CAN bus not connected")
            return {}
            
        try:
            msg = self.bus.recv(timeout=0.1)
            if msg:
                logger.debug(f"Received vehicle command: {msg.data.hex()}")
                return self._parse_vehicle_command(msg.data)
            return {}
        except can.CanError as e:
            logger.error(f"Failed to receive CAN message: {e}")
            return {}
    
    def _update_battery_state(self) -> None:
        """Simulate battery state changes for demonstration purposes."""
        # Random fluctuations for simulation
        self.battery_state['soc'] = max(0, min(100, self.battery_state['soc'] + random.uniform(-1, 1)))
        self.battery_state['voltage'] = 600 + random.uniform(-5, 5)
        self.battery_state['current'] = 50 + random.uniform(-10, 10)
        self.battery_state['temperature'] = max(20, min(50, self.battery_state['temperature'] + random.uniform(-0.5, 0.5)))
        
        # Simulate connection status changes
        if random.random() < 0.01:  # 1% chance to change status
            self.battery_state['status'] = random.choice(['connected', 'disconnected', 'charging', 'error'])
    
    def _pack_battery_data(self) -> bytes:
        """
        Pack battery state data into CAN message format according to UniSwapHD protocol.
        
        Returns:
            bytes: Packed CAN message data (8 bytes)
        """
        # Protocol format:
        # Byte 0: Status flags
        # Byte 1-2: SOC (0-100%, scaled to 0-65535)
        # Byte 3-4: Voltage (0-1000V, scaled to 0-65535)
        # Byte 5-6: Current (-1000 to +1000A, scaled to -32768 to +32767)
        # Byte 7: Temperature (0-255°C)
        
        status_byte = 0x00
        if self.battery_state['status'] == 'connected':
            status_byte |= 0x01
        elif self.battery_state['status'] == 'charging':
            status_byte |= 0x03
        elif self.battery_state['status'] == 'error':
            status_byte |= 0x80
        
        soc = int(self.battery_state['soc'] * 655.35)
        voltage = int(self.battery_state['voltage'] * 65.535)
        current = int(self.battery_state['current'] * 32.767)
        temperature = int(self.battery_state['temperature'])
        
        return bytes([
            status_byte,
            (soc >> 8) & 0xFF,
            soc & 0xFF,
            (voltage >> 8) & 0xFF,
            voltage & 0xFF,
            (current >> 8) & 0xFF,
            current & 0xFF,
            temperature
        ])
    
    def _parse_vehicle_command(self, data: bytes) -> Dict[str, Any]:
        """
        Parse vehicle command from CAN message.
        
        Args:
            data: Received CAN message data
            
        Returns:
            dict: Parsed command with keys 'command', 'power_request', 'charge_request'
        """
        if len(data) < 8:
            return {}
            
        command = {
            'command': 'noop',
            'power_request': 0.0,
            'charge_request': False
        }
        
        # Protocol format:
        # Byte 0: Command flags
        # Byte 1-2: Power request (0-100%, scaled to 0-65535)
        # Byte 3-7: Reserved
        
        flags = data[0]
        power_request = ((data[1] << 8) | data[2]) / 655.35
        
        if flags & 0x01:
            command['command'] = 'enable_power'
            command['power_request'] = power_request
        elif flags & 0x02:
            command['command'] = 'disable_power'
        elif flags & 0x04:
            command['command'] = 'start_charging'
            command['charge_request'] = True
        elif flags & 0x08:
            command['command'] = 'stop_charging'
        
        return command

def main():
    """Main simulation loop for CAN gateway communication."""
    # Initialize CAN gateway
    gateway = CANGateway(channel='can0')
    
    if not gateway.connect():
        return
    
    try:
        logger.info("Starting CAN gateway simulation...")
        while True:
            # Send battery data to vehicle
            gateway.send_battery_data()
            
            # Receive and process vehicle commands
            command = gateway.receive_vehicle_commands()
            if command:
                logger.info(f"Received vehicle command: {command}")
            
            # Simulation loop delay
            time.sleep(1)
            
    except KeyboardInterrupt:
        logger.info("Shutting down CAN gateway...")
    finally:
        gateway.disconnect()

if __name__ == "__main__":
    main()
```
