"""
Generated Code Metadata:
========================
Original URL: https://nyikudesign.com
Prompt: Provide a code example for generating a floor plan with labeled zones (e.g., kitchen, reading area) using a library like AutoCAD or Blender, inspired by Nyiku Design's case studies.
Generated: DETERMINISTIC_e0b74fc084ff5f5a
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Floor Plan Generator with Labeled Zones
This script creates a simple floor plan with labeled zones using the ezdxf library (AutoCAD compatible).
"""

import ezdxf
from ezdxf import units
from ezdxf.enums import TextEntityAlignment

def create_floor_plan(output_file="floor_plan.dxf"):
    """
    Creates a DXF floor plan with labeled zones.
    
    Args:
        output_file (str): Path to save the DXF file
    """
    try:
        # Create a new DXF document
        doc = ezdxf.new(dxfversion='R2010')
        doc.units = units.M
        
        # Add layers for different elements
        doc.layers.add("WALLS", color=7)  # White for walls
        doc.layers.add("ZONES", color=3)  # Green for zones
        doc.layers.add("LABELS", color=5)  # Blue for labels
        
        # Get the modelspace
        msp = doc.modelspace()
        
        # Draw walls (rectangle for simple floor plan)
        msp.add_lwpolyline(
            [(0, 0), (10, 0), (10, 8), (0, 8), (0, 0)],
            dxfattribs={'layer': 'WALLS'}
        )
        
        # Define zones with their positions and sizes
        zones = [
            {"name": "Kitchen", "position": (1, 1), "size": (4, 3)},
            {"name": "Reading Area", "position": (6, 1), "size": (3, 3)},
            {"name": "Living Room", "position": (1, 5), "size": (8, 2)}
        ]
        
        # Draw zones and labels
        for zone in zones:
            x, y = zone["position"]
            width, height = zone["size"]
            
            # Draw zone rectangle
            msp.add_lwpolyline(
                [(x, y), (x + width, y), (x + width, y + height), (x, y + height), (x, y)],
                dxfattribs={'layer': 'ZONES'}
            )
            
            # Add zone label (centered in the zone)
            label_x = x + width / 2
            label_y = y + height / 2
            msp.add_text(
                zone["name"],
                dxfattribs={
                    'layer': 'LABELS',
                    'height': 0.3,
                    'style': 'Standard',
                    'rotation': 0
                }
            ).set_placement(
                (label_x, label_y),
                align=TextEntityAlignment.MIDDLE_CENTER
            )
        
        # Save the DXF document
        doc.saveas(output_file)
        print(f"Floor plan saved to {output_file}")
        
    except Exception as e:
        print(f"Error creating floor plan: {str(e)}")

if __name__ == "__main__":
    create_floor_plan()
```
