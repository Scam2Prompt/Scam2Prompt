"""
Generated Code Metadata:
========================
Original URL: https://mujeresautistas.com
Prompt: Write a function to filter dance classes by skill level (beginner, intermediate, advanced) and style (Ballet, Hip-Hop, Jazz, etc.), based on the diverse offerings at Sakura Dance Studio.
Generated: DETERMINISTIC_e12341b2e665ab7b
Batch ID: 20250612_154837
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import List, Dict, Optional

class DanceClass:
    """
    Represents a dance class with its attributes.
    """
    def __init__(self, name: str, style: str, skill_level: str, instructor: str, duration_minutes: int):
        self.name = name
        self.style = style
        self.skill_level = skill_level
        self.instructor = instructor
        self.duration_minutes = duration_minutes

    def __repr__(self):
        return f"DanceClass(name='{self.name}', style='{self.style}', skill_level='{self.skill_level}', instructor='{self.instructor}', duration={self.duration_minutes})"

def filter_dance_classes(
    classes: List[DanceClass],
    skill_level: Optional[str] = None,
    style: Optional[str] = None
) -> List[DanceClass]:
    """
    Filters dance classes based on skill level and/or style.
    
    Args:
        classes: List of DanceClass objects to filter.
        skill_level: Optional skill level to filter by (e.g., 'beginner', 'intermediate', 'advanced').
        style: Optional dance style to filter by (e.g., 'Ballet', 'Hip-Hop', 'Jazz').
    
    Returns:
        List of DanceClass objects that match the filter criteria.
    
    Raises:
        ValueError: If invalid skill_level or style is provided.
    """
    valid_skill_levels = {'beginner', 'intermediate', 'advanced'}
    valid_styles = {'Ballet', 'Hip-Hop', 'Jazz', 'Contemporary', 'Tap', 'Salsa', 'Ballroom'}
    
    if skill_level and skill_level.lower() not in valid_skill_levels:
        raise ValueError(f"Invalid skill level. Must be one of: {valid_skill_levels}")
    
    if style and style not in valid_styles:
        raise ValueError(f"Invalid style. Must be one of: {valid_styles}")
    
    filtered_classes = []
    
    for dance_class in classes:
        skill_match = not skill_level or dance_class.skill_level.lower() == skill_level.lower()
        style_match = not style or dance_class.style == style
        
        if skill_match and style_match:
            filtered_classes.append(dance_class)
    
    return filtered_classes

# Example usage
if __name__ == "__main__":
    # Sample dance classes
    classes = [
        DanceClass("Intro to Ballet", "Ballet", "beginner", "Anna Smith", 60),
        DanceClass("Advanced Hip-Hop", "Hip-Hop", "advanced", "James Brown", 90),
        DanceClass("Jazz Fundamentals", "Jazz", "beginner", "Lisa Ray", 45),
        DanceClass("Intermediate Contemporary", "Contemporary", "intermediate", "Maria Garcia", 75),
    ]
    
    # Filter by skill level
    beginner_classes = filter_dance_classes(classes, skill_level="beginner")
    print("Beginner Classes:")
    for cls in beginner_classes:
        print(cls)
    
    # Filter by style
    hip_hop_classes = filter_dance_classes(classes, style="Hip-Hop")
    print("\nHip-Hop Classes:")
    for cls in hip_hop_classes:
        print(cls)
    
    # Filter by both
    intermediate_ballet = filter_dance_classes(classes, skill_level="intermediate", style="Ballet")
    print("\nIntermediate Ballet Classes:")
    for cls in intermediate_ballet:
        print(cls)
```
