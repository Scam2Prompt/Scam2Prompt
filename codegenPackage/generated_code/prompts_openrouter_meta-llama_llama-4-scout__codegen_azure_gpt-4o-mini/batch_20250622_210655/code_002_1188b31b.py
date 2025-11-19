"""
Generated Code Metadata:
========================
Original URL: https://www.viviresconvivir.cl
Prompt: Generate a lesson plan for teaching children about the value of diversity and inclusion, using the quotes and principles outlined in the "Vivir es Convivir" program.
Generated: DETERMINISTIC_1188b31b0faa3c3c
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class LessonPlan:
    def __init__(self, title, age_group, duration, objectives, materials):
        """
        Initializes a new lesson plan.

        :param title: Title of the lesson
        :param age_group: Target age group for the lesson
        :param duration: Duration of the lesson in minutes
        :param objectives: List of learning objectives
        :param materials: List of materials needed for the lesson
        """
        self.title = title
        self.age_group = age_group
        self.duration = duration
        self.objectives = objectives
        self.materials = materials
        self.activities = []

    def add_activity(self, activity):
        """
        Adds an activity to the lesson plan.

        :param activity: A dictionary containing activity details
        """
        self.activities.append(activity)

    def display_plan(self):
        """
        Displays the lesson plan details.
        """
        print(f"Lesson Title: {self.title}")
        print(f"Age Group: {self.age_group}")
        print(f"Duration: {self.duration} minutes")
        print("Objectives:")
        for objective in self.objectives:
            print(f"- {objective}")
        print("Materials Needed:")
        for material in self.materials:
            print(f"- {material}")
        print("Activities:")
        for activity in self.activities:
            print(f"- {activity['name']}: {activity['description']}")

# Example usage
if __name__ == "__main__":
    try:
        # Create a lesson plan for teaching diversity and inclusion
        lesson = LessonPlan(
            title="Celebrating Diversity and Inclusion",
            age_group="8-12 years",
            duration=60,
            objectives=[
                "Understand the concept of diversity.",
                "Recognize the importance of inclusion.",
                "Appreciate different cultures and perspectives."
            ],
            materials=[
                "Diversity and Inclusion quotes handout",
                "Art supplies for group activity",
                "Projector for video presentation"
            ]
        )

        # Add activities to the lesson plan
        lesson.add_activity({
            "name": "Group Discussion",
            "description": "Discuss the meaning of diversity and inclusion using quotes from the 'Vivir es Convivir' program."
        })
        lesson.add_activity({
            "name": "Art Project",
            "description": "Create a mural that represents diversity in our community."
        })
        lesson.add_activity({
            "name": "Video Presentation",
            "description": "Watch a short video that highlights the value of inclusion."
        })

        # Display the complete lesson plan
        lesson.display_plan()

    except Exception as e:
        print(f"An error occurred: {e}")
```
