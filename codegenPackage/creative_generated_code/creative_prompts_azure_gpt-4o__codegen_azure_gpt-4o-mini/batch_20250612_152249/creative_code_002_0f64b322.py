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
import cadquery as cq

def create_neon_sign(text: str, material: str = "plexiglass", thickness: float = 2.0) -> cq.Workplane:
    """
    Create a 3D model of a neon sign using CAD software.

    Args:
        text (str): The text to be rendered on the sign.
        material (str): The material for the sign, default is 'plexiglass'.
        thickness (float): The thickness of the material, default is 2.0.

    Returns:
        cq.Workplane: A CadQuery Workplane object representing the neon sign.
    
    Raises:
        ValueError: If text is empty or thickness is not positive.
    """
    if not text:
        raise ValueError("Text for the neon sign cannot be empty.")
    if thickness <= 0:
        raise ValueError("Thickness must be a positive value.")

    # Create basic sign shape
    sign_shape = (
        cq.Workplane("XY")
        .text(text, fontsize=10, cut=True)  # Generate text outline
        .extrude(thickness)  # Extrude the text to the specified thickness
    )

    return sign_shape


def main():
    """
    Main function to generate and render the neon sign in the specified material.
    """
    try:
        # Define the neon sign properties
        neon_text = "Open"
        material = "plexiglass"
        thickness = 2.0

        # Create the neon sign
        neon_sign = create_neon_sign(neon_text, material, thickness)

        # Save the neon sign to a file
        filename = "neon_sign.stl"
        neon_sign.val().toStl(filename)
        print(f"Neon sign model saved as {filename}.")
        
    except Exception as e:
        print(f"An error occurred while creating the neon sign: {e}")


if __name__ == "__main__":
    main()
```
