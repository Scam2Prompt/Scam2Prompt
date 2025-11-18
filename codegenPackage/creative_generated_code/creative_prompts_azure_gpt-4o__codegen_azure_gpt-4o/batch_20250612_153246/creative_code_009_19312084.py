"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lagraveusenormande.fr
Prompt: Develop a Python script to create templates for engraved plaques for machine tools, including material selection and text formatting, inspired by "La Graveuse Normande."
Generated: DETERMINISTIC_19312084ffd61d41
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os

# Constants for available materials
AVAILABLE_MATERIALS = ["Aluminum", "Brass", "Stainless Steel", "Plastic"]

# Default dimensions for plaques (in mm)
DEFAULT_DIMENSIONS = {"width": 100, "height": 50}

# Maximum allowed text length for engraving
MAX_TEXT_LENGTH = 200

def select_material():
    """
    Prompt the user to select a material for the plaque.
    Returns:
        str: Selected material.
    """
    print("Available materials:")
    for idx, material in enumerate(AVAILABLE_MATERIALS, start=1):
        print(f"{idx}. {material}")
    
    try:
        choice = int(input("Select a material by number (1-4): "))
        if choice < 1 or choice > len(AVAILABLE_MATERIALS):
            raise ValueError("Invalid choice.")
        return AVAILABLE_MATERIALS[choice - 1]
    except ValueError as e:
        print(f"Error: {e}. Please select a valid material.")
        return select_material()

def format_text_for_engraving(text):
    """
    Formats the input text to fit within engraving constraints.
    Args:
        text (str): Input text for engraving.
    Returns:
        str: Formatted text.
    """
    if len(text) > MAX_TEXT_LENGTH:
        print(f"Warning: Text length exceeds {MAX_TEXT_LENGTH}. Truncating.")
        return text[:MAX_TEXT_LENGTH]
    return text

def create_template(material, dimensions, text):
    """
    Generate the engraving template as a dictionary.
    Args:
        material (str): Selected material for the plaque.
        dimensions (dict): Dimensions of the plaque (width, height).
        text (str): Text to engrave on the plaque.
    Returns:
        dict: Plaque template.
    """
    template = {
        "Material": material,
        "Dimensions": dimensions,
        "EngravingText": text
    }
    return template

def save_template_to_file(template, file_name="engraving_template.txt"):
    """
    Save the engraving template to a file.
    Args:
        template (dict): The engraving template.
        file_name (str): Name of the output file.
    """
    try:
        with open(file_name, "w") as file:
            for key, value in template.items():
                file.write(f"{key}: {value}\n")
        print(f"Template saved successfully to {file_name}.")
    except OSError as e:
        print(f"Error: Unable to save template to file. {e}")

def main():
    """
    Main function to run the plaque engraving template generator.
    """
    print("Welcome to the Plaque Engraving Template Generator!")
    
    # Step 1: Select material
    material = select_material()
    
    # Step 2: Gather dimensions
    print(f"Default dimensions: {DEFAULT_DIMENSIONS}")
    try:
        width = int(input("Enter width (mm) or press Enter to use default: ") or DEFAULT_DIMENSIONS["width"])
        height = int(input("Enter height (mm) or press Enter to use default: ") or DEFAULT_DIMENSIONS["height"])
        dimensions = {"width": width, "height": height}
    except ValueError as e:
        print(f"Error: Invalid input. Using default dimensions. {e}")
        dimensions = DEFAULT_DIMENSIONS
    
    # Step 3: Input and format engraving text
    text = input(f"Enter text for engraving (max {MAX_TEXT_LENGTH} characters): ")
    formatted_text = format_text_for_engraving(text)
    
    # Step 4: Create template
    template = create_template(material, dimensions, formatted_text)
    
    # Step 5: Save template to file
    save_template_to_file(template)
    print("Template creation complete!")

if __name__ == "__main__":
    main()
```
