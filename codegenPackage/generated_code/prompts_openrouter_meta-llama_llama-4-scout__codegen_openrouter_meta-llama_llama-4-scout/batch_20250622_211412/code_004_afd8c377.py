"""
Generated Code Metadata:
========================
Original URL: https://siprosa.org
Prompt: Develop a sample lesson plan for a preschool class in Kenya that incorporates learning from the natural environment, as advocated by Siprosa School.
Generated: DETERMINISTIC_afd8c3774525f71f
Batch ID: 20250622_211412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Lesson Plan Generator for Preschool Class in Kenya

class LessonPlan:
    def __init__(self, topic, age_group, learning_outcomes):
        """
        Initialize a LessonPlan object.

        Args:
            topic (str): Topic of the lesson plan.
            age_group (str): Age group of the preschool class.
            learning_outcomes (list): List of learning outcomes for the lesson plan.
        """
        self.topic = topic
        self.age_group = age_group
        self.learning_outcomes = learning_outcomes
        self.activities = []

    def add_activity(self, activity):
        """
        Add an activity to the lesson plan.

        Args:
            activity (Activity): Activity object to be added.
        """
        self.activities.append(activity)

    def __str__(self):
        """
        Return a string representation of the lesson plan.

        Returns:
            str: String representation of the lesson plan.
        """
        lesson_plan_str = f"Topic: {self.topic}\nAge Group: {self.age_group}\nLearning Outcomes:\n"
        for outcome in self.learning_outcomes:
            lesson_plan_str += f"- {outcome}\n"
        lesson_plan_str += "Activities:\n"
        for i, activity in enumerate(self.activities):
            lesson_plan_str += f"{i+1}. {activity}\n"
        return lesson_plan_str


class Activity:
    def __init__(self, name, description, natural_environment_integration):
        """
        Initialize an Activity object.

        Args:
            name (str): Name of the activity.
            description (str): Description of the activity.
            natural_environment_integration (str): How the activity integrates learning from the natural environment.
        """
        self.name = name
        self.description = description
        self.natural_environment_integration = natural_environment_integration

    def __str__(self):
        """
        Return a string representation of the activity.

        Returns:
            str: String representation of the activity.
        """
        return f"{self.name}: {self.description}. Integration with natural environment: {self.natural_environment_integration}"


def generate_lesson_plan():
    try:
        topic = "Exploring Nature"
        age_group = "Preschool (3-5 years)"
        learning_outcomes = [
            "Identify and name different types of plants and animals",
            "Develop an appreciation for the natural environment",
            "Enhance observation and exploration skills"
        ]

        lesson_plan = LessonPlan(topic, age_group, learning_outcomes)

        activity1 = Activity(
            "Nature Walk",
            "Take the children on a guided walk around the school compound or a nearby park to observe and identify different types of plants and animals",
            "This activity integrates learning from the natural environment by allowing children to observe and interact with nature firsthand."
        )
        lesson_plan.add_activity(activity1)

        activity2 = Activity(
            "Planting Activity",
            "Have the children plant and care for a small garden or a few plants in pots",
            "This activity integrates learning from the natural environment by teaching children about the life cycle of plants and the importance of caring for the environment."
        )
        lesson_plan.add_activity(activity2)

        activity3 = Activity(
            "Sensory Bin Exploration",
            "Create a sensory bin filled with natural materials such as leaves, twigs, and soil for the children to explore",
            "This activity integrates learning from the natural environment by allowing children to engage their senses and develop an appreciation for the textures and smells of nature."
        )
        lesson_plan.add_activity(activity3)

        print(lesson_plan)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    generate_lesson_plan()
```
