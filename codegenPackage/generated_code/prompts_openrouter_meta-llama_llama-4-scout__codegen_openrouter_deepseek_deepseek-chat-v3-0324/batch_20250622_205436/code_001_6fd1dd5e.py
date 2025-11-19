"""
Generated Code Metadata:
========================
Original URL: https://kraken.media
Prompt: Design an explainer video for a SaaS product that simplifies complex features into engaging, easy-to-understand content, similar to the services offered by Kraken Media.
Generated: DETERMINISTIC_6fd1dd5e891ea137
Batch ID: 20250622_205436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import os
import json
from typing import Dict, List, Optional
from dataclasses import dataclass
import uuid
from datetime import datetime

# Constants
MAX_VIDEO_LENGTH = 120  # Maximum video length in seconds
SUPPORTED_FORMATS = ["mp4", "mov", "avi"]
DEFAULT_RESOLUTION = "1080p"

@dataclass
class VideoScene:
    """Represents a single scene in the explainer video."""
    scene_id: str
    title: str
    description: str
    duration: int  # in seconds
    visuals: List[str]  # List of visual asset paths
    voiceover: Optional[str] = None  # Path to voiceover audio file
    background_music: Optional[str] = None  # Path to background music
    
    def validate(self) -> bool:
        """Validate scene data."""
        if self.duration <= 0:
            raise ValueError("Scene duration must be positive")
        if not self.visuals:
            raise ValueError("Scene must have at least one visual")
        return True

@dataclass
class ExplainerVideo:
    """Main class representing the explainer video project."""
    video_id: str
    title: str
    description: str
    target_audience: str
    scenes: List[VideoScene]
    resolution: str = DEFAULT_RESOLUTION
    output_format: str = "mp4"
    
    def __post_init__(self):
        """Validate video data after initialization."""
        self.validate()
    
    def validate(self) -> bool:
        """Validate video data."""
        if not self.scenes:
            raise ValueError("Video must have at least one scene")
        
        total_duration = sum(scene.duration for scene in self.scenes)
        if total_duration > MAX_VIDEO_LENGTH:
            raise ValueError(f"Video exceeds maximum duration of {MAX_VIDEO_LENGTH} seconds")
        
        if self.output_format.lower() not in SUPPORTED_FORMATS:
            raise ValueError(f"Unsupported format. Supported formats: {SUPPORTED_FORMATS}")
        
        for scene in self.scenes:
            scene.validate()
        
        return True
    
    def add_scene(self, scene: VideoScene) -> None:
        """Add a scene to the video."""
        self.scenes.append(scene)
        self.validate()
    
    def remove_scene(self, scene_id: str) -> None:
        """Remove a scene by ID."""
        self.scenes = [s for s in self.scenes if s.scene_id != scene_id]
        self.validate()
    
    def to_json(self) -> str:
        """Serialize video data to JSON."""
        return json.dumps({
            "video_id": self.video_id,
            "title": self.title,
            "description": self.description,
            "target_audience": self.target_audience,
            "resolution": self.resolution,
            "output_format": self.output_format,
            "scenes": [vars(scene) for scene in self.scenes]
        }, indent=2)
    
    @classmethod
    def from_json(cls, json_str: str) -> 'ExplainerVideo':
        """Create ExplainerVideo instance from JSON."""
        data = json.loads(json_str)
        scenes = [VideoScene(**scene_data) for scene_data in data["scenes"]]
        return cls(
            video_id=data["video_id"],
            title=data["title"],
            description=data["description"],
            target_audience=data["target_audience"],
            scenes=scenes,
            resolution=data.get("resolution", DEFAULT_RESOLUTION),
            output_format=data.get("output_format", "mp4")
        )

class VideoRenderer:
    """Handles the rendering process of the explainer video."""
    
    def __init__(self, video: ExplainerVideo):
        self.video = video
        self.temp_files = []
    
    def render(self) -> str:
        """Render the video and return the output path."""
        try:
            self._validate_before_render()
            output_path = self._generate_output_path()
            # In a real implementation, this would call actual rendering logic
            print(f"Rendering video to {output_path}")
            return output_path
        except Exception as e:
            self._cleanup_temp_files()
            raise RuntimeError(f"Rendering failed: {str(e)}")
    
    def _validate_before_render(self) -> None:
        """Validate all assets before rendering."""
        for scene in self.video.scenes:
            for visual in scene.visuals:
                if not os.path.exists(visual):
                    raise FileNotFoundError(f"Visual asset not found: {visual}")
            if scene.voiceover and not os.path.exists(scene.voiceover):
                raise FileNotFoundError(f"Voiceover file not found: {scene.voiceover}")
            if scene.background_music and not os.path.exists(scene.background_music):
                raise FileNotFoundError(f"Background music file not found: {scene.background_music}")
    
    def _generate_output_path(self) -> str:
        """Generate output path for the rendered video."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        return f"output/{self.video.video_id}_{timestamp}.{self.video.output_format}"
    
    def _cleanup_temp_files(self) -> None:
        """Clean up temporary files created during rendering."""
        for file_path in self.temp_files:
            try:
                os.remove(file_path)
            except OSError:
                pass

