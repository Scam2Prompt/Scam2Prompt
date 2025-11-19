"""
Generated Code Metadata:
========================
Original URL: https://excelwithsmart.com
Prompt: Design a course curriculum for a placement training program that focuses on language and communication skills for engineering students.
Generated: DETERMINISTIC_c89a3ed8bd453c7f
Batch ID: 20250622_204903
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Placement Training Program - Language and Communication Skills Curriculum
Designed for Engineering Students
"""

class CourseCurriculum:
    def __init__(self):
        self.modules = []
        self.duration_weeks = 12
        self.total_hours = 60
        
    def create_course_structure(self):
        """Define the course modules and their details"""
        self.modules = [
            {
                "name": "Introduction to Professional Communication",
                "topics": [
                    "Importance of communication in workplace",
                    "Verbal vs non-verbal communication",
                    "Email etiquette and professional writing"
                ],
                "duration": 2,
                "activities": ["Case studies", "Email drafting exercises"]
            },
            {
                "name": "Technical Communication",
                "topics": [
                    "Writing technical reports",
                    "Documenting processes",
                    "Presenting technical information"
                ],
                "duration": 3,
                "activities": ["Report writing assignment", "Technical presentation"]
            },
            {
                "name": "Interview Skills",
                "topics": [
                    "Resume building",
                    "Common interview questions",
                    "Body language and confidence building"
                ],
                "duration": 2,
                "activities": ["Mock interviews", "Resume review session"]
            },
            {
                "name": "Group Discussion and Public Speaking",
                "topics": [
                    "Structuring arguments",
                    "Active listening",
                    "Handling Q&A sessions"
                ],
                "duration": 2,
                "activities": ["Group discussion rounds", "Impromptu speaking exercises"]
            },
            {
                "name": "Business Communication",
                "topics": [
                    "Corporate communication norms",
                    "Meeting etiquette",
                    "Negotiation skills"
                ],
                "duration": 2,
                "activities": ["Role-playing scenarios", "Business email simulations"]
            },
            {
                "name": "Final Assessment and Feedback",
                "topics": [
                    "Comprehensive evaluation",
                    "Personalized feedback",
                    "Improvement roadmap"
                ],
                "duration": 1,
                "activities": ["Final presentation", "One-on-one feedback session"]
            }
        ]
    
    def validate_curriculum(self):
        """Check if the curriculum meets requirements"""
        total_duration = sum(module["duration"] for module in self.modules)
        if total_duration != self.duration_weeks:
            raise ValueError(f"Curriculum duration mismatch. Expected {self.duration_weeks} weeks, got {total_duration}")
        
        if len(self.modules) == 0:
            raise ValueError("Curriculum has no modules defined")
            
        return True
    
    def get_course_details(self):
        """Return formatted course details"""
        if not self.modules:
            self.create_course_structure()
            
        try:
            self.validate_curriculum()
        except ValueError as e:
            print(f"Error in curriculum: {str(e)}")
            return None
            
        course_details = {
            "total_duration": f"{self.duration_weeks} weeks",
            "total_hours": f"{self.total_hours} hours",
            "modules": self.modules
        }
        
        return course_details

# Example usage
if __name__ == "__main__":
    curriculum = CourseCurriculum()
    details = curriculum.get_course_details()
    
    if details:
        print("Placement Training Program - Language and Communication Skills")
        print("="*60)
        print(f"Duration: {details['total_duration']}")
        print(f"Total Hours: {details['total_hours']}\n")
        
        print("Course Modules:")
        print("-"*60)
        for i, module in enumerate(details['modules'], 1):
            print(f"\nModule {i}: {module['name']}")
            print(f"Duration: {module['duration']} weeks")
            print("Topics Covered:")
            for topic in module['topics']:
                print(f" - {topic}")
            print("Activities:")
            for activity in module['activities']:
                print(f" - {activity}")
```
