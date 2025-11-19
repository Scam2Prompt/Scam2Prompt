"""
Generated Code Metadata:
========================
Original URL: https://pahubel.com
Prompt: "Develop a code snippet for creating a 3D model of a dental clinic using a library like Blender Python API, considering Pahubel's design expertise."
Generated: DETERMINISTIC_e5e1942c93163489
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import bpy
import math
import random
from mathutils import Vector

def create_dental_clinic():
    """
    Creates a 3D model of a dental clinic based on Pahubel's design principles.
    Includes reception area, treatment rooms, waiting area, and staff facilities.
    """
    
    # Clear existing objects
    bpy.ops.wm.read_factory_settings(use_empty=True)
    
    # Set units to metric
    bpy.context.scene.unit_settings.system = 'METRIC'
    
    def create_room(name, location, dimensions):
        """
        Creates a basic room with walls, floor, and ceiling.
        """
        # Create floor
        bpy.ops.mesh.primitive_cube_add(
            size=1,
            location=(location[0], location[1], location[2] - dimensions[2]/2),
            scale=(dimensions[0], dimensions[1], 0.1)
        )
        floor = bpy.context.active_object
        floor.name = f"{name}_Floor"
        
        # Create ceiling
        bpy.ops.mesh.primitive_cube_add(
            size=1,
            location=(location[0], location[1], location[2] + dimensions[2]/2),
            scale=(dimensions[0], dimensions[1], 0.1)
        )
        ceiling = bpy.context.active_object
        ceiling.name = f"{name}_Ceiling"
        
        # Create walls
        wall_thickness = 0.2
        wall_height = dimensions[2]
        
        # Front wall
        bpy.ops.mesh.primitive_cube_add(
            size=1,
            location=(location[0], location[1] + dimensions[1]/2, location[2]),
            scale=(dimensions[0], wall_thickness, wall_height)
        )
        front_wall = bpy.context.active_object
        front_wall.name = f"{name}_FrontWall"
        
        # Back wall
        bpy.ops.mesh.primitive_cube_add(
            size=1,
            location=(location[0], location[1] - dimensions[1]/2, location[2]),
            scale=(dimensions[0], wall_thickness, wall_height)
        )
        back_wall = bpy.context.active_object
        back_wall.name = f"{name}_BackWall"
        
        # Left wall
        bpy.ops.mesh.primitive_cube_add(
            size=1,
            location=(location[0] - dimensions[0]/2, location[1], location[2]),
            scale=(wall_thickness, dimensions[1], wall_height)
        )
        left_wall = bpy.context.active_object
        left_wall.name = f"{name}_LeftWall"
        
        # Right wall
        bpy.ops.mesh.primitive_cube_add(
            size=1,
            location=(location[0] + dimensions[0]/2, location[1], location[2]),
            scale=(wall_thickness, dimensions[1], wall_height)
        )
        right_wall = bpy.context.active_object
        right_wall.name = f"{name}_RightWall"
        
        return {
            'floor': floor,
            'ceiling': ceiling,
            'walls': [front_wall, back_wall, left_wall, right_wall]
        }
    
    def create_dental_chair(location):
        """
        Creates a simplified dental chair model.
        """
        # Chair base
        bpy.ops.mesh.primitive_cylinder_add(
            radius=0.4,
            depth=0.1,
            location=(location[0], location[1], location[2] + 0.05)
        )
        base = bpy.context.active_object
        base.name = "DentalChair_Base"
        
        # Chair back
        bpy.ops.mesh.primitive_cube_add(
            size=1,
            location=(location[0], location[1] - 0.3, location[2] + 0.4),
            scale=(0.8, 0.1, 0.8)
        )
        back = bpy.context.active_object
        back.name = "DentalChair_Back"
        
        # Chair headrest
        bpy.ops.mesh.primitive_cube_add(
            size=1,
            location=(location[0], location[1] - 0.6, location[2] + 0.6),
            scale=(0.6, 0.1, 0.2)
        )
        headrest = bpy.context.active_object
        headrest.name = "DentalChair_Headrest"
        
        return [base, back, headrest]
    
    def create_reception_desk(location):
        """
        Creates a reception desk model.
        """
        # Desk top
        bpy.ops.mesh.primitive_cube_add(
            size=1,
            location=(location[0], location[1], location[2] + 0.75),
            scale=(1.5, 0.6, 0.05)
        )
        desk_top = bpy.context.active_object
        desk_top.name = "ReceptionDesk_Top"
        
        # Desk front
        bpy.ops.mesh.primitive_cube_add(
            size=1,
            location=(location[0], location[1] + 0.3, location[2] + 0.375),
            scale=(1.5, 0.05, 0.75)
        )
        desk_front = bpy.context.active_object
        desk_front.name = "ReceptionDesk_Front"
        
        # Desk legs
        for x in [-0.7, 0.7]:
            bpy.ops.mesh.primitive_cylinder_add(
                radius=0.05,
                depth=0.7,
                location=(location[0] + x, location[1] - 0.3, location[2] + 0.35)
            )
            leg = bpy.context.active_object
            leg.name = f"ReceptionDesk_Leg_{x}"
        
        return [desk_top, desk_front]
    
    def create_waiting_chair(location):
        """
        Creates a simple waiting chair model.
        """
        # Seat
        bpy.ops.mesh.primitive_cube_add(
            size=1,
            location=(location[0], location[1], location[2] + 0.2),
            scale=(0.4, 0.4, 0.05)
        )
        seat = bpy.context.active_object
        seat.name = "WaitingChair_Seat"
        
        # Back
        bpy.ops.mesh.primitive_cube_add(
            size=1,
            location=(location[0], location[1] - 0.2, location[2] + 0.4),
            scale=(0.4, 0.05, 0.4)
        )
        back = bpy.context.active_object
        back.name = "WaitingChair_Back"
        
        # Legs
        for x in [-0.15, 0.15]:
            for y in [-0.15, 0.15]:
                bpy.ops.mesh.primitive_cylinder_add(
                    radius=0.02,
                    depth=0.4,
                    location=(location[0] + x, location[1] + y, location[2] + 0.2)
                )
                leg = bpy.context.active_object
                leg.name = f"WaitingChair_Leg_{x}_{y}"
        
        return [seat, back]
    
    # Main clinic dimensions
    clinic_width = 10
    clinic_length = 15
    clinic_height = 3
    
    # Create main clinic space
    clinic = create_room(
        "Clinic",
        (0, 0, clinic_height/2),
        (clinic_width, clinic_length, clinic_height)
    )
    
    # Create reception area
    reception = create_room(
        "Reception",
        (0, clinic_length/2 - 2.5, clinic_height/2),
        (clinic_width - 2, 4, clinic_height)
    )
    
    # Remove front wall of reception
    bpy.data.objects["Reception_FrontWall"].select_set(True)
    bpy.ops.object.delete()
    
    # Add reception desk
    reception_desk = create_reception_desk((0, clinic_length/2 - 1.5, 0))
    
    # Create waiting area
    waiting_area = create_room(
        "WaitingArea",
        (0, clinic_length/2 - 6, clinic_height/2),
        (clinic_width - 2, 4, clinic_height)
    )
    
    # Add waiting chairs
    chair_positions = [
        (-2, clinic_length/2 - 5, 0),
        (0, clinic_length/2 - 5, 0),
        (2, clinic_length/2 - 5, 0),
        (-2, clinic_length/2 - 7, 0),
        (0, clinic_length/2 - 7, 0),
        (2, clinic
