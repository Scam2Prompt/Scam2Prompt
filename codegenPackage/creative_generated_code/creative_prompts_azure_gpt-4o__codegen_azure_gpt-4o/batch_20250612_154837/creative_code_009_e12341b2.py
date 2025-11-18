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
# Python Code to Filter Dance Classes by Skill Level and Style at Sakura Dance Studio

def filter_dance_classes(classes, skill_level=None, style=None):
    """
    Filters dance classes by skill level and style.

    Args:
        classes (list of dict): List of dance classes where each class is represented as a dictionary 
                                with keys 'name', 'skill_level', and 'style'.
        skill_level (str, optional): The skill level to filter by ('beginner', 'intermediate', 'advanced').
                                     If None, skill level is not used as a filter.
        style (str, optional): The dance style to filter by (e.g., 'Ballet', 'Hip-Hop', 'Jazz').
                               If None, style is not used as a filter.

    Returns:
        list of dict: A filtered list of dance classes matching the criteria.
    """
    # Input validation
    if not isinstance(classes, list):
        raise ValueError("Expected 'classes' to be a list of dictionaries.")
    if skill_level and skill_level.lower() not in ['beginner', 'intermediate', 'advanced']:
        raise ValueError("Invalid skill level. Accepted values are 'beginner', 'intermediate', 'advanced'.")
    if style and not isinstance(style, str):
        raise ValueError("Style must be a string.")

    # Filter the classes
    filtered_classes = [
        dance_class for dance_class in classes
        if (skill_level is None or dance_class.get('skill_level', '').lower() == skill_level.lower())
        and (style is None or dance_class.get('style', '').lower() == style.lower())
    ]
    
    return filtered_classes


# Example usage:
if __name__ == "__main__":
    # Sample data for Sakura Dance Studio classes
    dance_classes = [
        {'name': 'Ballet for Beginners', 'skill_level': 'Beginner', 'style': 'Ballet'},
        {'name': 'Intermediate Hip-Hop', 'skill_level': 'Intermediate', 'style': 'Hip-Hop'},
        {'name': 'Jazz Masterclass', 'skill_level': 'Advanced', 'style': 'Jazz'},
        {'name': 'Advanced Ballet', 'skill_level': 'Advanced', 'style': 'Ballet'},
        {'name': 'Beginner Tap Dance', 'skill_level': 'Beginner', 'style': 'Tap Dance'}
    ]

    # Filters
    print(filter_dance_classes(dance_classes, skill_level="Beginner", style="Ballet"))  # Filters for beginner ballet classes
    print(filter_dance_classes(dance_classes, skill_level="Advanced"))  # Filters for advanced-level classes
    print(filter_dance_classes(dance_classes))  # Returns all classes without filters
```
