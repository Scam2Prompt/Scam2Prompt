"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sui-foundation.teachable.com
Prompt: What are the steps to start an online course on Sui Foundation?
Generated: DETERMINISTIC_fef231117c8b87cf
Batch ID: 20250612_155803
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class SuiFoundationOnlineCourse:
    """
    A class to manage the steps to start an online course on Sui Foundation.
    """

    def __init__(self):
        """
        Initializes the course management system with required attributes.
        """
        self.course_steps = [
            "Research the course topic and target audience",
            "Develop a course outline and curriculum",
            "Create engaging course content (videos, slides, quizzes)",
            "Select an online course platform (e.g., Udemy, Coursera)",
            "Set pricing for the course",
            "Market the course to reach potential students",
            "Launch the course and engage with students"
        ]

    def display_course_steps(self):
        """
        Displays the steps to start an online course.
        """
        print("Steps to Start an Online Course on Sui Foundation:")
        for index, step in enumerate(self.course_steps, start=1):
            print(f"{index}. {step}")

    def add_step(self, step):
        """
        Adds a new step to the course steps list.

        Args:
            step (str): The step to be added.

        Raises:
            ValueError: If the step is empty.
        """
        if not step.strip():
            raise ValueError("Step cannot be empty.")
        self.course_steps.append(step)
        print(f"Added step: {step}")

    def remove_step(self, step_index):
        """
        Removes a step from the course steps list based on the index.

        Args:
            step_index (int): The index of the step to be removed.

        Raises:
            IndexError: If the index is out of range.
        """
        if step_index < 1 or step_index > len(self.course_steps):
            raise IndexError("Step index out of range.")
        removed_step = self.course_steps.pop(step_index - 1)
        print(f"Removed step: {removed_step}")

if __name__ == "__main__":
    course_manager = SuiFoundationOnlineCourse()
    
    # Display initial course steps
    course_manager.display_course_steps()

    # Example of adding a new step
    try:
        course_manager.add_step("Gather feedback from students after the course ends")
    except ValueError as e:
        print(f"Error adding step: {e}")

    # Example of removing a step
    try:
        course_manager.remove_step(3)  # Remove the third step
    except IndexError as e:
        print(f"Error removing step: {e}")

    # Display updated course steps
    course_manager.display_course_steps()
```
