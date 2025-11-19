"""
Generated Code Metadata:
========================
Original URL: https://realorigin.org
Prompt: "Explain the importance of regular roof maintenance for extending its lifespan and avoiding costly repairs, including essential tasks like cleaning and inspecting."
Generated: DETERMINISTIC_4fae14d93179e355
Batch ID: 20250622_212122
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class RoofMaintenance:
    """
    A class to represent roof maintenance tasks and their importance in extending the lifespan of a roof.
    """

    def __init__(self, roof_age: int):
        """
        Initializes the RoofMaintenance class with the age of the roof.

        :param roof_age: Age of the roof in years
        """
        if roof_age < 0:
            raise ValueError("Roof age cannot be negative.")
        self.roof_age = roof_age
        self.tasks = [
            "Clean gutters and downspouts",
            "Inspect for missing or damaged shingles",
            "Check for signs of leaks or water damage",
            "Trim overhanging branches",
            "Inspect flashing and seals",
            "Remove debris from the roof surface"
        ]

    def perform_maintenance(self):
        """
        Performs essential maintenance tasks on the roof.
        """
        print(f"Performing maintenance on a {self.roof_age}-year-old roof.")
        for task in self.tasks:
            self._perform_task(task)

    def _perform_task(self, task: str):
        """
        Simulates performing a maintenance task.

        :param task: The maintenance task to perform
        """
        try:
            print(f"Task: {task} - Completed.")
        except Exception as e:
            print(f"Error performing task '{task}': {e}")

    def importance_of_maintenance(self):
        """
        Explains the importance of regular roof maintenance.
        """
        print("Importance of Regular Roof Maintenance:")
        print("- Extends the lifespan of the roof.")
        print("- Prevents costly repairs by identifying issues early.")
        print("- Maintains the aesthetic appeal of the home.")
        print("- Ensures proper drainage and prevents water damage.")
        print("- Enhances energy efficiency by preventing leaks.")

if __name__ == "__main__":
    try:
        # Example usage
        roof = RoofMaintenance(10)  # Create a RoofMaintenance instance for a 10-year-old roof
        roof.perform_maintenance()   # Perform maintenance tasks
        roof.importance_of_maintenance()  # Explain the importance of maintenance
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
