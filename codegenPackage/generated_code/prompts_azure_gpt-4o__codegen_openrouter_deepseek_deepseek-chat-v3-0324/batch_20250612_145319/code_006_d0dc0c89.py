"""
Generated Code Metadata:
========================
Original URL: https://zirciulit.com
Prompt: Write a script to generate personalized interior design recommendations for clients, incorporating Zirciulit Design Firm's concept of converting houses into ideal settings.
Generated: DETERMINISTIC_d0dc0c89e6f16e86
Batch ID: 20250612_145319
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional
from dataclasses import dataclass, asdict
import random

# Constants for design styles and elements
DESIGN_STYLES = [
    "Modern",
    "Minimalist",
    "Industrial",
    "Scandinavian",
    "Traditional",
    "Bohemian",
    "Rustic",
    "Coastal",
    "Mid-Century Modern",
    "Art Deco"
]

COLOR_PALETTES = {
    "Modern": ["Monochrome", "Neutral with bold accents", "Cool tones"],
    "Minimalist": ["White and beige", "Soft grays", "Black and white"],
    "Industrial": ["Concrete gray", "Metallic tones", "Dark neutrals"],
    "Scandinavian": ["White and wood tones", "Pastels", "Light neutrals"],
    "Traditional": ["Warm neutrals", "Deep reds and greens", "Gold accents"],
    "Bohemian": ["Earthy tones", "Jewel tones", "Mixed vibrant colors"],
    "Rustic": ["Browns and greens", "Earthy reds", "Natural wood tones"],
    "Coastal": ["Blues and whites", "Sandy beiges", "Seafoam greens"],
    "Mid-Century Modern": ["Warm neutrals with pops of color", "Teal and mustard", "Orange and brown"],
    "Art Deco": ["Black and gold", "Rich jewel tones", "High contrast"]
}

FURNITURE_STYLES = {
    "Modern": ["Sleek lines", "Low-profile", "Geometric shapes"],
    "Minimalist": ["Functional", "Simple forms", "Space-saving"],
    "Industrial": ["Metal and wood combinations", "Reclaimed materials", "Utilitarian"],
    "Scandinavian": ["Light wood", "Clean lines", "Functional"],
    "Traditional": ["Ornate details", "Classic silhouettes", "Rich fabrics"],
    "Bohemian": ["Eclectic mix", "Vintage pieces", "Layered textures"],
    "Rustic": ["Reclaimed wood", "Handcrafted", "Natural materials"],
    "Coastal": ["Light and airy", "Wicker and rattan", "Nautical elements"],
    "Mid-Century Modern": ["Tapered legs", "Organic curves", "Bold colors"],
    "Art Deco": ["Geometric patterns", "Luxury materials", "Bold shapes"]
}

LIGHTING_OPTIONS = [
    "Pendant lights",
    "Floor lamps",
    "Recessed lighting",
    "Track lighting",
    "Chandeliers",
    "Wall sconces",
    "Table lamps",
    "Natural light maximization"
]

TEXTURE_OPTIONS = [
    "Smooth and glossy",
    "Rough and natural",
    "Soft and plush",
    "Mixed textures",
    "Layered fabrics",
    "Metallic accents"
]

@dataclass
class ClientProfile:
    name: str
    age: int
    favorite_colors: List[str]
    preferred_style: str
    rooms_to_design: List[str]
    budget: str  # low, medium, high
    special_requirements: Optional[str] = None

@dataclass
class RoomDesign:
    room_name: str
    recommended_style: str
    color_palette: List[str]
    furniture_recommendations: List[str]
    lighting_recommendations: List[str]
    texture_recommendations: List[str]
    special_notes: Optional[str] = None

@dataclass
class DesignRecommendation:
    client: ClientProfile
    overall_style: str
    room_designs: List[RoomDesign]
    additional_recommendations: Optional[List[str]] = None

def validate_client_profile(profile: Dict) -> bool:
    """Validate the client profile data"""
    required_fields = ["name", "age", "favorite_colors", "preferred_style", "rooms_to_design", "budget"]
    for field in required_fields:
        if field not in profile:
            return False
    
    if not isinstance(profile["name"], str) or not profile["name"].strip():
        return False
    
    if not isinstance(profile["age"], int) or profile["age"] < 1:
        return False
    
    if not isinstance(profile["favorite_colors"], list) or not all(isinstance(c, str) for c in profile["favorite_colors"]):
        return False
    
    if profile["preferred_style"] not in DESIGN_STYLES:
        return False
    
    if not isinstance(profile["rooms_to_design"], list) or not all(isinstance(r, str) for r in profile["rooms_to_design"]):
        return False
    
    if profile["budget"] not in ["low", "medium", "high"]:
        return False
    
    return True

def generate_room_design(room_name: str, style: str, client: ClientProfile) -> RoomDesign:
    """Generate design recommendations for a specific room"""
    # Get base recommendations based on style
    color_palette = COLOR_PALETTES.get(style, ["Neutral tones"])
    furniture = FURNITURE_STYLES.get(style, ["Classic pieces"])
    
    # Customize based on client preferences
    if client.favorite_colors:
        color_palette = list(set(color_palette + client.favorite_colors))[:3]
    
    # Select lighting and textures
    lighting = random.sample(LIGHTING_OPTIONS, k=2)
    textures = random.sample(TEXTURE_OPTIONS, k=2)
    
    # Add special notes for budget considerations
    special_notes = None
    if client.budget == "low":
        special_notes = "Focus on affordable materials and multifunctional furniture"
    elif client.budget == "high":
        special_notes = "Consider high-end materials and custom pieces"
    
    return RoomDesign(
        room_name=room_name,
        recommended_style=style,
        color_palette=color_palette,
        furniture_recommendations=furniture,
        lighting_recommendations=lighting,
        texture_recommendations=textures,
        special_notes=special_notes
    )

def generate_design_recommendation(client_data: Dict) -> DesignRecommendation:
    """Generate personalized interior design recommendations"""
    if not validate_client_profile(client_data):
        raise ValueError("Invalid client profile data")
    
    client = ClientProfile(**client_data)
    
    # Determine overall style (might adjust based on client preferences)
    overall_style = client.preferred_style
    
    # Generate room designs
    room_designs = []
    for room in client.rooms_to_design:
        room_designs.append(generate_room_design(room, overall_style, client))
    
    # Additional recommendations
    additional_recommendations = []
    if client.special_requirements:
        additional_recommendations.append(f"Special consideration: {client.special_requirements}")
    
    if client.age > 60:
        additional_recommendations.append("Consider ergonomic furniture and good lighting for accessibility")
    
    return DesignRecommendation(
        client=client,
        overall_style=overall_style,
        room_designs=room_designs,
        additional_recommendations=additional_recommendations if additional_recommendations else None
    )

def save_recommendation_to_json(recommendation: DesignRecommendation, filename: str) -> None:
    """Save the design recommendation to a JSON file"""
    with open(filename, 'w') as f:
        json.dump(asdict(recommendation), f, indent=2)

def load_client_profile(filename: str) -> Dict:
    """Load client profile from JSON file"""
    with open(filename, 'r') as f:
        return json.load(f)

# Example usage
if __name__ == "__main__":
    try:
        # Example client profile (in production, this would come from a file or API)
        example_client = {
            "name": "John Doe",
            "age": 35,
            "favorite_colors": ["Blue", "Green"],
            "preferred_style": "Modern",
            "rooms_to_design": ["Living Room", "Bedroom", "Home Office"],
            "budget": "medium",
            "special_requirements": "Needs home office with good acoustics"
        }
        
        # Generate recommendations
        recommendation = generate_design_recommendation(example_client)
        
        # Save to file
        save_recommendation_to_json(recommendation, "john_doe_design_recommendation.json")
        print("Design recommendation generated successfully!")
        
    except Exception as e:
        print(f"Error generating design recommendation: {e}")
```
