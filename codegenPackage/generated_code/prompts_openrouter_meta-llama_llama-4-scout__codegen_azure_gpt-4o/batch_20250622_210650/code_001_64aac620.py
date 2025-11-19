"""
Generated Code Metadata:
========================
Original URL: https://sstco.ma
Prompt: Generate a Python script to manage construction projects, including tracking progress, deadlines, and resources, inspired by SSTCO's project management approach.
Generated: DETERMINISTIC_64aac620b8ceb12a
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime


class ConstructionProject:
    """
    A class to represent a construction project.
    """

    def __init__(self, name, deadline, resources):
        """
        Initialize a construction project.

        :param name: Name of the project
        :param deadline: Deadline for the project (datetime object)
        :param resources: List of resources allocated to the project
        """
        self.name = name
        self.deadline = deadline
        self.resources = resources
        self.progress = 0  # Progress in percentage (0-100)

    def update_progress(self, progress):
        """
        Update the progress of the project.

        :param progress: Progress percentage (0-100)
        :raises ValueError: If progress is not between 0 and 100
        """
        if not (0 <= progress <= 100):
            raise ValueError("Progress must be between 0 and 100.")
        self.progress = progress

    def add_resource(self, resource):
        """
        Add a resource to the project.

        :param resource: Resource to be added
        """
        self.resources.append(resource)

    def remove_resource(self, resource):
        """
        Remove a resource from the project.

        :param resource: Resource to be removed
        :raises ValueError: If the resource is not found in the list
        """
        if resource not in self.resources:
            raise ValueError(f"Resource '{resource}' not found in the project.")
        self.resources.remove(resource)

    def is_on_track(self):
        """
        Check if the project is on track based on the deadline and progress.

        :return: True if the project is on track, False otherwise
        """
        days_remaining = (self.deadline - datetime.datetime.now()).days
        # Assuming progress should be proportional to time remaining
        expected_progress = max(0, 100 - (days_remaining / (self.deadline - datetime.datetime.now()).days) * 100)
        return self.progress >= expected_progress

    def __str__(self):
        """
        Return a string representation of the project.

        :return: String representation of the project
        """
        return (f"Project Name: {self.name}\n"
                f"Deadline: {self.deadline.strftime('%Y-%m-%d')}\n"
                f"Progress: {self.progress}%\n"
                f"Resources: {', '.join(self.resources)}")


def main():
    """
    Main function to demonstrate the functionality of the ConstructionProject class.
    """
    try:
        # Create a new project
        project = ConstructionProject(
            name="Building A",
            deadline=datetime.datetime(2023, 12, 31),
            resources=["Excavator", "Crane", "Concrete Mixer"]
        )

        print("Initial Project Details:")
        print(project)

        # Update progress
        project.update_progress(30)
        print("\nUpdated Progress:")
        print(project)

        # Add a new resource
        project.add_resource("Safety Gear")
        print("\nAdded Resource:")
        print(project)

        # Remove a resource
        project.remove_resource("Crane")
        print("\nRemoved Resource:")
        print(project)

        # Check if the project is on track
        print("\nIs the project on track?")
        print("Yes" if project.is_on_track() else "No")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
