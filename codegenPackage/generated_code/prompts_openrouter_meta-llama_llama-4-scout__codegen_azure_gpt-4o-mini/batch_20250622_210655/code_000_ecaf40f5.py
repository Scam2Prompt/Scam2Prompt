"""
Generated Code Metadata:
========================
Original URL: https://bda.mcupr.ac.th
Prompt: "Generate a Python script to create a 3D model of the Sri Maha Pho Buddha Image using computer-aided design (CAD) software."
Generated: DETERMINISTIC_ecaf40f59094a0c5
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import cadquery as cq

def create_buddha_image():
    """
    Create a 3D model of the Sri Maha Pho Buddha Image using CadQuery.
    
    Returns:
        cq.Workplane: The 3D model of the Buddha image.
    """
    try:
        # Base parameters for the Buddha image
        height = 200  # Height of the Buddha image in mm
        width = 100   # Width of the Buddha image in mm
        depth = 50    # Depth of the Buddha image in mm

        # Create the base shape of the Buddha image
        buddha_base = (
            cq.Workplane("XY")
            .box(width, depth, height)  # Create a rectangular prism
            .translate((0, 0, height / 2))  # Move to the center
        )

        # Add features to represent the Buddha's head
        head_radius = 30
        head_height = 40
        buddha_head = (
            cq.Workplane("XY")
            .sphere(head_radius)  # Create a sphere for the head
            .translate((0, 0, height + head_height / 2))  # Position the head above the body
        )

        # Combine the base and head to form the complete Buddha image
        buddha_image = buddha_base.union(buddha_head)

        return buddha_image

    except Exception as e:
        print(f"An error occurred while creating the Buddha image: {e}")
        return None

def export_model(model, filename):
    """
    Export the 3D model to an STL file.
    
    Args:
        model (cq.Workplane): The 3D model to export.
        filename (str): The name of the file to save the model as.
    """
    try:
        if model is not None:
            model.val().exportStl(filename)
            print(f"Model exported successfully to {filename}")
        else:
            print("No model to export.")
    except Exception as e:
        print(f"An error occurred while exporting the model: {e}")

if __name__ == "__main__":
    # Create the Buddha image model
    buddha_model = create_buddha_image()
    
    # Export the model to an STL file
    export_model(buddha_model, "sri_maha_pho_buddha_image.stl")
```
