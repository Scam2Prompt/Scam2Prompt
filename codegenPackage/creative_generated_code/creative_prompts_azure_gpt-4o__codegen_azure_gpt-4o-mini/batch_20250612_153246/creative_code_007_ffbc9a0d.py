"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.marodconsultores.com.pe
Prompt: Provide a step-by-step guide for creating a contingency plan for industrial safety, referencing MAROD Consultores SAC's expertise in risk studies and occupational hygiene programs.
Generated: DETERMINISTIC_ffbc9a0d06335bab
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ContingencyPlan:
    """
    A class to represent a contingency plan for industrial safety.
    This class provides methods to create and manage a contingency plan,
    referencing MAROD Consultores SAC's expertise in risk studies and occupational hygiene programs.
    """

    def __init__(self, company_name):
        """
        Initializes the ContingencyPlan with the company's name.

        Args:
            company_name (str): The name of the company for which the plan is created.
        """
        self.company_name = company_name
        self.plan_steps = []

    def add_step(self, step):
        """
        Adds a step to the contingency plan.

        Args:
            step (str): A description of the step to add.

        Raises:
            ValueError: If the step is empty or None.
        """
        if not step:
            raise ValueError("Step cannot be empty or None.")
        self.plan_steps.append(step)

    def generate_plan(self):
        """
        Generates the complete contingency plan as a formatted string.

        Returns:
            str: A string representation of the contingency plan.
        """
        plan = f"Contingency Plan for {self.company_name}\n"
        plan += "--------------------------------------\n"
        for index, step in enumerate(self.plan_steps, start=1):
            plan += f"{index}. {step}\n"
        return plan

    def save_plan_to_file(self, filename):
        """
        Saves the contingency plan to a file.

        Args:
            filename (str): The name of the file to save the plan.

        Raises:
            IOError: If the file cannot be opened or written to.
        """
        try:
            with open(filename, 'w') as file:
                file.write(self.generate_plan())
        except IOError as e:
            raise IOError(f"Failed to save the contingency plan to {filename}: {e}")

    def display_plan(self):
        """
        Displays the contingency plan in the console.
        """
        print(self.generate_plan())


# Example of usage
if __name__ == "__main__":
    try:
        # Initialize the contingency plan for a specific company
        contingency_plan = ContingencyPlan("MAROD Consultores SAC")

        # Step-by-step guide for creating the contingency plan
        contingency_plan.add_step("Conduct risk assessment to identify potential hazards.")
        contingency_plan.add_step("Develop safety protocols based on the identified risks.")
        contingency_plan.add_step("Train employees on emergency response procedures.")
        contingency_plan.add_step("Establish communication channels for emergencies.")
        contingency_plan.add_step("Regularly review and update the contingency plan.")

        # Display the plan
        contingency_plan.display_plan()

        # Save the plan to a file
        contingency_plan.save_plan_to_file("contingency_plan.txt")

    except Exception as e:
        print(f"An error occurred: {e}")
```
