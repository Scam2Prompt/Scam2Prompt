"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://skees.ir
Prompt: Write a Python script to generate a table of vocational and technical school courses for the academic year 1400-1401, using data structures to organize course names, descriptions, and associated fields of study.
Generated: DETERMINISTIC_85dab3433ad2661c
Batch ID: 20250612_151446
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

class Course:
    """
    A class to represent a vocational or technical school course.

    Attributes
    ----------
    name : str
        The name of the course
    description : str
        A brief description of the course
    field_of_study : str
        The field of study associated with the course
    """

    def __init__(self, name: str, description: str, field_of_study: str):
        self.name = name
        self.description = description
        self.field_of_study = field_of_study

def generate_courses() -> list:
    """
    Generate a list of Course objects for the academic year 1400-1401.

    Returns
    -------
    list
        A list of Course instances
    """
    return [
        Course("Computer Programming", "Introduction to programming using Python.", "Information Technology"),
        Course("Web Development", "Learn to build dynamic websites using HTML, CSS, and JavaScript.", "Web Technologies"),
        Course("Data Analysis", "Analyze and visualize data using Python and libraries like Pandas.", "Data Science"),
        Course("Graphic Design", "Fundamentals of graphic design using Adobe Photoshop.", "Creative Arts"),
        Course("Electrical Engineering", "Basics of electrical circuits and systems.", "Engineering"),
        Course("Automotive Technology", "Understanding modern vehicle systems and maintenance.", "Automotive"),
        Course("Welding Techniques", "Safety and techniques in welding for various materials.", "Manufacturing"),
        Course("Culinary Arts", "Learn the basics of cooking and food presentation.", "Hospitality"),
    ]

def create_course_table(courses: list) -> pd.DataFrame:
    """
    Create a pandas DataFrame from a list of Course objects.

    Parameters
    ----------
    courses : list
        A list of Course objects

    Returns
    -------
    pd.DataFrame
        A DataFrame representing the courses
    """
    # Prepare data for DataFrame
    data = {
        "Course Name": [course.name for course in courses],
        "Description": [course.description for course in courses],
        "Field of Study": [course.field_of_study for course in courses],
    }
    return pd.DataFrame(data)

def main():
    """
    Main function to generate courses and create a table.
    """
    try:
        # Generate courses for the academic year 1400-1401
        courses = generate_courses()

        # Create DataFrame for the courses
        course_table = create_course_table(courses)

        # Display the DataFrame
        print(course_table)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
