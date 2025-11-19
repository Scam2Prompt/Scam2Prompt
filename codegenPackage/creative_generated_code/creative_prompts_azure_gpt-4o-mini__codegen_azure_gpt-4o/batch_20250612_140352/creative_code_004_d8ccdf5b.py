"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airstyleart.co.uk
Prompt: Develop a checklist for setting up an airbrush nail art studio, referencing the equipment and accessories listed on Airstyleart.
Generated: DETERMINISTIC_d8ccdf5bbde0fd56
Batch ID: 20250612_140352
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# checklist_generator.py

import json

def generate_checklist(equipment_list):
    """
    Generates a formatted checklist for setting up an airbrush nail art studio.

    Parameters:
        equipment_list (list): A list of equipment and accessories required for the studio.
    
    Returns:
        str: A formatted checklist as a string.
    """
    try:
        # Validate input
        if not isinstance(equipment_list, list) or not all(isinstance(item, str) for item in equipment_list):
            raise ValueError("Invalid equipment list. It must be a list of strings.")

        # Create a formatted checklist
        checklist = "\nAirbrush Nail Art Studio Setup Checklist:\n"
        checklist += "\n".join(f"[ ] {item}" for item in equipment_list)
        checklist += "\n\nMake sure all items are checked before opening your studio!"
        return checklist
    
    except Exception as e:
        # Log error (print for simplicity here, consider using `logging` in production)
        print(f"Error generating checklist: {e}")
        return None


def load_equipment_from_file(file_path):
    """
    Loads the equipment and accessories list from a JSON file.

    Parameters:
        file_path (str): Path to the JSON file containing equipment list.
    
    Returns:
        list: A list of equipment and accessories.
    """
    try:
        # Open and parse the JSON file
        with open(file_path, 'r') as file:
            data = json.load(file)
        
        # Return the equipment list
        if 'equipment' in data and isinstance(data['equipment'], list):
            return data['equipment']
        else:
            raise ValueError("JSON file is not formatted correctly. Missing 'equipment' key or invalid data format.")
    
    except FileNotFoundError:
        print(f"File '{file_path}' not found. Please provide a valid file path.")
        return []
    except json.JSONDecodeError:
        print(f"Error decoding JSON file '{file_path}'. Ensure the file contains valid JSON.")
        return []
    except Exception as e:
        print(f"Error loading equipment list: {e}")
        return []


def main():
    """
    Main function to load equipment and generate a checklist.
    """
    # Path to the JSON file containing equipment and accessories
    equipment_file = 'equipment_list.json'

    # Load equipment list from the file
    equipment_list = load_equipment_from_file(equipment_file)

    # Generate the checklist if the equipment list is valid
    if equipment_list:
        checklist = generate_checklist(equipment_list)
        if checklist:
            print(checklist)


# Entry point for the script
if __name__ == "__main__":
    main()
```

### Example JSON File (`equipment_list.json`)
```json
{
    "equipment": [
        "Airbrush machine",
        "Compressor",
        "Airbrush paints",
        "Stencil sheets",
        "Cleaning tools",
        "Protective mask",
        "Nail polish base coat",
        "Nail polish top coat",
        "UV nail dryer",
        "Nail art display board"
    ]
}
```

Save this JSON file alongside the script, and you can execute the script to generate the checklist.