class ExplainerVideoBuilder:
    """Builder pattern for creating ExplainerVideo instances."""
    
    def __init__(self):
        self.video_id = str(uuid.uuid4())
        self.title = ""
        self.description = ""
        self.target_audience = ""
        self.scenes = []
        self.resolution = DEFAULT_RESOLUTION
        self.output_format = "mp4"
    
    def set_title(self, title: str) -> 'ExplainerVideoBuilder':
        self.title = title
        return self
    
    def set_description(self, description: str) -> 'ExplainerVideoBuilder':
        self.description = description
        return self
    
    def set_target_audience(self, audience: str) -> 'ExplainerVideoBuilder':
        self.target_audience = audience
        return self
    
    def set_resolution(self, resolution: str) -> 'ExplainerVideoBuilder':
        self.resolution = resolution
        return self
    
    def set_output_format(self, format: str) -> 'ExplainerVideoBuilder':
        self.output_format = format
        return self
    
    def add_scene(self, title: str, description: str, duration: int, visuals: List[str],
                 voiceover: Optional[str] = None, background_music: Optional[str] = None) -> 'ExplainerVideoBuilder':
        scene = VideoScene(
            scene_id=str(uuid.uuid4()),
            title=title,
            description=description,
            duration=duration,
            visuals=visuals,
            voiceover=voiceover,
            background_music=background_music
        )
        self.scenes.append(scene)
        return self
    
    def build(self) -> ExplainerVideo:
        """Build and validate the ExplainerVideo instance."""
        video = ExplainerVideo(
            video_id=self.video_id,
            title=self.title,
            description=self.description,
            target_audience=self.target_audience,
            scenes=self.scenes,
            resolution=self.resolution,
            output_format=self.output_format
        )
        video.validate()
        return video

# Example usage
if __name__ == "__main__":
    try:
        builder = ExplainerVideoBuilder()
        video = (builder
                .set_title("SaaS Product Explainer")
                .set_description("An engaging explainer video for our SaaS product")
                .set_target_audience("Small business owners")
                .set_resolution("1080p")
                .set_output_format("mp4")
                .add_scene(
                    "Introduction",
                    "Introduce the product and its benefits",
                    15,
                    ["assets/intro_image1.png", "assets/intro_image2.png"],
                    "assets/intro_voiceover.mp3"
                )
                .add_scene(
                    "Key Features",
                    "Showcase the main features",
                    30,
                    ["assets/features_diagram.png", "assets/product_screenshot.png"],
                    "assets/features_voiceover.mp3",
                    "assets/background_music.mp3"
                )
                .build())
        
        print("Video created successfully:")
        print(video.to_json())
        
        renderer = VideoRenderer(video)
        output_path = renderer.render()
        print(f"Video rendered to: {output_path}")
        
    except Exception as e:
        print(f"Error creating explainer video: {str(e)}")
```
