"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://globalchainsas.com
Prompt: Generate a script to track and manage the execution timelines of industrial projects, ensuring compliance with specifications and quality standards, as emphasized by GlobalChain SAS.
Generated: DETERMINISTIC_da45729dc9de0cfb
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime


class Project:
    """
    Class to represent an industrial project and track its execution timeline.
    """

    def __init__(self, project_name, start_date, end_date, specs, quality_standards):
        """
        Initialize a new project instance.

        :param project_name: Name of the project
        :param start_date: Project start date (YYYY-MM-DD format)
        :param end_date: Project end date (YYYY-MM-DD format)
        :param specs: Specifications required for the project
        :param quality_standards: Quality standards required for the project
        """
        self.project_name = project_name
        try:
            self.start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
            self.end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")
        except ValueError as e:
            raise ValueError("Invalid date format. Use YYYY-MM-DD.") from e
        if self.start_date >= self.end_date:
            raise ValueError("End date must be after start date.")
        self.specs = specs
        self.quality_standards = quality_standards
        self.status = "Not Started"  # Status can be 'Not Started', 'In Progress', or 'Completed'

    def update_status(self, new_status):
        """
        Update the status of the project.

        :param new_status: New status of the project (e.g., 'In Progress', 'Completed')
        """
        allowed_statuses = {"Not Started", "In Progress", "Completed"}
        if new_status not in allowed_statuses:
            raise ValueError(f"Invalid status. Allowed statuses: {allowed_statuses}")
        self.status = new_status

    def is_on_schedule(self):
        """
        Check if the project is on schedule based on current date.

        :return: True if project is on schedule, False otherwise
        """
        now = datetime.datetime.now()
        if self.status == "Completed":
            return self.end_date >= now
        elif self.status == "In Progress":
            return now <= self.end_date
        return True

    def check_compliance(self):
        """
        Check compliance with specifications and quality standards.

        :return: True if compliant, False otherwise
        """
        # Placeholder logic for compliance checks.
        # In production, detailed logic based on `specs` and `quality_standards` should be implemented.
        if not self.specs or not self.quality_standards:
            return False
        return True

    def __str__(self):
        """
        String representation of the project.

        :return: Formatted string with project details
        """
        return (
            f"Project Name: {self.project_name}\n"
            f"Start Date: {self.start_date.strftime('%Y-%m-%d')}\n"
            f"End Date: {self.end_date.strftime('%Y-%m-%d')}\n"
            f"Status: {self.status}\n"
            f"Specifications: {self.specs}\n"
            f"Quality Standards: {self.quality_standards}\n"
            f"On Schedule: {'Yes' if self.is_on_schedule() else 'No'}\n"
            f"Compliance: {'Yes' if self.check_compliance() else 'No'}"
        )


def main():
    """
    Main function to demonstrate the tracking and managing of industrial projects.
    """
    try:
        # Create a sample project
        project = Project(
            project_name="GlobalChain SAS - Warehouse Expansion",
            start_date="2023-01-01",
            end_date="2023-12-31",
            specs={"materials": "steel, concrete", "capacity": "500,000 tons"},
            quality_standards={"ISO": "9001", "Safety": "OSHA"},
        )

        # Print project details
        print(project)

        # Simulate status update
        project.update_status("In Progress")
        print("\nAfter status update:")
        print(project)

        # Simulate completion
        project.update_status("Completed")
        print("\nAfter project completion:")
        print(project)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
