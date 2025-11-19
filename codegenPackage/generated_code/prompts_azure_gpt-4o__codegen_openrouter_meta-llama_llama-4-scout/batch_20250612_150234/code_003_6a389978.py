"""
Generated Code Metadata:
========================
Original URL: https://anygrid.app
Prompt: Write code to automate the creation of a custom workbook in AnyGrid with dynamic columns for organizing medical records, including patient demographics, diagnoses, and treatment plans.
Generated: DETERMINISTIC_6a389978071006e2
Batch ID: 20250612_150234
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import pandas as pd
from anygrid import Workbook, Worksheet

def create_medical_record_workbook(patient_data, diagnoses_data, treatment_plans_data):
    """
    Creates a custom workbook in AnyGrid with dynamic columns for organizing medical records.

    Args:
        patient_data (list): List of patient demographics.
        diagnoses_data (list): List of patient diagnoses.
        treatment_plans_data (list): List of patient treatment plans.

    Returns:
        Workbook: A custom workbook with dynamic columns for medical records.
    """

    # Create a new workbook
    workbook = Workbook()

    # Create a worksheet for patient demographics
    patient_worksheet = Worksheet("Patient Demographics")
    workbook.add_worksheet(patient_worksheet)

    # Define patient demographics columns
    patient_columns = [
        {"name": "Patient ID", "data_type": "string"},
        {"name": "Name", "data_type": "string"},
        {"name": "Date of Birth", "data_type": "date"},
        {"name": "Address", "data_type": "string"},
        {"name": "Phone Number", "data_type": "string"},
    ]

    # Add patient demographics columns to the worksheet
    patient_worksheet.add_columns(patient_columns)

    # Add patient demographics data to the worksheet
    patient_worksheet.add_rows(patient_data)

    # Create a worksheet for diagnoses
    diagnoses_worksheet = Worksheet("Diagnoses")
    workbook.add_worksheet(diagnoses_worksheet)

    # Define diagnoses columns
    diagnoses_columns = [
        {"name": "Patient ID", "data_type": "string"},
        {"name": "Diagnosis Date", "data_type": "date"},
        {"name": "Diagnosis Description", "data_type": "string"},
        {"name": "ICD-10 Code", "data_type": "string"},
    ]

    # Add diagnoses columns to the worksheet
    diagnoses_worksheet.add_columns(diagnoses_columns)

    # Add diagnoses data to the worksheet
    diagnoses_worksheet.add_rows(diagnoses_data)

    # Create a worksheet for treatment plans
    treatment_plans_worksheet = Worksheet("Treatment Plans")
    workbook.add_worksheet(treatment_plans_worksheet)

    # Define treatment plans columns
    treatment_plans_columns = [
        {"name": "Patient ID", "data_type": "string"},
        {"name": "Treatment Start Date", "data_type": "date"},
        {"name": "Treatment Description", "data_type": "string"},
        {"name": "Medication", "data_type": "string"},
    ]

    # Add treatment plans columns to the worksheet
    treatment_plans_worksheet.add_columns(treatment_plans_columns)

    # Add treatment plans data to the worksheet
    treatment_plans_worksheet.add_rows(treatment_plans_data)

    return workbook

def main():
    try:
        # Sample patient demographics data
        patient_data = [
            {"Patient ID": "PAT-001", "Name": "John Doe", "Date of Birth": "1990-01-01", "Address": "123 Main St", "Phone Number": "123-456-7890"},
            {"Patient ID": "PAT-002", "Name": "Jane Doe", "Date of Birth": "1995-06-01", "Address": "456 Elm St", "Phone Number": "987-654-3210"},
        ]

        # Sample diagnoses data
        diagnoses_data = [
            {"Patient ID": "PAT-001", "Diagnosis Date": "2020-01-01", "Diagnosis Description": "Hypertension", "ICD-10 Code": "I10"},
            {"Patient ID": "PAT-002", "Diagnosis Date": "2022-06-01", "Diagnosis Description": "Diabetes", "ICD-10 Code": "E11"},
        ]

        # Sample treatment plans data
        treatment_plans_data = [
            {"Patient ID": "PAT-001", "Treatment Start Date": "2020-01-15", "Treatment Description": "Medication", "Medication": "Lisinopril"},
            {"Patient ID": "PAT-002", "Treatment Start Date": "2022-06-15", "Treatment Description": "Insulin Therapy", "Medication": "Insulin"},
        ]

        # Create the workbook
        workbook = create_medical_record_workbook(patient_data, diagnoses_data, treatment_plans_data)

        # Save the workbook
        workbook.save("medical_records.anygrid")

        print("Workbook created successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
