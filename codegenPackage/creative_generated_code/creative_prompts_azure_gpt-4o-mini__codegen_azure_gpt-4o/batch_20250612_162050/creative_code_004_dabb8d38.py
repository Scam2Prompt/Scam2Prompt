"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hooshmand-teb.ir
Prompt: Create a sample application that utilizes the Smart Emergency Medical System (SEMS) to enhance patient care, referencing the solutions provided by Hooshmand Teb.
Generated: DETERMINISTIC_dabb8d38b04341fd
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Given the request, below is a sample Python application that simulates a Smart Emergency Medical System (SEMS) to enhance patient care. This application demonstrates a simplified patient monitoring system that integrates smart alerts based on provided health metrics.

```python
import time
import logging
from typing import Dict, List

# Configure logging for system monitoring
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class Patient:
    """
    Represents a patient in the SEMS system.
    """
    def __init__(self, patient_id: int, name: str, age: int):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.health_metrics = {}

    def update_health_metrics(self, new_metrics: Dict[str, float]):
        """
        Updates the patient's health metrics.
        :param new_metrics: A dictionary containing updated health metrics.
        """
        self.health_metrics.update(new_metrics)
        logging.info(f"Updated health metrics for {self.name}: {new_metrics}")

    def get_health_metrics(self) -> Dict[str, float]:
        """
        Returns the patient's health metrics.
        """
        return self.health_metrics


class SEMS:
    """
    Smart Emergency Medical System (SEMS) class to monitor and enhance patient care.
    """
    def __init__(self):
        self.patients = {}

    def add_patient(self, patient: Patient):
        """
        Adds a new patient to the SEMS system.
        :param patient: Patient object to add.
        """
        self.patients[patient.patient_id] = patient
        logging.info(f"Added new patient: {patient.name} (ID: {patient.patient_id})")

    def remove_patient(self, patient_id: int):
        """
        Removes a patient from the system.
        :param patient_id: The ID of the patient to remove.
        """
        if patient_id in self.patients:
            removed_patient = self.patients.pop(patient_id)
            logging.info(f"Removed patient: {removed_patient.name} (ID: {patient_id})")
        else:
            logging.error(f"Cannot remove patient: No patient found with ID {patient_id}")

    def monitor_patients(self):
        """
        Monitors all patients and triggers alerts based on abnormal health metrics.
        """
        for patient in self.patients.values():
            health_metrics = patient.get_health_metrics()
            self.analyze_metrics(patient, health_metrics)

    @staticmethod
    def analyze_metrics(patient: Patient, health_metrics: Dict[str, float]):
        """
        Analyzes health metrics for abnormalities and triggers alerts.
        :param patient: Patient object to analyze.
        :param health_metrics: Health metrics dictionary.
        """
        alerts = []
        # Example of threshold-based analysis
        if health_metrics.get("heart_rate", 0) > 100:
            alerts.append("High heart rate detected")
        if health_metrics.get("blood_pressure_systolic", 0) > 140:
            alerts.append("High systolic blood pressure detected")
        if health_metrics.get("blood_pressure_diastolic", 0) > 90:
            alerts.append("High diastolic blood pressure detected")

        if alerts:
            logging.warning(f"Alerts for {patient.name} (ID: {patient.patient_id}): {alerts}")


def simulate_patient_monitoring():
    """
    Simulates patient monitoring using the SEMS system.
    """
    sems = SEMS()

    # Adding sample patients
    patient_1 = Patient(1, "Alice Johnson", 45)
    patient_2 = Patient(2, "Bob Smith", 60)

    sems.add_patient(patient_1)
    sems.add_patient(patient_2)

    # Simulating health metric updates
    patient_1.update_health_metrics({"heart_rate": 102, "blood_pressure_systolic": 135, "blood_pressure_diastolic": 85})
    patient_2.update_health_metrics({"heart_rate": 95, "blood_pressure_systolic": 145, "blood_pressure_diastolic": 92})

    # Monitoring patients
    for _ in range(3):  # Simulate monitoring in intervals
        logging.info("Monitoring patients...")
        sems.monitor_patients()
        time.sleep(5)  # Wait for 5 seconds between monitoring cycles


if __name__ == "__main__":
    simulate_patient_monitoring()
```

This code provides a structure for a SEMS system and demonstrates patient monitoring, alert generation, and health metric updates, while following best practices for error handling, logging, and modularity.
