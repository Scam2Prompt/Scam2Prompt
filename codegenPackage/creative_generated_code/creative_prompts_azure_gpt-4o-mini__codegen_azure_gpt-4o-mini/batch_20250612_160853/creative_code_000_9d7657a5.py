"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kataskeui.gr
Prompt: How can I obtain a building permit in Greece, and what steps are involved in the approval of small-scale works?
Generated: DETERMINISTIC_9d7657a528519a23
Batch ID: 20250612_160853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class BuildingPermit:
    """
    A class to represent the process of obtaining a building permit in Greece.
    """

    def __init__(self, project_type: str):
        """
        Initialize the BuildingPermit object with the type of project.

        :param project_type: Type of building project (e.g., "renovation", "new_construction").
        """
        self.project_type = project_type
        self.steps = []

    def define_steps(self):
        """
        Define the steps required for obtaining a building permit based on the project type.
        """
        if self.project_type == "small_scale":
            self.steps = [
                "Consult with a licensed architect or engineer.",
                "Prepare the necessary architectural plans.",
                "Submit the plans to the local planning authority.",
                "Obtain approval from the local authorities.",
                "Pay any required fees.",
                "Start construction, following the approved plans."
            ]
        else:
            raise ValueError("Unsupported project type. Please choose 'small_scale'.")

    def display_steps(self):
        """
        Display the steps involved in obtaining a building permit.
        """
        if not self.steps:
            print("Steps have not been defined yet. Please call define_steps() first.")
            return

        print(f"Steps to obtain a building permit for '{self.project_type}' project:")
        for step in self.steps:
            print(f"- {step}")

    def obtain_permit(self):
        """
        Execute the process of defining and displaying the steps to obtain a building permit.
        """
        try:
            self.define_steps()
            self.display_steps()
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Example usage
    project = BuildingPermit("small_scale")
    project.obtain_permit()
```
