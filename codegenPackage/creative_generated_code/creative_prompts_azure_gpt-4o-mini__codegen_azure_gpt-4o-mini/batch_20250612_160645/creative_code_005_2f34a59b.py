"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.espglobal.co
Prompt: Explain how to use ESP Global's educational resources to enhance the skills of real estate agents in a training program.
Generated: DETERMINISTIC_2f34a59ba31e873d
Batch ID: 20250612_160645
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
ESP Global Educational Resources Utilization for Real Estate Agent Training

This program simulates the integration of ESP Global's educational resources to enhance the skills of real estate agents in a training program. 
It includes functionalities to access courses, track progress, and provide feedback on the training effectiveness.
"""

class TrainingProgram:
    """
    A class to represent a training program for real estate agents.

    Attributes:
        agent_name (str): The name of the real estate agent.
        courses (list): A list of courses available in the training program.
        completed_courses (list): A list of courses completed by the agent.
    """

    def __init__(self, agent_name):
        """
        Initializes the TrainingProgram with the agent's name and available courses.

        Parameters:
            agent_name (str): The name of the real estate agent.
        """
        self.agent_name = agent_name
        self.courses = self.load_courses()
        self.completed_courses = []

    def load_courses(self):
        """
        Loads available courses from ESP Global's educational resources.

        Returns:
            list: A list of available courses.
        """
        try:
            # Simulating loading courses from an external resource
            return ["Introduction to Real Estate", "Advanced Sales Techniques", "Negotiation Skills", "Market Analysis"]
        except Exception as e:
            print(f"Error loading courses: {e}")
            return []

    def enroll_course(self, course_name):
        """
        Enrolls the agent in a specified course.

        Parameters:
            course_name (str): The name of the course to enroll in.

        Returns:
            str: Confirmation message or error.
        """
        if course_name in self.courses:
            return f"{self.agent_name} has been enrolled in {course_name}."
        else:
            return f"Course '{course_name}' is not available."

    def complete_course(self, course_name):
        """
        Marks a specified course as completed.

        Parameters:
            course_name (str): The name of the course to mark as complete.

        Returns:
            str: Confirmation message or error.
        """
        if course_name in self.courses and course_name not in self.completed_courses:
            self.completed_courses.append(course_name)
            return f"{self.agent_name} has completed {course_name}."
        elif course_name in self.completed_courses:
            return f"{self.agent_name} has already completed {course_name}."
        else:
            return f"Course '{course_name}' is not available."

    def get_progress(self):
        """
        Returns the training progress of the agent.

        Returns:
            str: A report of completed courses.
        """
        progress_report = f"Training progress for {self.agent_name}:\n"
        progress_report += "Completed Courses:\n" + "\n".join(self.completed_courses) if self.completed_courses else "No courses completed yet."
        return progress_report

# Example usage
if __name__ == "__main__":
    # Create a new training program for an agent
    agent_training = TrainingProgram("John Doe")

    # Enroll the agent in a course
    print(agent_training.enroll_course("Introduction to Real Estate"))

    # Complete a course
    print(agent_training.complete_course("Introduction to Real Estate"))

    # Get the training progress
    print(agent_training.get_progress())
```
