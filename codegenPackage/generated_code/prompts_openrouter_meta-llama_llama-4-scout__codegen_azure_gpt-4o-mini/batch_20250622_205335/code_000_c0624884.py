"""
Generated Code Metadata:
========================
Original URL: https://complyaml.com
Prompt: Write a Python script to generate a customized AML training plan for a small corporate client in the finance industry using ComplyAML's interactive training modules.
Generated: DETERMINISTIC_c062488497a1acb2
Batch ID: 20250622_205335
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import random
from typing import List, Dict

class TrainingModule:
    """Class representing a training module for AML compliance."""
    
    def __init__(self, title: str, duration: int, level: str):
        """
        Initialize a training module.

        :param title: Title of the training module
        :param duration: Duration of the module in minutes
        :param level: Difficulty level of the module (e.g., 'beginner', 'intermediate', 'advanced')
        """
        self.title = title
        self.duration = duration
        self.level = level

    def to_dict(self) -> Dict:
        """Convert the training module to a dictionary."""
        return {
            "title": self.title,
            "duration": self.duration,
            "level": self.level
        }

class TrainingPlan:
    """Class to generate a customized AML training plan."""
    
    def __init__(self, client_name: str):
        """
        Initialize a training plan for a specific client.

        :param client_name: Name of the corporate client
        """
        self.client_name = client_name
        self.modules: List[TrainingModule] = []

    def add_module(self, module: TrainingModule):
        """Add a training module to the plan."""
        self.modules.append(module)

    def generate_plan(self) -> Dict:
        """Generate the training plan as a dictionary."""
        return {
            "client_name": self.client_name,
            "modules": [module.to_dict() for module in self.modules]
        }

    def save_plan(self, filename: str):
        """Save the training plan to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump(self.generate_plan(), file, indent=4)
            print(f"Training plan saved to {filename}")
        except IOError as e:
            print(f"Error saving training plan: {e}")

def create_training_modules() -> List[TrainingModule]:
    """Create a list of available training modules."""
    return [
        TrainingModule("Introduction to AML", 30, "beginner"),
        TrainingModule("AML Regulations Overview", 45, "intermediate"),
        TrainingModule("Risk Assessment Techniques", 60, "advanced"),
        TrainingModule("Transaction Monitoring", 50, "intermediate"),
        TrainingModule("Customer Due Diligence", 40, "beginner"),
        TrainingModule("AML Case Studies", 70, "advanced"),
    ]

def generate_custom_training_plan(client_name: str, num_modules: int) -> TrainingPlan:
    """
    Generate a customized AML training plan for a client.

    :param client_name: Name of the corporate client
    :param num_modules: Number of training modules to include in the plan
    :return: A TrainingPlan object
    """
    available_modules = create_training_modules()
    selected_modules = random.sample(available_modules, min(num_modules, len(available_modules)))

    training_plan = TrainingPlan(client_name)
    for module in selected_modules:
        training_plan.add_module(module)

    return training_plan

if __name__ == "__main__":
    # Example usage
    client_name = "ABC Finance Corp"
    num_modules = 3  # Number of modules to include in the training plan

    # Generate the training plan
    training_plan = generate_custom_training_plan(client_name, num_modules)

    # Save the training plan to a JSON file
    training_plan.save_plan("aml_training_plan.json")
```
