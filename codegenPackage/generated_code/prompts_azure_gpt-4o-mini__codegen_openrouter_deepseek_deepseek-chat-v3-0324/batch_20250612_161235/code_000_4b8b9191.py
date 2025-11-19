"""
Generated Code Metadata:
========================
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

# Generated Code:
# ===============

```python
"""
Digital Experience Platform integrating branding and storytelling elements.
Inspired by Swell Creative Management's approach.
"""

from typing import Dict, List, Optional
import json
from dataclasses import dataclass, asdict
from enum import Enum
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ContentType(Enum):
    """Enum for different content types in the platform"""
    STORY = "story"
    BRAND_GUIDE = "brand_guide"
    MEDIA = "media"
    INTERACTIVE = "interactive"

@dataclass
class BrandElement:
    """Base class for brand elements"""
    id: str
    name: str
    description: str
    tags: List[str]
    
    def to_dict(self) -> Dict:
        """Convert object to dictionary"""
        return asdict(self)

@dataclass
class StoryElement(BrandElement):
    """Class representing a storytelling element"""
    narrative: str
    emotional_tone: str
    target_audience: str
    content_type: ContentType = ContentType.STORY

@dataclass
class BrandGuide(BrandElement):
    """Class representing brand guidelines"""
    logo_url: str
    color_palette: Dict[str, str]
    typography: Dict[str, str]
    voice_tone: str
    content_type: ContentType = ContentType.BRAND_GUIDE

class DigitalExperiencePlatform:
    """Main platform class for managing branding and storytelling elements"""
    
    def __init__(self):
        self.content_registry: Dict[str, BrandElement] = {}
    
    def add_content(self, content: BrandElement) -> bool:
        """Add content to the platform"""
        try:
            if content.id in self.content_registry:
                raise ValueError(f"Content with ID {content.id} already exists")
            self.content_registry[content.id] = content
            logger.info(f"Added content: {content.name} ({content.id})")
            return True
        except Exception as e:
            logger.error(f"Error adding content: {str(e)}")
            return False
    
    def get_content(self, content_id: str) -> Optional[BrandElement]:
        """Retrieve content by ID"""
        try:
            return self.content_registry.get(content_id)
        except Exception as e:
            logger.error(f"Error retrieving content: {str(e)}")
            return None
    
    def get_content_by_type(self, content_type: ContentType) -> List[BrandElement]:
        """Get all content of a specific type"""
        try:
            return [content for content in self.content_registry.values() 
                   if content.content_type == content_type]
        except Exception as e:
            logger.error(f"Error filtering content: {str(e)}")
            return []
    
    def export_content(self, file_path: str) -> bool:
        """Export all content to JSON file"""
        try:
            content_list = [asdict(content) for content in self.content_registry.values()]
            with open(file_path, 'w') as f:
                json.dump(content_list, f, indent=2)
            logger.info(f"Exported content to {file_path}")
            return True
        except Exception as e:
            logger.error(f"Error exporting content: {str(e)}")
            return False
    
    def import_content(self, file_path: str) -> bool:
        """Import content from JSON file"""
        try:
            with open(file_path, 'r') as f:
                content_data = json.load(f)
            
            for item in content_data:
                content_type = ContentType(item['content_type'])
                if content_type == ContentType.STORY:
                    content = StoryElement(**item)
                elif content_type == ContentType.BRAND_GUIDE:
                    content = BrandGuide(**item)
                else:
                    continue
                self.add_content(content)
            
            logger.info(f"Imported content from {file_path}")
            return True
        except Exception as e:
            logger.error(f"Error importing content: {str(e)}")
            return False

# Example usage
if __name__ == "__main__":
    platform = DigitalExperiencePlatform()
    
    # Create brand elements
    brand_guide = BrandGuide(
        id="bg1",
        name="Primary Brand Guide",
        description="Main brand guidelines for our company",
        tags=["primary", "official"],
        logo_url="https://example.com/logo.png",
        color_palette={"primary": "#FF5733", "secondary": "#33FF57"},
        typography={"heading": "Roboto Bold", "body": "Roboto Regular"},
        voice_tone="Friendly and professional"
    )
    
    story = StoryElement(
        id="story1",
        name="Our Origin Story",
        description="How our company came to be",
        tags=["history", "founders"],
        narrative="Once upon a time...",
        emotional_tone="Inspirational",
        target_audience="Customers"
    )
    
    # Add to platform
    platform.add_content(brand_guide)
    platform.add_content(story)
    
    # Export to file
    platform.export_content("brand_content.json")
```
