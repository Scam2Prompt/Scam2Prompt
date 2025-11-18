"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mitmip.ac.in
Prompt: Develop a program to organize and display the syllabus and results for MBBS and MD/MS courses at MIMSR Medical College, referencing the "Syllabus & Results" section.
Generated: DETERMINISTIC_db6452cb630dfd84
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os

class Course:
    """Class representing a course with a syllabus and results."""
    
    def __init__(self, name):
        """Initialize the course with a name, syllabus, and results."""
        self.name = name
        self.syllabus = []
        self.results = []

    def add_syllabus(self, topic):
        """Add a syllabus topic to the course."""
        self.syllabus.append(topic)

    def add_result(self, year, score):
        """Add exam results for a given year."""
        self.results.append({'year': year, 'score': score})

    def display_info(self):
        """Display the course information including syllabus and results."""
        print(f"Course: {self.name}")
        print("Syllabus Topics:")
        for topic in self.syllabus:
            print(f"- {topic}")
        print("Results:")
        for result in self.results:
            print(f"Year: {result['year']}, Score: {result['score']}")


class College:
    """Class representing a college with courses."""
    
    def __init__(self, name):
        """Initialize the college with a name and an empty course list."""
        self.name = name
        self.courses = {}

    def add_course(self, course_name):
        """Add a new course to the college."""
        if course_name not in self.courses:
            self.courses[course_name] = Course(course_name)

    def get_course(self, course_name):
        """Retrieve a course by name."""
        return self.courses.get(course_name)

    def display_courses(self):
        """Display all courses offered by the college."""
        print(f"Courses offered at {self.name}:")
        for course in self.courses.keys():
            print(f"- {course}")


def load_data(file_path):
    """Load course data from a JSON file."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Data file {file_path} not found.")
    
    with open(file_path, 'r') as file:
        return json.load(file)


def main():
    """Main function to initialize the college and display information."""
    college_name = "MIMSR Medical College"
    college = College(college_name)

    # Load course data from a JSON file
    try:
        data = load_data('syllabus_and_results.json')
        
        # Populate the college with courses
        for course_name, course_data in data.items():
            college.add_course(course_name)
            course = college.get_course(course_name)
            
            # Add syllabus topics
            for topic in course_data.get('syllabus', []):
                course.add_syllabus(topic)
            
            # Add results
            for result in course_data.get('results', []):
                course.add_result(result['year'], result['score'])
    
    except FileNotFoundError as e:
        print(e)
        return
    except json.JSONDecodeError:
        print("Error decoding JSON data.")
        return

    # Display courses and their information
    college.display_courses()
    for course in college.courses.values():
        course.display_info()


if __name__ == "__main__":
    main()
```

### JSON structure expected in `syllabus_and_results.json`:
```json
{
    "MBBS": {
        "syllabus": ["Anatomy", "Physiology", "Biochemistry"],
        "results": [{"year": 1, "score": 85}, {"year": 2, "score": 90}]
    },
    "MD/MS": {
        "syllabus": ["Internal Medicine", "Surgery", "Pediatrics"],
        "results": [{"year": 1, "score": 88}, {"year": 2, "score": 92}]
    }
}
```
