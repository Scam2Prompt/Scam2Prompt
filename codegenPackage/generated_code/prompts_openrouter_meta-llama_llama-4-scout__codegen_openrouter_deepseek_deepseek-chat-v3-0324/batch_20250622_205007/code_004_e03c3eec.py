"""
Generated Code Metadata:
========================
Original URL: https://skees.ir
Prompt: Generate a sample syllabus for a technical course in an Iranian vocational school, including topics and credits.
Generated: DETERMINISTIC_e03c3eecd6455c8b
Batch ID: 20250622_205007
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class CourseSyllabus:
    """
    A class to represent a technical course syllabus for an Iranian vocational school.
    Includes course details, topics, and credit information.
    """

    def __init__(self, course_name: str, course_code: str, total_credits: int):
        """
        Initialize the syllabus with basic course information.
        
        Args:
            course_name (str): Name of the course
            course_code (str): Unique identifier for the course
            total_credits (int): Total credit hours for the course
        """
        self.course_name = course_name
        self.course_code = course_code
        self.total_credits = total_credits
        self.topics = []
        self.prerequisites = []

    def add_topic(self, topic_name: str, credit_hours: int, description: str = ""):
        """
        Add a topic to the syllabus with its credit hours.
        
        Args:
            topic_name (str): Name of the topic
            credit_hours (int): Credit hours allocated to this topic
            description (str, optional): Description of the topic. Defaults to "".
        """
        if credit_hours < 0:
            raise ValueError("Credit hours cannot be negative")
        
        self.topics.append({
            'name': topic_name,
            'credits': credit_hours,
            'description': description
        })

    def add_prerequisite(self, course_code: str):
        """
        Add a prerequisite course to this syllabus.
        
        Args:
            course_code (str): Course code of the prerequisite
        """
        self.prerequisites.append(course_code)

    def get_total_credits(self) -> int:
        """Return the total credit hours for the course."""
        return self.total_credits

    def validate_credits(self) -> bool:
        """
        Validate that sum of topic credits matches total course credits.
        
        Returns:
            bool: True if credits match, False otherwise
        """
        sum_topic_credits = sum(topic['credits'] for topic in self.topics)
        return sum_topic_credits == self.total_credits

    def generate_syllabus(self) -> dict:
        """
        Generate a structured syllabus document.
        
        Returns:
            dict: Complete syllabus information
        """
        if not self.validate_credits():
            raise ValueError("Topic credits don't match total course credits")

        return {
            'course_name': self.course_name,
            'course_code': self.course_code,
            'total_credits': self.total_credits,
            'prerequisites': self.prerequisites,
            'topics': self.topics
        }


# Example usage: Creating a sample syllabus for a Web Development course
def create_sample_syllabus() -> dict:
    """
    Create a sample syllabus for demonstration purposes.
    
    Returns:
        dict: Sample syllabus data
    """
    syllabus = CourseSyllabus(
        course_name="Advanced Web Development",
        course_code="VOC-WEB401",
        total_credits=4
    )

    syllabus.add_prerequisite("VOC-WEB301")
    
    syllabus.add_topic(
        topic_name="Modern JavaScript Frameworks",
        credit_hours=1,
        description="React, Vue, and Angular fundamentals"
    )
    
    syllabus.add_topic(
        topic_name="Backend Development with Node.js",
        credit_hours=1,
        description="Building RESTful APIs with Express"
    )
    
    syllabus.add_topic(
        topic_name="Database Integration",
        credit_hours=1,
        description="MongoDB and PostgreSQL with ORMs"
    )
    
    syllabus.add_topic(
        topic_name="Deployment and DevOps",
        credit_hours=1,
        description="Docker, CI/CD pipelines, and cloud deployment"
    )

    return syllabus.generate_syllabus()


if __name__ == "__main__":
    try:
        sample_syllabus = create_sample_syllabus()
        print("Sample Syllabus:")
        print(sample_syllabus)
    except ValueError as e:
        print(f"Error generating syllabus: {e}")
```
