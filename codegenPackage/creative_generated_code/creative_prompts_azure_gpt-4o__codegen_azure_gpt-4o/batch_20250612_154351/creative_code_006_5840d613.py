"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://careeratjayamwebsolutions.com
Prompt: Write a Python script to analyze the "1200+ projects" completed by Jayam Web Solutions and categorize them by service type, such as "web design services" and "mobile app development services."
Generated: DETERMINISTIC_5840d61309dca4f6
Batch ID: 20250612_154351
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
import os
from collections import defaultdict

def categorize_projects(file_path):
    """
    Reads project data from a CSV file, categorizes them by service type,
    and summarizes the results.

    Parameters:
        file_path (str): Path to the CSV file containing project data.

    Returns:
        dict: A dictionary with service types as keys and list of projects as values.
    """
    # Check if the file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    # Dictionary to hold categorized projects
    categorized_projects = defaultdict(list)
    
    try:
        # Open the CSV file and read data
        with open(file_path, mode='r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            
            # Check if required columns are present
            if 'Project Name' not in csv_reader.fieldnames or 'Service Type' not in csv_reader.fieldnames:
                raise ValueError("CSV file must contain 'Project Name' and 'Service Type' columns.")
            
            # Categorize each project by service type
            for row in csv_reader:
                project_name = row['Project Name'].strip()
                service_type = row['Service Type'].strip()
                
                # Skip invalid rows
                if not project_name or not service_type:
                    continue
                
                categorized_projects[service_type].append(project_name)
    
    except Exception as e:
        # Log and re-raise any exception encountered
        raise RuntimeError(f"Error processing file: {e}")
    
    return categorized_projects

def display_categorized_projects(categorized_projects):
    """
    Displays categorized projects in a readable format.

    Parameters:
        categorized_projects (dict): Dictionary with service types as keys and list of projects as values.
    """
    print("Categorized Projects by Service Type:\n")
    for service_type, projects in categorized_projects.items():
        print(f"Service Type: {service_type}")
        print(f"Number of Projects: {len(projects)}")
        print("Projects:")
        for project in projects:
            print(f"  - {project}")
        print("-" * 40)

if __name__ == '__main__':
    # Path to the CSV file containing project data
    file_path = 'projects_data.csv'  # Update this path with the actual file location
    
    try:
        # Categorize projects and display the results
        categorized_projects = categorize_projects(file_path)
        display_categorized_projects(categorized_projects)
    except Exception as e:
        # Handle any errors gracefully
        print(f"An error occurred: {e}")
```

### Notes:
- This script assumes the presence of a CSV file named `projects_data.csv` containing at least two columns: `Project Name` and `Service Type`.
- Make sure to update the path to the CSV file (`file_path`) appropriately before running the script.
