"""
Generated Code Metadata:
========================
Original URL: https://www.sadadeng.com
Prompt: Develop a Python script that generates a report summarizing the number of projects completed by a company like Sadad Engineering, categorized by type (e.g., metro stations, hospitals, parks).
Generated: DETERMINISTIC_63c73618cba2cfc7
Batch ID: 20250612_152326
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import csv
from collections import defaultdict
from datetime import datetime
import os

def generate_project_report(projects_data, output_file):
    """
    Generates a report summarizing the number of projects completed by category.
    
    Args:
        projects_data (list of dict): List of project dictionaries containing 'name', 'type', and 'completion_date'.
        output_file (str): Path to the output CSV file where the report will be saved.
    
    Returns:
        bool: True if report was generated successfully, False otherwise.
    """
    try:
        # Validate input data
        if not projects_data:
            raise ValueError("No project data provided")
        
        if not all(isinstance(project, dict) for project in projects_data):
            raise ValueError("Invalid project data format")
        
        required_fields = {'name', 'type', 'completion_date'}
        for project in projects_data:
            if not required_fields.issubset(project.keys()):
                raise ValueError(f"Project {project.get('name', 'unknown')} missing required fields")
        
        # Categorize projects by type
        category_counts = defaultdict(int)
        for project in projects_data:
            category_counts[project['type']] += 1
        
        # Prepare report data
        report_data = [
            {'Category': category, 'Count': count}
            for category, count in sorted(category_counts.items())
        ]
        
        # Add summary row
        total_projects = sum(category_counts.values())
        report_data.append({'Category': 'TOTAL', 'Count': total_projects})
        
        # Write to CSV
        os.makedirs(os.path.dirname(output_file) or '.', exist_ok=True)
        
        with open(output_file, 'w', newline='') as csvfile:
            fieldnames = ['Category', 'Count']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            writer.writerows(report_data)
        
        return True
    
    except Exception as e:
        print(f"Error generating report: {str(e)}")
        return False

def load_projects_from_csv(input_file):
    """
    Loads project data from a CSV file.
    
    Args:
        input_file (str): Path to the input CSV file.
    
    Returns:
        list: List of project dictionaries.
    """
    projects = []
    try:
        with open(input_file, mode='r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                projects.append({
                    'name': row.get('name', ''),
                    'type': row.get('type', ''),
                    'completion_date': row.get('completion_date', '')
                })
        return projects
    except Exception as e:
        print(f"Error loading projects: {str(e)}")
        return []

def main():
    # Example usage
    projects = [
        {'name': 'Downtown Metro', 'type': 'metro station', 'completion_date': '2022-01-15'},
        {'name': 'Central Hospital', 'type': 'hospital', 'completion_date': '2021-11-20'},
        {'name': 'Riverside Park', 'type': 'park', 'completion_date': '2023-03-10'},
        {'name': 'Westside Metro', 'type': 'metro station', 'completion_date': '2022-08-30'},
        {'name': 'Childrens Hospital', 'type': 'hospital', 'completion_date': '2023-01-05'}
    ]
    
    # Generate report from sample data
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"reports/project_summary_{timestamp}.csv"
    
    if generate_project_report(projects, output_file):
        print(f"Report generated successfully: {output_file}")
    else:
        print("Failed to generate report")

if __name__ == "__main__":
    main()
```
