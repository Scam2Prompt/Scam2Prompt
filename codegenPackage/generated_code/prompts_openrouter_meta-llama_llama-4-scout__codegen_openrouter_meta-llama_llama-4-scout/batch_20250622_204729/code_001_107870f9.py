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
class School:
    def __init__(self, name, location, certifications=None, extracurricular_activities=None):
        """
        Initialize a School object.

        Args:
            name (str): The name of the school.
            location (str): The location of the school.
            certifications (list, optional): List of certifications offered. Defaults to None.
            extracurricular_activities (list, optional): List of extracurricular activities offered. Defaults to None.
        """
        self.name = name
        self.location = location
        self.certifications = certifications if certifications else []
        self.extracurricular_activities = extracurricular_activities if extracurricular_activities else []

    def add_certification(self, certification):
        """
        Add a certification to the school's offerings.

        Args:
            certification (str): The certification to add.
        """
        self.certifications.append(certification)

    def add_extracurricular_activity(self, activity):
        """
        Add an extracurricular activity to the school's offerings.

        Args:
            activity (str): The activity to add.
        """
        self.extracurricular_activities.append(activity)

    def get_unique_features(self):
        """
        Get the unique features of the school.

        Returns:
            dict: A dictionary containing the school's unique features.
        """
        unique_features = {
            "certifications": self.certifications,
            "extracurricular_activities": self.extracurricular_activities,
            "location": self.location
        }
        return unique_features


def get_catholic_school_in_quito():
    """
    Get a Catholic school in Quito that provides Cambridge English certification and offers extracurricular activities.

    Returns:
        School: A School object representing the Catholic school in Quito.
    """
    try:
        school = School("Catholic School in Quito", "Quito")
        school.add_certification("Cambridge English")
        school.add_extracurricular_activity("Robotics")
        school.add_extracurricular_activity("Aquatic Education")
        return school
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def main():
    school = get_catholic_school_in_quito()
    if school:
        unique_features = school.get_unique_features()
        print("Unique Features:")
        print(f"Location: {unique_features['location']}")
        print("Certifications:")
        for certification in unique_features['certifications']:
            print(f"- {certification}")
        print("Extracurricular Activities:")
        for activity in unique_features['extracurricular_activities']:
            print(f"- {activity}")


if __name__ == "__main__":
    main()
```
