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
"""
Script to generate a table of vocational and technical school courses for the academic year 1400-1401.
Organizes course names, descriptions, and associated fields of study using data structures.
"""

import tabulate

# Define a class to represent a course
class Course:
    def __init__(self, name, description, field_of_study):
        """
        Initializes a Course instance.

        :param name: Name of the course
        :param description: Brief description of the course
        :param field_of_study: Associated field of study
        """
        self.name = name
        self.description = description
        self.field_of_study = field_of_study


# List of courses for the academic year 1400-1401
courses = [
    Course("Introduction to Welding", "Fundamentals of welding techniques and safety protocols.", "Manufacturing"),
    Course("Basic Electrical Engineering", "Understanding electrical circuits and components.", "Electrical"),
    Course("Automotive Maintenance", "Basics of vehicle repair and maintenance.", "Automotive"),
    Course("Graphic Design Principles", "Introduction to design concepts and tools.", "Arts and Design"),
    Course("CNC Machining", "Operating computer-controlled machining tools.", "Manufacturing"),
    Course("Web Development Basics", "Building and designing websites using HTML, CSS, and JavaScript.", "Information Technology"),
    Course("HVAC Systems", "Installation and repair of heating, ventilation, and air conditioning systems.", "Construction"),
    Course("Digital Marketing Fundamentals", "Overview of online marketing strategies and tools.", "Business"),
]

# Function to generate the course table
def generate_course_table(courses):
    """
    Generates a formatted table of courses.

    :param courses: List of Course objects
    :return: Table as a string
    """
    # Prepare data for the table
    table_data = []
    for course in courses:
        table_data.append([course.name, course.description, course.field_of_study])

    # Generate a table using the 'tabulate' library
    return tabulate.tabulate(
        table_data,
        headers=["Course Name", "Description", "Field of Study"],
        tablefmt="grid"
    )

# Main entry point of the script
def main():
    """
    Main function to execute the script logic.
    """
    try:
        # Generate and print the course table
        print("Vocational and Technical School Courses (Academic Year 1400-1401):")
        course_table = generate_course_table(courses)
        print(course_table)

    except Exception as e:
        print(f"An error occurred while generating the course table: {e}")


# Run the script
if __name__ == "__main__":
    main()
```
