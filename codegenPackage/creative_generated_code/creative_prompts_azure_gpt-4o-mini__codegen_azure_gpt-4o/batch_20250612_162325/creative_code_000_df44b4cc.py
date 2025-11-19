"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://childnepal.org
Prompt: Generate a Python script that implements community-based child protection systems as described by Child Nepal.
Generated: DETERMINISTIC_df44b4cc9cef136d
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Community-Based Child Protection System Implementation
Author: Expert Programmer
Description: This Python script implements a community-based child protection system.
It models key functionalities such as reporting cases, tracking interventions, 
and generating reports. The system is designed to align with community-driven 
approaches as described by Child Nepal.
"""

import datetime

# Define custom exceptions for error handling
class ChildProtectionError(Exception):
    """Custom exception for child protection system errors."""
    pass

# Define the core classes for the system
class Case:
    """
    Represents a child protection case in the system.
    Attributes:
        case_id (int): Unique identifier for the case.
        reporter_name (str): Name of the person reporting the case.
        description (str): Description of the case.
        status (str): Current status of the case ("Open", "In Progress", "Closed").
        interventions (list): List of interventions taken for the case.
        date_reported (datetime): Date when the case was reported.
    """
    case_counter = 1

    def __init__(self, reporter_name, description):
        if not reporter_name or not description:
            raise ChildProtectionError("Reporter name and case description are required.")
        
        self.case_id = Case.case_counter
        Case.case_counter += 1
        self.reporter_name = reporter_name
        self.description = description
        self.status = "Open"
        self.interventions = []
        self.date_reported = datetime.datetime.now()
    
    def add_intervention(self, intervention_description):
        """
        Adds an intervention to the case.
        Args:
            intervention_description (str): Description of the intervention.
        """
        if not intervention_description:
            raise ChildProtectionError("Intervention description cannot be empty.")
        
        intervention = {
            "description": intervention_description,
            "date": datetime.datetime.now()
        }
        self.interventions.append(intervention)
    
    def update_status(self, new_status):
        """
        Updates the status of the case.
        Args:
            new_status (str): New status of the case ("Open", "In Progress", "Closed").
        """
        if new_status not in ["Open", "In Progress", "Closed"]:
            raise ChildProtectionError("Invalid status. Valid statuses are: Open, In Progress, Closed.")
        
        self.status = new_status
    
    def generate_report(self):
        """
        Generates a detailed report for the case.
        Returns:
            str: Report containing case details, interventions, and status.
        """
        report = f"""
        Case ID: {self.case_id}
        Reporter Name: {self.reporter_name}
        Description: {self.description}
        Status: {self.status}
        Date Reported: {self.date_reported.strftime('%Y-%m-%d %H:%M:%S')}
        Interventions:
        """
        for i, intervention in enumerate(self.interventions, start=1):
            report += f"""
            {i}. {intervention['description']} (Date: {intervention['date'].strftime('%Y-%m-%d %H:%M:%S')})
            """
        return report


class ChildProtectionSystem:
    """
    Represents the community-based child protection system.
    Attributes:
        cases (dict): Dictionary of cases, keyed by case_id.
    """
    def __init__(self):
        self.cases = {}

    def report_case(self, reporter_name, description):
        """
        Reports a new child protection case.
        Args:
            reporter_name (str): Name of the person reporting the case.
            description (str): Description of the case.
        Returns:
            Case: The newly created case object.
        """
        case = Case(reporter_name, description)
        self.cases[case.case_id] = case
        return case

    def get_case_by_id(self, case_id):
        """
        Retrieves a case by its ID.
        Args:
            case_id (int): Unique identifier for the case.
        Returns:
            Case: The case object.
        """
        if case_id not in self.cases:
            raise ChildProtectionError(f"No case found with ID: {case_id}")
        return self.cases[case_id]

    def generate_system_report(self):
        """
        Generates a summary report for all cases in the system.
        Returns:
            str: Summary report for all cases.
        """
        report = f"Community-Based Child Protection System Report\nDate: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        report += f"Total Cases: {len(self.cases)}\n\n"
        for case in self.cases.values():
            report += case.generate_report() + "\n\n"
        return report


# Example usage (for testing)
if __name__ == "__main__":
    try:
        # Initialize the system
        system = ChildProtectionSystem()

        # Report new cases
        case_1 = system.report_case("John Doe", "Child seen begging in the street.")
        case_1.add_intervention("Contacted local authorities.")
        case_1.update_status("In Progress")

        case_2 = system.report_case("Jane Smith", "Child reportedly abused at home.")
        case_2.add_intervention("Referred to social services.")
        case_2.add_intervention("Conducted home visit.")
        case_2.update_status("Closed")

        # Generate system-wide report
        print(system.generate_system_report())

    except ChildProtectionError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
```
