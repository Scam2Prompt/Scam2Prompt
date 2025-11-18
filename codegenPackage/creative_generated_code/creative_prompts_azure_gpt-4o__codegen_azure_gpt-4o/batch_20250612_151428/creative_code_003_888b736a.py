"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://anima.art.br
Prompt: Create a Python function that organizes art courses into categories like "painting," "drawing," and "digital design," based on Ânima's course offerings.
Generated: DETERMINISTIC_888b736a8845bd47
Batch ID: 20250612_151428
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Importing necessary modules
from collections import defaultdict
from typing import List, Dict

def organize_art_courses(courses: List[str]) -> Dict[str, List[str]]:
    """
    Organizes art courses into predefined categories based on course names.

    Parameters:
        courses (List[str]): A list of course names to be categorized.
    
    Returns:
        Dict[str, List[str]]: A dictionary containing courses categorized into 
                              "painting," "drawing," and "digital design."
    """
    # Predefined categories and their associated keywords
    categories = {
        "painting": ["painting", "watercolor", "acrylic", "oil"],
        "drawing": ["drawing", "sketch", "charcoal", "pencil"],
        "digital design": ["digital", "graphic", "design", "photoshop", "illustrator"]
    }

    # Default dictionary to hold categorized courses
    categorized_courses = defaultdict(list)

    # Categorize each course based on keywords
    for course in courses:
        # Track if the course has been categorized
        categorized = False
        
        # Check each category and associated keywords
        for category, keywords in categories.items():
            for keyword in keywords:
                if keyword.lower() in course.lower():
                    categorized_courses[category].append(course)
                    categorized = True
                    break
            if categorized:
                break
        
        # If the course doesn't match any category, assign it to "uncategorized"
        if not categorized:
            categorized_courses["uncategorized"].append(course)

    return dict(categorized_courses)


# Example usage
if __name__ == "__main__":
    # Sample list of courses
    anima_courses = [
        "Introduction to Oil Painting",
        "Charcoal Drawing Basics",
        "Graphic Design with Photoshop",
        "Advanced Watercolor Techniques",
        "Pencil Sketching Mastery",
        "Digital Illustration Fundamentals",
        "Exploring Acrylic Styles",
        "Experimental Art Techniques"
    ]

    # Organizing courses into categories
    categorized = organize_art_courses(anima_courses)

    # Displaying organized courses
    for category, courses in categorized.items():
        print(f"{category.capitalize()}:")
        for course in courses:
            print(f"  - {course}")
```
