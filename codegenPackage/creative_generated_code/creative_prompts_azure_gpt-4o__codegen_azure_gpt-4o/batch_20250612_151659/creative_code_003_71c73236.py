"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mgel.com.br
Prompt: Create a script to analyze construction project data and generate reports on social and environmental responsibility, inspired by MGEL's management system.
Generated: DETERMINISTIC_71c732366cadaec4
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
import json
from datetime import datetime

# Define constants for file paths
CONSTRUCTION_DATA_FILE = "construction_data.csv"
REPORT_FILE = "project_report.json"

# Function to load construction project data from a CSV file
def load_construction_data(file_path):
    """
    Load construction data from a CSV file.

    :param file_path: Path to the CSV file containing project data
    :return: List of dictionaries containing project information
    """
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]
        return data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []
    except Exception as e:
        print(f"An error occurred while loading data: {e}")
        return []


# Function to calculate social and environmental responsibility metrics
def analyze_project_data(data):
    """
    Analyze construction project data for social and environmental responsibility.

    :param data: List of dictionaries containing project information
    :return: Dictionary containing analysis results
    """
    results = {
        "total_projects": 0,
        "projects_with_social_impact": 0,
        "projects_with_environmental_impact": 0,
        "average_impact_score": 0.0,
    }
    total_impact_score = 0

    for project in data:
        try:
            # Parse required fields from the data
            social_impact = int(project.get("social_impact", 0))
            environmental_impact = int(project.get("environmental_impact", 0))
            impact_score = float(project.get("impact_score", 0))

            # Update metrics
            results["total_projects"] += 1
            if social_impact > 0:
                results["projects_with_social_impact"] += 1
            if environmental_impact > 0:
                results["projects_with_environmental_impact"] += 1
            total_impact_score += impact_score
        except ValueError:
            print(f"Warning: Invalid data in project record - {project}")

    # Calculate average impact score
    if results["total_projects"] > 0:
        results["average_impact_score"] = total_impact_score / results["total_projects"]

    return results


# Function to generate a report and save it as a JSON file
def generate_report(summary, file_path):
    """
    Generate a report and save it to a JSON file.

    :param summary: Dictionary containing the analysis summary
    :param file_path: Path to save the JSON report file
    """
    try:
        with open(file_path, mode='w', encoding='utf-8') as file:
            json.dump(summary, file, indent=4)
        print(f"Report successfully generated and saved to '{file_path}'.")
    except Exception as e:
        print(f"An error occurred while saving the report: {e}")


# Main function to execute the script
def main():
    """
    Main function to analyze construction data and generate a report.
    """
    print("Loading construction data...")
    project_data = load_construction_data(CONSTRUCTION_DATA_FILE)

    if not project_data:
        print("No data to process. Exiting...")
        return

    print("Analyzing project data...")
    analysis_results = analyze_project_data(project_data)

    print("Generating report...")
    generate_report(analysis_results, REPORT_FILE)


# Entry point for the script
if __name__ == "__main__":
    main()
```
