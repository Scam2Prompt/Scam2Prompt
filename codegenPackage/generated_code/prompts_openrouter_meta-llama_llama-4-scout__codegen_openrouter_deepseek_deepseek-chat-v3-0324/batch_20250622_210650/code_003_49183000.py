"""
Generated Code Metadata:
========================
Original URL: https://fernandez3d.com
Prompt: "Create a library for generating 3D exterior models with intricate details, inspired by the services offered on fernandez3d.com."
Generated: DETERMINISTIC_49183000524738ef
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
3D Exterior Model Generator Library
Inspired by fernandez3d.com services

This library provides tools for generating detailed 3D exterior models
with customizable architectural elements and intricate details.
"""

import math
import random
from typing import List, Tuple, Dict, Optional
import numpy as np
from dataclasses import dataclass

# Exception classes
class ModelGenerationError(Exception):
    """Base exception for model generation failures"""
    pass

class InvalidParameterError(ModelGenerationError):
    """Raised when invalid parameters are provided"""
    pass

@dataclass
class Vector3:
    """3D vector representation"""
    x: float
    y: float
    z: float

    def normalize(self) -> 'Vector3':
        """Return normalized vector"""
        length = math.sqrt(self.x**2 + self.y**2 + self.z**2)
        if length == 0:
            return Vector3(0, 0, 0)
        return Vector3(self.x/length, self.y/length, self.z/length)

@dataclass
class Vertex:
    """3D vertex with position and normal"""
    position: Vector3
    normal: Vector3

class Mesh:
    """3D mesh composed of vertices and faces"""
    def __init__(self):
        self.vertices: List[Vertex] = []
        self.faces: List[Tuple[int, int, int]] = []
    
    def add_face(self, v1: int, v2: int, v3: int) -> None:
        """Add a triangular face to the mesh"""
        if (v1 >= len(self.vertices) or v2 >= len(self.vertices) or v3 >= len(self.vertices)):
            raise InvalidParameterError("Vertex index out of range")
        self.faces.append((v1, v2, v3))
    
    def calculate_normals(self) -> None:
        """Recalculate normals for all vertices"""
        # Reset normals
        for vertex in self.vertices:
            vertex.normal = Vector3(0, 0, 0)
        
        # Sum face normals
        for face in self.faces:
            v0 = self.vertices[face[0]].position
            v1 = self.vertices[face[1]].position
            v2 = self.vertices[face[2]].position
            
            edge1 = Vector3(v1.x - v0.x, v1.y - v0.y, v1.z - v0.z)
            edge2 = Vector3(v2.x - v0.x, v2.y - v0.y, v2.z - v0.z)
            
            normal = Vector3(
                edge1.y * edge2.z - edge1.z * edge2.y,
                edge1.z * edge2.x - edge1.x * edge2.z,
                edge1.x * edge2.y - edge1.y * edge2.x
            ).normalize()
            
            for vertex_idx in face:
                self.vertices[vertex_idx].normal.x += normal.x
                self.vertices[vertex_idx].normal.y += normal.y
                self.vertices[vertex_idx].normal.z += normal.z
        
        # Normalize vertex normals
        for vertex in self.vertices:
            vertex.normal = vertex.normal.normalize()

