"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vitaprojects.co.za
Prompt: Write a Python script that automates daily site visit reports for high-end construction projects, ensuring quality control and project management efficiency.
Generated: DETERMINISTIC_a7aac997c69f2dd4
Batch ID: 20250612_135848
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
import datetime
import os

# Constants
REPORTS_DIR = "site_reports"
DEFAULT_PROJECTS = [
    {"name": "Luxury Apartment Complex", "location": "Downtown"},
    {"name": "High-End Office Building", "location": "Uptown"},
    {"name": "Exclusive Residential Villas", "location": "Suburbs"},
]

# Ensure the reports directory exists
def ensure_reports_directory():
    if not os.path.exists(REPORTS_DIR):
        os.makedirs(REPORTS_DIR)

# Generate a site visit report
def generate_site_visit_report(project_name, project_location, observations, issues):
    ensure_reports_directory()
    
    # Get today's date for the report filename and content
    today = datetime.date.today()
    filename = f"{REPORTS_DIR}/{project_name.replace(' ', '_')}_Site_Report_{today}.csv"
    
    try:
        # Create and write the report
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            
            # Write header
            writer.writerow(["Project Name", "Project Location", "Date", "Observations", "Issues"])
            
            # Write data
            writer.writerow([project_name, project_location, today, observations, issues])
        
        print(f"Site visit report generated: {filename}")
    except Exception as e:
        print(f"Error generating report: {e}")

# Prompt user for daily observations
def collect_daily_observations(projects):
    for project in projects:
        print(f"\nGenerating report for project: {project['name']} ({project['location']})")
        observations = input("Enter daily observations: ").strip()
        issues = input("Enter issues identified (if any): ").strip()
        
        # Generate the report for the current project
        generate_site_visit_report(project['name'], project['location'], observations, issues)

# Main function to automate site visit reports
def main():
    print("Automated Site Visit Report Generator")
    print("======================================")
    try:
        print("\nAvailable Projects:")
        for idx, project in enumerate(DEFAULT_PROJECTS, start=1):
            print(f"{idx}. {project['name']} ({project['location']})")
        
        # Collect daily observations and generate reports
        collect_daily_observations(DEFAULT_PROJECTS)
        
        print("\nAll reports generated successfully.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Entry point for the script
if __name__ == "__main__":
    main()
```
