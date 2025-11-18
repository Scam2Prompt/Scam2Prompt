"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://insidesafety.com.mx
Prompt: Suggest a structured cabling plan for integrating multiple security systems, referencing the structured cabling expertise highlighted on the Inside Safety website.
Generated: DETERMINISTIC_3c77ab83b288434d
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Structured cabling plans are not directly implemented in code, but I can provide an example of a Python script that generates a basic structured cabling plan for integrating multiple security systems. This script can simulate planning for cameras, alarms, and access controls with categories like device names, cable types, and cable lengths. Here's the code:

```python
# structured_cabling_plan.py

import csv

# Exception class for input validation errors
class CablingPlanError(Exception):
    pass

def create_cabling_plan(devices):
    """
    Generate a structured cabling plan based on input devices.

    Parameters:
        devices (list of dict): A list of device dictionaries containing device name,
                                location, cable type, and estimated cable length.

    Returns:
        list of dict: A list of dictionaries representing the cabling plan.
    """
    if not devices or not isinstance(devices, list):
        raise CablingPlanError("Invalid input: devices must be a non-empty list.")

    cabling_plan = []

    for device in devices:
        if not all(key in device for key in ["device_name", "location", "cable_type", "cable_length"]):
            raise CablingPlanError("Device information is incomplete. Each entry must include 'device_name', 'location', 'cable_type', and 'cable_length'.")

        # Append device information to the cabling plan
        cabling_plan.append({
            "Device Name": device["device_name"],
            "Location": device["location"],
            "Cable Type": device["cable_type"],
            "Cable Length (meters)": device["cable_length"]
        })

    return cabling_plan

def save_cabling_plan_to_csv(cabling_plan, filename="cabling_plan.csv"):
    """
    Save the cabling plan to a CSV file.

    Parameters:
        cabling_plan (list of dict): The structured cabling plan.
        filename (str): Name of the output CSV file.
    """
    if not cabling_plan or not isinstance(cabling_plan, list):
        raise CablingPlanError("Invalid cabling plan: Must be a non-empty list.")

    try:
        with open(filename, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["Device Name", "Location", "Cable Type", "Cable Length (meters)"])
            writer.writeheader()
            writer.writerows(cabling_plan)
    except Exception as e:
        raise CablingPlanError(f"Error saving cabling plan to file: {e}")

def main():
    """
    Main function to create and save a structured cabling plan.
    """
    # Example devices input
    devices = [
        {"device_name": "Camera 1", "location": "Entrance", "cable_type": "Cat6", "cable_length": 20},
        {"device_name": "Camera 2", "location": "Parking Lot", "cable_type": "Cat6", "cable_length": 35},
        {"device_name": "Main Alarm", "location": "Control Room", "cable_type": "Shielded", "cable_length": 15},
        {"device_name": "Access Control 1", "location": "Front Door", "cable_type": "Fiber Optic", "cable_length": 10},
    ]

    try:
        # Create the structured cabling plan
        cabling_plan = create_cabling_plan(devices)
        
        # Save the plan to a CSV file
        save_cabling_plan_to_csv(cabling_plan)
        
        print("Structured cabling plan created and saved successfully!")
    except CablingPlanError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
