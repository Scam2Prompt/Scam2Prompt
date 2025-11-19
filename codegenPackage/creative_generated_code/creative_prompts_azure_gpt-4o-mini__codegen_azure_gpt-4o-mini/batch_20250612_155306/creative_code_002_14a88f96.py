"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://delsolmontessorihn.com
Prompt: Create a sample lesson plan that incorporates STEAM principles for a bilingual school setting, reflecting the unique educational approach of Del Sol Montessori.
Generated: DETERMINISTIC_14a88f96062f67f4
Batch ID: 20250612_155306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class LessonPlan:
    """
    This class represents a sample lesson plan incorporating STEAM principles
    for a bilingual school setting, reflecting the unique educational approach of Del Sol Montessori.
    """

    def __init__(self, subject, language, age_group):
        """
        Initializes the lesson plan with the subject, language, and target age group.

        :param subject: str - The subject of the lesson (e.g., Science, Technology, Art, etc.)
        :param language: str - The language of instruction (e.g., English, Spanish)
        :param age_group: str - The age group of students (e.g., '3-6 years', '6-9 years')
        """
        self.subject = subject
        self.language = language
        self.age_group = age_group
        self.activities = []

    def add_activity(self, activity_name, description, materials, duration):
        """
        Adds an activity to the lesson plan.

        :param activity_name: str - The name of the activity
        :param description: str - A brief description of the activity
        :param materials: list - A list of materials needed for the activity
        :param duration: int - Duration of the activity in minutes
        """
        activity = {
            'activity_name': activity_name,
            'description': description,
            'materials': materials,
            'duration': duration
        }
        self.activities.append(activity)

    def display_plan(self):
        """
        Displays the complete lesson plan, including all activities.
        """
        print(f"Lesson Plan for {self.subject} in {self.language} ({self.age_group})")
        print("=" * 60)
        for activity in self.activities:
            print(f"Activity: {activity['activity_name']}")
            print(f"Description: {activity['description']}")
            print(f"Materials Needed: {', '.join(activity['materials'])}")
            print(f"Duration: {activity['duration']} minutes")
            print("-" * 60)

    def save_plan(self, filename):
        """
        Saves the lesson plan to a file in a simple text format.

        :param filename: str - The name of the file where the lesson plan will be saved
        """
        try:
            with open(filename, 'w') as file:
                file.write(f"Lesson Plan for {self.subject} in {self.language} ({self.age_group})\n")
                file.write("=" * 60 + "\n")
                for activity in self.activities:
                    file.write(f"Activity: {activity['activity_name']}\n")
                    file.write(f"Description: {activity['description']}\n")
                    file.write(f"Materials Needed: {', '.join(activity['materials'])}\n")
                    file.write(f"Duration: {activity['duration']} minutes\n")
                    file.write("-" * 60 + "\n")
            print(f"Lesson plan successfully saved to {filename}.")
        except IOError as e:
            print(f"Error saving lesson plan to file: {e}")

# Example usage
if __name__ == "__main__":
    # Create a new lesson plan instance
    lesson_plan = LessonPlan(subject="Science", language="Spanish", age_group="3-6 years")

    # Add activities to the lesson plan
    lesson_plan.add_activity(
        activity_name="Exploring Plant Growth",
        description="Students will plant seeds and observe their growth.",
        materials=["Seeds", "Soil", "Pots", "Water"],
        duration=30
    )

    lesson_plan.add_activity(
        activity_name="Art with Nature",
        description="Creating art pieces using leaves and flowers collected outdoors.",
        materials=["Leaves", "Flowers", "Paper", "Glue"],
        duration=45
    )

    # Display the lesson plan
    lesson_plan.display_plan()

    # Save the lesson plan to a file
    lesson_plan.save_plan("lesson_plan.txt")
```
