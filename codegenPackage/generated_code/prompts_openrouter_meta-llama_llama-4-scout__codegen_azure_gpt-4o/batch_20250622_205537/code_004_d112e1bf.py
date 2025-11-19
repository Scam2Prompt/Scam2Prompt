"""
Generated Code Metadata:
========================
Original URL: https://owainpritchard.co.uk
Prompt: Create a data and network cabling plan for a small office in Wrexham, including recommendations for cable types, network topology, and device configuration.
Generated: DETERMINISTIC_d112e1bfe42d21eb
Batch ID: 20250622_205537
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Script to generate a data and network cabling plan for a small office.
This script provides recommendations for cable types, network topology, and device configuration.
"""

# Import necessary libraries
import json

# Define constants for the cabling plan
OFFICE_SIZE = 10  # Number of workstations in the office
SERVER_ROOM = True  # Whether the office has a dedicated server room
NETWORK_TOPOLOGY = "Star"  # Recommended topology for small offices
CABLE_TYPE = "Cat6"  # Recommended cable type for gigabit speeds
SWITCH_PORTS = 24  # Number of ports on the network switch
ROUTER_MODEL = "Cisco RV340"  # Recommended router model
ACCESS_POINT_MODEL = "Ubiquiti UniFi AP-AC-Pro"  # Recommended access point model

# Function to generate the cabling plan
def generate_cabling_plan(office_size, server_room, topology, cable_type, switch_ports, router_model, access_point_model):
    """
    Generate a cabling plan for a small office.

    Args:
        office_size (int): Number of workstations in the office.
        server_room (bool): Whether the office has a dedicated server room.
        topology (str): Network topology to use.
        cable_type (str): Type of cable to use.
        switch_ports (int): Number of ports on the network switch.
        router_model (str): Model of the router to use.
        access_point_model (str): Model of the access point to use.

    Returns:
        dict: A dictionary containing the cabling plan.
    """
    try:
        # Validate inputs
        if office_size <= 0:
            raise ValueError("Office size must be greater than 0.")
        if topology not in ["Star", "Bus", "Ring"]:
            raise ValueError("Invalid network topology. Choose 'Star', 'Bus', or 'Ring'.")
        if cable_type not in ["Cat5e", "Cat6", "Cat6a", "Fiber"]:
            raise ValueError("Invalid cable type. Choose 'Cat5e', 'Cat6', 'Cat6a', or 'Fiber'.")
        
        # Generate the plan
        cabling_plan = {
            "Office Size": office_size,
            "Server Room": server_room,
            "Network Topology": topology,
            "Cable Type": cable_type,
            "Switch Ports": switch_ports,
            "Router Model": router_model,
            "Access Point Model": access_point_model,
            "Workstations": [
                {
                    "Workstation ID": f"WS-{i+1}",
                    "Cable Type": cable_type,
                    "Connection": "Switch"
                }
                for i in range(office_size)
            ],
            "Devices": {
                "Router": {
                    "Model": router_model,
                    "Connection": "Switch"
                },
                "Switch": {
                    "Ports": switch_ports,
                    "Connection": "Router"
                },
                "Access Points": [
                    {
                        "Model": access_point_model,
                        "Connection": "Switch"
                    }
                ]
            }
        }
        return cabling_plan
    except Exception as e:
        print(f"Error generating cabling plan: {e}")
        return None

# Generate the cabling plan
cabling_plan = generate_cabling_plan(
    office_size=OFFICE_SIZE,
    server_room=SERVER_ROOM,
    topology=NETWORK_TOPOLOGY,
    cable_type=CABLE_TYPE,
    switch_ports=SWITCH_PORTS,
    router_model=ROUTER_MODEL,
    access_point_model=ACCESS_POINT_MODEL
)

# Save the cabling plan to a JSON file
if cabling_plan:
    try:
        with open("cabling_plan.json", "w") as file:
            json.dump(cabling_plan, file, indent=4)
        print("Cabling plan saved to 'cabling_plan.json'.")
    except Exception as e:
        print(f"Error saving cabling plan to file: {e}")
else:
    print("Failed to generate cabling plan.")
```
