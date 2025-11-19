"""
Generated Code Metadata:
========================
Original URL: https://nucleicinsights.com
Prompt: Suggest a set of colors and typography for a brand identity design project, inspired by Umama Shahid's design experience and skills.
Generated: DETERMINISTIC_3ad7c16834e4e350
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Brand Identity Color and Typography System
Inspired by Umama Shahid's design aesthetic
"""

from typing import Dict, List, Tuple
from dataclasses import dataclass

@dataclass
class ColorPalette:
    primary: str
    secondary: str
    accent: str
    neutral: str
    success: str
    warning: str
    error: str

@dataclass
class TypographySystem:
    font_family: str
    font_weights: Dict[str, int]
    font_sizes: Dict[str, str]
    line_heights: Dict[str, float]

def get_brand_identity() -> Tuple[ColorPalette, TypographySystem]:
    """
    Returns a cohesive brand identity system with colors and typography
    """
    colors = ColorPalette(
        primary="#3A86FF",  # Vibrant blue
        secondary="#8338EC",  # Royal purple
        accent="#FF006E",  # Energetic pink
        neutral="#1A1A2E",  # Dark navy
        success="#06D6A0",  # Mint green
        warning="#FFBE0B",  # Golden yellow
        error="#EF476F"   # Coral red
    )

    typography = TypographySystem(
        font_family="'Inter', sans-serif",
        font_weights={
            "light": 300,
            "regular": 400,
            "medium": 500,
            "bold": 700,
            "black": 900
        },
        font_sizes={
            "small": "0.875rem",  # 14px
            "base": "1rem",      # 16px
            "medium": "1.25rem",  # 20px
            "large": "1.5rem",    # 24px
            "xl": "2rem",        # 32px
            "xxl": "3rem"        # 48px
        },
        line_heights={
            "tight": 1.2,
            "normal": 1.5,
            "loose": 1.8
        }
    )

    return colors, typography

def validate_color_hex(color: str) -> bool:
    """Validates if a string is a valid hex color code"""
    if not color.startswith('#'):
        return False
    try:
        int(color[1:], 16)
        return len(color) == 7  # #RRGGBB format
    except ValueError:
        return False

def validate_font_weight(weight: int) -> bool:
    """Validates if font weight is within typical range"""
    return 100 <= weight <= 900 and weight % 100 == 0
```
