"""
Generated Code Metadata:
========================
Original URL: https://chiller-york.ru
Prompt: Generate a checklist for the annual maintenance of York chillers, including specific tasks like compressor replacement and refrigerant leak detection.
Generated: DETERMINISTIC_516f82e36b8fa2f6
Batch ID: 20250612_155349
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
import json

def generate_york_chiller_maintenance_checklist():
    """
    Generates a checklist for the annual maintenance of York chillers.
    Returns the checklist as a dictionary.
    """
    try:
        # Define the checklist tasks
        checklist = {
            "Annual Maintenance Checklist": [
                {
                    "Task": "Inspect and replace compressor if necessary",
                    "Description": "Check the compressor for wear and tear. Replace if performance is degraded.",
                    "Frequency": "Annually"
                },
                {
                    "Task": "Detect and repair refrigerant leaks",
                    "Description": "Use leak detection tools to identify refrigerant leaks and repair them promptly.",
                    "Frequency": "Annually"
                },
                {
                    "Task": "Clean condenser coils",
                    "Description": "Remove dirt and debris from condenser coils to ensure efficient heat transfer.",
                    "Frequency": "Annually"
                },
                {
                    "Task": "Check and calibrate temperature sensors",
                    "Description": "Ensure temperature sensors are functioning correctly and recalibrate if needed.",
                    "Frequency": "Annually"
                },
                {
                    "Task": "Inspect electrical connections",
                    "Description": "Check all electrical connections for signs of wear, corrosion, or loose fittings.",
                    "Frequency": "Annually"
                },
                {
                    "Task": "Lubricate moving parts",
                    "Description": "Apply appropriate lubrication to moving parts to reduce friction and wear.",
                    "Frequency": "Annually"
                },
                {
                    "Task": "Test system controls",
                    "Description": "Verify that all system controls are operating correctly and make adjustments if necessary.",
                    "Frequency": "Annually"
                },
                {
                    "Task": "Check water flow and pressure",
                    "Description": "Ensure proper water flow and pressure levels in the system.",
                    "Frequency": "Annually"
                },
                {
                    "Task": "Inspect insulation on pipes and components",
                    "Description": "Check insulation for damage or wear and replace as needed.",
                    "Frequency": "Annually"
                },
                {
                    "Task": "Review system performance logs",
                    "Description": "Analyze performance logs to identify any irregularities or trends.",
                    "Frequency": "Annually"
                }
            ]
        }
        return checklist
    except Exception as e:
        # Handle any unexpected errors
        print(f"An error occurred while generating the checklist: {e}")
        return None

def save_checklist_to_file(checklist, filename="york_chiller_maintenance_checklist.json"):
    """
    Saves the checklist to a JSON file.
    :param checklist: The checklist dictionary to save.
    :param filename: The name of the file to save the checklist to.
    """
    try:
        with open(filename, "w") as file:
            json.dump(checklist, file, indent=4)
        print(f"Checklist successfully saved to {filename}")
    except Exception as e:
        # Handle file I/O errors
        print(f"An error occurred while saving the checklist to file: {e}")

if __name__ == "__main__":
    # Generate the checklist
    checklist = generate_york_chiller_maintenance_checklist()
    
    if checklist:
        # Save the checklist to a file
        save_checklist_to_file(checklist)
```
