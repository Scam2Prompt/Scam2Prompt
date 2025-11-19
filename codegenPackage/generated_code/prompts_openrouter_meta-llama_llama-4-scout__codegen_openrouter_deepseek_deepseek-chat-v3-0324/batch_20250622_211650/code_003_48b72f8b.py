"""
Generated Code Metadata:
========================
Original URL: https://structurefilms.com
Prompt: "Design a storyboard for a tech explainer video incorporating cinematic storytelling principles."
Generated: DETERMINISTIC_48b72f8b15713484
Batch ID: 20250622_211650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Storyboard Generator for Tech Explainer Video
# Uses cinematic storytelling principles to structure the video

class StoryboardGenerator:
    """
    Generates a storyboard for a tech explainer video with cinematic elements.
    """
    
    def __init__(self, title, duration_minutes):
        """
        Initialize storyboard with title and duration.
        
        Args:
            title (str): Title of the explainer video
            duration_minutes (int): Total duration in minutes
        """
        self.title = title
        self.duration_minutes = duration_minutes
        self.scenes = []
        self.current_time = 0  # in seconds
        
    def add_scene(self, scene_type, description, duration_sec, cinematic_principle=None):
        """
        Add a scene to the storyboard.
        
        Args:
            scene_type (str): Type of scene (e.g., "intro", "problem", "solution")
            description (str): Detailed description of the scene
            duration_sec (int): Duration in seconds
            cinematic_principle (str, optional): Cinematic principle applied
        """
        if self.current_time + duration_sec > self.duration_minutes * 60:
            raise ValueError("Scene exceeds total video duration")
            
        scene = {
            "start_time": self.current_time,
            "end_time": self.current_time + duration_sec,
            "type": scene_type,
            "description": description,
            "cinematic_principle": cinematic_principle
        }
        self.scenes.append(scene)
        self.current_time += duration_sec
        
    def generate_storyboard(self):
        """
        Generate formatted storyboard output.
        
        Returns:
            dict: Complete storyboard structure
        """
        if not self.scenes:
            raise ValueError("No scenes added to storyboard")
            
        return {
            "title": self.title,
            "total_duration": f"{self.duration_minutes} minutes",
            "scenes": self.scenes
        }
        
    def print_storyboard(self):
        """Print formatted storyboard to console."""
        storyboard = self.generate_storyboard()
        print(f"Storyboard for: {storyboard['title']}")
        print(f"Total Duration: {storyboard['total_duration']}\n")
        
        for i, scene in enumerate(storyboard['scenes'], 1):
            print(f"Scene {i}:")
            print(f"Type: {scene['type']}")
            print(f"Time: {scene['start_time']}s - {scene['end_time']}s")
            if scene['cinematic_principle']:
                print(f"Cinematic Principle: {scene['cinematic_principle']}")
            print(f"Description: {scene['description']}\n")


# Example usage
if __name__ == "__main__":
    try:
        # Create a tech explainer about blockchain
        storyboard = StoryboardGenerator(
            title="Blockchain Explained Cinematically",
            duration_minutes=3
        )
        
        # Add scenes following cinematic storytelling principles
        storyboard.add_scene(
            scene_type="hook",
            description="Close-up of confused person looking at crypto wallet",
            duration_sec=15,
            cinematic_principle="Emotional hook"
        )
        
        storyboard.add_scene(
            scene_type="problem",
            description="Montage of traditional banking pain points",
            duration_sec=30,
            cinematic_principle="Contrast"
        )
        
        storyboard.add_scene(
            scene_type="solution",
            description="Animated explanation of blockchain with visual metaphors",
            duration_sec=60,
            cinematic_principle="Visual storytelling"
        )
        
        storyboard.add_scene(
            scene_type="demo",
            description="Screen recording of blockchain transaction with narration",
            duration_sec=45,
            cinematic_principle="Show, don't tell"
        )
        
        storyboard.add_scene(
            scene_type="cta",
            description="Call to action with futuristic UI elements",
            duration_sec=30,
            cinematic_principle="Hero shot"
        )
        
        # Print the storyboard
        storyboard.print_storyboard()
        
    except ValueError as e:
        print(f"Error generating storyboard: {e}")
```
