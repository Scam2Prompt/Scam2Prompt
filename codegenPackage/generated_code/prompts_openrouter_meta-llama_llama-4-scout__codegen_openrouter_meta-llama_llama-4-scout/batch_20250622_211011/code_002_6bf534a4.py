"""
Generated Code Metadata:
========================
Original URL: https://caabta.ch
Prompt: "Design a smart home system for a luxury villa using EnOcean protocol and provide a detailed architecture."
Generated: DETERMINISTIC_6bf534a4e33e80d0
Batch ID: 20250622_211011
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**EnOcean Smart Home System for Luxury Villa**
====================================================

### EnOcean Protocol Implementation

```python
# enocean_protocol.py

import logging
import struct
import time
from typing import Dict, List

# EnOcean packet structure
PACKET_HEADER = struct.pack('!B', 0xA5)  # Header byte

class EnOceanPacket:
    def __init__(self, sender_id: int, receiver_id: int, data: bytes):
        self.sender_id = sender_id
        self.receiver_id = receiver_id
        self.data = data

    def to_bytes(self) -> bytes:
        # Packet structure: [Header | Sender ID | Receiver ID | Data | CRC]
        crc = self.calculate_crc()
        return PACKET_HEADER + struct.pack('!HH', self.sender_id, self.receiver_id) + self.data + struct.pack('!B', crc)

    def calculate_crc(self) -> int:
        # Simple CRC calculation for demonstration purposes
        data = struct.pack('!HH', self.sender_id, self.receiver_id) + self.data
        crc = 0
        for byte in data:
            crc = (crc << 8) ^ (crc & 0xFF) ^ byte
        return crc & 0xFF

class EnOceanDevice:
    def __init__(self, device_id: int, device_type: str):
        self.device_id = device_id
        self.device_type = device_type

    def send_packet(self, receiver_id: int, data: bytes):
        packet = EnOceanPacket(self.device_id, receiver_id, data)
        return packet.to_bytes()

class EnOceanGateway:
    def __init__(self):
        self.devices: Dict[int, EnOceanDevice] = {}

    def add_device(self, device: EnOceanDevice):
        self.devices[device.device_id] = device

    def remove_device(self, device_id: int):
        if device_id in self.devices:
            del self.devices[device_id]

    def send_packet(self, device_id: int, receiver_id: int, data: bytes):
        if device_id in self.devices:
            return self.devices[device_id].send_packet(receiver_id, data)
        else:
            logging.error(f"Device {device_id} not found")
            return None

# Example usage
if __name__ == "__main__":
    gateway = EnOceanGateway()

    # Create devices
    device1 = EnOceanDevice(0x1234, "Lighting")
    device2 = EnOceanDevice(0x5678, "Thermostat")

    # Add devices to gateway
    gateway.add_device(device1)
    gateway.add_device(device2)

    # Send packet from device1 to device2
    data = struct.pack('!B', 0x01)  # Example data
    packet = gateway.send_packet(0x1234, 0x5678, data)
    if packet:
        print(f"Sent packet: {packet.hex()}")
```

### Smart Home System Architecture

```python
# smart_home_system.py

import logging
from typing import Dict, List
from enocean_protocol import EnOceanGateway, EnOceanDevice

class SmartHomeSystem:
    def __init__(self):
        self.gateway = EnOceanGateway()
        self.devices: Dict[int, Dict[str, str]] = {}

    def add_device(self, device_id: int, device_type: str, location: str):
        device = EnOceanDevice(device_id, device_type)
        self.gateway.add_device(device)
        self.devices[device_id] = {"type": device_type, "location": location}

    def remove_device(self, device_id: int):
        self.gateway.remove_device(device_id)
        if device_id in self.devices:
            del self.devices[device_id]

    def control_device(self, device_id: int, command: str):
        if device_id in self.devices:
            # Send command to device using EnOcean protocol
            data = command.encode()
            packet = self.gateway.send_packet(device_id, 0xFFFF, data)
            if packet:
                logging.info(f"Sent command '{command}' to device {device_id}")
            else:
                logging.error(f"Failed to send command to device {device_id}")
        else:
            logging.error(f"Device {device_id} not found")

    def get_device_status(self, device_id: int) -> Dict[str, str]:
        if device_id in self.devices:
            return self.devices[device_id]
        else:
            logging.error(f"Device {device_id} not found")
            return {}

# Example usage
if __name__ == "__main__":
    system = SmartHomeSystem()

    # Add devices
    system.add_device(0x1234, "Lighting", "Living Room")
    system.add_device(0x5678, "Thermostat", "Bedroom")

    # Control device
    system.control_device(0x1234, "Turn On")

    # Get device status
    status = system.get_device_status(0x5678)
    print(f"Device status: {status}")
```

### Device Controllers

```python
# device_controllers.py

from typing import Dict
from smart_home_system import SmartHomeSystem

class LightingController:
    def __init__(self, system: SmartHomeSystem):
        self.system = system

    def turn_on(self, device_id: int):
        self.system.control_device(device_id, "Turn On")

    def turn_off(self, device_id: int):
        self.system.control_device(device_id, "Turn Off")

class ThermostatController:
    def __init__(self, system: SmartHomeSystem):
        self.system = system

    def set_temperature(self, device_id: int, temperature: int):
        self.system.control_device(device_id, f"Set Temperature {temperature}")

# Example usage
if __name__ == "__main__":
    system = SmartHomeSystem()

    # Add devices
    system.add_device(0x1234, "Lighting", "Living Room")
    system.add_device(0x5678, "Thermostat", "Bedroom")

    # Create controllers
    lighting_controller = LightingController(system)
    thermostat_controller = ThermostatController(system)

    # Control devices
    lighting_controller.turn_on(0x1234)
    thermostat_controller.set_temperature(0x5678, 22)
```

### Web Interface

```python
# web_interface.py

from flask import Flask, request, jsonify
from smart_home_system import SmartHomeSystem

app = Flask(__name__)

system = SmartHomeSystem()

# Add devices
system.add_device(0x1234, "Lighting", "Living Room")
system.add_device(0x5678, "Thermostat", "Bedroom")

@app.route('/devices', methods=['GET'])
def get_devices():
    devices = []
    for device_id, device_info in system.devices.items():
        devices.append({"id": device_id, "type": device_info["type"], "location": device_info["location"]})
    return jsonify(devices)

@app.route('/devices/<int:device_id>/control', methods=['POST'])
def control_device(device_id):
    command = request.json["command"]
    system.control_device(device_id, command)
    return jsonify({"success": True})

@app.route('/devices/<int:device_id>/status', methods=['GET'])
def get_device_status(device_id):
    status = system.get_device_status(device_id)
    return jsonify(status)

if __name__ == "__main__":
    app.run(debug=True)
```
