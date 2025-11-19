"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://anima.art.br
Prompt: Outline a project plan for a jewelry design application, referencing the design courses offered at Ânima.
Generated: DETERMINISTIC_defbbd9e1b8568db
Batch ID: 20250612_164021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# jewelry_design_app.py

"""
Jewelry Design Application

This application serves as a project plan outline for a jewelry design application. 
It leverages design courses offered at Ânima to enhance user learning and skill development 
in jewelry design.
"""

from typing import List, Dict, Optional

class Course:
    """Class representing a design course offered at Ânima."""

    def __init__(self, title: str, description: str, duration: str):
        self.title = title
        self.description = description
        self.duration = duration

    def __repr__(self):
        return f"{self.title} ({self.duration}) - {self.description}"


class JewelryDesignApp:
    """Main application class for managing jewelry design projects and courses."""

    def __init__(self):
        self.courses: List[Course] = []
        self.project_plan: Dict[str, List[str]] = {}

    def add_course(self, course: Course) -> None:
        """Adds a new course to the application."""
        self.courses.append(course)

    def create_project_plan(self, project_name: str, course_titles: List[str]) -> None:
        """
        Creates a project plan for a specific jewelry design project.

        Args:
            project_name (str): Name of the jewelry design project.
            course_titles (List[str]): List of course titles to include in the project plan.

        Raises:
            ValueError: If a course title is not found in the available courses.
        """
        if project_name in self.project_plan:
            raise ValueError(f"Project plan for '{project_name}' already exists.")

        for title in course_titles:
            if title not in [course.title for course in self.courses]:
                raise ValueError(f"Course '{title}' not found.")

        self.project_plan[project_name] = course_titles

    def get_course_details(self) -> List[str]:
        """Returns a list of course details."""
        return [str(course) for course in self.courses]

    def get_project_plans(self) -> Dict[str, List[str]]:
        """Returns a dictionary of existing project plans."""
        return self.project_plan


# Example usage:
if __name__ == "__main__":
    app = JewelryDesignApp()
    
    # Adding courses offered at Ânima
    app.add_course(Course("Basic Jewelry Design", "Introduction to jewelry design basics.", "4 weeks"))
    app.add_course(Course("Advanced Gemology", "Study of gemstones and their properties.", "6 weeks"))
    app.add_course(Course("Metalworking Techniques", "Hands-on training in metalworking techniques.", "8 weeks"))

    # Print available courses
    print("Available Courses:")
    for course in app.get_course_details():
        print(course)

    # Creating a project plan
    try:
        app.create_project_plan("Artisan Jewelry", ["Basic Jewelry Design", "Metalworking Techniques"])
        print("Project Plans:")
        for project, courses in app.get_project_plans().items():
            print(f"{project}: {courses}")
    except ValueError as e:
        print(f"Error: {e}")
```
