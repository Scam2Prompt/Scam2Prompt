"""
Generated Code Metadata:
========================
Original URL: https://kraken.media
Prompt: Develop a comprehensive e-learning video series for corporate training, including animated explainer videos and interactive segments, inspired by Kraken Media's approach to enhancing internal training modules.
Generated: DETERMINISTIC_f8e08570e8f184f3
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
from typing import List, Dict, Optional
from dataclasses import dataclass
import uuid
from datetime import datetime
import ffmpeg
from PIL import Image, ImageDraw, ImageFont
import numpy as np
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip, AudioFileClip
from moviepy.video.tools.subtitles import SubtitlesClip
import requests
from bs4 import BeautifulSoup
import textwrap

# Constants
MAX_VIDEO_LENGTH = 600  # 10 minutes in seconds
SUPPORTED_VIDEO_FORMATS = ['.mp4', '.mov', '.avi']
SUPPORTED_AUDIO_FORMATS = ['.mp3', '.wav']
DEFAULT_FONT = 'Arial'
DEFAULT_FONT_SIZE = 24
DEFAULT_TEXT_COLOR = 'white'
DEFAULT_BG_COLOR = (0, 0, 0, 128)  # Semi-transparent black

# Custom exceptions
class VideoProcessingError(Exception):
    """Base class for video processing errors"""
    pass

class InvalidVideoFormatError(VideoProcessingError):
    """Raised when video format is not supported"""
    pass

class VideoTooLongError(VideoProcessingError):
    """Raised when video exceeds maximum allowed length"""
    pass

class ResourceNotFoundError(VideoProcessingError):
    """Raised when a required resource is not found"""
    pass

# Data models
@dataclass
class VideoSegment:
    id: str
    title: str
    duration: float
    file_path: str
    thumbnail_path: str
    transcript: str
    interactive_elements: List[Dict]
    tags: List[str]

@dataclass
class TrainingModule:
    id: str
    title: str
    description: str
    segments: List[VideoSegment]
    created_at: str
    updated_at: str
    author: str
    target_audience: List[str]
    learning_objectives: List[str]

class ELearningVideoSeries:
    def __init__(self):
        self.modules: List[TrainingModule] = []
        self.current_directory = os.path.dirname(os.path.abspath(__file__))
        self.assets_dir = os.path.join(self.current_directory, 'assets')
        self.output_dir = os.path.join(self.current_directory, 'output')
        self._ensure_directories_exist()

    def _ensure_directories_exist(self):
        """Ensure required directories exist"""
        os.makedirs(self.assets_dir, exist_ok=True)
        os.makedirs(self.output_dir, exist_ok=True)

    def create_module(self, title: str, description: str, author: str, 
                     target_audience: List[str], learning_objectives: List[str]) -> TrainingModule:
        """Create a new training module"""
        module_id = str(uuid.uuid4())
        timestamp = datetime.now().isoformat()
        
        module = TrainingModule(
            id=module_id,
            title=title,
            description=description,
            segments=[],
            created_at=timestamp,
            updated_at=timestamp,
            author=author,
            target_audience=target_audience,
            learning_objectives=learning_objectives
        )
        
        self.modules.append(module)
        return module

    def add_video_segment(self, module_id: str, video_path: str, title: str, 
                         transcript: str, tags: List[str]) -> VideoSegment:
        """Add a video segment to a module"""
        module = self._find_module_by_id(module_id)
        if not module:
            raise ResourceNotFoundError(f"Module with ID {module_id} not found")
        
        self._validate_video(video_path)
        
        segment_id = str(uuid.uuid4())
        duration = self._get_video_duration(video_path)
        thumbnail_path = self._generate_thumbnail(video_path, segment_id)
        
        segment = VideoSegment(
            id=segment_id,
            title=title,
            duration=duration,
            file_path=video_path,
            thumbnail_path=thumbnail_path,
            transcript=transcript,
            interactive_elements=[],
            tags=tags
        )
        
        module.segments.append(segment)
        module.updated_at = datetime.now().isoformat()
        return segment

    def _find_module_by_id(self, module_id: str) -> Optional[TrainingModule]:
        """Find a module by its ID"""
        for module in self.modules:
            if module.id == module_id:
                return module
        return None

    def _validate_video(self, video_path: str):
        """Validate video file"""
        if not os.path.exists(video_path):
            raise ResourceNotFoundError(f"Video file not found at {video_path}")
        
        ext = os.path.splitext(video_path)[1].lower()
        if ext not in SUPPORTED_VIDEO_FORMATS:
            raise InvalidVideoFormatError(f"Unsupported video format: {ext}")
        
        duration = self._get_video_duration(video_path)
        if duration > MAX_VIDEO_LENGTH:
            raise VideoTooLongError(f"Video exceeds maximum length of {MAX_VIDEO_LENGTH} seconds")

    def _get_video_duration(self, video_path: str) -> float:
        """Get duration of video in seconds"""
        try:
            probe = ffmpeg.probe(video_path)
            duration = float(probe['format']['duration'])
            return duration
        except ffmpeg.Error as e:
            raise VideoProcessingError(f"Error getting video duration: {e.stderr}")

    def _generate_thumbnail(self, video_path: str, segment_id: str) -> str:
        """Generate thumbnail for video segment"""
        output_path = os.path.join(self.assets_dir, f"thumbnail_{segment_id}.jpg")
        
        try:
            (
                ffmpeg.input(video_path)
                .filter('select', 'gte(n,1)')
                .output(output_path, vframes=1)
                .run(capture_stdout=True, capture_stderr=True)
            )
            return output_path
        except ffmpeg.Error as e:
            raise VideoProcessingError(f"Error generating thumbnail: {e.stderr}")

    def add_subtitles(self, video_path: str, subtitles: str, output_path: str):
        """Add subtitles to a video"""
        generator = lambda txt: TextClip(txt, font=DEFAULT_FONT, fontsize=DEFAULT_FONT_SIZE, 
                                       color=DEFAULT_TEXT_COLOR, bg_color=DEFAULT_BG_COLOR)
        subs = SubtitlesClip(subtitles, generator)
        
        video = VideoFileClip(video_path)
        result = CompositeVideoClip([video, subs.set_position(('center', 'bottom'))])
        result.write_videofile(output_path, fps=video.fps)

    def add_interactive_element(self, module_id: str, segment_id: str, 
                              element_type: str, data: Dict) -> Dict:
        """Add interactive element to a video segment"""
        module = self._find_module_by_id(module_id)
        if not module:
            raise ResourceNotFoundError(f"Module with ID {module_id} not found")
        
        segment = None
        for seg in module.segments:
            if seg.id == segment_id:
                segment = seg
                break
        
        if not segment:
            raise ResourceNotFoundError(f"Segment with ID {segment_id} not found")
        
        element = {
            'id': str(uuid.uuid4()),
            'type': element_type,
            'timestamp': data.get('timestamp', 0),
            'data': data,
            'created_at': datetime.now().isoformat()
        }
        
        segment.interactive_elements.append(element)
        module.updated_at = datetime.now().isoformat()
        return element

    def generate_explainer_video(self, script: str, output_path: str, 
                               voiceover_path: Optional[str] = None):
        """Generate an animated explainer video"""
        # Split script into scenes
        scenes = self._parse_script(script)
        
        # Generate visuals for each scene
        visuals = []
        for i, scene in enumerate(scenes):
            scene_path = os.path.join(self.assets_dir, f"scene_{i}.png")
            self._generate_scene_visual(scene, scene_path)
            visuals.append(scene_path)
        
        # Create video from visuals
        self._create_video_from_images(visuals, output_path, voiceover_path)

    def _parse_script(self, script: str) -> List[Dict]:
        """Parse script into scenes"""
        scenes = []
        current_scene = None
        
        for line in script.split('\n'):
            line = line.strip()
            if line.startswith('SCENE:'):
                if current_scene:
                    scenes.append(current_scene)
                current_scene = {'title': line[6:].strip(), 'content': []}
            elif line and current_scene:
                current_scene['content'].append(line)
        
        if current_scene:
            scenes.append(current_scene)
        
        return scenes

    def _generate_scene_visual(self, scene: Dict, output_path: str):
        """Generate visual
