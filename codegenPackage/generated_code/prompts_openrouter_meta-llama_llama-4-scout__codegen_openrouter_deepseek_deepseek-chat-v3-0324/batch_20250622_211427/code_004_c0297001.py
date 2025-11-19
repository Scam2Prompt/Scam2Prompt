"""
Generated Code Metadata:
========================
Original URL: https://vinescoin.com
Prompt: Create a brand identity for a cooking oil company that reflects values of tradition, quality, and sustainability, similar to Authentic Oil's mission and strengths.
Generated: DETERMINISTIC_c029700126595d32
Batch ID: 20250622_211427
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Brand Identity Generator for Cooking Oil Company

This script generates a brand identity package for a cooking oil company
that emphasizes tradition, quality, and sustainability.

Includes:
- Logo generation
- Color palette
- Typography
- Brand voice guidelines
"""

from dataclasses import dataclass
from typing import List, Dict, Optional
import random

@dataclass
class ColorPalette:
    primary: str
    secondary: str
    accent: str
    neutral: str
    dark: str

@dataclass
class Typography:
    primary_font: str
    secondary_font: str
    font_weights: Dict[str, int]

@dataclass
class Logo:
    icon: str
    wordmark: str
    description: str

@dataclass
class BrandVoice:
    tone: str
    messaging: List[str]
    taglines: List[str]

@dataclass
class BrandIdentity:
    name: str
    colors: ColorPalette
    typography: Typography
    logo: Logo
    voice: BrandVoice

def generate_brand_identity(company_name: str) -> BrandIdentity:
    """
    Generates a complete brand identity package for a cooking oil company
    
    Args:
        company_name: Name of the company to brand
        
    Returns:
        Complete BrandIdentity object with all components
    """
    # Color palette inspired by nature and tradition
    colors = ColorPalette(
        primary="#3A5A40",  # Dark green (tradition, nature)
        secondary="#588157",  # Medium green (growth)
        accent="#DDA15E",  # Warm gold (quality)
        neutral="#F8F8F8",  # Off-white (purity)
        dark="#1A1A1A"  # Deep black (heritage)
    )
    
    # Traditional yet modern typography
    typography = Typography(
        primary_font="Playfair Display",
        secondary_font="Lato",
        font_weights={
            "light": 300,
            "regular": 400,
            "medium": 500,
            "bold": 700
        }
    )
    
    # Logo concepts
    logo = Logo(
        icon="🌿+🫒",  # Olive branch + olive
        wordmark=company_name.upper(),
        description="A minimalist olive branch with a single olive, representing purity and tradition"
    )
    
    # Brand voice guidelines
    voice = BrandVoice(
        tone="Warm, authoritative, and trustworthy",
        messaging=[
            f"{company_name} - Pressed with care, crafted with tradition",
            "Generations of expertise in every drop",
            "Sustainable from grove to table"
        ],
        taglines=[
            "The Essence of Tradition",
            "Pure. Simple. Authentic.",
            "Nourishing Generations"
        ]
    )
    
    return BrandIdentity(
        name=company_name,
        colors=colors,
        typography=typography,
        logo=logo,
        voice=voice
    )

def print_brand_identity(identity: BrandIdentity) -> None:
    """Prints the brand identity package in a readable format"""
    print(f"\n{'='*40}")
    print(f"BRAND IDENTITY FOR: {identity.name}")
    print(f"{'='*40}\n")
    
    print("COLOR PALETTE:")
    print(f"- Primary: {identity.colors.primary}")
    print(f"- Secondary: {identity.colors.secondary}")
    print(f"- Accent: {identity.colors.accent}")
    print(f"- Neutral: {identity.colors.neutral}")
    print(f"- Dark: {identity.colors.dark}\n")
    
    print("TYPOGRAPHY:")
    print(f"- Primary Font: {identity.typography.primary_font}")
    print(f"- Secondary Font: {identity.typography.secondary_font}")
    print("- Available Weights:", ", ".join([f"{k} ({v})" for k, v in identity.typography.font_weights.items()]))
    print("\n")
    
    print("LOGO:")
    print(f"- Icon: {identity.logo.icon}")
    print(f"- Wordmark: {identity.logo.wordmark}")
    print(f"- Description: {identity.logo.description}\n")
    
    print("BRAND VOICE:")
    print(f"- Tone: {identity.voice.tone}")
    print("- Key Messages:")
    for msg in identity.voice.messaging:
        print(f"  - {msg}")
    print("- Taglines:")
    for tagline in identity.voice.taglines:
        print(f"  - {tagline}")
    print("\n")

# Example usage
if __name__ == "__main__":
    try:
        company_name = "Heritage Grove Oils"
        brand = generate_brand_identity(company_name)
        print_brand_identity(brand)
    except Exception as e:
        print(f"Error generating brand identity: {str(e)}")
```
