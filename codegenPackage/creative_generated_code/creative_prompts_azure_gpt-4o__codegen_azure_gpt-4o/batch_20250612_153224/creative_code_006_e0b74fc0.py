"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nyikudesign.com
Prompt: Provide a code example for generating a floor plan with labeled zones (e.g., kitchen, reading area) using a library like AutoCAD or Blender, inspired by Nyiku Design's case studies.
Generated: DETERMINISTIC_e0b74fc084ff5f5a
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a Python example using the `ezdxf` library to generate a floor plan with labeled zones.

```python
# Import the necessary library
import ezdxf

def create_floor_plan(output_file):
    """
    Generates a simple floor plan with labeled zones and saves it to a DXF file.

    Args:
        output_file (str): The name of the output DXF file.
    """
    try:
        # Create a new DXF document
        doc = ezdxf.new()
        msp = doc.modelspace()  # Access the model space where drawings are created

        # Define dimensions for the floor plan (in units)
        width = 1500  # Width of the floor plan
        height = 1000  # Height of the floor plan

        # Draw the boundary of the floor plan
        msp.add_lwpolyline([(0, 0), (width, 0), (width, height), (0, height), (0, 0)],
                           close=True, dxfattribs={"color": 7})  # White color

        # Define zones within the floor plan
        zones = {
            "Kitchen": [(50, 50), (450, 50), (450, 350), (50, 350), (50, 50)],
            "Reading Area": [(500, 50), (950, 50), (950, 350), (500, 350), (500, 50)],
            "Living Room": [(50, 400), (950, 400), (950, 950), (50, 950), (50, 400)]
        }

        # Draw and label each zone
        for zone_name, points in zones.items():
            # Draw the zone boundary
            msp.add_lwpolyline(points, close=True, dxfattribs={"color": 3})  # Green color

            # Calculate the centroid of the zone for placing the label
            centroid_x = sum(point[0] for point in points[:-1]) / len(points[:-1])
            centroid_y = sum(point[1] for point in points[:-1]) / len(points[:-1])

            # Add the label text
            msp.add_text(zone_name, dxfattribs={
                "style": "Standard",
                "height": 20,
                "color": 1  # Red color
            }).set_pos((centroid_x, centroid_y), align="MIDDLE_CENTER")

        # Save the DXF file
        doc.saveas(output_file)
        print(f"Floor plan saved to {output_file}")

    except Exception as e:
        print(f"An error occurred while generating the floor plan: {e}")


if __name__ == "__main__":
    # Generate the floor plan and save it to 'floor_plan.dxf'
    create_floor_plan("floor_plan.dxf")
```

This code generates a DXF file with a simple floor plan containing three labeled zones: Kitchen, Reading Area, and Living Room. You can run this code to produce the DXF file, which can then be opened with AutoCAD or similar software.
