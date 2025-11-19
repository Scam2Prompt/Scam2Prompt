"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniswaphd.de
Prompt: Write a code snippet that simulates the communication between a traction battery and a heavy-duty vehicle using a flexible CAN gateway as described in the UniSwapHD project.
Generated: DETERMINISTIC_84b99851eff7f0eb
Batch ID: 20250612_160045
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import time
import logging
from queue import Queue, Empty
from threading import Thread

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class CANMessage:
    """ Class to represent a CAN message with ID and data payload. """
    
    def __init__(self, msg_id: int, data: bytes):
        self.msg_id = msg_id
        self.data = data
    
    def __str__(self):
        return f'CANMessage(ID={self.msg_id}, Data={self.data.hex()})'


class CANGateway:
    """ A flexible CAN gateway simulating communication with a traction battery. """
    
    def __init__(self):
        self.message_queue = Queue()
        self.running = True
        
    def send_message(self, message: CANMessage):
        """ Sends a CAN message to the queue. """
        logging.debug(f"Sending message: {message}")
        self.message_queue.put(message)

    def receive_message(self):
        """ Receives a CAN message from the queue. """
        try:
            message = self.message_queue.get(timeout=1)  # Wait for a message for up to 1 second
            logging.debug(f"Received message: {message}")
            return message
        except Empty:
            logging.debug("No message received within the timeout period.")
            return None

    def stop(self):
        """ Stops the CAN gateway. """
        self.running = False
        logging.info("Stopping CAN Gateway.")


class BatterySimulator:
    """ Simulates the traction battery and its communication with the CAN gateway. """
    
    def __init__(self, gateway: CANGateway):
        self.gateway = gateway
    
    def simulate_battery_status(self):
        """ Simulates battery status messages. """
        while self.gateway.running:
            # Generate random battery voltage and current values
            voltage = random.uniform(300, 400)  # Example voltage range
            current = random.uniform(-100, 100)  # Example current range
            status_message = CANMessage(0x100, f'{voltage:.2f},{current:.2f}'.encode('utf-8'))
            self.gateway.send_message(status_message)
            time.sleep(2)  # Send a message every 2 seconds


class VehicleSimulator:
    """ Simulates a heavy-duty vehicle that consumes messages from the CAN gateway. """
    
    def __init__(self, gateway: CANGateway):
        self.gateway = gateway
    
    def process_messages(self):
        """ Processes incoming CAN messages from the gateway. """
        while self.gateway.running:
            message = self.gateway.receive_message()
            if message:
                # Process the message (for demonstration, just log it)
                logging.info(f"Processing message: {message}")
            time.sleep(1)  # Check for messages every second


def main():
    """ Main function to start the simulation. """
    gateway = CANGateway()
    battery_simulator = BatterySimulator(gateway)
    vehicle_simulator = VehicleSimulator(gateway)
    
    # Start battery and vehicle simulators in separate threads
    battery_thread = Thread(target=battery_simulator.simulate_battery_status)
    vehicle_thread = Thread(target=vehicle_simulator.process_messages)
    
    battery_thread.start()
    vehicle_thread.start()
    
    try:
        # Run the simulation for a limited time
        time.sleep(20)  # Run for 20 seconds
    except KeyboardInterrupt:
        logging.info("Simulation interrupted by user.")
    finally:
        gateway.stop()  # Stop the gateway
    
    # Wait for threads to finish
    battery_thread.join()
    vehicle_thread.join()
    logging.info("Simulation ended.")


if __name__ == "__main__":
    main()
```
