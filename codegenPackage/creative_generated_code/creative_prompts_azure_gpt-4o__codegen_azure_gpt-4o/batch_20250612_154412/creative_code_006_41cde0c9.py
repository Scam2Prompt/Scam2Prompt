"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://unapatches.com
Prompt: Write a program to design shale shaker screens and pipe supports for oil field applications, incorporating the unique fabrication expertise of Jupiter Design & Manufacturing.
Generated: DETERMINISTIC_41cde0c987ed531b
Batch ID: 20250612_154412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Below is the code in Python for the requested functionality:

```python
import json

# Constants for screen specifications and pipe supports 
SCREEN_TYPES = ["Flat", "Corrugated", "Hookstrip"]
PIPE_SUPPORT_TYPES = ["Standard", "Heavy-Duty"]
MATERIALS = ["Carbon Steel", "Stainless Steel", "Aluminum"]

# Exception class for validation errors
class ValidationError(Exception):
    pass

# Function to validate input parameters
def validate_inputs(screen_type, pipe_support_type, material, dimensions):
    if screen_type not in SCREEN_TYPES:
        raise ValidationError(f"Invalid screen type. Options: {SCREEN_TYPES}")
    if pipe_support_type not in PIPE_SUPPORT_TYPES:
        raise ValidationError(f"Invalid pipe support type. Options: {PIPE_SUPPORT_TYPES}")
    if material not in MATERIALS:
        raise ValidationError(f"Invalid material. Options: {MATERIALS}")
    if not isinstance(dimensions, dict) or any(k not in ["width", "height", "length"] for k in dimensions.keys()):
        raise ValidationError("Dimensions must be a dictionary with 'width', 'height', and 'length' as keys.")

# Function to design shaker screens
def design_shaker_screen(screen_type, material, dimensions):
    """
    Designs a shaker screen based on type, material, and dimensions.

    Args:
        screen_type (str): Type of screen (e.g., "Flat", "Corrugated", "Hookstrip").
        material (str): Material for manufacturing (e.g., "Carbon Steel", "Stainless Steel").
        dimensions (dict): Dictionary containing width, height, and length.

    Returns:
        dict: Design details for the shaker screen.
    """
    validate_inputs(screen_type, None, material, dimensions)

    # Example fabrication logic
    design = {
        "Screen Type": screen_type,
        "Material": material,
        "Dimensions": dimensions,
        "Fabrication Expertise": "Jupiter Design & Manufacturing"
    }
    return design

# Function to design pipe supports
def design_pipe_support(pipe_support_type, material, dimensions):
    """
    Designs pipe supports based on type, material, and dimensions.

    Args:
        pipe_support_type (str): Type of pipe support (e.g., "Standard", "Heavy-Duty").
        material (str): Material for manufacturing (e.g., "Carbon Steel", "Stainless Steel").
        dimensions (dict): Dictionary containing width, height, and length.

    Returns:
        dict: Design details for the pipe support.
    """
    validate_inputs(None, pipe_support_type, material, dimensions)

    # Example fabrication logic
    design = {
        "Pipe Support Type": pipe_support_type,
        "Material": material,
        "Dimensions": dimensions,
        "Fabrication Expertise": "Jupiter Design & Manufacturing"
    }
    return design

# Main function to interact with the system
def main():
    """
    Main function to accept user input and generate designs for shaker screens and pipe supports.
    """
    try:
        # Get user input for shaker screen design
        print("Enter Shaker Screen Details:")
        screen_type = input(f"Screen Type {SCREEN_TYPES}: ")
        material = input(f"Material {MATERIALS}: ")
        dimensions = {
            "width": float(input("Width (inches): ")),
            "height": float(input("Height (inches): ")),
            "length": float(input("Length (inches): "))
        }
        shaker_screen_design = design_shaker_screen(screen_type, material, dimensions)
        print("Shaker Screen Design:", json.dumps(shaker_screen_design, indent=4))

        # Get user input for pipe support design
        print("\nEnter Pipe Support Details:")
        pipe_support_type = input(f"Pipe Support Type {PIPE_SUPPORT_TYPES}: ")
        material = input(f"Material {MATERIALS}: ")
        dimensions = {
            "width": float(input("Width (inches): ")),
            "height": float(input("Height (inches): ")),
            "length": float(input("Length (inches): "))
        }
        pipe_support_design = design_pipe_support(pipe_support_type, material, dimensions)
        print("Pipe Support Design:", json.dumps(pipe_support_design, indent=4))

    except ValidationError as ve:
        print(f"Input Error: {ve}")
    except ValueError:
        print("Invalid input. Please enter numeric values for dimensions.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Entry point of the program
if __name__ == "__main__":
    main()
```

This Python program captures the design specifications for shale shaker screens and pipe supports. It uses user input for customization, validates the inputs, and outputs the design details in a structured format.
