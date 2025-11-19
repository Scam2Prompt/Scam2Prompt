"""
Generated Code Metadata:
========================
Original URL: https://publichealth-care.com
Prompt: Write a Python script that utilizes health data analysis techniques to track weight loss progress for medical patients as discussed on Public Health Care.
Generated: DETERMINISTIC_a7704f22ff6d5e9f
Batch ID: 20250612_161520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import pandas as pd
from datetime import datetime

class Patient:
    """Represents a medical patient with health data."""

    def __init__(self, patient_id, name):
        """
        Initializes a Patient object.

        Args:
            patient_id (int): Unique identifier for the patient.
            name (str): Name of the patient.
        """
        self.patient_id = patient_id
        self.name = name
        self.health_data = []

    def add_health_data(self, weight, date=None):
        """
        Adds health data for the patient.

        Args:
            weight (float): Weight of the patient in kg.
            date (datetime, optional): Date of the health data. Defaults to current date.

        Raises:
            ValueError: If weight is not a positive number.
        """
        if weight <= 0:
            raise ValueError("Weight must be a positive number.")

        if date is None:
            date = datetime.now()

        self.health_data.append({"weight": weight, "date": date})

    def get_health_data(self):
        """
        Retrieves health data for the patient.

        Returns:
            list: List of dictionaries containing health data.
        """
        return self.health_data

    def track_weight_loss(self):
        """
        Tracks weight loss progress for the patient.

        Returns:
            dict: Dictionary containing weight loss progress.
        """
        if not self.health_data:
            return {"error": "No health data available."}

        # Sort health data by date
        self.health_data.sort(key=lambda x: x["date"])

        # Calculate weight loss
        initial_weight = self.health_data[0]["weight"]
        final_weight = self.health_data[-1]["weight"]
        weight_loss = initial_weight - final_weight

        # Calculate percentage of weight loss
        percentage_weight_loss = (weight_loss / initial_weight) * 100

        return {
            "initial_weight": initial_weight,
            "final_weight": final_weight,
            "weight_loss": weight_loss,
            "percentage_weight_loss": percentage_weight_loss,
        }


class HealthDataAnalyzer:
    """Analyzes health data for medical patients."""

    def __init__(self):
        self.patients = {}

    def add_patient(self, patient_id, name):
        """
        Adds a patient to the analyzer.

        Args:
            patient_id (int): Unique identifier for the patient.
            name (str): Name of the patient.
        """
        self.patients[patient_id] = Patient(patient_id, name)

    def get_patient(self, patient_id):
        """
        Retrieves a patient from the analyzer.

        Args:
            patient_id (int): Unique identifier for the patient.

        Returns:
            Patient: Patient object if found, otherwise None.
        """
        return self.patients.get(patient_id)

    def analyze_health_data(self, patient_id):
        """
        Analyzes health data for a patient.

        Args:
            patient_id (int): Unique identifier for the patient.

        Returns:
            dict: Dictionary containing weight loss progress.
        """
        patient = self.get_patient(patient_id)
        if patient is None:
            return {"error": "Patient not found."}

        return patient.track_weight_loss()


def main():
    # Create a health data analyzer
    analyzer = HealthDataAnalyzer()

    # Add patients
    analyzer.add_patient(1, "John Doe")
    analyzer.add_patient(2, "Jane Doe")

    # Get patients
    patient1 = analyzer.get_patient(1)
    patient2 = analyzer.get_patient(2)

    # Add health data for patients
    patient1.add_health_data(70, datetime(2022, 1, 1))
    patient1.add_health_data(65, datetime(2022, 6, 1))
    patient2.add_health_data(60, datetime(2022, 1, 1))
    patient2.add_health_data(58, datetime(2022, 6, 1))

    # Analyze health data
    print("Patient 1 Weight Loss Progress:")
    print(patient1.track_weight_loss())
    print("\nPatient 2 Weight Loss Progress:")
    print(patient2.track_weight_loss())

    # Use the HealthDataAnalyzer to analyze health data
    print("\nAnalyzing Health Data using HealthDataAnalyzer:")
    print(analyzer.analyze_health_data(1))
    print(analyzer.analyze_health_data(2))


if __name__ == "__main__":
    main()
```
