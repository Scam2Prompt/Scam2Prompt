"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://complyaml.com
Prompt: Create a training plan breakdown for AML compliance that includes beginner-friendly modules and certification options.
Generated: DETERMINISTIC_9fce64d8e51a6108
Batch ID: 20250612_135717
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class AMLTrainingPlan:
    """
    A class to represent a training plan for Anti-Money Laundering (AML) compliance.
    This training plan includes beginner-friendly modules and certification options.
    """

    def __init__(self):
        """Initialize the AMLTrainingPlan with modules and certifications."""
        self.modules = []
        self.certifications = []

    def add_module(self, title, description, duration):
        """
        Add a training module to the AML plan.

        Args:
            title (str): The title of the training module.
            description (str): A brief description of the module.
            duration (int): The duration of the module in hours.

        Raises:
            ValueError: If the duration is not a positive number.
        """
        if duration <= 0:
            raise ValueError("Duration must be a positive number.")
        
        module = {
            'title': title,
            'description': description,
            'duration': duration
        }
        self.modules.append(module)

    def add_certification(self, title, provider, cost):
        """
        Add a certification option to the AML plan.

        Args:
            title (str): The title of the certification.
            provider (str): The organization providing the certification.
            cost (float): The cost of the certification.

        Raises:
            ValueError: If the cost is not a non-negative number.
        """
        if cost < 0:
            raise ValueError("Cost must be a non-negative number.")
        
        certification = {
            'title': title,
            'provider': provider,
            'cost': cost
        }
        self.certifications.append(certification)

    def get_training_plan(self):
        """
        Retrieve the complete training plan including modules and certifications.

        Returns:
            dict: A dictionary containing modules and certifications.
        """
        return {
            'modules': self.modules,
            'certifications': self.certifications
        }

    def display_training_plan(self):
        """
        Print the training plan in a readable format.
        """
        training_plan = self.get_training_plan()
        
        print("AML Training Plan:")
        print("\nModules:")
        for module in training_plan['modules']:
            print(f"- {module['title']}: {module['description']} (Duration: {module['duration']} hours)")
        
        print("\nCertifications:")
        for cert in training_plan['certifications']:
            print(f"- {cert['title']} by {cert['provider']} (Cost: ${cert['cost']:.2f})")

# Example usage
if __name__ == "__main__":
    try:
        aml_training = AMLTrainingPlan()
        
        # Adding beginner-friendly modules
        aml_training.add_module("Introduction to AML", "Overview of AML regulations and importance.", 2)
        aml_training.add_module("Identifying Money Laundering", "Learn how to identify signs of money laundering.", 3)
        aml_training.add_module("AML Reporting Procedures", "Understand the reporting responsibilities.", 2)

        # Adding certification options
        aml_training.add_certification("Certified Anti-Money Laundering Specialist (CAMS)", "ACAMS", 1295)
        aml_training.add_certification("Anti-Money Laundering Certification", "ACFE", 600)

        # Display the training plan
        aml_training.display_training_plan()

    except ValueError as e:
        print(f"Error: {e}")
```
