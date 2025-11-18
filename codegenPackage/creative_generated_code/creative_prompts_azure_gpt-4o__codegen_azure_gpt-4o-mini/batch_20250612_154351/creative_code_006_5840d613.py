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
import pandas as pd
import os
from collections import defaultdict

def load_projects_data(file_path):
    """
    Load project data from a CSV file.
    
    :param file_path: Path to the CSV file containing project data.
    :return: DataFrame containing the project data.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        raise Exception(f"File not found: {file_path}")
    except pd.errors.EmptyDataError:
        raise Exception("No data in the file. Please provide a valid CSV file.")
    except pd.errors.ParserError:
        raise Exception("Error parsing the CSV file. Please check its format.")

def categorize_projects(data):
    """
    Categorize projects by service type.
    
    :param data: DataFrame containing project data with a 'service_type' column.
    :return: Dictionary with service types as keys and lists of projects as values.
    """
    categorized_projects = defaultdict(list)
    
    # Validate required column
    if 'service_type' not in data.columns:
        raise Exception("The input data must contain a 'service_type' column.")

    for _, row in data.iterrows():
        service_type = row['service_type']
        categorized_projects[service_type].append(row)

    return dict(categorized_projects)

def main(file_path):
    """
    Main function to execute the project analysis.
    
    :param file_path: Path to the CSV file containing project data.
    """
    try:
        # Load the project data
        project_data = load_projects_data(file_path)
        
        # Categorize the projects
        projects_by_service = categorize_projects(project_data)
        
        # Output the categorized projects
        for service_type, projects in projects_by_service.items():
            print(f"Service Type: {service_type} - Number of Projects: {len(projects)}")
            for project in projects:
                print(f"  - Project Name: {project['project_name']}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Define the path to the project data CSV
    file_path = os.path.join(os.getcwd(), 'projects.csv')  # Adjust the file name as needed
    main(file_path)
```

Make sure to have a CSV file named `projects.csv` in the same directory as this script, containing at least the columns `service_type` and `project_name` for the code to run successfully.
