"""
Generated Code Metadata:
========================
Original URL: https://traceybaptiste.com
Prompt: Create a lesson plan for teaching children about Caribbean culture and folklore using Tracey Baptiste's books as a resource.
Generated: DETERMINISTIC_fe1e688815a0161f
Batch ID: 20250622_211514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class LessonPlan:
    """
    A class to represent a lesson plan for teaching children about Caribbean culture and folklore.
    """

    def __init__(self, title, age_group, duration, resources):
        """
        Initializes the lesson plan with a title, age group, duration, and resources.

        :param title: str - The title of the lesson plan
        :param age_group: str - The target age group for the lesson
        :param duration: int - Duration of the lesson in minutes
        :param resources: list - List of resources to be used in the lesson
        """
        self.title = title
        self.age_group = age_group
        self.duration = duration
        self.resources = resources

    def display_plan(self):
        """
        Displays the lesson plan details.
        """
        print(f"Lesson Title: {self.title}")
        print(f"Target Age Group: {self.age_group}")
        print(f"Duration: {self.duration} minutes")
        print("Resources:")
        for resource in self.resources:
            print(f"- {resource}")

    def add_resource(self, resource):
        """
        Adds a new resource to the lesson plan.

        :param resource: str - The resource to be added
        """
        if isinstance(resource, str) and resource:
            self.resources.append(resource)
        else:
            raise ValueError("Resource must be a non-empty string.")

    def remove_resource(self, resource):
        """
        Removes a resource from the lesson plan.

        :param resource: str - The resource to be removed
        """
        try:
            self.resources.remove(resource)
        except ValueError:
            print(f"Resource '{resource}' not found in the lesson plan.")


# Example usage
if __name__ == "__main__":
    # Create a lesson plan for teaching Caribbean culture and folklore
    try:
        lesson_title = "Exploring Caribbean Culture and Folklore"
        target_age_group = "8-12 years"
        lesson_duration = 60  # in minutes
        lesson_resources = [
            "Tracey Baptiste's 'The Jumbies'",
            "Tracey Baptiste's 'The Jumbies' Activity Guide",
            "Videos on Caribbean folklore",
            "Art supplies for creative projects"
        ]

        # Instantiate the lesson plan
        caribbean_lesson = LessonPlan(lesson_title, target_age_group, lesson_duration, lesson_resources)

        # Display the lesson plan
        caribbean_lesson.display_plan()

        # Add a new resource
        caribbean_lesson.add_resource("Tracey Baptiste's 'Islands'")

        # Remove a resource
        caribbean_lesson.remove_resource("Videos on Caribbean folklore")

        # Display updated lesson plan
        print("\nUpdated Lesson Plan:")
        caribbean_lesson.display_plan()

    except Exception as e:
        print(f"An error occurred: {e}")
```
