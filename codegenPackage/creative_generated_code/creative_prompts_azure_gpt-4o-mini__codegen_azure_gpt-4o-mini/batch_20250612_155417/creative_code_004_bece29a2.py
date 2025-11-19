"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://45ybook.ueh.edu.vn
Prompt: Suggest a framework for developing a multi-disciplinary curriculum in higher education, using examples from the UEH special issue.
Generated: DETERMINISTIC_bece29a20d20485a
Batch ID: 20250612_155417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Curriculum development framework for multi-disciplinary programs in higher education

class Course:
    """
    A class to represent a course in the curriculum.
    
    Attributes:
        title (str): The title of the course.
        description (str): A brief description of the course content.
        credits (int): The number of credits the course offers.
    """
    
    def __init__(self, title: str, description: str, credits: int):
        if credits <= 0:
            raise ValueError("Credits must be a positive integer.")
        self.title = title
        self.description = description
        self.credits = credits


class Curriculum:
    """
    A class to represent a curriculum comprising multiple courses.
    
    Attributes:
        name (str): The name of the curriculum.
        courses (list): A list of Course objects included in the curriculum.
    """
    
    def __init__(self, name: str):
        self.name = name
        self.courses = []

    def add_course(self, course: Course):
        """
        Adds a course to the curriculum.
        
        Parameters:
            course (Course): A Course object to be added.
        """
        self.courses.append(course)

    def total_credits(self) -> int:
        """
        Calculates the total number of credits in the curriculum.
        
        Returns:
            int: Total credits of the courses in the curriculum.
        """
        return sum(course.credits for course in self.courses)

    def display_curriculum(self):
        """
        Displays the details of the curriculum including all courses and total credits.
        """
        print(f"Curriculum Name: {self.name}")
        print("Courses Offered:")
        for course in self.courses:
            print(f"- {course.title} ({course.credits} credits): {course.description}")
        print(f"Total Credits: {self.total_credits()}")


# Example Usage
if __name__ == "__main__":
    try:
        # Create a new curriculum
        curriculum = Curriculum("Interdisciplinary Studies Program")

        # Define some courses using examples inspired by the UEH special issue
        course1 = Course("Data Science Fundamentals", "Introduction to data science concepts and tools.", 3)
        course2 = Course("Digital Marketing Strategies", "Study of marketing techniques in the digital age.", 4)
        course3 = Course("Environmental Economics", "Analysis of economic aspects of environmental issues.", 3)
        
        # Add courses to the curriculum
        curriculum.add_course(course1)
        curriculum.add_course(course2)
        curriculum.add_course(course3)

        # Display the entire curriculum
        curriculum.display_curriculum()

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
