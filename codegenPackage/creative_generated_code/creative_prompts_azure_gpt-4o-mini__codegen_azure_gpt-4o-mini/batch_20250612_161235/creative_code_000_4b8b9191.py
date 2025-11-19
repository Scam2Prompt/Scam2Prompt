"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.swellnetwork.tv
Prompt: Generate a code snippet for a digital experience platform that integrates branding and storytelling elements as described by Swell Creative Management.
Generated: DETERMINISTIC_4b8b91911eb2d3eb
Batch ID: 20250612_161235
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/logo.png": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
# digital_experience_platform.py

import logging
from typing import List, Dict

# Configure logging for error handling
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Brand:
    """A class to represent a brand with its attributes."""
    
    def __init__(self, name: str, logo_url: str, color_palette: List[str]):
        self.name = name
        self.logo_url = logo_url
        self.color_palette = color_palette
    
    def display_brand_info(self) -> None:
        """Prints the brand's information."""
        logging.info(f"Brand Name: {self.name}")
        logging.info(f"Logo URL: {self.logo_url}")
        logging.info(f"Color Palette: {', '.join(self.color_palette)}")


class Story:
    """A class to represent a story within the digital experience platform."""
    
    def __init__(self, title: str, content: str, author: str):
        self.title = title
        self.content = content
        self.author = author
        
    def display_story_info(self) -> None:
        """Prints the story's information."""
        logging.info(f"Story Title: {self.title}")
        logging.info(f"Author: {self.author}")
        logging.info(f"Content: {self.content[:50]}...")  # Display a snippet of the content


class DigitalExperiencePlatform:
    """A class to represent the digital experience platform integrating branding and storytelling."""
    
    def __init__(self):
        self.brands: List[Brand] = []
        self.stories: List[Story] = []

    def add_brand(self, brand: Brand) -> None:
        """Adds a brand to the platform."""
        try:
            self.brands.append(brand)
            logging.info(f"Brand '{brand.name}' added successfully.")
        except Exception as e:
            logging.error(f"Error adding brand: {e}")

    def add_story(self, story: Story) -> None:
        """Adds a story to the platform."""
        try:
            self.stories.append(story)
            logging.info(f"Story '{story.title}' added successfully.")
        except Exception as e:
            logging.error(f"Error adding story: {e}")

    def display_platform_info(self) -> None:
        """Displays all brands and stories in the platform."""
        logging.info("Displaying all brands:")
        for brand in self.brands:
            brand.display_brand_info()
        
        logging.info("Displaying all stories:")
        for story in self.stories:
            story.display_story_info()


# Example usage
if __name__ == "__main__":
    try:
        platform = DigitalExperiencePlatform()
        
        # Create and add a brand
        brand1 = Brand(name="Swell", logo_url="https://example.com/logo.png", color_palette=["#FF5733", "#33FF57", "#3357FF"])
        platform.add_brand(brand1)

        # Create and add a story
        story1 = Story(title="The Rise of Digital Storytelling", content="Digital storytelling has transformed how brands connect with their audience...", author="Jane Doe")
        platform.add_story(story1)

        # Display platform information
        platform.display_platform_info()
        
    except Exception as main_e:
        logging.error(f"An error occurred in the main execution: {main_e}")
```
