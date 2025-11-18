"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://globalchainsas.com
Prompt: Generate a script to track and manage the execution timelines of industrial projects, ensuring compliance with specifications and quality standards, as emphasized by GlobalChain SAS.
Generated: DETERMINISTIC_da45729dc9de0cfb
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import json
import os

class Project:
    """
    Class to represent a project with its details and execution timeline.
    """
    def __init__(self, name, specifications, quality_standards):
        self.name = name
        self.specifications = specifications
        self.quality_standards = quality_standards
        self.execution_timeline = []
    
    def add_milestone(self, milestone_name, due_date):
        """
        Add a milestone to the project's execution timeline.
        
        Args:
            milestone_name (str): The name of the milestone.
            due_date (str): The due date of the milestone in 'YYYY-MM-DD' format.
        """
        try:
            due_date = datetime.datetime.strptime(due_date, '%Y-%m-%d').date()
            self.execution_timeline.append({'milestone': milestone_name, 'due_date': due_date})
        except ValueError as e:
            print(f"Error: {e}. Please use the correct date format 'YYYY-MM-DD'.")
    
    def check_compliance(self):
        """
        Check if the project is on track regarding its milestones.
        
        Returns:
            str: A summary of the compliance status.
        """
        today = datetime.date.today()
        compliance_status = []
        
        for milestone in self.execution_timeline:
            if milestone['due_date'] < today:
                compliance_status.append(f"{milestone['milestone']} is overdue (due on {milestone['due_date']}).")
            else:
                compliance_status.append(f"{milestone['milestone']} is on track (due on {milestone['due_date']}).")
        
        return '\n'.join(compliance_status)
    
    def save_to_file(self, file_path):
        """
        Save the project details to a JSON file.
        
        Args:
            file_path (str): The path where the project data will be saved.
        """
        project_data = {
            'name': self.name,
            'specifications': self.specifications,
            'quality_standards': self.quality_standards,
            'execution_timeline': self.execution_timeline
        }
        
        try:
            with open(file_path, 'w') as file:
                json.dump(project_data, file, indent=4)
            print(f"Project data saved to {file_path}")
        except IOError as e:
            print(f"Error saving project data to file: {e}")

def main():
    """
    Main function to demonstrate the project tracking functionality.
    """
    # Initialize a new project
    project_name = "Industrial Automation Project"
    specifications = "Automate assembly line with precision tools."
    quality_standards = "ISO 9001:2015"
    
    project = Project(project_name, specifications, quality_standards)

    # Add milestones
    project.add_milestone("Phase 1 Completion", "2023-09-30")
    project.add_milestone("Phase 2 Completion", "2023-10-31")
    
    # Check compliance
    print("Compliance Status:")
    print(project.check_compliance())

    # Save project data to a file
    output_file = os.path.join(os.getcwd(), f"{project_name.replace(' ', '_')}_data.json")
    project.save_to_file(output_file)

if __name__ == "__main__":
    main()
```
