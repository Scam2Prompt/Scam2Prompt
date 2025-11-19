"""
Generated Code Metadata:
========================
Original URL: https://rneta-mask-wallet.blogspot.com.ar
Prompt: Generate code using a CAD API to create a 3D model of a glass guardrail with tempered glass panels and stainless steel supports, adhering to ABNT safety standards.
Generated: DETERMINISTIC_5f63034270116c63
Batch ID: 20250612_150343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import cadquery as cq
from cadquery import exporters
import math

# Constants for ABNT safety standards
MIN_GLASS_THICKNESS = 10  # mm
MIN_RAIL_HEIGHT = 1100  # mm
MAX_PANEL_WIDTH = 1200  # mm
SUPPORT_SPACING = 1000  # mm
SUPPORT_DIAMETER = 50  # mm
HANDRAIL_DIAMETER = 42  # mm
HANDRAIL_HEIGHT = 100  # mm above glass

def create_glass_panel(width, height, thickness=MIN_GLASS_THICKNESS):
    """
    Creates a tempered glass panel with the specified dimensions.
    Args:
        width: Width of the panel in mm (must be <= MAX_PANEL_WIDTH)
        height: Height of the panel in mm (must be >= MIN_RAIL_HEIGHT)
        thickness: Thickness of the glass in mm (defaults to MIN_GLASS_THICKNESS)
    Returns:
        A CADQuery Workplane object representing the glass panel
    """
    if width > MAX_PANEL_WIDTH:
        raise ValueError(f"Panel width exceeds maximum allowed ({MAX_PANEL_WIDTH}mm)")
    if height < MIN_RAIL_HEIGHT:
        raise ValueError(f"Panel height below minimum required ({MIN_RAIL_HEIGHT}mm)")
    if thickness < MIN_GLASS_THICKNESS:
        raise ValueError(f"Glass thickness below minimum required ({MIN_GLASS_THICKNESS}mm)")
    
    return cq.Workplane("XY").box(width, thickness, height)

def create_support_post(height):
    """
    Creates a stainless steel support post.
    Args:
        height: Total height of the post in mm
    Returns:
        A CADQuery Workplane object representing the support post
    """
    post = (
        cq.Workplane("XY")
        .circle(SUPPORT_DIAMETER/2)
        .extrude(height)
    )
    
    # Add mounting plate at base
    post = (
        post.faces("<Z")
        .workplane()
        .rect(SUPPORT_DIAMETER*2, SUPPORT_DIAMETER*2)
        .extrude(10)
    )
    
    return post

def create_handrail(length):
    """
    Creates a stainless steel handrail.
    Args:
        length: Length of the handrail in mm
    Returns:
        A CADQuery Workplane object representing the handrail
    """
    return (
        cq.Workplane("XY")
        .circle(HANDRAIL_DIAMETER/2)
        .extrude(length)
    )

def create_guardrail_section(panel_width, total_height):
    """
    Creates a complete guardrail section with glass panel, supports, and handrail.
    Args:
        panel_width: Width of the glass panel in mm
        total_height: Total height of the guardrail in mm
    Returns:
        A CADQuery Assembly containing the complete guardrail section
    """
    # Calculate components dimensions
    glass_height = total_height - HANDRAIL_HEIGHT
    support_height = total_height
    
    # Create components
    glass_panel = create_glass_panel(panel_width, glass_height)
    left_support = create_support_post(support_height)
    right_support = create_support_post(support_height)
    handrail = create_handrail(panel_width + SUPPORT_DIAMETER * 2)
    
    # Position components
    glass_panel = glass_panel.translate((0, 0, glass_height/2))
    
    left_support = left_support.translate((
        -panel_width/2 - SUPPORT_DIAMETER/2,
        0,
        support_height/2
    ))
    
    right_support = right_support.translate((
        panel_width/2 + SUPPORT_DIAMETER/2,
        0,
        support_height/2
    ))
    
    handrail = handrail.translate((
        0,
        0,
        total_height - HANDRAIL_HEIGHT/2
    ))
    
    # Create assembly
    assembly = cq.Assembly()
    assembly.add(glass_panel, name="glass_panel", color=cq.Color(0, 0, 1, 0.5))  # Semi-transparent blue
    assembly.add(left_support, name="left_support", color=cq.Color(0.8, 0.8, 0.8))  # Stainless steel color
    assembly.add(right_support, name="right_support", color=cq.Color(0.8, 0.8, 0.8))
    assembly.add(handrail, name="handrail", color=cq.Color(0.8, 0.8, 0.8))
    
    return assembly

def create_guardrail_system(length, height=MIN_RAIL_HEIGHT + HANDRAIL_HEIGHT):
    """
    Creates a complete guardrail system with multiple sections.
    Args:
        length: Total length of the guardrail in mm
        height: Total height of the guardrail in mm
    Returns:
        A CADQuery Assembly containing the complete guardrail system
    """
    num_sections = math.ceil(length / MAX_PANEL_WIDTH)
    section_width = length / num_sections
    
    full_assembly = cq.Assembly()
    
    for i in range(num_sections):
        section = create_guardrail_section(section_width, height)
        section = section.translate((i * section_width, 0, 0))
        full_assembly.add(section, name=f"section_{i}")
    
    return full_assembly

# Example usage
if __name__ == "__main__":
    try:
        # Create a 3m guardrail system
        guardrail = create_guardrail_system(3000)
        
        # Export to STEP file
        exporters.export(guardrail.toCompound(), "glass_guardrail.step")
        
        # Export to STL for visualization
        exporters.export(guardrail.toCompound(), "glass_guardrail.stl")
        
        print("Guardrail model created successfully.")
    except Exception as e:
        print(f"Error creating guardrail model: {str(e)}")
```
