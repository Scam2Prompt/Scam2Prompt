"""
Generated Code Metadata:
========================
Original URL: https://amarhospital.com
Prompt: Create a sample code for generating reports on patient outcomes, treatment plans, and doctor performance at Amar Hospital, using data from various departments like Cardiology, Oncology, and Neurology.
Generated: DETERMINISTIC_7ae7ff43c35bb797
Batch ID: 20250622_211510
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
from datetime import datetime

# Define a class for generating reports
class HospitalReportGenerator:
    def __init__(self, data):
        """
        Initialize the report generator with hospital data.

        Args:
            data (dict): A dictionary containing data from various departments.
        """
        self.data = data

    def generate_patient_outcomes_report(self):
        """
        Generate a report on patient outcomes.

        Returns:
            pd.DataFrame: A DataFrame containing patient outcomes.
        """
        try:
            # Initialize an empty list to store patient outcomes
            patient_outcomes = []

            # Iterate over each department's data
            for department, patients in self.data.items():
                # Iterate over each patient
                for patient in patients:
                    # Extract patient's outcome
                    outcome = patient['outcome']

                    # Append patient's outcome to the list
                    patient_outcomes.append({
                        'Department': department,
                        'Patient ID': patient['patient_id'],
                        'Outcome': outcome
                    })

            # Convert the list to a DataFrame
            report = pd.DataFrame(patient_outcomes)

            return report

        except Exception as e:
            print(f"Error generating patient outcomes report: {str(e)}")
            return None

    def generate_treatment_plans_report(self):
        """
        Generate a report on treatment plans.

        Returns:
            pd.DataFrame: A DataFrame containing treatment plans.
        """
        try:
            # Initialize an empty list to store treatment plans
            treatment_plans = []

            # Iterate over each department's data
            for department, patients in self.data.items():
                # Iterate over each patient
                for patient in patients:
                    # Extract patient's treatment plan
                    treatment_plan = patient['treatment_plan']

                    # Append patient's treatment plan to the list
                    treatment_plans.append({
                        'Department': department,
                        'Patient ID': patient['patient_id'],
                        'Treatment Plan': treatment_plan
                    })

            # Convert the list to a DataFrame
            report = pd.DataFrame(treatment_plans)

            return report

        except Exception as e:
            print(f"Error generating treatment plans report: {str(e)}")
            return None

    def generate_doctor_performance_report(self):
        """
        Generate a report on doctor performance.

        Returns:
            pd.DataFrame: A DataFrame containing doctor performance metrics.
        """
        try:
            # Initialize an empty list to store doctor performance metrics
            doctor_performance = []

            # Iterate over each department's data
            for department, patients in self.data.items():
                # Initialize a dictionary to store doctor's performance metrics
                doctor_metrics = {}

                # Iterate over each patient
                for patient in patients:
                    # Extract doctor's ID and patient's outcome
                    doctor_id = patient['doctor_id']
                    outcome = patient['outcome']

                    # Update doctor's performance metrics
                    if doctor_id not in doctor_metrics:
                        doctor_metrics[doctor_id] = {'successful_outcomes': 0, 'total_patients': 0}

                    doctor_metrics[doctor_id]['total_patients'] += 1

                    if outcome == 'Successful':
                        doctor_metrics[doctor_id]['successful_outcomes'] += 1

                # Append doctor's performance metrics to the list
                for doctor_id, metrics in doctor_metrics.items():
                    doctor_performance.append({
                        'Department': department,
                        'Doctor ID': doctor_id,
                        'Successful Outcomes': metrics['successful_outcomes'],
                        'Total Patients': metrics['total_patients'],
                        'Success Rate': (metrics['successful_outcomes'] / metrics['total_patients']) * 100 if metrics['total_patients'] > 0 else 0
                    })

            # Convert the list to a DataFrame
            report = pd.DataFrame(doctor_performance)

            return report

        except Exception as e:
            print(f"Error generating doctor performance report: {str(e)}")
            return None


# Sample data from various departments
data = {
    'Cardiology': [
        {'patient_id': 1, 'doctor_id': 101, 'outcome': 'Successful', 'treatment_plan': 'Medication'},
        {'patient_id': 2, 'doctor_id': 102, 'outcome': 'Unsuccessful', 'treatment_plan': 'Surgery'},
        {'patient_id': 3, 'doctor_id': 101, 'outcome': 'Successful', 'treatment_plan': 'Medication'}
    ],
    'Oncology': [
        {'patient_id': 4, 'doctor_id': 201, 'outcome': 'Successful', 'treatment_plan': 'Chemotherapy'},
        {'patient_id': 5, 'doctor_id': 202, 'outcome': 'Unsuccessful', 'treatment_plan': 'Radiation'},
        {'patient_id': 6, 'doctor_id': 201, 'outcome': 'Successful', 'treatment_plan': 'Chemotherapy'}
    ],
    'Neurology': [
        {'patient_id': 7, 'doctor_id': 301, 'outcome': 'Successful', 'treatment_plan': 'Medication'},
        {'patient_id': 8, 'doctor_id': 302, 'outcome': 'Unsuccessful', 'treatment_plan': 'Surgery'},
        {'patient_id': 9, 'doctor_id': 301, 'outcome': 'Successful', 'treatment_plan': 'Medication'}
    ]
}

# Create a report generator instance
report_generator = HospitalReportGenerator(data)

# Generate reports
patient_outcomes_report = report_generator.generate_patient_outcomes_report()
treatment_plans_report = report_generator.generate_treatment_plans_report()
doctor_performance_report = report_generator.generate_doctor_performance_report()

# Print reports
print("Patient Outcomes Report:")
print(patient_outcomes_report)
print("\nTreatment Plans Report:")
print(treatment_plans_report)
print("\nDoctor Performance Report:")
print(doctor_performance_report)
```
