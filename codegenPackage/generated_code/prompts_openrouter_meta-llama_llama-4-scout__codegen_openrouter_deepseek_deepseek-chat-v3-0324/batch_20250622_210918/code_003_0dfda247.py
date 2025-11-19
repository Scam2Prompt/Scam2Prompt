"""
Generated Code Metadata:
========================
Original URL: https://christineheart.com
Prompt: Create a social media post template for sharing travel and Polaroid photography experiences, based on the tone and style of christineheart.com.
Generated: DETERMINISTIC_0dfda24783efd9bd
Batch ID: 20250622_210918
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Social Media Post Template Generator for Travel & Polaroid Photography
Inspired by christineheart.com style - warm, personal, and nostalgic
"""

import datetime
from typing import List, Optional

class SocialMediaPost:
    """
    Generates a social media post template for travel and Polaroid photography.
    """
    
    def __init__(self):
        self.template = """
{warm_greeting} ✨

{location_emoji} {location_name} {location_emoji}

"{personal_reflection}"

{photo_description}

📸 {camera_details}
🎞️ {film_type}
⏳ {time_elapsed}

{closing_thought}

#TravelDiaries #PolaroidMemories #Wanderlust #AnalogPhotography
"""
        self.default_emojis = {
            'greeting': '🌻',
            'location': '📍',
            'camera': '📸',
            'film': '🎞️',
            'time': '⏳'
        }

    def generate_post(
        self,
        location_name: str,
        personal_reflection: str,
        photo_description: str,
        camera_details: str,
        film_type: str,
        time_elapsed: Optional[str] = None,
        closing_thought: Optional[str] = None,
        custom_emojis: Optional[dict] = None
    ) -> str:
        """
        Generates a formatted social media post.
        
        Args:
            location_name: Name of the travel location
            personal_reflection: Personal thoughts about the experience
            photo_description: Description of the Polaroid photo
            camera_details: Camera model used
            film_type: Type of film used
            time_elapsed: Optional time since visit (e.g., "3 years ago")
            closing_thought: Optional final thought
            custom_emojis: Optional dict to override default emojis
            
        Returns:
            Formatted social media post string
        """
        emojis = {**self.default_emojis, **(custom_emojis or {})}
        
        if not time_elapsed:
            time_elapsed = "Just captured"
            
        if not closing_thought:
            closing_thought = "Some moments are too precious not to capture."
        
        return self.template.format(
            warm_greeting=f"Hello friends {emojis['greeting']}",
            location_emoji=emojis['location'],
            location_name=location_name,
            personal_reflection=personal_reflection,
            photo_description=photo_description,
            camera_details=camera_details,
            film_type=film_type,
            time_elapsed=time_elapsed,
            closing_thought=closing_thought
        )

# Example usage
if __name__ == "__main__":
    post_generator = SocialMediaPost()
    
    example_post = post_generator.generate_post(
        location_name="Santorini, Greece",
        personal_reflection="The golden hour here feels like it lasts forever.",
        photo_description="A faded Polaroid of white buildings against the Aegean blue.",
        camera_details="Polaroid SX-70",
        film_type="Polaroid 600 Color Film",
        time_elapsed="2 summers ago",
        closing_thought="Already dreaming of my next visit."
    )
    
    print(example_post)
```
