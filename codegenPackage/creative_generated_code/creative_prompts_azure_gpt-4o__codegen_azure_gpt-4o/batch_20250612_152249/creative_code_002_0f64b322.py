"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://novaforma.hr
Prompt: Generate code to model and render 3D designs for neon signs using CAD software, incorporating Nova Forma's expertise in plexiglass and aluminum processing.
Generated: DETERMINISTIC_0f64b3221d693423
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import cadquery as cq  # CAD software library for 3D modeling

# Constants for neon sign dimensions and materials
SIGN_WIDTH = 500  # Width of the neon sign in mm
SIGN_HEIGHT = 300  # Height of the neon sign in mm
SIGN_DEPTH = 50  # Depth of the neon sign in mm
PLEXIGLASS_THICKNESS = 5  # Thickness of the plexiglass base in mm
ALUMINUM_FRAME_THICKNESS = 10  # Thickness of the aluminum frame in mm
NEON_TUBE_RADIUS = 3  # Radius of the neon tubes in mm

# Function to create the plexiglass base
def create_plexiglass_base(width, height, thickness):
    """
    Creates the plexiglass base for the neon sign.

    :param width: Width of the base in mm
    :param height: Height of the base in mm
    :param thickness: Thickness of the base in mm
    :return: 3D model of the plexiglass base
    """
    return cq.Workplane("XY").box(width, height, thickness)

# Function to create the aluminum frame
def create_aluminum_frame(width, height, depth, frame_thickness):
    """
    Creates the aluminum frame for the neon sign.

    :param width: Width of the sign in mm
    :param height: Height of the sign in mm
    :param depth: Depth of the sign in mm
    :param frame_thickness: Thickness of the aluminum frame in mm
    :return: 3D model of the aluminum frame
    """
    outer_frame = cq.Workplane("XY").box(width, height, depth)
    inner_cutout = cq.Workplane("XY").box(
        width - 2 * frame_thickness,
        height - 2 * frame_thickness,
        depth - frame_thickness,
    )
    return outer_frame.cut(inner_cutout)

# Function to create neon tubes in a custom design
def create_neon_tube(design_path, tube_radius):
    """
    Creates neon tubes based on a custom design path.

    :param design_path: List of (x, y, z) coordinates for the neon tube path
    :param tube_radius: Radius of the neon tube in mm
    :return: 3D model of the neon tube
    """
    # Create a wire path from the design coordinates
    path = cq.Workplane("XY").polyline(design_path)
    # Sweep a circular profile along the path
    return path.sweep(cq.Workplane("XY").circle(tube_radius))

# Function to assemble the neon sign
def assemble_neon_sign(base, frame, tubes):
    """
    Assembles the entire neon sign with base, frame, and tubes.

    :param base: Plexiglass base model
    :param frame: Aluminum frame model
    :param tubes: List of neon tube models
    :return: Assembled 3D model of the neon sign
    """
    assembly = base.union(frame)
    for tube in tubes:
        assembly = assembly.union(tube)
    return assembly

# Main function
def main():
    try:
        # Step 1: Create the plexiglass base
        plexiglass_base = create_plexiglass_base(SIGN_WIDTH, SIGN_HEIGHT, PLEXIGLASS_THICKNESS)

        # Step 2: Create the aluminum frame
        aluminum_frame = create_aluminum_frame(SIGN_WIDTH, SIGN_HEIGHT, SIGN_DEPTH, ALUMINUM_FRAME_THICKNESS)

        # Step 3: Define neon tube design paths
        # Example path: A simple zigzag design
        design_paths = [
            [(50, 50, 0), (200, 100, 0), (350, 50, 0)],  # Path 1
            [(50, 250, 0), (200, 200, 0), (350, 250, 0)],  # Path 2
        ]

        # Step 4: Create neon tubes
        neon_tubes = [create_neon_tube(path, NEON_TUBE_RADIUS) for path in design_paths]

        # Step 5: Assemble the neon sign
        neon_sign = assemble_neon_sign(plexiglass_base, aluminum_frame, neon_tubes)

        # Step 6: Export the final design to a file
        neon_sign.exportStep("neon_sign.step")  # Export as STEP file for CAD software
        print("Neon sign design successfully exported to 'neon_sign.step'.")

    except Exception as e:
        print(f"An error occurred during the design process: {e}")

# Run the main function
if __name__ == "__main__":
    main()
```
