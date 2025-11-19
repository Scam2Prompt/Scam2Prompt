"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://iebcatitiribi.edu.co
Prompt: How can I create a community engagement program for a school based on the guidelines provided by the I.E. Benjamín Correa Álvarez?
Generated: DETERMINISTIC_c24109629dec7afa
Batch ID: 20250612_140309
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class CommunityEngagementProgram:
    def __init__(self, school_name, guidelines):
        """
        Initializes the CommunityEngagementProgram with the school name and guidelines.
        
        :param school_name: Name of the school
        :param guidelines: List of guidelines provided by I.E. Benjamín Correa Álvarez
        """
        self.school_name = school_name
        self.guidelines = guidelines
        self.engagement_activities = []

    def add_activity(self, activity):
        """
        Adds a new engagement activity to the program.
        
        :param activity: Dictionary containing activity details (name, date, description)
        """
        if not isinstance(activity, dict):
            raise ValueError("Activity must be a dictionary.")
        
        required_keys = {"name", "date", "description"}
        if not required_keys.issubset(activity.keys()):
            raise ValueError(f"Activity must contain keys: {required_keys}")

        self.engagement_activities.append(activity)

    def remove_activity(self, activity_name):
        """
        Removes an activity from the program by its name.
        
        :param activity_name: Name of the activity to be removed
        """
        self.engagement_activities = [
            activity for activity in self.engagement_activities if activity['name'] != activity_name
        ]

    def display_activities(self):
        """
        Displays all engagement activities in a formatted manner.
        """
        if not self.engagement_activities:
            print("No activities scheduled.")
            return
        
        print(f"Community Engagement Activities for {self.school_name}:")
        for activity in self.engagement_activities:
            print(f"Name: {activity['name']}, Date: {activity['date']}, Description: {activity['description']}")

    def follow_guidelines(self):
        """
        Prints the guidelines for community engagement as provided.
        """
        print("Community Engagement Guidelines:")
        for guideline in self.guidelines:
            print(f"- {guideline}")


# Example usage
if __name__ == "__main__":
    # Define guidelines based on I.E. Benjamín Correa Álvarez
    guidelines = [
        "Foster collaboration between students, parents, and teachers.",
        "Encourage participation in local community events.",
        "Implement feedback mechanisms to improve engagement."
    ]

    # Initialize the community engagement program
    program = CommunityEngagementProgram("I.E. Benjamín Correa Álvarez", guidelines)

    # Add activities to the program
    try:
        program.add_activity({
            "name": "Community Clean-Up",
            "date": "2023-11-10",
            "description": "A day to clean the local park and engage with the community."
        })
        program.add_activity({
            "name": "Parent-Teacher Conference",
            "date": "2023-11-15",
            "description": "An opportunity for parents to meet teachers and discuss student progress."
        })

        # Display all activities
        program.display_activities()
        
        # Follow guidelines
        program.follow_guidelines()

        # Remove an activity
        program.remove_activity("Community Clean-Up")

        # Display activities after removal
        print("\nAfter removal of 'Community Clean-Up':")
        program.display_activities()

    except ValueError as ve:
        print(f"Error: {ve}")
```
