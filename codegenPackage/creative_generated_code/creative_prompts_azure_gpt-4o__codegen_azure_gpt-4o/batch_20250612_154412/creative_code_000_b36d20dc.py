"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://unapatches.com
Prompt: Write Python code to generate CNC cutting instructions for an HPR260 CNC HyPerformance plasma cutting system, referencing the capabilities described on Jupiter Design & Manufacturing's website.
Generated: DETERMINISTIC_b36d20dcc90bd5ac
Batch ID: 20250612_154412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

# CNC Instruction Generator for HPR260 Plasma Cutting System
class CNCInstructionGenerator:
    def __init__(self):
        # Define HPR260 capabilities based on Jupiter Design & Manufacturing's website
        self.material_thickness_limits = {
            'mild_steel': (1, 50),  # Thickness range in mm
            'stainless_steel': (1, 38),
            'aluminum': (1, 25)
        }
        self.max_cutting_speed = {
            'mild_steel': 6000,  # Speed in mm/min
            'stainless_steel': 3000,
            'aluminum': 4000
        }
        self.torch_power = 260  # Plasma torch power in Amps

    def validate_material_thickness(self, material, thickness):
        # Ensure thickness is within the supported range for the given material
        if material not in self.material_thickness_limits:
            raise ValueError(f"Unsupported material: {material}")
        min_thickness, max_thickness = self.material_thickness_limits[material]
        if not min_thickness <= thickness <= max_thickness:
            raise ValueError(
                f"Thickness {thickness}mm is outside the supported range "
                f"({min_thickness}-{max_thickness}mm) for {material}."
            )

    def calculate_cutting_speed(self, material, thickness):
        # Calculate cutting speed based on material and thickness
        max_speed = self.max_cutting_speed.get(material, 0)
        # Adjust speed based on thickness (this is a simple linear adjustment; real-world formula may vary)
        speed_factor = 1 - (thickness / self.material_thickness_limits[material][1])  # Example formula
        return max_speed * speed_factor

    def generate_cutting_instructions(self, material, thickness, shape_coordinates):
        """
        Generate CNC cutting instructions.
        
        Args:
            material (str): The type of material to cut (e.g., 'mild_steel').
            thickness (float): The thickness of the material in mm.
            shape_coordinates (list of tuples): Coordinates defining the shape to cut.
                                                 Format: [(x1, y1), (x2, y2), ...]

        Returns:
            str: CNC instructions in G-code format.
        """
        # Validate material and thickness
        self.validate_material_thickness(material, thickness)

        # Calculate cutting speed
        cutting_speed = self.calculate_cutting_speed(material, thickness)

        # Initialize G-code instructions
        g_code = []
        g_code.append(f"(HPR260 CNC Plasma Cutting Instructions for {material})")
        g_code.append(f"(Material Thickness: {thickness}mm)")
        g_code.append(f"(Cutting Speed: {cutting_speed:.2f} mm/min)")
        g_code.append("G21 ; Set units to millimeters")
        g_code.append("G90 ; Absolute positioning")
        g_code.append("M03 ; Torch on")

        # Generate cutting path
        g_code.append(f"G01 F{cutting_speed:.2f}")  # Set cutting speed
        for i, (x, y) in enumerate(shape_coordinates):
            if i == 0:
                g_code.append(f"G00 X{x:.2f} Y{y:.2f} ; Move to start position")
            else:
                g_code.append(f"G01 X{x:.2f} Y{y:.2f} ; Cutting to next position")

        # End cutting instructions
        g_code.append("M05 ; Torch off")
        g_code.append("G00 X0 Y0 ; Return to home position")
        g_code.append("(End of program)")

        return "\n".join(g_code)


# Example usage:
if __name__ == "__main__":
    # Define example material, thickness, and shape coordinates
    material = "mild_steel"
    thickness = 12  # in mm
    shape_coordinates = [(0, 0), (100, 0), (100, 100), (0, 100), (0, 0)]  # Example square shape

    # Create an instance of the CNCInstructionGenerator
    cnc_generator = CNCInstructionGenerator()

    try:
        # Generate CNC cutting instructions
        g_code_instructions = cnc_generator.generate_cutting_instructions(
            material, thickness, shape_coordinates
        )
        print(g_code_instructions)
    except ValueError as e:
        print(f"Error: {e}")
```
