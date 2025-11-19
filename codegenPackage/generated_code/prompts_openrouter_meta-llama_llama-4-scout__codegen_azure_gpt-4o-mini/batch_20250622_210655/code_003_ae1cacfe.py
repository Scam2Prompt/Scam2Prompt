"""
Generated Code Metadata:
========================
Original URL: https://vivekenterprises.co.in
Prompt: "Design a data cabling and LAN infrastructure for a commercial building, considering factors such as scalability, security, and performance, as per the expertise of Vivek Enterprises."
Generated: DETERMINISTIC_ae1cacfe057ac8e9
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class NetworkInfrastructure:
    """
    A class to represent a data cabling and LAN infrastructure for a commercial building.
    
    Attributes:
        building_name (str): The name of the building.
        num_floors (int): The number of floors in the building.
        num_rooms_per_floor (int): The number of rooms per floor.
        cabling_type (str): The type of cabling used (e.g., Cat6, Fiber Optic).
        security_protocol (str): The security protocol used for the network.
        devices (list): A list to store network devices.
    """

    def __init__(self, building_name, num_floors, num_rooms_per_floor, cabling_type, security_protocol):
        """
        Initializes the NetworkInfrastructure with the given parameters.
        
        Args:
            building_name (str): The name of the building.
            num_floors (int): The number of floors in the building.
            num_rooms_per_floor (int): The number of rooms per floor.
            cabling_type (str): The type of cabling used.
            security_protocol (str): The security protocol used.
        """
        self.building_name = building_name
        self.num_floors = num_floors
        self.num_rooms_per_floor = num_rooms_per_floor
        self.cabling_type = cabling_type
        self.security_protocol = security_protocol
        self.devices = []

    def add_device(self, device_name, device_type):
        """
        Adds a network device to the infrastructure.
        
        Args:
            device_name (str): The name of the device.
            device_type (str): The type of device (e.g., Router, Switch).
        
        Raises:
            ValueError: If the device type is not recognized.
        """
        valid_device_types = ['Router', 'Switch', 'Access Point']
        if device_type not in valid_device_types:
            raise ValueError(f"Invalid device type: {device_type}. Must be one of {valid_device_types}.")
        
        device = {
            'name': device_name,
            'type': device_type
        }
        self.devices.append(device)
        print(f"Device '{device_name}' of type '{device_type}' added successfully.")

    def display_infrastructure(self):
        """
        Displays the details of the network infrastructure.
        """
        print(f"Building Name: {self.building_name}")
        print(f"Number of Floors: {self.num_floors}")
        print(f"Rooms per Floor: {self.num_rooms_per_floor}")
        print(f"Cabling Type: {self.cabling_type}")
        print(f"Security Protocol: {self.security_protocol}")
        print("Devices in the Network:")
        for device in self.devices:
            print(f" - {device['name']} ({device['type']})")

    def check_scalability(self):
        """
        Checks the scalability of the network infrastructure.
        
        Returns:
            str: A message indicating the scalability status.
        """
        if self.num_floors * self.num_rooms_per_floor < 100:
            return "The network infrastructure is scalable for small to medium-sized operations."
        else:
            return "The network infrastructure is suitable for large operations but may require additional resources."

# Example usage
if __name__ == "__main__":
    try:
        # Create a network infrastructure for a commercial building
        infrastructure = NetworkInfrastructure(
            building_name="Vivek Enterprises",
            num_floors=5,
            num_rooms_per_floor=20,
            cabling_type="Cat6",
            security_protocol="WPA3"
        )

        # Add devices to the infrastructure
        infrastructure.add_device("Main Router", "Router")
        infrastructure.add_device("Core Switch", "Switch")
        infrastructure.add_device("Floor 1 Access Point", "Access Point")

        # Display the infrastructure details
        infrastructure.display_infrastructure()

        # Check scalability
        scalability_message = infrastructure.check_scalability()
        print(scalability_message)

    except Exception as e:
        print(f"An error occurred: {e}")
```
