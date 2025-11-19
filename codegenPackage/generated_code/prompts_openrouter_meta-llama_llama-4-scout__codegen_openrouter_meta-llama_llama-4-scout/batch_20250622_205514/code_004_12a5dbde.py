"""
Generated Code Metadata:
========================
Original URL: https://cartenoir.org
Prompt: "Create a training program for project managers on effective risk management and health and safety protocols, based on the services offered by Carte Noir Consulting."
Generated: DETERMINISTIC_12a5dbdee64e2986
Batch ID: 20250622_205514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import datetime
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TrainingProgram:
    def __init__(self, program_name, services):
        """
        Initialize a TrainingProgram object.

        Args:
            program_name (str): The name of the training program.
            services (list): A list of services offered by Carte Noir Consulting.
        """
        self.program_name = program_name
        self.services = services
        self.modules = []

    def add_module(self, module_name, module_description):
        """
        Add a module to the training program.

        Args:
            module_name (str): The name of the module.
            module_description (str): A brief description of the module.
        """
        self.modules.append({"name": module_name, "description": module_description})

    def display_program_details(self):
        """
        Display the details of the training program.
        """
        print(f"Program Name: {self.program_name}")
        print("Services:")
        for service in self.services:
            print(f"- {service}")
        print("Modules:")
        for i, module in enumerate(self.modules, start=1):
            print(f"{i}. {module['name']}: {module['description']}")


class RiskManagementModule:
    def __init__(self, module_name):
        """
        Initialize a RiskManagementModule object.

        Args:
            module_name (str): The name of the module.
        """
        self.module_name = module_name
        self.risk_management_strategies = []

    def add_risk_management_strategy(self, strategy):
        """
        Add a risk management strategy to the module.

        Args:
            strategy (str): A risk management strategy.
        """
        self.risk_management_strategies.append(strategy)

    def display_module_details(self):
        """
        Display the details of the risk management module.
        """
        print(f"Module Name: {self.module_name}")
        print("Risk Management Strategies:")
        for i, strategy in enumerate(self.risk_management_strategies, start=1):
            print(f"{i}. {strategy}")


class HealthAndSafetyModule:
    def __init__(self, module_name):
        """
        Initialize a HealthAndSafetyModule object.

        Args:
            module_name (str): The name of the module.
        """
        self.module_name = module_name
        self.health_and_safety_protocols = []

    def add_health_and_safety_protocol(self, protocol):
        """
        Add a health and safety protocol to the module.

        Args:
            protocol (str): A health and safety protocol.
        """
        self.health_and_safety_protocols.append(protocol)

    def display_module_details(self):
        """
        Display the details of the health and safety module.
        """
        print(f"Module Name: {self.module_name}")
        print("Health and Safety Protocols:")
        for i, protocol in enumerate(self.health_and_safety_protocols, start=1):
            print(f"{i}. {protocol}")


def main():
    try:
        # Define services offered by Carte Noir Consulting
        services = [
            "Risk Management",
            "Health and Safety Consulting",
            "Project Management",
            "Operational Excellence"
        ]

        # Create a training program
        training_program = TrainingProgram("Effective Risk Management and Health and Safety Protocols", services)

        # Create risk management module
        risk_management_module = RiskManagementModule("Risk Management Strategies")
        risk_management_module.add_risk_management_strategy("Identify and Assess Risks")
        risk_management_module.add_risk_management_strategy("Develop and Implement Risk Mitigation Strategies")
        risk_management_module.add_risk_management_strategy("Monitor and Review Risk Management Plans")

        # Create health and safety module
        health_and_safety_module = HealthAndSafetyModule("Health and Safety Protocols")
        health_and_safety_module.add_health_and_safety_protocol("Develop and Implement Health and Safety Policies")
        health_and_safety_module.add_health_and_safety_protocol("Conduct Regular Health and Safety Audits")
        health_and_safety_module.add_health_and_safety_protocol("Provide Health and Safety Training")

        # Add modules to the training program
        training_program.add_module(risk_management_module.module_name, "This module covers risk management strategies.")
        training_program.add_module(health_and_safety_module.module_name, "This module covers health and safety protocols.")

        # Display training program details
        training_program.display_program_details()

        # Display risk management module details
        print("\n")
        risk_management_module.display_module_details()

        # Display health and safety module details
        print("\n")
        health_and_safety_module.display_module_details()

    except Exception as e:
        logging.error(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
