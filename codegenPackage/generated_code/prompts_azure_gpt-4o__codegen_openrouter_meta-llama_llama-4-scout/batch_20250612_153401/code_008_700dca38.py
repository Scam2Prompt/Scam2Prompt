"""
Generated Code Metadata:
========================
Original URL: https://educarcomitan.mx
Prompt: Generate code to create a course recommendation system for students based on their admission exam level (secondary, high school, or university), as described on Educar Comitán's webpage.
Generated: DETERMINISTIC_700dca3851708f12
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# course_recommendation_system.py

class Course:
    """Represents a course with its name and required admission level."""

    def __init__(self, name, required_level):
        """
        Initializes a Course object.

        Args:
            name (str): The name of the course.
            required_level (str): The required admission level for the course.
        """
        self.name = name
        self.required_level = required_level

class Student:
    """Represents a student with their admission exam level."""

    def __init__(self, admission_level):
        """
        Initializes a Student object.

        Args:
            admission_level (str): The admission exam level of the student.

        Raises:
            ValueError: If the admission level is not one of 'secondary', 'high school', or 'university'.
        """
        valid_levels = ['secondary', 'high school', 'university']
        if admission_level.lower() not in valid_levels:
            raise ValueError("Invalid admission level. Must be one of: {}".format(", ".join(valid_levels)))
        self.admission_level = admission_level.lower()

class CourseRecommendationSystem:
    """Provides course recommendations for students based on their admission exam level."""

    def __init__(self):
        """
        Initializes a CourseRecommendationSystem object with a list of available courses.
        """
        self.courses = [
            Course("Mathematics", "secondary"),
            Course("Science", "secondary"),
            Course("History", "high school"),
            Course("English", "high school"),
            Course("Computer Science", "university"),
            Course("Engineering", "university"),
        ]

    def recommend_courses(self, student):
        """
        Recommends courses for a student based on their admission exam level.

        Args:
            student (Student): The student for whom to recommend courses.

        Returns:
            list[Course]: A list of recommended courses.
        """
        recommended_courses = [course for course in self.courses if course.required_level == student.admission_level]
        return recommended_courses

def main():
    try:
        # Create a course recommendation system
        crs = CourseRecommendationSystem()

        # Create students with different admission levels
        secondary_student = Student("secondary")
        high_school_student = Student("high school")
        university_student = Student("university")

        # Recommend courses for each student
        print("Recommended courses for secondary student:")
        for course in crs.recommend_courses(secondary_student):
            print(course.name)

        print("\nRecommended courses for high school student:")
        for course in crs.recommend_courses(high_school_student):
            print(course.name)

        print("\nRecommended courses for university student:")
        for course in crs.recommend_courses(university_student):
            print(course.name)

    except Exception as e:
        print("An error occurred: {}".format(str(e)))

if __name__ == "__main__":
    main()
```
