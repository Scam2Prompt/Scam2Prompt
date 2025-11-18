"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://novaforma.hr
Prompt: Write code to calculate material requirements for constructing freestanding illuminated letters, using Nova Forma's range of materials like aluminum and plexiglass.
Generated: DETERMINISTIC_39a975ae36588110
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Material Requirements Calculator for Illuminated Freestanding Letters
Using Nova Forma's range of materials (Aluminum and Plexiglass)

Assume each letter has the following characteristics:
1. Height (in cm)
2. Width (in cm)
3. Depth (in cm)
4. Material thickness (in cm)
5. Type of illumination (LED strip length required)

This program calculates the total material requirements for constructing letters
and provides estimated costs based on material prices.

Dependencies:
- Python >= 3.6
"""

# Constants for material density and costs (mock values)
ALUMINUM_COST_PER_CM2 = 0.05  # Cost per square centimeter of aluminum
PLEXIGLASS_COST_PER_CM2 = 0.03  # Cost per square centimeter of plexiglass
LED_COST_PER_CM = 0.2  # Cost per centimeter of LED strip

def calculate_material_cost(height: float, width: float, depth: float, material_thickness: float, material_type: str) -> dict:
    """
    Calculate the material cost and LED requirements for a single illuminated letter.

    Parameters:
        height (float): Height of the letter in cm.
        width (float): Width of the letter in cm.
        depth (float): Depth of the letter in cm.
        material_thickness (float): Thickness of the material in cm.
        material_type (str): Material type ('aluminum' or 'plexiglass').

    Returns:
        dict: A dictionary containing material area, cost, and LED requirements.
    """
    # Validate material_type input
    if material_type not in ['aluminum', 'plexiglass']:
        raise ValueError("Invalid material type. Choose 'aluminum' or 'plexiglass'.")

    # Calculate surface area (simplified formula for rectangular letters)
    front_and_back_area = 2 * (height * width)  # Front and back faces
    side_area = 2 * (height * depth) + 2 * (width * depth)  # Sides
    total_material_area = front_and_back_area + side_area

    # Calculate material cost
    material_cost_per_cm2 = ALUMINUM_COST_PER_CM2 if material_type == 'aluminum' else PLEXIGLASS_COST_PER_CM2
    total_material_cost = total_material_area * material_cost_per_cm2

    # Calculate LED strip length (assuming perimeter lighting)
    led_strip_length = 2 * (height + width)

    # Calculate LED strip cost
    led_cost = led_strip_length * LED_COST_PER_CM

    return {
        "material_area_cm2": total_material_area,
        "material_cost": round(total_material_cost, 2),
        "led_strip_length_cm": round(led_strip_length, 2),
        "led_cost": round(led_cost, 2)
    }


def main():
    """
    Main function to handle user input and calculate material requirements for letters.
    """
    print("Material Requirements Calculator for Illuminated Freestanding Letters")

    try:
        # Collect user input
        height = float(input("Enter the height of the letter (cm): "))
        width = float(input("Enter the width of the letter (cm): "))
        depth = float(input("Enter the depth of the letter (cm): "))
        material_thickness = float(input("Enter the material thickness (cm): "))
        material_type = input("Enter the material type ('aluminum' or 'plexiglass'): ").strip().lower()

        # Perform calculation
        result = calculate_material_cost(height, width, depth, material_thickness, material_type)

        # Display results
        print("\nMaterial Requirements and Costs:")
        print(f"Total Material Area: {result['material_area_cm2']} cm²")
        print(f"Material Cost: ${result['material_cost']}")
        print(f"LED Strip Length: {result['led_strip_length_cm']} cm")
        print(f"LED Cost: ${result['led_cost']}")
        print(f"Total Cost: ${result['material_cost'] + result['led_cost']}")
    
    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Entry point
if __name__ == "__main__":
    main()
```
