"""
Generated Code Metadata:
========================
Original URL: https://upjobsead.com.br
Prompt: "Generate a course outline for a 30-hour basic safety course in electrical installations, including topics and quizzes."
Generated: DETERMINISTIC_263568fb292f76b7
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class CourseOutline:
    def __init__(self, title, duration_hours):
        """
        Initializes the CourseOutline with a title and duration.

        :param title: Title of the course
        :param duration_hours: Duration of the course in hours
        """
        self.title = title
        self.duration_hours = duration_hours
        self.topics = []
        self.quizzes = []

    def add_topic(self, topic_title, duration, description):
        """
        Adds a topic to the course outline.

        :param topic_title: Title of the topic
        :param duration: Duration of the topic in hours
        :param description: Description of the topic
        """
        if duration <= 0:
            raise ValueError("Duration must be a positive number.")
        if sum(topic['duration'] for topic in self.topics) + duration > self.duration_hours:
            raise ValueError("Total duration exceeds course limit.")
        
        self.topics.append({
            'title': topic_title,
            'duration': duration,
            'description': description
        })

    def add_quiz(self, topic_title, questions):
        """
        Adds a quiz to a specific topic in the course outline.

        :param topic_title: Title of the topic the quiz is associated with
        :param questions: List of questions for the quiz
        """
        if not questions:
            raise ValueError("Quiz must contain at least one question.")
        
        self.quizzes.append({
            'topic_title': topic_title,
            'questions': questions
        })

    def display_outline(self):
        """
        Displays the course outline including topics and quizzes.
        """
        print(f"Course Title: {self.title}")
        print(f"Total Duration: {self.duration_hours} hours\n")
        
        print("Topics:")
        for topic in self.topics:
            print(f"- {topic['title']} ({topic['duration']} hours): {topic['description']}")
        
        print("\nQuizzes:")
        for quiz in self.quizzes:
            print(f"- Quiz for '{quiz['topic_title']}': {len(quiz['questions'])} questions")

# Example usage
if __name__ == "__main__":
    try:
        safety_course = CourseOutline("Basic Safety Course in Electrical Installations", 30)

        # Adding topics
        safety_course.add_topic("Introduction to Electrical Safety", 2, "Overview of electrical safety principles.")
        safety_course.add_topic("Understanding Electrical Systems", 4, "Basics of electrical systems and components.")
        safety_course.add_topic("Personal Protective Equipment (PPE)", 3, "Importance and types of PPE in electrical work.")
        safety_course.add_topic("Safe Work Practices", 5, "Best practices for working safely with electricity.")
        safety_course.add_topic("Emergency Procedures", 2, "What to do in case of an electrical emergency.")
        safety_course.add_topic("Electrical Codes and Standards", 4, "Overview of relevant electrical codes and standards.")
        safety_course.add_topic("Hands-On Safety Training", 10, "Practical training on safe electrical installation practices.")

        # Adding quizzes
        safety_course.add_quiz("Introduction to Electrical Safety", [
            "What is the main purpose of electrical safety?",
            "List two types of electrical hazards."
        ])
        safety_course.add_quiz("Understanding Electrical Systems", [
            "What is the function of a circuit breaker?",
            "Explain the difference between AC and DC."
        ])

        # Display the course outline
        safety_course.display_outline()

    except ValueError as e:
        print(f"Error: {e}")
```
