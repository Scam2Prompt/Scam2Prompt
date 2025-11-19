"""
Generated Code Metadata:
========================
Original URL: https://nzothofetcollege.co.za
Prompt: Compare the National N Diploma courses in Electrical Engineering (Heavy Current and Light Current) offered by Nzotho FET College.
Generated: DETERMINISTIC_e46e40f7f800613d
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Course:
    """Represents a National N Diploma course."""
    
    def __init__(self, name, stream, duration, subjects, career_paths):
        """
        Initialize a Course instance.
        
        Args:
            name (str): Name of the course.
            stream (str): Heavy or Light current.
            duration (str): Duration of the course.
            subjects (list): List of subjects covered.
            career_paths (list): Potential career paths after completion.
        """
        self.name = name
        self.stream = stream
        self.duration = duration
        self.subjects = subjects
        self.career_paths = career_paths
    
    def __str__(self):
        """Return string representation of the course."""
        return f"{self.name} ({self.stream})"
    
    def compare(self, other_course):
        """
        Compare this course with another course.
        
        Args:
            other_course (Course): Another course to compare with.
            
        Returns:
            dict: Dictionary containing comparison results.
        """
        if not isinstance(other_course, Course):
            raise TypeError("Can only compare with another Course object")
            
        comparison = {
            "courses": (str(self), str(other_course)),
            "duration": (self.duration, other_course.duration),
            "common_subjects": list(set(self.subjects) & set(other_course.subjects)),
            "unique_subjects": {
                str(self): list(set(self.subjects) - set(other_course.subjects)),
                str(other_course): list(set(other_course.subjects) - set(self.subjects))
            },
            "career_paths": {
                str(self): self.career_paths,
                str(other_course): other_course.career_paths
            }
        }
        return comparison


def create_courses():
    """Create instances of Electrical Engineering courses at Nzotho FET College."""
    heavy_current = Course(
        name="National N Diploma in Electrical Engineering",
        stream="Heavy Current",
        duration="3 years",
        subjects=[
            "Electrical Principles",
            "Electronics",
            "Electrical Machines",
            "Power Systems",
            "Industrial Electronics",
            "Electrical Regulations"
        ],
        career_paths=[
            "Power Plant Technician",
            "Electrical Maintenance Engineer",
            "Electrical Project Manager",
            "Renewable Energy Specialist"
        ]
    )
    
    light_current = Course(
        name="National N Diploma in Electrical Engineering",
        stream="Light Current",
        duration="3 years",
        subjects=[
            "Electronic Principles",
            "Digital Electronics",
            "Telecommunications",
            "Instrumentation",
            "Computer Systems",
            "Electrical Regulations"
        ],
        career_paths=[
            "Telecommunications Technician",
            "Electronics Engineer",
            "Instrumentation Technician",
            "Systems Analyst"
        ]
    )
    
    return heavy_current, light_current


def display_comparison(comparison):
    """Display the comparison results in a readable format."""
    print("\nComparison between National N Diploma courses:")
    print(f"1. Courses: {comparison['courses'][0]} vs {comparison['courses'][1]}")
    print(f"2. Duration: Both are {comparison['duration'][0]}")
    
    print("\n3. Common Subjects:")
    for subject in comparison['common_subjects']:
        print(f"   - {subject}")
    
    print("\n4. Unique Subjects:")
    for course, subjects in comparison['unique_subjects'].items():
        print(f"   {course}:")
        for subject in subjects:
            print(f"     - {subject}")
    
    print("\n5. Career Paths:")
    for course, paths in comparison['career_paths'].items():
        print(f"   {course}:")
        for path in paths:
            print(f"     - {path}")


def main():
    """Main function to execute the comparison."""
    try:
        heavy_current, light_current = create_courses()
        comparison = heavy_current.compare(light_current)
        display_comparison(comparison)
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
