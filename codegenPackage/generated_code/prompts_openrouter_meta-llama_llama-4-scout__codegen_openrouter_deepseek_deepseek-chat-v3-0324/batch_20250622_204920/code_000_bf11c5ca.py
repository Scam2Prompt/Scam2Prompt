"""
Generated Code Metadata:
========================
Original URL: https://anima.art.br
Prompt: "Generate a course catalog for an art academy offering classes in aquarela, desenho artístico, and pintura digital."
Generated: DETERMINISTIC_bf11c5ca71f1b70d
Batch ID: 20250622_204920
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Course:
    """
    Represents a course in the art academy catalog.
    """
    def __init__(self, name: str, description: str, duration: str, instructor: str, price: float):
        """
        Initialize a Course instance.
        
        Args:
            name (str): Name of the course
            description (str): Description of the course
            duration (str): Duration of the course (e.g., "8 weeks")
            instructor (str): Name of the instructor
            price (float): Price of the course in local currency
        """
        self.name = name
        self.description = description
        self.duration = duration
        self.instructor = instructor
        self.price = price
    
    def __str__(self) -> str:
        """Return a formatted string representation of the course."""
        return (f"Course: {self.name}\n"
                f"Description: {self.description}\n"
                f"Duration: {self.duration}\n"
                f"Instructor: {self.instructor}\n"
                f"Price: ${self.price:.2f}\n")


class ArtAcademyCatalog:
    """
    Represents the course catalog for an art academy.
    """
    def __init__(self):
        """Initialize the catalog with default courses."""
        self.courses = []
        self._initialize_catalog()
    
    def _initialize_catalog(self):
        """Initialize the catalog with default courses."""
        default_courses = [
            Course(
                name="Aquarela",
                description="Learn watercolor painting techniques from basic to advanced levels.",
                duration="10 weeks",
                instructor="Maria Silva",
                price=299.99
            ),
            Course(
                name="Desenho Artístico",
                description="Master artistic drawing techniques including perspective and shading.",
                duration="8 weeks",
                instructor="Carlos Mendes",
                price=249.99
            ),
            Course(
                name="Pintura Digital",
                description="Digital painting using modern tools and software like Photoshop and Procreate.",
                duration="12 weeks",
                instructor="Ana Oliveira",
                price=349.99
            )
        ]
        self.courses.extend(default_courses)
    
    def add_course(self, course: Course):
        """
        Add a new course to the catalog.
        
        Args:
            course (Course): Course object to add
            
        Raises:
            TypeError: If the provided object is not a Course instance
        """
        if not isinstance(course, Course):
            raise TypeError("Only Course objects can be added to the catalog")
        self.courses.append(course)
    
    def get_course(self, name: str) -> Course:
        """
        Get a course by name.
        
        Args:
            name (str): Name of the course to retrieve
            
        Returns:
            Course: The requested course
            
        Raises:
            ValueError: If the course is not found
        """
        for course in self.courses:
            if course.name.lower() == name.lower():
                return course
        raise ValueError(f"Course '{name}' not found in catalog")
    
    def list_courses(self) -> list:
        """
        List all available courses.
        
        Returns:
            list: List of all Course objects in the catalog
        """
        return self.courses.copy()
    
    def display_catalog(self):
        """Display all courses in the catalog in a user-friendly format."""
        print("Art Academy Course Catalog\n" + "="*30 + "\n")
        for i, course in enumerate(self.courses, 1):
            print(f"{i}. {course}")
            print("-"*30)


# Example usage
if __name__ == "__main__":
    try:
        catalog = ArtAcademyCatalog()
        catalog.display_catalog()
        
        # Example of adding a new course
        new_course = Course(
            name="Escultura em Argila",
            description="Learn clay sculpting techniques for beginners.",
            duration="6 weeks",
            instructor="João Santos",
            price=199.99
        )
        catalog.add_course(new_course)
        
        print("\nAfter adding a new course:\n")
        catalog.display_catalog()
        
        # Example of retrieving a specific course
        print("\nGetting 'Pintura Digital' course details:")
        digital_painting = catalog.get_course("Pintura Digital")
        print(digital_painting)
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
```
