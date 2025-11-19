"""
Generated Code Metadata:
========================
Original URL: https://simice-tec-elevators.cz
Prompt: "Develop a training program outline for teaching technicians about the latest elevator technologies, including courses on Schindler ID, Miconic TX GC, and other systems from major manufacturers like KONE, OTIS, and ThyssenKrupp."
Generated: DETERMINISTIC_34a408a99ba0acc8
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class TrainingProgram:
    """
    A training program outline for teaching technicians about the latest elevator technologies.
    Includes courses on major elevator systems from manufacturers like Schindler, KONE, OTIS, etc.
    """
    
    def __init__(self):
        self.program_name = "Elevator Technician Certification Program"
        self.duration_weeks = 12
        self.courses = []
        self._initialize_courses()
    
    def _initialize_courses(self):
        """Initialize the course catalog with standard offerings"""
        self.courses = [
            {
                'title': "Schindler ID System Fundamentals",
                'duration': 2,
                'topics': [
                    "ID System Architecture",
                    "Troubleshooting ID Controllers",
                    "Modernization Procedures",
                    "Hands-on Lab Exercises"
                ],
                'prerequisites': "Basic Electrical Knowledge"
            },
            {
                'title': "Miconic TX GC Advanced Training",
                'duration': 3,
                'topics': [
                    "TX GC System Overview",
                    "Programming and Configuration",
                    "Fault Diagnosis",
                    "Preventive Maintenance"
                ],
                'prerequisites': "Schindler ID Fundamentals or equivalent"
            },
            {
                'title': "KONE EcoDisc Technology",
                'duration': 2,
                'topics': [
                    "EcoDisc Motor Principles",
                    "Energy Efficiency Features",
                    "Maintenance Best Practices",
                    "Troubleshooting Techniques"
                ],
                'prerequisites': "Basic Mechanical Knowledge"
            },
            {
                'title': "OTIS Gen2 Elevator Systems",
                'duration': 2,
                'topics': [
                    "Gen2 System Components",
                    "ROPES Technology",
                    "Diagnostic Tools",
                    "Modernization Strategies"
                ],
                'prerequisites': "Basic Elevator Knowledge"
            },
            {
                'title': "ThyssenKrupp TWIN Elevator Systems",
                'duration': 3,
                'topics': [
                    "TWIN System Architecture",
                    "Safety Systems",
                    "Capacity Planning",
                    "Advanced Diagnostics"
                ],
                'prerequisites': "Intermediate Elevator Technology"
            }
        ]
    
    def add_course(self, title, duration, topics, prerequisites):
        """
        Add a custom course to the training program
        Args:
            title (str): Course title
            duration (int): Duration in weeks
            topics (list): List of topics covered
            prerequisites (str): Required knowledge
        """
        if not isinstance(topics, list):
            raise ValueError("Topics must be provided as a list")
        
        self.courses.append({
            'title': title,
            'duration': duration,
            'topics': topics,
            'prerequisites': prerequisites
        })
    
    def get_program_outline(self):
        """Return the complete program outline"""
        outline = {
            'program_name': self.program_name,
            'total_duration': self.duration_weeks,
            'courses': self.courses
        }
        return outline
    
    def calculate_total_hours(self, hours_per_week=20):
        """
        Calculate total training hours
        Args:
            hours_per_week (int): Hours per week (default 20)
        Returns:
            int: Total program hours
        """
        return self.duration_weeks * hours_per_week
    
    def validate_prerequisites(self, course_index, student_qualifications):
        """
        Check if student meets prerequisites for a course
        Args:
            course_index (int): Index of course in courses list
            student_qualifications (str): Student's qualifications
        Returns:
            bool: True if prerequisites are met
        Raises:
            IndexError: If course_index is invalid
        """
        if course_index < 0 or course_index >= len(self.courses):
            raise IndexError("Invalid course index")
        
        required = self.courses[course_index]['prerequisites']
        return required.lower() in student_qualifications.lower()


# Example usage
if __name__ == "__main__":
    try:
        program = TrainingProgram()
        
        # Add a custom course
        program.add_course(
            title="Mitsubishi NEXIEZ-S System",
            duration=2,
            topics=[
                "NEXIEZ-S Overview",
                "Destination Control Systems",
                "Energy Saving Features"
            ],
            prerequisites="Basic Elevator Knowledge"
        )
        
        # Get program details
        outline = program.get_program_outline()
        print(f"Program Name: {outline['program_name']}")
        print(f"Total Duration: {outline['total_duration']} weeks")
        print("\nCourses:")
        for course in outline['courses']:
            print(f"\n{course['title']} ({course['duration']} weeks)")
            print(f"Prerequisites: {course['prerequisites']}")
            print("Topics:")
            for topic in course['topics']:
                print(f"- {topic}")
        
        # Check prerequisites
        student_skills = "Basic Electrical Knowledge, Basic Elevator Knowledge"
        course_to_check = 0  # Schindler ID course
        if program.validate_prerequisites(course_to_check, student_skills):
            print("\nStudent meets prerequisites for selected course")
        else:
            print("\nStudent does not meet prerequisites")
            
    except Exception as e:
        print(f"Error: {str(e)}")
```
