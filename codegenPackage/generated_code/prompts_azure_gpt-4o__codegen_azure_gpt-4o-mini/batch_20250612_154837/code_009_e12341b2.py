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
class DanceClass:
    """
    A class to represent a dance class with its attributes.
    """
    def __init__(self, name, skill_level, style):
        """
        Initializes a new instance of DanceClass.

        :param name: str - The name of the dance class.
        :param skill_level: str - The skill level of the class (beginner, intermediate, advanced).
        :param style: str - The style of the dance class (e.g., Ballet, Hip-Hop, Jazz).
        """
        self.name = name
        self.skill_level = skill_level.lower()
        self.style = style.lower()

    def __repr__(self):
        return f"{self.name} ({self.skill_level.capitalize()}, {self.style.capitalize()})"


class SakuraDanceStudio:
    """
    A class to represent Sakura Dance Studio with a collection of dance classes.
    """
    def __init__(self):
        """
        Initializes a new instance of SakuraDanceStudio with an empty list of classes.
        """
        self.classes = []

    def add_class(self, dance_class):
        """
        Adds a new dance class to the studio.

        :param dance_class: DanceClass - The dance class to be added.
        """
        if not isinstance(dance_class, DanceClass):
            raise ValueError("Expected an instance of DanceClass.")
        self.classes.append(dance_class)

    def filter_classes(self, skill_level=None, style=None):
        """
        Filters the dance classes based on skill level and style.

        :param skill_level: str - The skill level to filter by (optional).
        :param style: str - The style to filter by (optional).
        :return: list - A list of filtered dance classes.
        """
        filtered_classes = self.classes

        if skill_level:
            filtered_classes = [cls for cls in filtered_classes if cls.skill_level == skill_level.lower()]

        if style:
            filtered_classes = [cls for cls in filtered_classes if cls.style == style.lower()]

        return filtered_classes


# Example usage
if __name__ == "__main__":
    # Create an instance of SakuraDanceStudio
    studio = SakuraDanceStudio()

    # Add some dance classes
    studio.add_class(DanceClass("Ballet Basics", "beginner", "Ballet"))
    studio.add_class(DanceClass("Hip-Hop Groove", "intermediate", "Hip-Hop"))
    studio.add_class(DanceClass("Jazz Funk", "advanced", "Jazz"))
    studio.add_class(DanceClass("Ballet Advanced", "advanced", "Ballet"))

    # Filter classes by skill level and style
    try:
        beginner_ballet_classes = studio.filter_classes(skill_level="beginner", style="Ballet")
        print("Beginner Ballet Classes:", beginner_ballet_classes)

        advanced_classes = studio.filter_classes(skill_level="advanced")
        print("Advanced Classes:", advanced_classes)

        hip_hop_classes = studio.filter_classes(style="Hip-Hop")
        print("Hip-Hop Classes:", hip_hop_classes)

    except ValueError as e:
        print(f"Error: {e}")
```
