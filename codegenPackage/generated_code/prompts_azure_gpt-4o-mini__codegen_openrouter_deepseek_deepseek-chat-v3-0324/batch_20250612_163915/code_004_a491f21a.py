"""
Generated Code Metadata:
========================
Original URL: https://www.steamcommunity.ru
Prompt: Create a tutorial on designing custom maps for Half-Life, focusing on object modeling and texture application as outlined in the technical documentation.
Generated: DETERMINISTIC_a491f21a762b38b7
Batch ID: 20250612_163915
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# Half-Life Custom Map Tutorial - Object Modeling and Texture Application

```python
"""
Half-Life Custom Map Creation Tutorial
This script demonstrates object modeling and texture application for Half-Life maps.
It uses Python with PyHammer (a Hammer editor scripting library) for demonstration.
"""

import os
import sys
import math
from typing import List, Tuple, Dict

try:
    import pyhammer
except ImportError:
    raise ImportError("PyHammer library not found. Please install it to run this tutorial.")

class HalfLifeMapBuilder:
    """
    A class to demonstrate Half-Life map building techniques including:
    - Basic geometry creation
    - Texture application
    - Entity placement
    - Lighting setup
    """
    
    def __init__(self, map_name: str = "tutorial_map"):
        """
        Initialize the map builder with default settings.
        
        Args:
            map_name: Name of the map file (without extension)
        """
        self.map_name = map_name
        self.map = pyhammer.Map()
        self.textures = {
            'concrete': 'concrete/concretefloor001a',
            'metal': 'metal/metalwall006a',
            'sky': 'sky/sky_day01_01',
            'light': 'common/light'
        }
        self.materials_path = "materials/"
        
    def create_basic_room(self, dimensions: Tuple[float, float, float]) -> None:
        """
        Create a basic rectangular room with the given dimensions.
        
        Args:
            dimensions: (length, width, height) of the room in units
        """
        try:
            length, width, height = dimensions
            
            # Create floor
            floor = pyhammer.Brush()
            floor.create_cube(
                origin=(0, 0, 0),
                size=(length, width, 32),
                texture=self.textures['concrete']
            )
            
            # Create ceiling
            ceiling = pyhammer.Brush()
            ceiling.create_cube(
                origin=(0, 0, height),
                size=(length, width, 32),
                texture=self.textures['concrete']
            )
            
            # Create walls
            wall_thickness = 32
            walls = []
            
            # North wall
            walls.append(pyhammer.Brush())
            walls[-1].create_cube(
                origin=(0, -wall_thickness/2, 0),
                size=(length, wall_thickness, height),
                texture=self.textures['metal']
            )
            
            # South wall
            walls.append(pyhammer.Brush())
            walls[-1].create_cube(
                origin=(0, width + wall_thickness/2, 0),
                size=(length, wall_thickness, height),
                texture=self.textures['metal']
            )
            
            # West wall
            walls.append(pyhammer.Brush())
            walls[-1].create_cube(
                origin=(-wall_thickness/2, 0, 0),
                size=(wall_thickness, width, height),
                texture=self.textures['metal']
            )
            
            # East wall
            walls.append(pyhammer.Brush())
            walls[-1].create_cube(
                origin=(length + wall_thickness/2, 0, 0),
                size=(wall_thickness, width, height),
                texture=self.textures['metal']
            )
            
            # Add all brushes to map
            self.map.add_brush(floor)
            self.map.add_brush(ceiling)
            for wall in walls:
                self.map.add_brush(wall)
                
        except Exception as e:
            print(f"Error creating room: {str(e)}")
            raise

    def add_light(self, position: Tuple[float, float, float], brightness: int = 200) -> None:
        """
        Add a light entity to the map.
        
        Args:
            position: (x, y, z) coordinates for the light
            brightness: Light intensity (0-255)
        """
        try:
            light = pyhammer.Entity()
            light.set_classname("light")
            light.set_origin(position)
            light.set_property("_light", f"{brightness} {brightness} {brightness} 200")
            light.set_property("style", "0")
            self.map.add_entity(light)
        except Exception as e:
            print(f"Error adding light: {str(e)}")
            raise

    def add_player_spawn(self, position: Tuple[float, float, float]) -> None:
        """
        Add a player spawn point to the map.
        
        Args:
            position: (x, y, z) coordinates for the spawn point
        """
        try:
            spawn = pyhammer.Entity()
            spawn.set_classname("info_player_start")
            spawn.set_origin(position)
            self.map.add_entity(spawn)
        except Exception as e:
            print(f"Error adding player spawn: {str(e)}")
            raise

    def add_textured_object(self, origin: Tuple[float, float, float], 
                          size: Tuple[float, float, float], 
                          texture: str, 
                          rotation: Tuple[float, float, float] = (0, 0, 0)) -> None:
        """
        Add a textured object to the map.
        
        Args:
            origin: (x, y, z) coordinates for the object
            size: (length, width, height) of the object
            texture: Texture name/path
            rotation: (pitch, yaw, roll) rotation angles
        """
        try:
            obj = pyhammer.Brush()
            obj.create_cube(origin, size, texture)
            
            if any(rotation):
                obj.rotate(rotation[0], rotation[1], rotation[2])
                
            self.map.add_brush(obj)
        except Exception as e:
            print(f"Error adding textured object: {str(e)}")
            raise

    def save_map(self) -> None:
        """
        Save the map to a .map file.
        """
        try:
            if not os.path.exists('maps'):
                os.makedirs('maps')
            
            map_path = os.path.join('maps', f"{self.map_name}.map")
            self.map.save(map_path)
            print(f"Map saved successfully to {map_path}")
        except Exception as e:
            print(f"Error saving map: {str(e)}")
            raise

def run_tutorial():
    """Main function to run the map building tutorial."""
    try:
        print("Half-Life Custom Map Tutorial - Object Modeling and Texture Application")
        
        # Initialize map builder
        builder = HalfLifeMapBuilder("hl_tutorial_map")
        
        # Create a basic room (20x15 units, 10 units tall)
        builder.create_basic_room((2048, 1536, 1024))
        
        # Add player spawn
        builder.add_player_spawn((1024, 768, 128))
        
        # Add lights
        builder.add_light((512, 512, 800))
        builder.add_light((1536, 512, 800))
        builder.add_light((512, 1024, 800))
        builder.add_light((1536, 1024, 800))
        
        # Add some textured objects
        builder.add_textured_object(
            origin=(1024, 768, 256),
            size=(256, 256, 32),
            texture=builder.textures['metal'],
            rotation=(0, 45, 0)
        )
        
        builder.add_textured_object(
            origin=(500, 500, 128),
            size=(128, 128, 128),
            texture=builder.textures['concrete']
        )
        
        # Save the map
        builder.save_map()
        
        print("Tutorial completed successfully!")
        
    except Exception as e:
        print(f"Tutorial failed: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    run_tutorial()
```
