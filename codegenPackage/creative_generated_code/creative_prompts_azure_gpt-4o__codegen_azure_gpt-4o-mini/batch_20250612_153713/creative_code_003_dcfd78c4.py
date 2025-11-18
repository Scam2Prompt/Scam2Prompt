"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stethevent.org
Prompt: Provide step-by-step instructions to design and 3D print a rotating drying station for fishing lures, similar to the "3D Printed Fishing Lure Rotating Drying Station" project on Instructables.
Generated: DETERMINISTIC_dcfd78c4febb6c22
Batch ID: 20250612_153713
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries for 3D printing design
import cadquery as cq

def create_rotating_drying_station():
    """
    Create a rotating drying station for fishing lures using CadQuery.
    The station consists of a base, a vertical support, and a rotating arm 
    to hold the fishing lures during the drying process.
    """
    
    # Define parameters for the drying station
    base_diameter = 200  # Diameter of the base in mm
    base_height = 10     # Height of the base in mm
    support_height = 150 # Height of the vertical support in mm
    arm_length = 100     # Length of the rotating arm in mm
    arm_thickness = 10   # Thickness of the rotating arm in mm
    
    # Create the base of the drying station
    base = (
        cq.Workplane("XY")
        .circle(base_diameter / 2)
        .extrude(base_height)
    )
    
    # Create the vertical support
    support = (
        cq.Workplane("XY")
        .transformed(offset=(0, 0, base_height))
        .rect(arm_thickness, arm_thickness)
        .extrude(support_height)
    )
    
    # Create the rotating arm
    arm = (
        cq.Workplane("XY")
        .transformed(offset=(0, 0, base_height + support_height))
        .rect(arm_length, arm_thickness)
        .extrude(arm_thickness)
    )
    
    # Combine the base, support, and arm into one solid
    drying_station = base.union(support).union(arm)
    
    # Create a hole for rotation at the joint between support and arm
    rotation_hole = (
        cq.Workplane("XY")
        .transformed(offset=(0, 0, base_height + support_height - arm_thickness / 2))
        .circle(arm_thickness / 2)
        .cutThruAll()
    )
    
    # Finalize the model by cutting out the rotation hole
    drying_station = drying_station.cut(rotation_hole)

    return drying_station

# Function to export the model to an STL file for 3D printing
def export_to_stl(model, filename):
    """
    Export the provided CadQuery model to an STL file.

    :param model: The CadQuery model to export.
    :param filename: The name of the output STL file.
    """
    # Error handling for file export
    try:
        model.exportStl(filename)
        print(f"Model successfully exported to {filename}")
    except Exception as e:
        print(f"An error occurred while exporting the model: {e}")

# Main execution
if __name__ == "__main__":
    # Create the drying station model
    drying_station_model = create_rotating_drying_station()
    
    # Define the output STL filename
    output_filename = "fishing_lure_rotating_drying_station.stl"
    
    # Export the model to an STL file
    export_to_stl(drying_station_model, output_filename)
```
