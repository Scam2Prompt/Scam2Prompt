"""
Generated Code Metadata:
========================
Original URL: https://unisonplus.vn
Prompt: Write a Python script that uses 3D simulation software to create a unique infrastructure design based on specific project requirements.
Generated: DETERMINISTIC_ee2e035bb9540620
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import bpy
import random
import math
import sys
from mathutils import Vector

class InfrastructureDesigner:
    """
    A 3D infrastructure design generator using Blender's Python API.
    Creates a unique infrastructure design based on project requirements.
    """

    def __init__(self, project_name, area_width=100, area_length=100):
        """
        Initialize the infrastructure designer with project parameters.
        
        Args:
            project_name (str): Name of the project
            area_width (float): Width of the design area in meters
            area_length (float): Length of the design area in meters
        """
        self.project_name = project_name
        self.area_width = area_width
        self.area_length = area_length
        self.roads = []
        self.buildings = []
        self.parks = []
        
        # Clear existing objects
        self._clear_scene()
        
        # Create ground plane
        self._create_ground()
        
    def _clear_scene(self):
        """Clear all objects from the current scene."""
        try:
            bpy.ops.object.select_all(action='SELECT')
            bpy.ops.object.delete()
        except Exception as e:
            print(f"Error clearing scene: {e}")
            sys.exit(1)
    
    def _create_ground(self):
        """Create a ground plane for the infrastructure."""
        try:
            bpy.ops.mesh.primitive_plane_add(
                size=max(self.area_width, self.area_length),
                location=(0, 0, 0)
            )
            ground = bpy.context.object
            ground.name = f"{self.project_name}_Ground"
            ground.scale.x = self.area_width / 10
            ground.scale.y = self.area_length / 10
            
            # Apply material
            mat = bpy.data.materials.new(name="GroundMaterial")
            mat.diffuse_color = (0.2, 0.3, 0.1, 1)
            ground.data.materials.append(mat)
        except Exception as e:
            print(f"Error creating ground: {e}")
            sys.exit(1)
    
    def generate_road_network(self, num_main_roads=2, num_side_roads=4):
        """
        Generate a road network for the infrastructure.
        
        Args:
            num_main_roads (int): Number of main roads
            num_side_roads (int): Number of side roads
        """
        try:
            # Main roads (longer, wider)
            for i in range(num_main_roads):
                x_pos = random.uniform(-self.area_width/2, self.area_width/2)
                self._create_road(
                    location=(x_pos, 0, 0.1),
                    dimensions=(5, self.area_length, 0.2),
                    name=f"MainRoad_{i}"
                )
                
                y_pos = random.uniform(-self.area_length/2, self.area_length/2)
                self._create_road(
                    location=(0, y_pos, 0.1),
                    dimensions=(self.area_width, 5, 0.2),
                    name=f"MainRoad_{i+num_main_roads}"
                )
            
            # Side roads (shorter, narrower)
            for i in range(num_side_roads):
                x_pos = random.uniform(-self.area_width/2, self.area_width/2)
                self._create_road(
                    location=(x_pos, 0, 0.1),
                    dimensions=(3, self.area_length*0.7, 0.2),
                    name=f"SideRoad_{i}"
                )
                
                y_pos = random.uniform(-self.area_length/2, self.area_length/2)
                self._create_road(
                    location=(0, y_pos, 0.1),
                    dimensions=(self.area_width*0.7, 3, 0.2),
                    name=f"SideRoad_{i+num_side_roads}"
                )
        except Exception as e:
            print(f"Error generating road network: {e}")
            sys.exit(1)
    
    def _create_road(self, location, dimensions, name):
        """Create a single road segment."""
        try:
            bpy.ops.mesh.primitive_cube_add(
                size=1,
                location=location
            )
            road = bpy.context.object
            road.name = name
            road.scale = dimensions
            road.data.materials.append(self._create_road_material())
            self.roads.append(road)
        except Exception as e:
            print(f"Error creating road: {e}")
            raise
    
    def _create_road_material(self):
        """Create a material for roads."""
        mat = bpy.data.materials.new(name="RoadMaterial")
        mat.diffuse_color = (0.1, 0.1, 0.1, 1)
        mat.roughness = 0.8
        return mat
    
    def generate_buildings(self, num_buildings=10):
        """
        Generate buildings in the infrastructure.
        
        Args:
            num_buildings (int): Number of buildings to generate
        """
        try:
            for i in range(num_buildings):
                # Random position avoiding roads
                x = random.uniform(-self.area_width/2 + 10, self.area_width/2 - 10)
                y = random.uniform(-self.area_length/2 + 10, self.area_length/2 - 10)
                
                # Random dimensions
                width = random.uniform(5, 15)
                length = random.uniform(5, 15)
                height = random.uniform(5, 30)
                
                self._create_building(
                    location=(x, y, height/2),
                    dimensions=(width, length, height),
                    name=f"Building_{i}"
                )
        except Exception as e:
            print(f"Error generating buildings: {e}")
            sys.exit(1)
    
    def _create_building(self, location, dimensions, name):
        """Create a single building."""
        try:
            bpy.ops.mesh.primitive_cube_add(
                size=1,
                location=location
            )
            building = bpy.context.object
            building.name = name
            building.scale = dimensions
            
            # Random building color
            mat = bpy.data.materials.new(name=f"BuildingMaterial_{name}")
            mat.diffuse_color = (
                random.uniform(0.3, 0.9),
                random.uniform(0.3, 0.9),
                random.uniform(0.3, 0.9),
                1
            )
            building.data.materials.append(mat)
            
            self.buildings.append(building)
        except Exception as e:
            print(f"Error creating building: {e}")
            raise
    
    def generate_parks(self, num_parks=2):
        """
        Generate parks in the infrastructure.
        
        Args:
            num_parks (int): Number of parks to generate
        """
        try:
            for i in range(num_parks):
                # Random position avoiding roads and buildings
                x = random.uniform(-self.area_width/2 + 20, self.area_width/2 - 20)
                y = random.uniform(-self.area_length/2 + 20, self.area_length/2 - 20)
                
                # Random dimensions
                width = random.uniform(10, 30)
                length = random.uniform(10, 30)
                
                self._create_park(
                    location=(x, y, 0.1),
                    dimensions=(width, length, 0.1),
                    name=f"Park_{i}"
                )
        except Exception as e:
            print(f"Error generating parks: {e}")
            sys.exit(1)
    
    def _create_park(self, location, dimensions, name):
        """Create a single park area."""
        try:
            bpy.ops.mesh.primitive_cube_add(
                size=1,
                location=location
            )
            park = bpy.context.object
            park.name = name
            park.scale = dimensions
            
            # Park material (green)
            mat = bpy.data.materials.new(name=f"ParkMaterial_{name}")
            mat.diffuse_color = (0.1, 0.4, 0.1, 1)
            park.data.materials.append(mat)
            
            self.parks.append(park)
            
            # Add some trees to the park
            self._add_trees_to_park(park, num_trees=random.randint(3, 10))
        except Exception as e:
            print(f"Error creating park: {e}")
            raise
    
    def _add_trees_to_park(self, park, num_trees=5):
        """Add trees to a park area."""
        try:
            park_center = Vector(park.location)
            park_dim = Vector(park.dimensions)
            
            for i in range(num_trees):
                # Random position within park boundaries
                x = random.uniform(
                    park_center.x - park_dim.x/2 + 2,
                    park_center.x + park_dim.x/2 -
