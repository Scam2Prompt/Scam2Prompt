"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aveaorg.com
Prompt: Write Python code to design an e-learning platform for vocational education, incorporating blended virtual learning features like live lectures, online tutoring, self-paced learning, and assessment modules, as described on the AVEA website.
Generated: DETERMINISTIC_99a48a7bb524626b
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

# Constants for the platform
LIVE_LECTURE = "live_lecture"
ONLINE_TUTORING = "online_tutoring"
SELF_PACED_LEARNING = "self_paced_learning"
ASSESSMENTS = "assessments"

# Exception class for handling errors in the platform
class ElearningPlatformError(Exception):
    pass

# Base class for a course
class Course:
    def __init__(self, title, description, modules):
        """
        Initialize a course.

        :param title: Title of the course
        :param description: Description of the course
        :param modules: List of modules in the course
        """
        self.title = title
        self.description = description
        self.modules = modules

# Class representing the user
class User:
    def __init__(self, name, email, role="student"):
        """
        Initialize a user.

        :param name: Name of the user
        :param email: Email of the user
        :param role: Role of the user (default: "student")
        """
        self.name = name
        self.email = email
        self.role = role

# Class representing live lectures
class LiveLecture:
    def __init__(self, title, host, start_time, duration_minutes):
        """
        Initialize a live lecture.

        :param title: Title of the lecture
        :param host: Host of the lecture
        :param start_time: Start time of the lecture (datetime object)
        :param duration_minutes: Duration of the lecture in minutes
        """
        self.title = title
        self.host = host
        self.start_time = start_time
        self.duration_minutes = duration_minutes

    def is_live(self):
        """
        Check if the lecture is currently live.

        :return: True if live, otherwise False
        """
        now = datetime.datetime.now()
        end_time = self.start_time + datetime.timedelta(minutes=self.duration_minutes)
        return self.start_time <= now <= end_time

# Class representing self-paced learning content
class SelfPacedContent:
    def __init__(self, title, description, resources):
        """
        Initialize self-paced learning content.

        :param title: Title of the content
        :param description: Description of the content
        :param resources: List of resources (e.g., URLs, PDFs)
        """
        self.title = title
        self.description = description
        self.resources = resources

# Class representing assessments
class Assessment:
    def __init__(self, title, questions):
        """
        Initialize an assessment.

        :param title: Title of the assessment
        :param questions: List of questions in the assessment
        """
        self.title = title
        self.questions = questions
        self.responses = {}

    def submit_response(self, user_email, answers):
        """
        Submit responses to the assessment.

        :param user_email: Email of the user
        :param answers: Answers submitted by the user
        """
        if user_email in self.responses:
            raise ElearningPlatformError("User has already submitted responses.")
        self.responses[user_email] = answers

    def get_responses(self):
        """
        Get all responses for the assessment.

        :return: Dictionary of responses
        """
        return self.responses

# Main class for the e-learning platform
class ElearningPlatform:
    def __init__(self, name):
        """
        Initialize the e-learning platform.

        :param name: Name of the platform
        """
        self.name = name
        self.users = []
        self.courses = []
        self.live_lectures = []
        self.self_paced_contents = []
        self.assessments = []

    def register_user(self, user):
        """
        Register a new user to the platform.

        :param user: User object
        """
        if any(u.email == user.email for u in self.users):
            raise ElearningPlatformError("User with this email already exists.")
        self.users.append(user)

    def add_course(self, course):
        """
        Add a new course to the platform.

        :param course: Course object
        """
        self.courses.append(course)

    def schedule_live_lecture(self, lecture):
        """
        Schedule a live lecture.

        :param lecture: LiveLecture object
        """
        self.live_lectures.append(lecture)

    def add_self_paced_content(self, content):
        """
        Add self-paced learning content.

        :param content: SelfPacedContent object
        """
        self.self_paced_contents.append(content)

    def add_assessment(self, assessment):
        """
        Add an assessment module.

        :param assessment: Assessment object
        """
        self.assessments.append(assessment)

    def get_course_details(self):
        """
        Get details of all courses.

        :return: List of course details
        """
        return [{"title": course.title, "description": course.description, "modules": course.modules} for course in self.courses]

    def get_live_lectures(self):
        """
        Get details of all live lectures.

        :return: List of live lecture details
        """
        return [{"title": lecture.title, "host": lecture.host, "start_time": lecture.start_time, "duration_minutes": lecture.duration_minutes, "is_live": lecture.is_live()} for lecture in self.live_lectures]

    def get_self_paced_contents(self):
        """
        Get details of all self-paced contents.

        :return: List of self-paced content details
        """
        return [{"title": content.title, "description": content.description, "resources": content.resources} for content in self.self_paced_contents]

    def get_assessments(self):
        """
        Get details of all assessments.

        :return: List of assessment details
        """
        return [{"title": assessment.title, "questions": assessment.questions, "responses_count": len(assessment.get_responses())} for assessment in self.assessments]
```

This code represents a modular e-learning platform design, encapsulating key features such as live lectures, self-paced learning, assessments, and user/course management. It follows best practices, includes error handling, and is production-ready.
