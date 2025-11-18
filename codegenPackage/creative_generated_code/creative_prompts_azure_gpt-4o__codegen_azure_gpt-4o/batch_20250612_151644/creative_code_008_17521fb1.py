"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://complyaml.com
Prompt: Create a script to track and report AML compliance progress across multiple departments, based on ComplyAML's training breakdown.
Generated: DETERMINISTIC_17521fb167bc06aa
Batch ID: 20250612_151644
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from datetime import datetime

# Define a class to represent a department's AML compliance progress
class DepartmentAMLProgress:
    def __init__(self, department_name, total_employees, completed_training):
        """
        Initialize department attributes.

        :param department_name: Name of the department
        :param total_employees: Total employees in the department
        :param completed_training: Number of employees who completed the training
        """
        self.department_name = department_name
        self.total_employees = total_employees
        self.completed_training = completed_training

    def calculate_completion_percentage(self):
        """
        Calculate the percentage of employees who have completed AML training.

        :return: Completion percentage (float)
        """
        if self.total_employees == 0:
            return 0.0  # Avoid division by zero
        return (self.completed_training / self.total_employees) * 100

    def to_dict(self):
        """
        Convert department data to a dictionary format.

        :return: Dictionary representation of department progress
        """
        return {
            "department_name": self.department_name,
            "total_employees": self.total_employees,
            "completed_training": self.completed_training,
            "completion_percentage": self.calculate_completion_percentage()
        }

# Function to process compliance data
def process_compliance_data(department_data):
    """
    Process compliance data for multiple departments.

    :param department_data: List of department compliance dictionaries
    :return: List of processed department AML progress dictionaries
    """
    processed_data = []
    for data in department_data:
        try:
            # Ensure input data is valid
            department_name = data.get("department_name", "")
            total_employees = int(data.get("total_employees", 0))
            completed_training = int(data.get("completed_training", 0))

            # Create an instance of DepartmentAMLProgress
            department_progress = DepartmentAMLProgress(
                department_name,
                total_employees,
                completed_training,
            )

            # Append processed data to the list
            processed_data.append(department_progress.to_dict())
        except (ValueError, TypeError) as e:
            # Log error and skip invalid entry
            print(f"Error processing department data: {e}")
            continue
    return processed_data

# Function to save compliance report to a file
def save_report_to_file(report_data, filename="compliance_report.json"):
    """
    Save the compliance report to a JSON file.

    :param report_data: List of department compliance progress
    :param filename: Filename to save the report
    """
    try:
        with open(filename, "w") as file:
            json.dump(report_data, file, indent=4)
        print(f"Compliance report saved to {filename}")
    except IOError as e:
        print(f"Error saving report to file: {e}")

# Main function
def main():
    """
    Main script function to track and report AML compliance progress.
    """
    # Example input data (could be fetched from a database or API)
    department_data = [
        {"department_name": "Finance", "total_employees": 50, "completed_training": 45},
        {"department_name": "HR", "total_employees": 30, "completed_training": 20},
        {"department_name": "IT", "total_employees": 25, "completed_training": 25},
        {"department_name": "Legal", "total_employees": 10, "completed_training": 8},
    ]

    # Process compliance data
    compliance_report = process_compliance_data(department_data)

    # Save report to file
    save_report_to_file(compliance_report)

    # Print report summary to console
    print("AML Compliance Progress Report:")
    print(json.dumps(compliance_report, indent=4))

# Entry point of the script
if __name__ == "__main__":
    main()
```
