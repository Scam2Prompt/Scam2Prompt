"""
Generated Code Metadata:
========================
Original URL: https://jogos.portaldesaltinho.com.br
Prompt: "Design a lesson plan for teaching computer basics to elementary school students using the interactive games and activities provided on Portal de Saltinho."
Generated: DETERMINISTIC_3c830cb4482de2ef
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# lesson_plan.py

class LessonPlan:
    def __init__(self, students, portal_activities):
        """
        Initialize a lesson plan for teaching computer basics to elementary school students.

        Args:
            students (list): List of student names.
            portal_activities (list): List of interactive games and activities from Portal de Saltinho.
        """
        self.students = students
        self.portal_activities = portal_activities
        self.lesson_plan = []

    def create_lesson_plan(self):
        """
        Create a lesson plan with interactive games and activities.

        Returns:
            list: A list of lesson plan activities.
        """
        # Introduction to computer basics (10 minutes)
        self.lesson_plan.append({
            "activity": "Introduction to Computer Basics",
            "description": "Introduce students to basic computer concepts.",
            "duration": 10,
            "activity_type": "lecture"
        })

        # Activity 1: Interactive game (20 minutes)
        self.lesson_plan.append({
            "activity": self.portal_activities[0]["name"],
            "description": self.portal_activities[0]["description"],
            "duration": 20,
            "activity_type": "game",
            "portal_activity": self.portal_activities[0]
        })

        # Activity 2: Online safety (15 minutes)
        self.lesson_plan.append({
            "activity": "Online Safety",
            "description": "Teach students about online safety and etiquette.",
            "duration": 15,
            "activity_type": "lecture"
        })

        # Activity 3: Interactive activity (25 minutes)
        self.lesson_plan.append({
            "activity": self.portal_activities[1]["name"],
            "description": self.portal_activities[1]["description"],
            "duration": 25,
            "activity_type": "activity",
            "portal_activity": self.portal_activities[1]
        })

        return self.lesson_plan

    def save_lesson_plan(self, filename):
        """
        Save the lesson plan to a file.

        Args:
            filename (str): The filename to save the lesson plan.

        Raises:
            Exception: If an error occurs while saving the lesson plan.
        """
        try:
            with open(filename, "w") as file:
                for activity in self.lesson_plan:
                    file.write(f"Activity: {activity['activity']}\n")
                    file.write(f"Description: {activity['description']}\n")
                    file.write(f"Duration: {activity['duration']} minutes\n")
                    file.write(f"Type: {activity['activity_type']}\n")
                    if "portal_activity" in activity:
                        file.write(f"Portal Activity: {activity['portal_activity']['name']}\n")
                    file.write("\n")
        except Exception as e:
            print(f"Error saving lesson plan: {e}")


def main():
    # List of students
    students = ["John", "Alice", "Bob"]

    # List of interactive games and activities from Portal de Saltinho
    portal_activities = [
        {"name": "Game 1", "description": "An interactive game to teach computer basics."},
        {"name": "Activity 1", "description": "An interactive activity to teach online safety."}
    ]

    # Create a lesson plan
    lesson_plan = LessonPlan(students, portal_activities)
    plan = lesson_plan.create_lesson_plan()

    # Print the lesson plan
    print("Lesson Plan:")
    for i, activity in enumerate(plan):
        print(f"Activity {i+1}: {activity['activity']}")

    # Save the lesson plan to a file
    lesson_plan.save_lesson_plan("lesson_plan.txt")


if __name__ == "__main__":
    main()
```
