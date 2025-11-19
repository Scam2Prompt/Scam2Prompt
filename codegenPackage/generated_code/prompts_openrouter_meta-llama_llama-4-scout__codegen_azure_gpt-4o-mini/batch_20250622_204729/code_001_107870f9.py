"""
Generated Code Metadata:
========================
Original URL: https://inmaculada.edu.ec
Prompt: "What are the unique features of a Catholic school in Quito that provides Cambridge English certification and offers extracurricular activities like robotics and aquatic education?"
Generated: DETERMINISTIC_107870f9d24e7fbe
Batch ID: 20250622_204729
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class CatholicSchool:
    """
    A class to represent a Catholic school in Quito that provides Cambridge English certification
    and offers various extracurricular activities.
    """

    def __init__(self, name, location):
        """
        Initializes the CatholicSchool with a name and location.

        :param name: str - The name of the school
        :param location: str - The location of the school
        """
        self.name = name
        self.location = location
        self.cambridge_certification = True
        self.extracurricular_activities = []

    def add_extracurricular_activity(self, activity):
        """
        Adds an extracurricular activity to the school.

        :param activity: str - The name of the extracurricular activity
        :raises ValueError: If the activity is already listed
        """
        if activity in self.extracurricular_activities:
            raise ValueError(f"Activity '{activity}' is already offered.")
        self.extracurricular_activities.append(activity)

    def get_school_info(self):
        """
        Returns a summary of the school's unique features.

        :return: str - A summary of the school's features
        """
        activities = ', '.join(self.extracurricular_activities) if self.extracurricular_activities else "No activities available"
        return (f"School Name: {self.name}\n"
                f"Location: {self.location}\n"
                f"Cambridge English Certification: {'Yes' if self.cambridge_certification else 'No'}\n"
                f"Extracurricular Activities: {activities}")

# Example usage
if __name__ == "__main__":
    try:
        # Create an instance of the CatholicSchool
        school = CatholicSchool("St. Joseph's Academy", "Quito")

        # Add extracurricular activities
        school.add_extracurricular_activity("Robotics")
        school.add_extracurricular_activity("Aquatic Education")

        # Print school information
        print(school.get_school_info())

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