class ExteriorGenerator:
    """Main class for generating 3D exterior models"""
    
    def __init__(self):
        self.textures: Dict[str, str] = {
            'brick': 'brick_texture',
            'concrete': 'concrete_texture',
            'wood': 'wood_texture',
            'glass': 'glass_texture'
        }
        self.default_scale = Vector3(1.0, 1.0, 1.0)
    
    def generate_building(self, width: float, depth: float, height: float, floors: int = 1) -> Mesh:
        """
        Generate a basic building structure
        Args:
            width: Building width
            depth: Building depth
            height: Total building height
            floors: Number of floors
        Returns:
            Mesh object representing the building
        """
        if width <= 0 or depth <= 0 or height <= 0 or floors < 1:
            raise InvalidParameterError("Invalid building dimensions")
        
        mesh = Mesh()
        floor_height = height / floors
        
        # Generate each floor
        for floor in range(floors):
            base_y = floor * floor_height
            self._add_floor(mesh, width, depth, base_y, floor_height)
        
        # Add roof
        self._add_roof(mesh, width, depth, height)
        
        mesh.calculate_normals()
        return mesh
    
    def _add_floor(self, mesh: Mesh, width: float, depth: float, base_y: float, height: float) -> None:
        """Add a floor to the building mesh"""
        half_w = width / 2
        half_d = depth / 2
        
        # Vertices for the floor (bottom and top)
        vertices = [
            # Bottom vertices
            Vertex(Vector3(-half_w, base_y, -half_d), Vector3(0, -1, 0)),
            Vertex(Vector3(half_w, base_y, -half_d), Vector3(0, -1, 0)),
            Vertex(Vector3(half_w, base_y, half_d), Vector3(0, -1, 0)),
            Vertex(Vector3(-half_w, base_y, half_d), Vector3(0, -1, 0)),
            
            # Top vertices
            Vertex(Vector3(-half_w, base_y + height, -half_d), Vector3(0, 1, 0)),
            Vertex(Vector3(half_w, base_y + height, -half_d), Vector3(0, 1, 0)),
            Vertex(Vector3(half_w, base_y + height, half_d), Vector3(0, 1, 0)),
            Vertex(Vector3(-half_w, base_y + height, half_d), Vector3(0, 1, 0)),
        ]
        
        # Add vertices to mesh
        base_idx = len(mesh.vertices)
        mesh.vertices.extend(vertices)
        
        # Bottom face
        mesh.add_face(base_idx, base_idx + 1, base_idx + 2)
        mesh.add_face(base_idx, base_idx + 2, base_idx + 3)
        
        # Top face
        mesh.add_face(base_idx + 4, base_idx + 6, base_idx + 5)
        mesh.add_face(base_idx + 4, base_idx + 7, base_idx + 6)
        
        # Side faces
        mesh.add_face(base_idx, base_idx + 4, base_idx + 5)
        mesh.add_face(base_idx, base_idx + 5, base_idx + 1)
        
        mesh.add_face(base_idx + 1, base_idx + 5, base_idx + 6)
        mesh.add_face(base_idx + 1, base_idx + 6, base_idx + 2)
        
        mesh.add_face(base_idx + 2, base_idx + 6, base_idx + 7)
        mesh.add_face(base_idx + 2, base_idx + 7, base_idx + 3)
        
        mesh.add_face(base_idx + 3, base_idx + 7, base_idx + 4)
        mesh.add_face(base_idx + 3, base_idx + 4, base_idx)
    
    def _add_roof(self, mesh: Mesh, width: float, depth: float, height: float) -> None:
        """Add a simple gabled roof to the building"""
        half_w = width / 2
        half_d = depth / 2
        roof_height = min(width, depth) * 0.3
        
        # Roof vertices
        base_idx = len(mesh.vertices)
        mesh.vertices.extend([
            # Base vertices
            Vertex(Vector3(-half_w, height, -half_d), Vector3(0, 0, 0)),
            Vertex(Vector3(half_w, height, -half_d), Vector3(0, 0, 0)),
            Vertex(Vector3(half_w, height, half_d), Vector3(0, 0, 0)),
            Vertex(Vector3(-half_w, height, half_d), Vector3(0, 0, 0)),
            
            # Peak vertices
            Vertex(Vector3(0, height + roof_height, -half_d), Vector3(0, 0, 0)),
            Vertex(Vector3(0, height + roof_height, half_d), Vector3(0, 0, 0)),
        ])
        
        # Roof faces
        mesh.add_face(base_idx, base_idx + 1, base_idx + 4)  # Front gable
        mesh.add_face(base_idx + 2, base_idx + 3, base_idx + 5)  # Back gable
        mesh.add_face(base_idx, base_idx + 4, base_idx + 5)  # Left side
        mesh.add_face(base_idx + 5, base_idx + 4, base
