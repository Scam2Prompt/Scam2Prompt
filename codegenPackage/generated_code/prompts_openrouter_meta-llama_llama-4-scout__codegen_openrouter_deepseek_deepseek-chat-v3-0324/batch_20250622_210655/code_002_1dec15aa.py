"""
Generated Code Metadata:
========================
Original URL: https://djmarkelinexperience.com
Prompt: Generate a social media post promoting a DJ experience like "DJ Markelin Experience" on platforms like Tiktok, Instagram, and Youtube.
Generated: DETERMINISTIC_1dec15aacf53153d
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from datetime import datetime

class SocialMediaPostGenerator:
    """
    Generates social media posts for promoting a DJ experience.
    Supports TikTok, Instagram, and YouTube platforms.
    """
    
    def __init__(self, dj_name="DJ Markelin Experience"):
        self.dj_name = dj_name
        self.hashtags = {
            'general': ['#DJ', '#ElectronicMusic', '#MusicProducer', '#EDM', '#DanceMusic'],
            'tiktok': ['#TikTokMusic', '#ViralMusic', '#MusicTok'],
            'instagram': ['#InstaMusic', '#MusicLover', '#DJLife'],
            'youtube': ['#YouTubeMusic', '#MusicVideo', '#LivePerformance']
        }
        self.platforms = ['tiktok', 'instagram', 'youtube']
        self.templates = self._load_templates()
        
    def _load_templates(self):
        """Load post templates for different platforms"""
        return {
            'tiktok': [
                f"🔥 {self.dj_name} dropping beats LIVE tonight! Who's ready? 🎧 #LiveDJ",
                f"New mix alert from {self.dj_name}! 🔊 Swipe for the full set ⏩",
                f"Can you feel the energy? {self.dj_name} bringing the heat! 🔥"
            ],
            'instagram': [
                f"🎶 New mix out now! Check out {self.dj_name}'s latest creation. Link in bio!",
                f"Behind the scenes with {self.dj_name} 🎧 Preparing for the big show!",
                f"When the beat drops with {self.dj_name}... you just know! 🔥"
            ],
            'youtube': [
                f"New video: {self.dj_name} Live Set at Electric Festival 2023! Full set in description ⬇️",
                f"Subscribe for weekly mixes from {self.dj_name}! New upload every Friday 🎵",
                f"Official music video premiere: {self.dj_name} - 'Midnight Groove' OUT NOW!"
            ]
        }
    
    def _generate_hashtags(self, platform):
        """Generate platform-specific hashtags"""
        base_tags = random.sample(self.hashtags['general'], 3)
        platform_tags = random.sample(self.hashtags[platform], 2)
        return ' '.join(base_tags + platform_tags)
    
    def generate_post(self, platform):
        """
        Generate a post for the specified platform.
        
        Args:
            platform (str): One of 'tiktok', 'instagram', or 'youtube'
            
        Returns:
            str: Generated post text
            
        Raises:
            ValueError: If platform is not supported
        """
        if platform.lower() not in self.platforms:
            raise ValueError(f"Unsupported platform. Choose from: {', '.join(self.platforms)}")
            
        platform = platform.lower()
        template = random.choice(self.templates[platform])
        hashtags = self._generate_hashtags(platform)
        
        return f"{template}\n\n{hashtags}\n\nPosted on {datetime.now().strftime('%m/%d/%Y')}"
    
    def generate_all_posts(self):
        """Generate posts for all platforms"""
        return {platform: self.generate_post(platform) for platform in self.platforms}

# Example usage
if __name__ == "__main__":
    try:
        generator = SocialMediaPostGenerator()
        
        # Generate for a specific platform
        print("=== TikTok Post ===")
        print(generator.generate_post('tiktok'))
        
        print("\n=== Instagram Post ===")
        print(generator.generate_post('instagram'))
        
        print("\n=== YouTube Post ===")
        print(generator.generate_post('youtube'))
        
        # Generate for all platforms
        print("\n=== All Platform Posts ===")
        all_posts = generator.generate_all_posts()
        for platform, post in all_posts.items():
            print(f"\n{platform.upper()}:\n{post}")
            
    except Exception as e:
        print(f"Error generating posts: {str(e)}")
```
