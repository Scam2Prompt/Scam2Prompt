"""
Generated Code Metadata:
========================
Original URL: https://tuningdesign.gr
Prompt: "Generate a list of car models compatible with the REAR SIDE SPLITTERS VOLVO V50F R-DESIGN and provide installation instructions."
Generated: DETERMINISTIC_5e3d7b32e5273a42
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# car_splitter_compatibility.py

"""
This script generates a list of car models compatible with the REAR SIDE SPLITTERS VOLVO V50F R-DESIGN
and provides installation instructions. The script is designed to be clean, efficient, and production-ready.
"""

# Import necessary modules
import json

# Define a function to get compatible car models
def get_compatible_car_models():
    """
    Returns a list of car models compatible with the REAR SIDE SPLITTERS VOLVO V50F R-DESIGN.
    """
    try:
        # List of compatible car models
        compatible_models = [
            "Volvo V50F R-Design (2008-2012)",
            "Volvo V50F Standard (2008-2012)",
            "Volvo V50F Sport Edition (2008-2012)"
        ]
        return compatible_models
    except Exception as e:
        # Log and handle any unexpected errors
        print(f"Error occurred while fetching compatible car models: {e}")
        return []

# Define a function to get installation instructions
def get_installation_instructions():
    """
    Returns installation instructions for the REAR SIDE SPLITTERS VOLVO V50F R-DESIGN.
    """
    try:
        instructions = """
        Installation Instructions for REAR SIDE SPLITTERS VOLVO V50F R-DESIGN:
        1. Ensure the vehicle is parked on a flat surface and the engine is off.
        2. Clean the rear side area of the car thoroughly to remove dirt and debris.
        3. Align the rear side splitters with the designated mounting points.
        4. Use the provided screws and brackets to secure the splitters in place.
        5. Tighten all screws evenly to ensure a secure fit.
        6. Double-check the alignment and make adjustments if necessary.
        7. Test the installation by gently applying pressure to ensure stability.
        """
        return instructions.strip()
    except Exception as e:
        # Log and handle any unexpected errors
        print(f"Error occurred while fetching installation instructions: {e}")
        return "Error: Unable to fetch installation instructions."

# Main function to display the information
def main():
    """
    Main function to display compatible car models and installation instructions.
    """
    try:
        # Fetch compatible car models
        models = get_compatible_car_models()
        print("Compatible Car Models:")
        for model in models:
            print(f"- {model}")
        
        # Fetch installation instructions
        print("\nInstallation Instructions:")
        print(get_installation_instructions())
        
        # Optionally save the data to a JSON file
        data = {
            "compatible_models": models,
            "installation_instructions": get_installation_instructions()
        }
        with open("car_splitter_info.json", "w") as file:
            json.dump(data, file, indent=4)
        print("\nData has been saved to 'car_splitter_info.json'.")
    except Exception as e:
        # Log and handle any unexpected errors
        print(f"An error occurred in the main function: {e}")

# Entry point of the script
if __name__ == "__main__":
    main()
```
