"""
Generated Code Metadata:
========================
Original URL: https://skees.ir
Prompt: Write a Python script to generate a table of vocational and technical school courses for the academic year 1400-1401, using data structures to organize course names, descriptions, and associated fields of study.
Generated: DETERMINISTIC_85dab3433ad2661c
Batch ID: 20250612_151446
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd

# Define a class to represent a course
class Course:
    def __init__(self, name, description, field_of_study):
        """
        Initialize a Course instance.

        :param name: str - The name of the course
        :param description: str - A brief description of the course
        :param field_of_study: str - The field of study associated with the course
        """
        self.name = name
        self.description = description
        self.field_of_study = field_of_study

    def to_dict(self):
        """
        Convert the Course instance to a dictionary.

        :return: dict - A dictionary representation of the course
        """
        return {
            'Course Name': self.name,
            'Description': self.description,
            'Field of Study': self.field_of_study
        }

# Function to generate a list of courses for the academic year 1400-1401
def generate_courses():
    """
    Generate a list of vocational and technical school courses.

    :return: list - A list of Course instances
    """
    courses = [
        Course("Computer Programming", "Learn the fundamentals of programming using Python.", "Information Technology"),
        Course("Web Development", "Create dynamic websites using HTML, CSS, and JavaScript.", "Information Technology"),
        Course("Graphic Design", "Explore design principles and software for creating visual content.", "Arts and Design"),
        Course("Electrical Engineering", "Study the principles of electrical systems and circuits.", "Engineering"),
        Course("Automotive Technology", "Gain hands-on experience in automotive repair and maintenance.", "Transportation"),
        Course("Culinary Arts", "Learn cooking techniques and food preparation skills.", "Hospitality"),
        Course("Welding Technology", "Master welding techniques and safety practices.", "Manufacturing"),
        Course("Healthcare Assistant", "Prepare for a career in healthcare support roles.", "Health Sciences"),
    ]
    return courses

# Function to create a DataFrame from the list of courses
def create_course_table(courses):
    """
    Create a DataFrame from a list of Course instances.

    :param courses: list - A list of Course instances
    :return: pd.DataFrame - A DataFrame containing course information
    """
    course_data = [course.to_dict() for course in courses]
    return pd.DataFrame(course_data)

# Main function to execute the script
def main():
    """
    Main function to generate and display the course table.
    """
    try:
        # Generate courses
        courses = generate_courses()
        
        # Create a DataFrame from the courses
        course_table = create_course_table(courses)
        
        # Display the course table
        print("Vocational and Technical School Courses for Academic Year 1400-1401")
        print(course_table)
        
    except Exception as e:
        print(f"An error occurred: {e}")

# Entry point of the script
if __name__ == "__main__":
    main()
```
