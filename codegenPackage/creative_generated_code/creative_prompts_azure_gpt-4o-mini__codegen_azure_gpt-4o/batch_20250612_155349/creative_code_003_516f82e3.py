"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chiller-york.ru
Prompt: Generate a checklist for the annual maintenance of York chillers, including specific tasks like compressor replacement and refrigerant leak detection.
Generated: DETERMINISTIC_516f82e36b8fa2f6
Batch ID: 20250612_155349
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

def generate_maintenance_checklist():
    """
    Generates a checklist for the annual maintenance of York chillers.
    Includes tasks like compressor replacement and refrigerant leak detection.
    """
    checklist = [
        {
            "task": "Visual inspection of chiller components",
            "description": "Inspect all visible components for signs of wear, corrosion, or damage.",
            "priority": "High",
        },
        {
            "task": "Compressor replacement",
            "description": "Replace the compressor if it shows signs of excessive wear, overheating, or reduced performance.",
            "priority": "Critical",
        },
        {
            "task": "Refrigerant leak detection",
            "description": "Inspect the system for refrigerant leaks using an electronic leak detector or soap solution.",
            "priority": "High",
        },
        {
            "task": "Check oil levels and quality",
            "description": "Verify that oil levels are sufficient and the oil is free of contaminants.",
            "priority": "Medium",
        },
        {
            "task": "Clean condenser coils",
            "description": "Remove debris and clean the coils to improve heat transfer efficiency.",
            "priority": "High",
        },
        {
            "task": "Inspect electrical connections",
            "description": "Ensure all wiring and connections are secure and free of damage.",
            "priority": "Medium",
        },
        {
            "task": "Test safety controls",
            "description": "Verify that all safety controls are operational, including high-pressure and low-pressure cutouts.",
            "priority": "Critical",
        },
        {
            "task": "Lubricate moving parts",
            "description": "Lubricate bearings, motors, and other moving parts to reduce wear and ensure smooth operation.",
            "priority": "Medium",
        },
        {
            "task": "Verify operational efficiency",
            "description": "Run the chiller and verify that it performs within expected efficiency levels.",
            "priority": "High",
        }
    ]
    return checklist

def save_checklist_to_file(checklist, filename="york_chiller_maintenance.json"):
    """
    Saves the maintenance checklist to a JSON file.

    Args:
        checklist (list): The checklist to save.
        filename (str): The name of the file to save the checklist in (default: 'york_chiller_maintenance.json').
    """
    try:
        with open(filename, "w") as file:
            json.dump(checklist, file, indent=4)
        print(f"Checklist successfully saved to {filename}")
    except Exception as e:
        print(f"Error saving checklist to file: {e}")

def main():
    """
    Main function to generate and save the York chillers maintenance checklist.
    """
    checklist = generate_maintenance_checklist()
    save_checklist_to_file(checklist)

if __name__ == "__main__":
    main()
```
