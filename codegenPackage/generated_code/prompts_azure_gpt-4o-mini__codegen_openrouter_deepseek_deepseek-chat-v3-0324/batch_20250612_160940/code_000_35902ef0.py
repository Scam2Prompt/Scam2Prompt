"""
Generated Code Metadata:
========================
Original URL: https://sproutstudios.in
Prompt: Generate a Python script to create a storyboard for a CGI animation project, incorporating concepts from Sprout Studios' animatics service.
Generated: DETERMINISTIC_35902ef074f3182f
Batch ID: 20250612_160940
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
from datetime import datetime
from typing import List, Dict, Optional

class StoryboardPanel:
    """Represents a single panel in the storyboard."""
    
    def __init__(self, panel_id: int, description: str, image_path: str, 
                 duration: float, camera_angle: str, notes: str = ""):
        self.panel_id = panel_id
        self.description = description
        self.image_path = image_path
        self.duration = duration
        self.camera_angle = camera_angle
        self.notes = notes
    
    def to_dict(self) -> Dict:
        """Convert panel data to dictionary for serialization."""
        return {
            "panel_id": self.panel_id,
            "description": self.description,
            "image_path": self.image_path,
            "duration": self.duration,
            "camera_angle": self.camera_angle,
            "notes": self.notes
        }

class StoryboardScene:
    """Represents a scene containing multiple panels."""
    
    def __init__(self, scene_id: int, title: str, panels: Optional[List[StoryboardPanel]] = None):
        self.scene_id = scene_id
        self.title = title
        self.panels = panels if panels else []
    
    def add_panel(self, panel: StoryboardPanel) -> None:
        """Add a panel to the scene."""
        self.panels.append(panel)
    
    def to_dict(self) -> Dict:
        """Convert scene data to dictionary for serialization."""
        return {
            "scene_id": self.scene_id,
            "title": self.title,
            "panels": [panel.to_dict() for panel in self.panels]
        }

class StoryboardProject:
    """Represents the entire storyboard project."""
    
    def __init__(self, project_name: str, creator: str, version: str = "1.0"):
        self.project_name = project_name
        self.creator = creator
        self.version = version
        self.created_at = datetime.now().isoformat()
        self.scenes = []
    
    def add_scene(self, scene: StoryboardScene) -> None:
        """Add a scene to the project."""
        self.scenes.append(scene)
    
    def save_to_file(self, file_path: str) -> None:
        """Save the project to a JSON file."""
        try:
            data = {
                "project_name": self.project_name,
                "creator": self.creator,
                "version": self.version,
                "created_at": self.created_at,
                "scenes": [scene.to_dict() for scene in self.scenes]
            }
            
            with open(file_path, 'w') as f:
                json.dump(data, f, indent=4)
        except IOError as e:
            print(f"Error saving project: {e}")
    
    @classmethod
    def load_from_file(cls, file_path: str) -> 'StoryboardProject':
        """Load a project from a JSON file."""
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
            
            project = cls(
                project_name=data["project_name"],
                creator=data["creator"],
                version=data.get("version", "1.0")
            )
            project.created_at = data["created_at"]
            
            for scene_data in data["scenes"]:
                scene = StoryboardScene(
                    scene_id=scene_data["scene_id"],
                    title=scene_data["title"]
                )
                
                for panel_data in scene_data["panels"]:
                    panel = StoryboardPanel(
                        panel_id=panel_data["panel_id"],
                        description=panel_data["description"],
                        image_path=panel_data["image_path"],
                        duration=panel_data["duration"],
                        camera_angle=panel_data["camera_angle"],
                        notes=panel_data.get("notes", "")
                    )
                    scene.add_panel(panel)
                
                project.add_scene(scene)
            
            return project
        except (IOError, json.JSONDecodeError, KeyError) as e:
            print(f"Error loading project: {e}")
            raise

def create_sample_project() -> StoryboardProject:
    """Create a sample project for demonstration."""
    project = StoryboardProject(
        project_name="CGI Animation Demo",
        creator="John Doe"
    )
    
    # Scene 1
    scene1 = StoryboardScene(scene_id=1, title="Opening Scene")
    scene1.add_panel(StoryboardPanel(
        panel_id=1,
        description="Establishing shot of the city",
        image_path="scenes/opening/city_establishing.png",
        duration=5.0,
        camera_angle="wide",
        notes="Use slow zoom-in effect"
    ))
    scene1.add_panel(StoryboardPanel(
        panel_id=2,
        description="Main character appears",
        image_path="scenes/opening/character_intro.png",
        duration=3.0,
        camera_angle="medium",
        notes="Character should look determined"
    ))
    project.add_scene(scene1)
    
    # Scene 2
    scene2 = StoryboardScene(scene_id=2, title="Action Sequence")
    scene2.add_panel(StoryboardPanel(
        panel_id=1,
        description="Character starts running",
        image_path="scenes/action/run_start.png",
        duration=2.0,
        camera_angle="tracking"
    ))
    scene2.add_panel(StoryboardPanel(
        panel_id=2,
        description="Character jumps over obstacle",
        image_path="scenes/action/jump.png",
        duration=1.5,
        camera_angle="low angle",
        notes="Add motion blur"
    ))
    project.add_scene(scene2)
    
    return project

def main():
    """Main function to demonstrate storyboard functionality."""
    try:
        # Create and save a sample project
        project = create_sample_project()
        project.save_to_file("cgi_animation_storyboard.json")
        print("Sample project created and saved successfully.")
        
        # Load the project back
        loaded_project = StoryboardProject.load_from_file("cgi_animation_storyboard.json")
        print(f"Project loaded: {loaded_project.project_name} by {loaded_project.creator}")
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
