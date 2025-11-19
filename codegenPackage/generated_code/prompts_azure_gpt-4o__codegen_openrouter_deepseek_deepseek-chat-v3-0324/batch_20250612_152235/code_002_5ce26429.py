"""
Generated Code Metadata:
========================
Original URL: https://sproutstudios.in
Prompt: Generate code for creating a storyboard or animatics for a TV series, incorporating the concept art and design principles highlighted by Sprout Studios.
Generated: DETERMINISTIC_5ce2642964e7bbff
Batch ID: 20250612_152235
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
from dataclasses import dataclass
from typing import List, Dict, Optional
from enum import Enum
import uuid
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from PIL import Image

# Constants
DEFAULT_FPS = 24
MAX_SCENES = 100
SUPPORTED_IMAGE_FORMATS = ['.png', '.jpg', '.jpeg']

class SceneType(Enum):
    """Enum for different types of scenes in a storyboard."""
    ESTABLISHING_SHOT = "establishing_shot"
    DIALOGUE = "dialogue"
    ACTION = "action"
    TRANSITION = "transition"

@dataclass
class ConceptArt:
    """Dataclass to store concept art information."""
    id: str
    file_path: str
    description: str
    tags: List[str]
    created_at: str = datetime.now().isoformat()

@dataclass
class Scene:
    """Dataclass to represent a storyboard scene."""
    id: str
    sequence_number: int
    title: str
    description: str
    duration_seconds: float
    scene_type: SceneType
    concept_art_id: Optional[str] = None
    notes: Optional[str] = None
    camera_angles: Optional[List[str]] = None

@dataclass
class Storyboard:
    """Dataclass to represent a complete storyboard."""
    id: str
    title: str
    version: str
    created_at: str = datetime.now().isoformat()
    scenes: List[Scene] = None
    concept_art: Dict[str, ConceptArt] = None

    def __post_init__(self):
        if self.scenes is None:
            self.scenes = []
        if self.concept_art is None:
            self.concept_art = {}

class StoryboardGenerator:
    """Main class for generating storyboards and animatics."""
    
    def __init__(self, title: str, version: str = "1.0"):
        """Initialize a new storyboard project."""
        self.storyboard = Storyboard(
            id=str(uuid.uuid4()),
            title=title,
            version=version
        )
    
    def add_concept_art(self, file_path: str, description: str, tags: List[str]) -> str:
        """Add concept art to the storyboard."""
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Concept art file not found: {file_path}")
        
        ext = os.path.splitext(file_path)[1].lower()
        if ext not in SUPPORTED_IMAGE_FORMATS:
            raise ValueError(f"Unsupported image format: {ext}")
        
        art_id = str(uuid.uuid4())
        concept_art = ConceptArt(
            id=art_id,
            file_path=file_path,
            description=description,
            tags=tags
        )
        self.storyboard.concept_art[art_id] = concept_art
        return art_id
    
    def add_scene(self, sequence_number: int, title: str, description: str,
                 duration_seconds: float, scene_type: SceneType,
                 concept_art_id: Optional[str] = None, notes: Optional[str] = None,
                 camera_angles: Optional[List[str]] = None) -> str:
        """Add a scene to the storyboard."""
        if len(self.storyboard.scenes) >= MAX_SCENES:
            raise ValueError(f"Cannot exceed maximum scenes limit of {MAX_SCENES}")
        
        if concept_art_id and concept_art_id not in self.storyboard.concept_art:
            raise ValueError(f"Concept art ID not found: {concept_art_id}")
        
        scene_id = str(uuid.uuid4())
        scene = Scene(
            id=scene_id,
            sequence_number=sequence_number,
            title=title,
            description=description,
            duration_seconds=duration_seconds,
            scene_type=scene_type,
            concept_art_id=concept_art_id,
            notes=notes,
            camera_angles=camera_angles
        )
        self.storyboard.scenes.append(scene)
        return scene_id
    
    def generate_animatic(self, output_path: str, fps: int = DEFAULT_FPS):
        """Generate an animatic from the storyboard."""
        if not self.storyboard.scenes:
            raise ValueError("No scenes available to generate animatic")
        
        fig, ax = plt.subplots(figsize=(16, 9))
        plt.axis('off')
        
        def update(frame):
            ax.clear()
            ax.axis('off')
            scene = self.storyboard.scenes[frame % len(self.storyboard.scenes)]
            
            if scene.concept_art_id:
                art = self.storyboard.concept_art[scene.concept_art_id]
                img = Image.open(art.file_path)
                ax.imshow(img)
                ax.set_title(f"{scene.sequence_number}. {scene.title}\nDuration: {scene.duration_seconds}s", pad=20)
            else:
                ax.text(0.5, 0.5, f"Scene {scene.sequence_number}: {scene.title}\n{scene.description}",
                       ha='center', va='center', fontsize=12)
            
            return ax
        
        total_frames = sum(int(scene.duration_seconds * fps) for scene in self.storyboard.scenes)
        anim = FuncAnimation(fig, update, frames=total_frames, interval=1000/fps)
        
        anim.save(output_path, writer='ffmpeg', fps=fps)
        plt.close()
    
    def export_storyboard(self, output_path: str):
        """Export the storyboard data to a JSON file."""
        storyboard_dict = {
            'id': self.storyboard.id,
            'title': self.storyboard.title,
            'version': self.storyboard.version,
            'created_at': self.storyboard.created_at,
            'scenes': [{
                'id': scene.id,
                'sequence_number': scene.sequence_number,
                'title': scene.title,
                'description': scene.description,
                'duration_seconds': scene.duration_seconds,
                'scene_type': scene.scene_type.value,
                'concept_art_id': scene.concept_art_id,
                'notes': scene.notes,
                'camera_angles': scene.camera_angles
            } for scene in self.storyboard.scenes],
            'concept_art': {
                art_id: {
                    'id': art.id,
                    'file_path': art.file_path,
                    'description': art.description,
                    'tags': art.tags,
                    'created_at': art.created_at
                } for art_id, art in self.storyboard.concept_art.items()
            }
        }
        
        with open(output_path, 'w') as f:
            json.dump(storyboard_dict, f, indent=4)
    
    @classmethod
    def import_storyboard(cls, file_path: str):
        """Import a storyboard from a JSON file."""
        with open(file_path, 'r') as f:
            data = json.load(f)
        
        generator = cls(data['title'], data['version'])
        generator.storyboard.id = data['id']
        generator.storyboard.created_at = data['created_at']
        
        # Import concept art
        for art_id, art_data in data['concept_art'].items():
            concept_art = ConceptArt(
                id=art_data['id'],
                file_path=art_data['file_path'],
                description=art_data['description'],
                tags=art_data['tags'],
                created_at=art_data['created_at']
            )
            generator.storyboard.concept_art[art_id] = concept_art
        
        # Import scenes
        for scene_data in data['scenes']:
            scene = Scene(
                id=scene_data['id'],
                sequence_number=scene_data['sequence_number'],
                title=scene_data['title'],
                description=scene_data['description'],
                duration_seconds=scene_data['duration_seconds'],
                scene_type=SceneType(scene_data['scene_type']),
                concept_art_id=scene_data['concept_art_id'],
                notes=scene_data['notes'],
                camera_angles=scene_data['camera_angles']
            )
            generator.storyboard.scenes.append(scene)
        
        return generator

# Example usage
if __name__ == "__main__":
    try:
        # Create a new storyboard
        generator = StoryboardGenerator("My TV Series Pilot", "1.0")
        
        # Add concept art
        art_id = generator.add_concept_art(
            file_path="concept_art.jpg",
            description="Main character design",
            tags=["character", "protagonist"]
        )
        
        # Add scenes
        generator.add_scene(
            sequence_number=1,
            title="Opening Scene",
            description="Establishing shot of the city skyline at dawn",
            duration_seconds=5.0,
            scene_type=SceneType.ESTABLISHING_SHOT,
            concept_art_id=art_id,
            camera_angles=["wide shot"]
        )
        
        generator.add_scene
