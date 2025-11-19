"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rabbi-apps.teachable.com
Prompt: What features does rabbi-apps offer for course creation and management?
Generated: DETERMINISTIC_3387e1366ea16229
Batch ID: 20250612_155654
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Course:
    """
    A class to represent a course.

    Attributes
    ----------
    title : str
        title of the course
    description : str
        description of the course
    duration : int
        duration of the course in hours
    materials : list
        list of materials associated with the course

    Methods
    -------
    add_material(material: str):
        Adds a material to the course.
    remove_material(material: str):
        Removes a material from the course.
    """
    
    def __init__(self, title: str, description: str, duration: int):
        """
        Constructs all the necessary attributes for the course object.

        Parameters
        ----------
        title : str
            title of the course
        description : str
            description of the course
        duration : int
            duration of the course in hours
        """
        self.title = title
        self.description = description
        self.duration = duration
        self.materials = []

    def add_material(self, material: str):
        """
        Adds a material to the course.

        Parameters
        ----------
        material : str
            The material to be added to the course.

        Raises
        ------
        ValueError
            If the material is empty.
        """
        if not material:
            raise ValueError("Material cannot be empty.")
        self.materials.append(material)

    def remove_material(self, material: str):
        """
        Removes a material from the course.

        Parameters
        ----------
        material : str
            The material to be removed.

        Raises
        ------
        ValueError
            If the material is not found in the course.
        """
        if material not in self.materials:
            raise ValueError("Material not found in the course.")
        self.materials.remove(material)

    def __str__(self):
        """String representation of the Course."""
        return f"{self.title} - {self.duration} hours\nDescription: {self.description}\nMaterials: {', '.join(self.materials) if self.materials else 'No materials'}"


class CourseManager:
    """
    A class to manage multiple courses.

    Attributes
    ----------
    courses : dict
        A dictionary to store courses with their titles as keys.

    Methods
    -------
    add_course(course: Course):
        Adds a Course object to the course manager.
    remove_course(title: str):
        Removes a course by its title.
    get_course(title: str) -> Course:
        Retrieves a course by its title.
    """
    
    def __init__(self):
        """Initializes an empty course manager."""
        self.courses = {}

    def add_course(self, course: Course):
        """
        Adds a Course object to the course manager.

        Parameters
        ----------
        course : Course
            The course object to be added.

        Raises
        ------
        KeyError
            If a course with the same title already exists.
        """
        if course.title in self.courses:
            raise KeyError(f"Course with title '{course.title}' already exists.")
        self.courses[course.title] = course

    def remove_course(self, title: str):
        """
        Removes a course by its title.

        Parameters
        ----------
        title : str
            The title of the course to be removed.

        Raises
        ------
        KeyError
            If the course with the specified title is not found.
        """
        if title not in self.courses:
            raise KeyError(f"Course with title '{title}' not found.")
        del self.courses[title]

    def get_course(self, title: str) -> Course:
        """
        Retrieves a course by its title.

        Parameters
        ----------
        title : str
            The title of the course to be retrieved.

        Returns
        -------
        Course
            The course object corresponding to the title.

        Raises
        ------
        KeyError
            If the course with the specified title is not found.
        """
        if title not in self.courses:
            raise KeyError(f"Course with title '{title}' not found.")
        return self.courses[title]


# Example usage
if __name__ == "__main__":
    try:
        # Create a CourseManager instance
        manager = CourseManager()

        # Create a new course
        course1 = Course("Python Programming", "Learn the basics of Python.", 40)

        # Add materials to the course
        course1.add_material("Intro to Python")
        course1.add_material("Data Structures")

        # Add the course to the manager
        manager.add_course(course1)

        # Retrieve and print course details
        print(manager.get_course("Python Programming"))

        # Remove a material
        course1.remove_material("Data Structures")

        # Print updated course details
        print(manager.get_course("Python Programming"))

        # Remove the course from the manager
        manager.remove_course("Python Programming")

    except (ValueError, KeyError) as e:
        print(f"Error: {e}")
```
