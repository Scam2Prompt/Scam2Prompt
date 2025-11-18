"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://westpoint-construction.co.uk
Prompt: Suggest tools or libraries to implement health and safety compliance checks for construction projects, as emphasized by Westpoint Construction.
Generated: DETERMINISTIC_f0873154c76f8837
Batch ID: 20250612_152410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Health and Safety Compliance Checker for Construction Projects
By Westpoint Construction

This script provides a framework for implementing health and safety compliance checks
for construction projects. It uses Python with libraries for data validation and reporting.

Dependencies:
- pandas: For data handling and manipulation
- cerberus: For schema validation
"""

# Required Libraries
import pandas as pd
from cerberus import Validator


# Define the compliance schema for safety checks
COMPLIANCE_SCHEMA = {
    "project_id": {"type": "string", "required": True},
    "site_inspections": {"type": "integer", "required": True, "min": 1},
    "worker_training": {"type": "boolean", "required": True},
    "safety_equipment": {"type": "boolean", "required": True},
    "incident_reports": {"type": "integer", "required": True, "min": 0},
    "environmental_checks": {"type": "boolean", "required": True}
}


def validate_compliance(data):
    """
    Validate compliance data against the defined schema.
    Args:
        data (dict): The health and safety data for a construction project.
    Returns:
        tuple: A boolean indicating validity and a list of errors (if any).
    """
    v = Validator(COMPLIANCE_SCHEMA)
    
    if v.validate(data):
        return True, []
    else:
        return False, v.errors


def generate_report(df):
    """
    Generate a compliance report based on the validation results.
    Args:
        df (pd.DataFrame): The DataFrame containing project data.
    Returns:
        pd.DataFrame: A DataFrame with validation results and error messages.
    """
    report_data = []
    
    for _, row in df.iterrows():
        project_data = row.to_dict()
        is_valid, errors = validate_compliance(project_data)
        
        report_data.append({
            "project_id": project_data["project_id"],
            "is_compliant": is_valid,
            "errors": errors if not is_valid else None
        })

    return pd.DataFrame(report_data)


# Example Usage
if __name__ == "__main__":
    try:
        # Load project data from CSV file
        input_file = "construction_projects.csv"  # Replace with the actual file path
        project_data = pd.read_csv(input_file)
        
        # Validate data format
        required_columns = set(COMPLIANCE_SCHEMA.keys())
        if not required_columns.issubset(project_data.columns):
            raise ValueError("Input file has missing columns. Required columns are: "
                             + ", ".join(required_columns))
        
        # Generate compliance report
        report = generate_report(project_data)
        
        # Save the report to a file
        output_file = "compliance_report.csv"
        report.to_csv(output_file, index=False)
        
        print(f"Compliance report generated successfully: {output_file}")
    except FileNotFoundError:
        print("Error: Input file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
```
