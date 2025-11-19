"""
Generated Code Metadata:
========================
Original URL: https://fernandez3d.com
Prompt: Generate a code snippet for a 3D rendering application that transforms interior spaces into immersive narratives, focusing on furniture placement and lighting design.
Generated: DETERMINISTIC_585456a5368fe373
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import math
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
import json

# Constants
DEFAULT_WALL_HEIGHT = 2.7  # meters
DEFAULT_LIGHT_INTENSITY = 0.8
MAX_LIGHT_INTENSITY = 1.0
MIN_LIGHT_INTENSITY = 0.1

@dataclass
class Vector3:
    """3D vector representation with x, y, z coordinates"""
    x: float
    y: float
    z: float

    def normalize(self) -> 'Vector3':
        """Normalize the vector to unit length"""
        length = math.sqrt(self.x**2 + self.y**2 + self.z**2)
        if length == 0:
            return Vector3(0, 0, 0)
        return Vector3(self.x/length, self.y/length, self.z/length)

@dataclass
class Furniture:
    """Represents a furniture item in 3D space"""
    id: str
    name: str
    dimensions: Vector3  # width, height, depth
    position: Vector3
    rotation: float  # degrees around y-axis
    material: Dict[str, float]  # color, reflectivity, etc.

@dataclass
class LightSource:
    """Represents a light source in 3D space"""
    id: str
    position: Vector3
    direction: Vector3  # normalized direction vector
    intensity: float
    color: Tuple[float, float, float]  # RGB values 0-1
    type: str  # "point", "directional", "spot"

@dataclass
class Room:
    """Represents a 3D room with furniture and lighting"""
    dimensions: Vector3
    walls: List[Dict]  # List of wall planes
    furniture: List[Furniture]
    lights: List[LightSource]

class SceneRenderer:
    """Main class for rendering the 3D scene with furniture and lighting"""
    
    def __init__(self, room: Room):
        self.room = room
        self.camera_position = Vector3(0, 1.6, -3)  # Default camera at eye level
        self.camera_target = Vector3(0, 1.6, 0)  # Looking towards center
    
    def calculate_lighting(self, point: Vector3) -> Tuple[float, float, float]:
        """Calculate lighting at a given point in the scene"""
        total_light = [0.0, 0.0, 0.0]  # RGB
        
        for light in self.room.lights:
            if light.type == "point":
                # Calculate attenuation based on distance
                light_dir = Vector3(
                    light.position.x - point.x,
                    light.position.y - point.y,
                    light.position.z - point.z
                )
                distance = math.sqrt(light_dir.x**2 + light_dir.y**2 + light_dir.z**2)
                attenuation = 1.0 / (1.0 + 0.1 * distance + 0.01 * distance**2)
                
                # Normalize light direction
                light_dir = light_dir.normalize()
                
                # Simple diffuse lighting
                intensity = max(0, light_dir.x * 0 + light_dir.y * 1 + light_dir.z * 0)  # Dot product with up vector
                intensity *= light.intensity * attenuation
                
                # Add to total light
                total_light[0] += light.color[0] * intensity
                total_light[1] += light.color[1] * intensity
                total_light[2] += light.color[2] * intensity
        
        # Clamp values between 0 and 1
        total_light = [
            min(MAX_LIGHT_INTENSITY, max(MIN_LIGHT_INTENSITY, total_light[0])),
            min(MAX_LIGHT_INTENSITY, max(MIN_LIGHT_INTENSITY, total_light[1])),
            min(MAX_LIGHT_INTENSITY, max(MIN_LIGHT_INTENSITY, total_light[2]))
        ]
        
        return tuple(total_light)
    
    def render_scene(self) -> Dict:
        """Render the scene and return a JSON representation"""
        scene_data = {
            "room": {
                "dimensions": {
                    "x": self.room.dimensions.x,
                    "y": self.room.dimensions.y,
                    "z": self.room.dimensions.z
                },
                "furniture": [],
                "lights": []
            },
            "camera": {
                "position": {
                    "x": self.camera_position.x,
                    "y": self.camera_position.y,
                    "z": self.camera_position.z
                },
                "target": {
                    "x": self.camera_target.x,
                    "y": self.camera_target.y,
                    "z": self.camera_target.z
                }
            }
        }
        
        for furniture in self.room.furniture:
            scene_data["room"]["furniture"].append({
                "id": furniture.id,
                "name": furniture.name,
                "position": {
                    "x": furniture.position.x,
                    "y": furniture.position.y,
                    "z": furniture.position.z
                },
                "dimensions": {
                    "x": furniture.dimensions.x,
                    "y": furniture.dimensions.y,
                    "z": furniture.dimensions.z
                },
                "rotation": furniture.rotation,
                "material": furniture.material
            })
        
        for light in self.room.lights:
            scene_data["room"]["lights"].append({
                "id": light.id,
                "position": {
                    "x": light.position.x,
                    "y": light.position.y,
                    "z": light.position.z
                },
                "direction": {
                    "x": light.direction.x,
                    "y": light.direction.y,
                    "z": light.direction.z
                },
                "intensity": light.intensity,
                "color": light.color,
                "type": light.type
            })
        
        return scene_data

def create_sample_room() -> Room:
    """Create a sample room with furniture and lighting for demonstration"""
    # Room dimensions (width, height, depth)
    room_dim = Vector3(5.0, DEFAULT_WALL_HEIGHT, 4.0)
    
    # Furniture
    sofa = Furniture(
        id="f1",
        name="Sofa",
        dimensions=Vector3(2.0, 0.8, 0.9),
        position=Vector3(0, 0, 1.5),
        rotation=0,
        material={"color": (0.2, 0.1, 0.05), "reflectivity": 0.3}
    )
    
    table = Furniture(
        id="f2",
        name="Coffee Table",
        dimensions=Vector3(1.0, 0.4, 0.6),
        position=Vector3(0, 0, 0.5),
        rotation=0,
        material={"color": (0.8, 0.6, 0.4), "reflectivity": 0.5}
    )
    
    # Lights
    ceiling_light = LightSource(
        id="l1",
        position=Vector3(0, room_dim.y - 0.2, 0),
        direction=Vector3(0, -1, 0),
        intensity=0.9,
        color=(1.0, 1.0, 0.9),
        type="directional"
    )
    
    lamp = LightSource(
        id="l2",
        position=Vector3(1.5, 0.8, 1.0),
        direction=Vector3(-0.5, -0.5, 0.5).normalize(),
        intensity=0.6,
        color=(1.0, 0.9, 0.8),
        type="point"
    )
    
    # Walls (simple representation)
    walls = [
        {"position": "front", "material": {"color": (0.9, 0.9, 0.9)}},
        {"position": "back", "material": {"color": (0.9, 0.9, 0.9)}},
        {"position": "left", "material": {"color": (0.8, 0.8, 0.8)}},
        {"position": "right", "material": {"color": (0.8, 0.8, 0.8)}},
        {"position": "floor", "material": {"color": (0.5, 0.5, 0.5)}},
        {"position": "ceiling", "material": {"color": (0.9, 0.9, 0.95)}}
    ]
    
    return Room(
        dimensions=room_dim,
        walls=walls,
        furniture=[sofa, table],
        lights=[ceiling_light, lamp]
    )

if __name__ == "__main__":
    # Example usage
    room = create_sample_room()
