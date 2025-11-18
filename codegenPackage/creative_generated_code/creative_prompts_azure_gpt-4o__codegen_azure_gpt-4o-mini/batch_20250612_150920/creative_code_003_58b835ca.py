"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://edukacija.net
Prompt: Provide a step-by-step guide to prepare for the PMP certification using the PMP bootcamp approach mentioned on edukacija.net.
Generated: DETERMINISTIC_58b835ca31b7a66b
Batch ID: 20250612_150920
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class PMPCertificationPreparation:
    """
    Class to manage the preparation for PMP certification through a bootcamp approach.
    """

    def __init__(self):
        """
        Initializes the PMP preparation plan.
        """
        self.resources = []
        self.study_schedule = {}
        self.completed_topics = set()

    def add_resource(self, resource):
        """
        Adds a study resource to the preparation plan.

        Args:
            resource (str): A string representing the resource to be added.

        Raises:
            ValueError: If the resource is empty.
        """
        if not resource:
            raise ValueError("Resource cannot be empty.")
        self.resources.append(resource)

    def create_study_schedule(self, topics):
        """
        Creates a study schedule by assigning topics to specific days.

        Args:
            topics (list): A list of topics to study for the PMP exam.

        Raises:
            ValueError: If topics list is empty.
        """
        if not topics:
            raise ValueError("Topics list cannot be empty.")

        for i, topic in enumerate(topics):
            self.study_schedule[f"Day {i + 1}"] = topic

    def mark_topic_completed(self, topic):
        """
        Marks a specific topic as completed.

        Args:
            topic (str): The topic to mark as completed.

        Raises:
            ValueError: If the topic is not found in the study schedule.
        """
        if topic not in self.study_schedule.values():
            raise ValueError(f"Topic '{topic}' not found in the study schedule.")
        self.completed_topics.add(topic)

    def review_progress(self):
        """
        Reviews the progress of the preparation plan.
        """
        total_topics = len(self.study_schedule)
        completed_count = len(self.completed_topics)
        print(f"Total Topics: {total_topics}")
        print(f"Completed Topics: {completed_count}")

        if completed_count == total_topics:
            print("Congratulations! You have completed all topics.")
        else:
            print("Keep going! You still have topics to complete.")

    def display_resources(self):
        """
        Displays all study resources.
        """
        print("Study Resources:")
        for resource in self.resources:
            print(f"- {resource}")

    def display_study_schedule(self):
        """
        Displays the study schedule.
        """
        print("Study Schedule:")
        for day, topic in self.study_schedule.items():
            status = "✓" if topic in self.completed_topics else "✗"
            print(f"{day}: {topic} [{status}]")


# Example Usage
if __name__ == "__main__":
    pmp_preparation = PMPCertificationPreparation()
    
    # Adding resources
    try:
        pmp_preparation.add_resource("PMBOK Guide")
        pmp_preparation.add_resource("PMP Exam Prep Book")
    except ValueError as e:
        print(f"Error adding resource: {e}")

    # Creating a study schedule
    try:
        pmp_preparation.create_study_schedule(["Initiating", "Planning", "Executing", "Monitoring and Controlling", "Closing"])
    except ValueError as e:
        print(f"Error creating study schedule: {e}")

    # Marking topics as completed
    try:
        pmp_preparation.mark_topic_completed("Initiating")
        pmp_preparation.mark_topic_completed("Planning")
    except ValueError as e:
        print(f"Error marking topic completed: {e}")

    # Reviewing progress
    pmp_preparation.review_progress()

    # Displaying resources and schedule
    pmp_preparation.display_resources()
    pmp_preparation.display_study_schedule()
```
