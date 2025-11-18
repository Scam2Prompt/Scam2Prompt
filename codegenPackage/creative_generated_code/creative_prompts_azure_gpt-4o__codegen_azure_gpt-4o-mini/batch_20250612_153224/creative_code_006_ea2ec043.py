"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solucionestecnologicasbogota.com
Prompt: Write code to implement a vehicle access control system using barriers and automation, referencing the solutions for access control systems described by Space Technologies Bogotá.
Generated: DETERMINISTIC_ea2ec0434b8e3841
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import random
import logging

# Configure logging for the system
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class VehicleAccessControlSystem:
    def __init__(self):
        # Initialize the access control system
        self.allowed_vehicles = set()  # Set of allowed vehicle IDs
        self.barrier_status = 'CLOSED'  # Initial status of the barrier
        self.access_attempts = []  # Track access attempts for logging

    def add_allowed_vehicle(self, vehicle_id):
        """Add a vehicle ID to the allowed vehicles list."""
        self.allowed_vehicles.add(vehicle_id)
        logging.info(f"Vehicle {vehicle_id} added to allowed vehicles.")

    def remove_allowed_vehicle(self, vehicle_id):
        """Remove a vehicle ID from the allowed vehicles list if it exists."""
        if vehicle_id in self.allowed_vehicles:
            self.allowed_vehicles.remove(vehicle_id)
            logging.info(f"Vehicle {vehicle_id} removed from allowed vehicles.")
        else:
            logging.warning(f"Attempted to remove a non-existing vehicle ID: {vehicle_id}")

    def check_access(self, vehicle_id):
        """Check if a vehicle is allowed access."""
        if vehicle_id in self.allowed_vehicles:
            logging.info(f"Access granted for vehicle ID: {vehicle_id}")
            self.open_barrier()
            return True
        else:
            logging.warning(f"Access denied for vehicle ID: {vehicle_id}")
            self.log_access_attempt(vehicle_id, success=False)
            return False

    def open_barrier(self):
        """Open the access barrier and schedule it to close after a delay."""
        if self.barrier_status == 'CLOSED':
            self.barrier_status = 'OPEN'
            logging.info("Barrier opened.")
            # Simulate barrier being open for a period
            time.sleep(5)  # Barrier stays open for 5 seconds
            self.close_barrier()
        else:
            logging.warning("Attempted to open the barrier, but it is already open.")

    def close_barrier(self):
        """Close the access barrier."""
        self.barrier_status = 'CLOSED'
        logging.info("Barrier closed.")

    def log_access_attempt(self, vehicle_id, success):
        """Log the access attempt."""
        attempt_record = {
            'vehicle_id': vehicle_id,
            'success': success,
            'timestamp': time.time()
        }
        self.access_attempts.append(attempt_record)
        logging.info(f"Access attempt logged: {attempt_record}")

    def simulate_access(self):
        """Simulate random access attempts for testing."""
        test_vehicles = ['ABC123', 'XYZ456', 'LMN789']
        for _ in range(10):
            vehicle_id = random.choice(test_vehicles + ['INVALID_VEHICLE'])
            self.check_access(vehicle_id)
            time.sleep(1)  # Delay between attempts

if __name__ == "__main__":
    # Instantiate the vehicle access control system
    access_control_system = VehicleAccessControlSystem()

    # Populate with some allowed vehicles
    access_control_system.add_allowed_vehicle('ABC123')
    access_control_system.add_allowed_vehicle('XYZ456')

    # Simulate vehicle access attempts
    access_control_system.simulate_access()
```
