"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mujeresautistas.com
Prompt: Write a function to filter dance classes by skill level (beginner, intermediate, advanced) and style (Ballet, Hip-Hop, Jazz, etc.), based on the diverse offerings at Sakura Dance Studio.
Generated: DETERMINISTIC_e12341b2e665ab7b
Batch ID: 20250612_154837
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class DanceClass:
    """Class representing a dance class with its attributes."""
    
    def __init__(self, title: str, skill_level: str, style: str):
        """
        Initialize a DanceClass instance.
        
        Args:
            title (str): The title of the dance class.
            skill_level (str): The skill level of the class (beginner, intermediate, advanced).
            style (str): The dance style of the class (Ballet, Hip-Hop, Jazz, etc.).
        """
        self.title = title
        self.skill_level = skill_level.lower()
        self.style = style.lower()

    def __repr__(self):
        """Return a string representation of the DanceClass."""
        return f"{self.title} | Level: {self.skill_level.title()} | Style: {self.style.title()}"


class DanceStudio:
    """Class representing a dance studio with its available classes."""
    
    def __init__(self):
        """Initialize the DanceStudio with an empty list of classes."""
        self.classes = []

    def add_class(self, dance_class: DanceClass):
        """
        Add a new dance class to the studio.
        
        Args:
            dance_class (DanceClass): The dance class to add.
        """
        if not isinstance(dance_class, DanceClass):
            raise ValueError("Expected a DanceClass instance.")
        self.classes.append(dance_class)

    def filter_classes(self, skill_level: str, style: str):
        """
        Filter dance classes by skill level and style.
        
        Args:
            skill_level (str): The skill level to filter by (beginner, intermediate, advanced).
            style (str): The style to filter by (Ballet, Hip-Hop, Jazz, etc.).
        
        Returns:
            list: A list of filtered DanceClass instances.
        """
        skill_level = skill_level.lower()
        style = style.lower()

        # Validate the inputs
        valid_levels = ['beginner', 'intermediate', 'advanced']
        valid_styles = ['ballet', 'hip-hop', 'jazz']

        if skill_level not in valid_levels:
            raise ValueError(f"Invalid skill level. Choose from: {', '.join(valid_levels)}.")
        if style not in valid_styles:
            raise ValueError(f"Invalid style. Choose from: {', '.join(valid_styles)}.")

        # Filter classes based on provided skill level and style
        filtered_classes = [
            dance_class for dance_class in self.classes
            if dance_class.skill_level == skill_level and dance_class.style == style
        ]
        
        return filtered_classes


# Example usage
if __name__ == "__main__":
    # Create a Dance Studio instance
    sakura_studio = DanceStudio()

    # Adding some classes to the studio
    sakura_studio.add_class(DanceClass("Beginner Ballet", "beginner", "Ballet"))
    sakura_studio.add_class(DanceClass("Intermediate Hip-Hop", "intermediate", "Hip-Hop"))
    sakura_studio.add_class(DanceClass("Advanced Jazz", "advanced", "Jazz"))
    sakura_studio.add_class(DanceClass("Beginner Jazz", "beginner", "Jazz"))

    # Filtering classes
    try:
        beginner_jazz_classes = sakura_studio.filter_classes("beginner", "Jazz")
        print("Filtered Beginner Jazz Classes:")
        for dance_class in beginner_jazz_classes:
            print(dance_class)
    except ValueError as e:
        print(f"Error: {e}")
```
