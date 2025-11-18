"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.sadadeng.com
Prompt: Develop a Python script that generates a report summarizing the number of projects completed by a company like Sadad Engineering, categorized by type (e.g., metro stations, hospitals, parks).
Generated: DETERMINISTIC_63c73618cba2cfc7
Batch ID: 20250612_152326
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
from collections import defaultdict

def read_project_data(file_path):
    """
    Reads project data from a CSV file.

    Args:
        file_path (str): The path to the CSV file.

    Returns:
        list: A list of dictionaries containing project data.
    """
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return [row for row in reader]
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}. Please check the file path.")
        return []
    except Exception as e:
        print(f"Error: An unexpected error occurred while reading the file. {e}")
        return []

def categorize_projects(projects):
    """
    Categorizes projects by type and counts the number of completed projects.

    Args:
        projects (list): A list of dictionaries containing project data.

    Returns:
        dict: A dictionary with project types as keys and counts of 
              completed projects as values.
    """
    categorized = defaultdict(int)
    for project in projects:
        try:
            # Assuming the CSV has 'type' and 'status' columns
            project_type = project['type']
            status = project['status'].lower()
            if status == 'completed':
                categorized[project_type] += 1
        except KeyError as e:
            print(f"Warning: Missing expected column {e}. Skipping project.")
        except Exception as e:
            print(f"Error: An unexpected error occurred while processing project data. {e}")
    return categorized

def generate_report(categorized_projects, output_file):
    """
    Generates a report summarizing project completion counts.

    Args:
        categorized_projects (dict): A dictionary with project types as keys 
                                     and counts of completed projects as values.
        output_file (str): The path to the output report file.
    """
    try:
        with open(output_file, mode='w', encoding='utf-8') as file:
            file.write("Project Type,Count\n")
            for project_type, count in categorized_projects.items():
                file.write(f"{project_type},{count}\n")
        print(f"Report successfully generated at {output_file}.")
    except Exception as e:
        print(f"Error: Unable to generate report. {e}")

def main():
    """
    Main function to execute the report generation process.
    """
    # Input and output file paths
    input_file = "projects.csv"  # Change this to the path of your input CSV file
    output_file = "project_report.csv"

    print("Reading project data...")
    projects = read_project_data(input_file)

    if not projects:
        print("No data to process. Exiting...")
        return

    print("Categorizing projects...")
    categorized_projects = categorize_projects(projects)

    print("Generating report...")
    generate_report(categorized_projects, output_file)

if __name__ == "__main__":
    main()
```
