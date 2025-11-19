"""
Generated Code Metadata:
========================
Original URL: https://on1force.web.app
Prompt: Develop a script to generate 3D assets for the 0N1VERSE ecosystem using open-source libraries, ensuring compatibility with the original 0N1 Force NFT traits.
Generated: DETERMINISTIC_2659faca4a49d4c5
Batch ID: 20250612_154657
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
import random
from pathlib import Path
from typing import Dict, List, Optional, Tuple
import numpy as np
from PIL import Image
import trimesh
from trimesh import creation, transformations
from trimesh.exchange.export import export_mesh

# Constants
TRAITS_DIR = "traits"
OUTPUT_DIR = "assets"
METADATA_FILE = "metadata.json"
TEXTURE_SIZE = (1024, 1024)
BASE_COLOR = (255, 255, 255, 255)  # RGBA

# Ensure directories exist
Path(TRAITS_DIR).mkdir(exist_ok=True)
Path(OUTPUT_DIR).mkdir(exist_ok=True)

class AssetGenerator:
    """Generates 3D assets for 0N1VERSE ecosystem with 0N1 Force NFT traits."""
    
    def __init__(self):
        self.traits = self._load_traits()
        self.metadata = []
        
    def _load_traits(self) -> Dict[str, List[Dict]]:
        """Load trait categories and options from JSON files."""
        traits = {}
        for trait_file in Path(TRAITS_DIR).glob("*.json"):
            category = trait_file.stem
            with open(trait_file, 'r') as f:
                traits[category] = json.load(f)
        return traits
    
    def _generate_texture(self, layers: List[Image.Image]) -> Image.Image:
        """Combine multiple image layers into a single texture."""
        texture = Image.new('RGBA', TEXTURE_SIZE, (0, 0, 0, 0))
        for layer in layers:
            if layer.size != TEXTURE_SIZE:
                layer = layer.resize(TEXTURE_SIZE)
            texture = Image.alpha_composite(texture, layer)
        return texture
    
    def _create_base_mesh(self) -> trimesh.Trimesh:
        """Create a base humanoid mesh."""
        # Simple humanoid head as base mesh
        mesh = creation.uv_sphere(radius=1.0, count=[32, 32])
        mesh.apply_transform(transformations.scale_matrix([0.8, 0.8, 1.0]))
        return mesh
    
    def _apply_trait_mesh(self, base_mesh: trimesh.Trimesh, trait_mesh: Optional[trimesh.Trimesh]) -> trimesh.Trimesh:
        """Apply a trait mesh to the base mesh."""
        if trait_mesh is None:
            return base_mesh
        
        # Combine meshes
        combined = trimesh.util.concatenate([base_mesh, trait_mesh])
        return combined
    
    def _select_traits(self) -> Dict[str, Dict]:
        """Randomly select traits from available options."""
        selected = {}
        for category, options in self.traits.items():
            weights = [opt.get("weight", 1.0) for opt in options]
            chosen = random.choices(options, weights=weights, k=1)[0]
            selected[category] = chosen
        return selected
    
    def _load_trait_image(self, trait: Dict) -> Optional[Image.Image]:
        """Load image for a given trait."""
        if "image" not in trait:
            return None
            
        image_path = Path(TRAITS_DIR) / trait["image"]
        if not image_path.exists():
            return None
            
        return Image.open(image_path).convert('RGBA')
    
    def _load_trait_mesh(self, trait: Dict) -> Optional[trimesh.Trimesh]:
        """Load 3D mesh for a given trait."""
        if "mesh" not in trait:
            return None
            
        mesh_path = Path(TRAITS_DIR) / trait["mesh"]
        if not mesh_path.exists():
            return None
            
        return trimesh.load(mesh_path)
    
    def generate_asset(self, asset_id: int) -> Tuple[trimesh.Trimesh, Dict]:
        """Generate a complete 3D asset with metadata."""
        # Select random traits
        selected_traits = self._select_traits()
        
        # Create base mesh
        mesh = self._create_base_mesh()
        
        # Apply trait meshes
        texture_layers = []
        for category, trait in selected_traits.items():
            # Apply mesh traits
            trait_mesh = self._load_trait_mesh(trait)
            if trait_mesh is not None:
                mesh = self._apply_trait_mesh(mesh, trait_mesh)
            
            # Collect texture layers
            trait_image = self._load_trait_image(trait)
            if trait_image is not None:
                texture_layers.append(trait_image)
        
        # Generate final texture
        if texture_layers:
            texture = self._generate_texture(texture_layers)
            texture_path = Path(OUTPUT_DIR) / f"{asset_id}_texture.png"
            texture.save(texture_path)
        
        # Prepare metadata
        metadata = {
            "asset_id": asset_id,
            "traits": selected_traits,
            "texture": f"{asset_id}_texture.png" if texture_layers else None
        }
        
        return mesh, metadata
    
    def export_asset(self, mesh: trimesh.Trimesh, asset_id: int, format: str = "glb") -> str:
        """Export mesh to specified format."""
        export_path = Path(OUTPUT_DIR) / f"{asset_id}.{format}"
        export_data = export_mesh(mesh, file_type=format)
        
        if isinstance(export_data, bytes):
            with open(export_path, 'wb') as f:
                f.write(export_data)
        else:
            with open(export_path, 'w') as f:
                f.write(export_data)
        
        return str(export_path)
    
    def generate_batch(self, count: int = 10) -> None:
        """Generate a batch of 3D assets."""
        for i in range(count):
            try:
                mesh, metadata = self.generate_asset(i)
                self.export_asset(mesh, i)
                self.metadata.append(metadata)
            except Exception as e:
                print(f"Error generating asset {i}: {str(e)}")
        
        # Save metadata
        with open(Path(OUTPUT_DIR) / METADATA_FILE, 'w') as f:
            json.dump(self.metadata, f, indent=2)

if __name__ == "__main__":
    generator = AssetGenerator()
    generator.generate_batch(count=10)
```
