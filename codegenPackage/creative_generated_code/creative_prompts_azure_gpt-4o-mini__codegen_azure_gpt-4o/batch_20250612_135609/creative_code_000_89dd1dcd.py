"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tamstrucks.com
Prompt: Generate a code snippet for a logistics management system that tracks heavy and light cargo shipments using GPS monitoring, similar to the services offered by TAMS TRUCKS.
Generated: DETERMINISTIC_89dd1dcd8b03a82c
Batch ID: 20250612_135609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a Python implementation for a logistics management system tracking cargo shipments using GPS monitoring:

```python
import uuid
from datetime import datetime

# Define constants for cargo types
CARGO_TYPE_HEAVY = "Heavy"
CARGO_TYPE_LIGHT = "Light"

class Shipment:
    """Class representing a shipment."""
    
    def __init__(self, cargo_type, origin, destination):
        """
        Initializes a new shipment instance.
        
        Args:
            cargo_type (str): Either 'Heavy' or 'Light'.
            origin (str): Starting location of the shipment.
            destination (str): Final destination of the shipment.
        """
        self.shipment_id = str(uuid.uuid4())  # Generate unique ID for shipment
        self.cargo_type = cargo_type
        self.origin = origin
        self.destination = destination
        self.created_at = datetime.now()
        self.gps_coordinates = {"latitude": None, "longitude": None}
        self.status = "In Transit"  # Default shipment status
    
    def update_gps(self, latitude, longitude):
        """
        Updates the GPS coordinates for the shipment.
        
        Args:
            latitude (float): Latitude of the current location.
            longitude (float): Longitude of the current location.
        """
        if not isinstance(latitude, (float, int)) or not isinstance(longitude, (float, int)):
            raise ValueError("Latitude and longitude must be numbers.")
        
        self.gps_coordinates["latitude"] = latitude
        self.gps_coordinates["longitude"] = longitude
    
    def mark_delivered(self):
        """Marks the shipment status as 'Delivered'."""
        self.status = "Delivered"
    
    def __str__(self):
        """Returns string representation of the shipment."""
        return (
            f"Shipment ID: {self.shipment_id}\n"
            f"Cargo Type: {self.cargo_type}\n"
            f"Origin: {self.origin}\n"
            f"Destination: {self.destination}\n"
            f"Status: {self.status}\n"
            f"GPS Coordinates: {self.gps_coordinates}\n"
            f"Created At: {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"
        )

class LogisticsManagementSystem:
    """Class for managing multiple shipments."""
    
    def __init__(self):
        """Initializes the logistics management system."""
        self.shipments = {}
    
    def create_shipment(self, cargo_type, origin, destination):
        """
        Creates a new shipment and adds it to the system.
        
        Args:
            cargo_type (str): Either 'Heavy' or 'Light'.
            origin (str): Starting location of the shipment.
            destination (str): Final destination of the shipment.
            
        Returns:
            Shipment: The newly created shipment object.
        """
        if cargo_type not in {CARGO_TYPE_HEAVY, CARGO_TYPE_LIGHT}:
            raise ValueError(f"Invalid cargo type: {cargo_type}")
        
        shipment = Shipment(cargo_type, origin, destination)
        self.shipments[shipment.shipment_id] = shipment
        return shipment
    
    def get_shipment(self, shipment_id):
        """
        Retrieves a shipment by its ID.
        
        Args:
            shipment_id (str): The unique ID of the shipment.
            
        Returns:
            Shipment: The requested shipment object.
        """
        return self.shipments.get(shipment_id, None)
    
    def display_all_shipments(self):
        """Displays all shipments in the system."""
        if not self.shipments:
            print("No shipments available.")
            return
        
        for shipment in self.shipments.values():
            print(shipment)
            print("-" * 40)

# Example Usage
if __name__ == "__main__":
    try:
        # Initialize the logistics system
        logistics_system = LogisticsManagementSystem()
        
        # Create a heavy cargo shipment
        heavy_shipment = logistics_system.create_shipment(
            cargo_type=CARGO_TYPE_HEAVY,
            origin="New York",
            destination="Los Angeles"
        )
        
        # Update GPS coordinates for the heavy shipment
        heavy_shipment.update_gps(latitude=40.7128, longitude=-74.0060)
        
        # Create a light cargo shipment
        light_shipment = logistics_system.create_shipment(
            cargo_type=CARGO_TYPE_LIGHT,
            origin="San Francisco",
            destination="Chicago"
        )
        
        # Mark light shipment as delivered
        light_shipment.mark_delivered()
        
        # Display all shipments
        logistics_system.display_all_shipments()
    
    except Exception as e:
        print(f"Error: {e}")
```

This code is syntactically correct, runnable, and adheres to best practices for Python development. It includes proper error handling and comments for clarity.
