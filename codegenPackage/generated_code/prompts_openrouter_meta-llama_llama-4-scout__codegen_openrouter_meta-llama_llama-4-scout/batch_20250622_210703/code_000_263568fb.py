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
# Course Outline Generator for Basic Safety Course in Electrical Installations

class Course:
    def __init__(self, name, duration):
        """
        Initialize a Course object.

        Args:
            name (str): Name of the course.
            duration (int): Duration of the course in hours.
        """
        self.name = name
        self.duration = duration
        self.topics = []
        self.quizzes = []

    def add_topic(self, topic):
        """
        Add a topic to the course.

        Args:
            topic (Topic): Topic object to add.
        """
        self.topics.append(topic)

    def add_quiz(self, quiz):
        """
        Add a quiz to the course.

        Args:
            quiz (Quiz): Quiz object to add.
        """
        self.quizzes.append(quiz)

    def generate_outline(self):
        """
        Generate the course outline.

        Returns:
            str: Course outline as a string.
        """
        outline = f"Course: {self.name} ({self.duration} hours)\n\n"
        outline += "Topics:\n"
        for i, topic in enumerate(self.topics, 1):
            outline += f"{i}. {topic.name} ({topic.duration} hours)\n"
        outline += "\nQuizzes:\n"
        for i, quiz in enumerate(self.quizzes, 1):
            outline += f"{i}. Quiz {i} - {quiz.topic_name}\n"
        return outline


class Topic:
    def __init__(self, name, duration):
        """
        Initialize a Topic object.

        Args:
            name (str): Name of the topic.
            duration (int): Duration of the topic in hours.
        """
        self.name = name
        self.duration = duration


class Quiz:
    def __init__(self, topic_name, questions):
        """
        Initialize a Quiz object.

        Args:
            topic_name (str): Name of the topic the quiz is based on.
            questions (list): List of questions for the quiz.
        """
        self.topic_name = topic_name
        self.questions = questions


def main():
    try:
        # Create course
        course = Course("Basic Safety Course in Electrical Installations", 30)

        # Create topics
        topics = [
            Topic("Introduction to Electrical Safety", 2),
            Topic("Electrical Shock and Protection", 4),
            Topic("Electrical Equipment and Tools", 4),
            Topic("Hazardous Locations and Atmospheres", 4),
            Topic("Lockout/Tagout and Electrical Safety Procedures", 6),
            Topic("Final Assessment and Review", 2),
        ]

        # Add topics to course
        for topic in topics:
            course.add_topic(topic)

        # Create quizzes
        quizzes = [
            Quiz("Introduction to Electrical Safety", ["What is electrical safety?", "Why is electrical safety important?"]),
            Quiz("Electrical Shock and Protection", ["What is electrical shock?", "How can electrical shock be prevented?"]),
            Quiz("Electrical Equipment and Tools", ["What are the types of electrical equipment?", "How to use electrical tools safely?"]),
            Quiz("Hazardous Locations and Atmospheres", ["What are hazardous locations?", "How to work safely in hazardous atmospheres?"]),
            Quiz("Lockout/Tagout and Electrical Safety Procedures", ["What is lockout/tagout?", "How to perform electrical safety procedures?"]),
        ]

        # Add quizzes to course
        for quiz in quizzes:
            course.add_quiz(quiz)

        # Generate and print course outline
        print(course.generate_outline())

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
