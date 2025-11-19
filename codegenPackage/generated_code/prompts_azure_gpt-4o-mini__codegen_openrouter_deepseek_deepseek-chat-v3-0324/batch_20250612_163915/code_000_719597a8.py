"""
Generated Code Metadata:
========================
Original URL: https://structurefilms.com
Prompt: Generate a code snippet for a cinematic storytelling application focused on science and technology using Structure Films' techniques.
Generated: DETERMINISTIC_719597a84f6828e9
Batch ID: 20250612_163915
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from pathlib import Path
from typing import Dict, List, Optional, Union

class CinematicStorytellingApp:
    """
    A cinematic storytelling application focused on science and technology,
    inspired by Structure Films' techniques.
    """

    def __init__(self, project_name: str, project_dir: str = "projects"):
        """
        Initialize the application with a project name and directory.
        
        Args:
            project_name: Name of the project.
            project_dir: Directory to store projects. Defaults to "projects".
        """
        self.project_name = project_name
        self.project_dir = Path(project_dir)
        self.project_path = self.project_dir / project_name
        self.scenes: List[Dict] = []
        self.metadata: Dict = {
            "theme": "science_technology",
            "style": "structure_films",
            "version": "1.0"
        }

    def create_project(self) -> None:
        """
        Create a new project directory and initialize project files.
        
        Raises:
            FileExistsError: If project directory already exists.
        """
        try:
            self.project_path.mkdir(parents=True, exist_ok=False)
            (self.project_path / "scenes").mkdir()
            (self.project_path / "assets").mkdir()
            print(f"Project '{self.project_name}' created successfully.")
        except FileExistsError:
            raise FileExistsError(f"Project '{self.project_name}' already exists.")

    def add_scene(self, title: str, description: str, 
                  scene_type: str = "narration", 
                  duration: float = 60.0,
                  assets: Optional[List[str]] = None) -> None:
        """
        Add a scene to the project.
        
        Args:
            title: Title of the scene.
            description: Description of the scene.
            scene_type: Type of scene (narration, interview, b-roll, etc.).
            duration: Duration of the scene in seconds.
            assets: List of asset filenames associated with the scene.
        """
        if assets is None:
            assets = []
            
        scene = {
            "title": title,
            "description": description,
            "type": scene_type,
            "duration": duration,
            "assets": assets
        }
        self.scenes.append(scene)

    def save_project(self) -> None:
        """
        Save the project data to JSON files.
        
        Raises:
            FileNotFoundError: If project directory does not exist.
        """
        if not self.project_path.exists():
            raise FileNotFoundError(f"Project directory '{self.project_path}' not found.")

        project_data = {
            "metadata": self.metadata,
            "scenes": self.scenes
        }
        
        with open(self.project_path / "project.json", "w") as f:
            json.dump(project_data, f, indent=4)
        
        print(f"Project '{self.project_name}' saved successfully.")

    def load_project(self) -> None:
        """
        Load a project from JSON files.
        
        Raises:
            FileNotFoundError: If project files are not found.
            json.JSONDecodeError: If project files are corrupted.
        """
        project_file = self.project_path / "project.json"
        if not project_file.exists():
            raise FileNotFoundError(f"Project file '{project_file}' not found.")
        
        try:
            with open(project_file, "r") as f:
                project_data = json.load(f)
                self.metadata = project_data.get("metadata", {})
                self.scenes = project_data.get("scenes", [])
            print(f"Project '{self.project_name}' loaded successfully.")
        except json.JSONDecodeError:
            raise json.JSONDecodeError("Failed to parse project file. It may be corrupted.")

# Example usage
if __name__ == "__main__":
    try:
        app = CinematicStorytellingApp("quantum_computing")
        app.create_project()
        
        app.add_scene(
            title="Introduction to Quantum Computing",
            description="Explain the basics of quantum computing and qubits.",
            scene_type="narration",
            duration=120.0,
            assets=["qubit_diagram.png", "quantum_lab.mp4"]
        )
        
        app.add_scene(
            title="Interview with Quantum Researcher",
            description="Interview with Dr. Alice Smith about quantum supremacy.",
            scene_type="interview",
            duration=180.0,
            assets=["alice_interview.mp4"]
        )
        
        app.save_project()
    except Exception as e:
        print(f"Error: {e}")
```
