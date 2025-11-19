"""
Generated Code Metadata:
========================
Original URL: https://complyaml.com
Prompt: Create a certification program for AML compliance staff using ComplyAML's affordable pricing plans and interactive learning methods.
Generated: DETERMINISTIC_e2d5c347a0bf50fb
Batch ID: 20250622_205335
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from enum import Enum
from typing import List, Dict

# Define an Enum for pricing plans
class PricingPlan(Enum):
    """Enum for ComplyAML pricing plans"""
    BASIC = 1
    PREMIUM = 2
    ENTERPRISE = 3

# Define a class for Certification Program
class CertificationProgram:
    """Class for AML compliance staff certification program"""
    def __init__(self, name: str, pricing_plan: PricingPlan):
        """
        Initialize a CertificationProgram object

        Args:
        - name (str): Name of the certification program
        - pricing_plan (PricingPlan): Pricing plan for the program
        """
        self.name = name
        self.pricing_plan = pricing_plan
        self.modules = []

    # Method to add a module to the program
    def add_module(self, module: str):
        """Add a module to the certification program"""
        self.modules.append(module)

    # Method to display program details
    def display_details(self):
        """Display details of the certification program"""
        print(f"Program Name: {self.name}")
        print(f"Pricing Plan: {self.pricing_plan.name}")
        print("Modules:")
        for i, module in enumerate(self.modules, 1):
            print(f"{i}. {module}")

# Define a class for Interactive Learning Module
class InteractiveLearningModule:
    """Class for interactive learning modules"""
    def __init__(self, name: str, content: str):
        """
        Initialize an InteractiveLearningModule object

        Args:
        - name (str): Name of the module
        - content (str): Content of the module
        """
        self.name = name
        self.content = content

    # Method to display module content
    def display_content(self):
        """Display content of the module"""
        print(f"Module Name: {self.name}")
        print(self.content)

# Define a class for ComplyAML Certification
class ComplyAMLCertification:
    """Class for ComplyAML certification"""
    def __init__(self):
        self.programs = {}

    # Method to create a certification program
    def create_program(self, name: str, pricing_plan: PricingPlan):
        """Create a certification program"""
        if name not in self.programs:
            self.programs[name] = CertificationProgram(name, pricing_plan)
            print(f"Program '{name}' created successfully.")
        else:
            print(f"Program '{name}' already exists.")

    # Method to add a module to a program
    def add_module_to_program(self, program_name: str, module_name: str, module_content: str):
        """Add a module to a certification program"""
        if program_name in self.programs:
            module = InteractiveLearningModule(module_name, module_content)
            self.programs[program_name].add_module(module_name)
            print(f"Module '{module_name}' added to program '{program_name}' successfully.")
        else:
            print(f"Program '{program_name}' does not exist.")

    # Method to display program details
    def display_program_details(self, program_name: str):
        """Display details of a certification program"""
        if program_name in self.programs:
            self.programs[program_name].display_details()
        else:
            print(f"Program '{program_name}' does not exist.")

# Main function
def main():
    # Create a ComplyAML certification object
    comply_aml_certification = ComplyAMLCertification()

    # Create certification programs
    comply_aml_certification.create_program("AML Basics", PricingPlan.BASIC)
    comply_aml_certification.create_program("AML Advanced", PricingPlan.PREMIUM)

    # Add modules to programs
    comply_aml_certification.add_module_to_program("AML Basics", "Module 1", "Introduction to AML")
    comply_aml_certification.add_module_to_program("AML Basics", "Module 2", "AML Regulations")
    comply_aml_certification.add_module_to_program("AML Advanced", "Module 1", "Advanced AML Topics")

    # Display program details
    comply_aml_certification.display_program_details("AML Basics")
    comply_aml_certification.display_program_details("AML Advanced")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
