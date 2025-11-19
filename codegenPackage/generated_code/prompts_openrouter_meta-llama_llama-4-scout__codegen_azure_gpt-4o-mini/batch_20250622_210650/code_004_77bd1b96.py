"""
Generated Code Metadata:
========================
Original URL: https://dfivetechnologies.com
Prompt: "Create a technical training plan for application development and test automation skills based on DFIVE Technologies' experience-based training approach."
Generated: DETERMINISTIC_77bd1b968a3f03c2
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class TrainingPlan:
    """
    A class to represent a technical training plan for application development and test automation skills.
    """

    def __init__(self, company_name):
        """
        Initializes the training plan with the company name.

        Args:
            company_name (str): The name of the company providing the training.
        """
        self.company_name = company_name
        self.modules = []

    def add_module(self, module_name, duration, description):
        """
        Adds a training module to the plan.

        Args:
            module_name (str): The name of the training module.
            duration (int): The duration of the module in hours.
            description (str): A brief description of the module.

        Raises:
            ValueError: If duration is not a positive integer.
        """
        if not isinstance(duration, int) or duration <= 0:
            raise ValueError("Duration must be a positive integer.")
        
        module = {
            'name': module_name,
            'duration': duration,
            'description': description
        }
        self.modules.append(module)

    def generate_plan(self):
        """
        Generates a formatted training plan.

        Returns:
            str: A string representation of the training plan.
        """
        plan = f"Training Plan for {self.company_name}\n"
        plan += "=" * (len(plan) - 1) + "\n"
        for module in self.modules:
            plan += f"Module: {module['name']}\n"
            plan += f"Duration: {module['duration']} hours\n"
            plan += f"Description: {module['description']}\n"
            plan += "-" * 40 + "\n"
        return plan.strip()

# Example usage
if __name__ == "__main__":
    try:
        training_plan = TrainingPlan("DFIVE Technologies")
        training_plan.add_module("Introduction to Application Development", 10, "Basics of application development.")
        training_plan.add_module("Advanced Test Automation", 8, "In-depth techniques for test automation.")
        training_plan.add_module("Agile Methodologies", 6, "Understanding Agile principles and practices.")
        
        print(training_plan.generate_plan())
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
