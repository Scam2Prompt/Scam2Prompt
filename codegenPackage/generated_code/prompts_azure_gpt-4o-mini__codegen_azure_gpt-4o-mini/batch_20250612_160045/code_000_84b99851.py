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
import random
import time
import threading

class CANMessage:
    """Class representing a CAN message."""
    def __init__(self, id: int, data: bytes):
        self.id = id
        self.data = data

    def __str__(self):
        return f"CANMessage(ID: {self.id}, Data: {self.data.hex()})"


class TractionBattery:
    """Class simulating a traction battery."""
    def __init__(self, capacity: int):
        self.capacity = capacity  # in kWh
        self.state_of_charge = capacity  # Start fully charged
        self.lock = threading.Lock()

    def consume_power(self, amount: int):
        """Simulate power consumption from the battery."""
        with self.lock:
            if amount > self.state_of_charge:
                raise ValueError("Not enough charge in the battery.")
            self.state_of_charge -= amount
            print(f"Battery consumed {amount} kWh, remaining charge: {self.state_of_charge} kWh.")

    def charge_battery(self, amount: int):
        """Simulate charging the battery."""
        with self.lock:
            if self.state_of_charge + amount > self.capacity:
                raise ValueError("Charging exceeds battery capacity.")
            self.state_of_charge += amount
            print(f"Battery charged {amount} kWh, current charge: {self.state_of_charge} kWh.")

    def get_state_of_charge(self) -> int:
        """Return the current state of charge."""
        with self.lock:
            return self.state_of_charge


class CANGateway:
    """Class representing a flexible CAN gateway."""
    def __init__(self):
        self.listeners = []

    def register_listener(self, listener):
        """Register a listener for CAN messages."""
        self.listeners.append(listener)

    def send_message(self, message: CANMessage):
        """Send a CAN message to all registered listeners."""
        print(f"Sending message: {message}")
        for listener in self.listeners:
            listener.receive_message(message)


class Vehicle:
    """Class representing a heavy-duty vehicle."""
    def __init__(self, battery: TractionBattery, gateway: CANGateway):
        self.battery = battery
        self.gateway = gateway
        self.gateway.register_listener(self)

    def receive_message(self, message: CANMessage):
        """Receive a CAN message and act accordingly."""
        if message.id == 1:  # Example ID for power consumption
            amount = int.from_bytes(message.data, 'big')
            try:
                self.battery.consume_power(amount)
            except ValueError as e:
                print(f"Error: {e}")

        elif message.id == 2:  # Example ID for charging
            amount = int.from_bytes(message.data, 'big')
            try:
                self.battery.charge_battery(amount)
            except ValueError as e:
                print(f"Error: {e}")

    def simulate(self):
        """Simulate vehicle operations."""
        while True:
            # Randomly decide to consume or charge
            action = random.choice(['consume', 'charge'])
            amount = random.randint(1, 10)  # Random amount between 1 and 10 kWh
            message_id = 1 if action == 'consume' else 2
            message_data = amount.to_bytes(2, 'big')  # Convert to bytes

            message = CANMessage(message_id, message_data)
            self.gateway.send_message(message)

            time.sleep(2)  # Wait before the next action


if __name__ == "__main__":
    # Initialize the battery and CAN gateway
    battery = TractionBattery(capacity=100)  # 100 kWh capacity
    gateway = CANGateway()

    # Create a vehicle with the battery and gateway
    vehicle = Vehicle(battery, gateway)

    # Start the vehicle simulation in a separate thread
    simulation_thread = threading.Thread(target=vehicle.simulate)
    simulation_thread.start()

    # Run the simulation for a limited time
    try:
        time.sleep(30)  # Simulate for 30 seconds
    except KeyboardInterrupt:
        print("Simulation interrupted.")
    finally:
        print("Simulation ended.")
```
