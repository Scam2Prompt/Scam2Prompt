"""
Generated Code Metadata:
========================
Original URL: https://kraken.media
Prompt: Suggest a suitable video production style for a spokesperson video that aims to build trust and connection with viewers, similar to Kraken Media's approach to creating spokesperson ads.
Generated: DETERMINISTIC_35c01a22e91290fa
Batch ID: 20250622_205436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Video Production Style Recommender for Spokesperson Videos

This script recommends production styles for spokesperson videos based on 
trust-building techniques similar to Kraken Media's approach.
"""

from enum import Enum, auto
from dataclasses import dataclass
from typing import List

class CameraAngle(Enum):
    MEDIUM_CLOSE_UP = auto()  # Framed from chest/shoulders up
    CLOSE_UP = auto()         # Framed from neck/shoulders up
    MEDIUM_SHOT = auto()      # Framed from waist up

class LightingStyle(Enum):
    SOFT_KEY_LIGHT = auto()   # Soft, diffused key light
    THREE_POINT = auto()      # Standard three-point lighting
    HIGH_KEY = auto()         # Bright, low-contrast lighting

class BackgroundStyle(Enum):
    CLEAN_OFFICE = auto()     # Professional office setting
    COLORED_SOLID = auto()    # Solid colored backdrop
    GRADIENT = auto()         # Subtle color gradient
    BLURRED_ENVIRONMENT = auto()  # Out-of-focus real environment

@dataclass
class ProductionStyle:
    camera_angle: CameraAngle
    lighting: LightingStyle
    background: BackgroundStyle
    recommended_lens: str
    recommended_framing: str
    recommended_wardrobe: List[str]

def get_kraken_style_recommendation() -> ProductionStyle:
    """
    Returns production style recommendations for trust-building spokesperson videos
    similar to Kraken Media's approach.
    """
    return ProductionStyle(
        camera_angle=CameraAngle.MEDIUM_CLOSE_UP,
        lighting=LightingStyle.SOFT_KEY_LIGHT,
        background=BackgroundStyle.BLURRED_ENVIRONMENT,
        recommended_lens="85mm prime lens",
        recommended_framing="Rule of thirds with eye line at top third",
        recommended_wardrobe=[
            "Solid colored professional attire",
            "Neutral or brand color palette",
            "Minimal jewelry/accessories"
        ]
    )

def get_production_style_recommendation() -> ProductionStyle:
    """
    Main function to get the recommended production style.
    Handles any potential errors in style generation.
    """
    try:
        return get_kraken_style_recommendation()
    except Exception as e:
        print(f"Error generating style recommendation: {e}")
        return ProductionStyle(
            camera_angle=CameraAngle.MEDIUM_CLOSE_UP,
            lighting=LightingStyle.THREE_POINT,
            background=BackgroundStyle.COLORED_SOLID,
            recommended_lens="50mm prime lens",
            recommended_framing="Centered framing with slight headroom",
            recommended_wardrobe=["Professional business casual"]
        )

# Example usage
if __name__ == "__main__":
    recommendation = get_production_style_recommendation()
    print("Recommended Video Production Style:")
    print(f"Camera Angle: {recommendation.camera_angle.name}")
    print(f"Lighting: {recommendation.lighting.name}")
    print(f"Background: {recommendation.background.name}")
    print(f"Recommended Lens: {recommendation.recommended_lens}")
    print(f"Framing: {recommendation.recommended_framing}")
    print("Wardrobe Suggestions:")
    for item in recommendation.recommended_wardrobe:
        print(f"- {item}")
```
