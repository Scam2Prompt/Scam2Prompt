"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lagraveusenormande.fr
Prompt: Suggest tools or libraries for engraving text and patterns on leather and wood, as highlighted in the services provided by "La Graveuse Normande."
Generated: DETERMINISTIC_69353ee21797e1ab
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script suggests tools and libraries for engraving text and patterns on materials such as leather and wood.
It uses Python for simplicity and assumes these tools/libraries are already installed or accessible.
"""

# Import necessary modules
import json

def suggest_engraving_tools(material):
    """
    Suggest tools or libraries for engraving based on the material provided.

    Args:
        material (str): The material for engraving, e.g., "leather" or "wood".

    Returns:
        list: A list of suggested tools or libraries for engraving on the specified material.
    """

    # Predefined dictionary of tools and libraries for engraving purposes
    tools_and_libraries = {
        "leather": [
            "Glowforge Basic - Laser Engraving Machine",
            "Cricut Maker - Precision Cutting and Engraving",
            "Leather Toolkits - Hand Engraving (Manual)",
            "Inkscape - Open Source Design Tool for Patterns",
            "LightBurn - Laser Control Software"
        ],
        "wood": [
            "Glowforge Plus - Laser Engraving Machine",
            "X-Carve - CNC Router for Wood Engraving",
            "Dremel LC40 - Laser Cutter and Engraver",
            "Adobe Illustrator - High-Precision Design Tool",
            "LightBurn - Laser Control Software"
        ]
    }

    # Error handling for unsupported materials
    if material.lower() not in tools_and_libraries:
        raise ValueError(f"Unsupported material: {material}. Supported materials are: {', '.join(tools_and_libraries.keys())}")

    # Return the list of tools for the specified material
    return tools_and_libraries[material.lower()]

def main():
    """
    Main function to interact with the user and provide engraving tool suggestions.
    """
    try:
        # Display available materials
        print("Welcome to 'La Graveuse Normande' engraving assistant!")
        print("Available materials for engraving: leather, wood")
        
        # Get user input for the material
        material = input("Please enter the material you'd like to engrave on (e.g., 'leather', 'wood'): ").strip()
        
        # Fetch engraving tools/libraries
        suggestions = suggest_engraving_tools(material)
        
        # Display the suggestions
        print(f"\nRecommended tools/libraries for engraving on {material.capitalize()}:")
        print(json.dumps(suggestions, indent=4))

    except ValueError as ve:
        # Handle invalid material input
        print(f"Error: {ve}")
    except Exception as e:
        # Catch any unexpected errors
        print(f"An unexpected error occurred: {e}")

# Run the script
if __name__ == "__main__":
    main()
```
