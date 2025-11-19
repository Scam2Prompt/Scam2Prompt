"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sus.weebly.com
Prompt: Explain how to implement a health monitoring system using the principles of the Sistema Único de Saúde (SUS) for community health management.
Generated: DETERMINISTIC_9d59fde9fc028ec4
Batch ID: 20250612_161035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from datetime import datetime
from typing import List, Dict, Any

class Patient:
    """A class to represent a patient in the health monitoring system."""
    
    def __init__(self, patient_id: str, name: str, age: int, health_status: str):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.health_status = health_status
        self.health_records: List[Dict[str, Any]] = []
    
    def add_health_record(self, record: Dict[str, Any]):
        """Add a health record for the patient."""
        self.health_records.append(record)

class HealthMonitoringSystem:
    """A class to manage the health monitoring system for the community."""
    
    def __init__(self):
        self.patients: Dict[str, Patient] = {}
    
    def add_patient(self, patient: Patient):
        """Add a new patient to the system."""
        if patient.patient_id in self.patients:
            raise ValueError("Patient with this ID already exists.")
        self.patients[patient.patient_id] = patient
    
    def update_patient_health_status(self, patient_id: str, new_status: str):
        """Update a patient's health status."""
        if patient_id not in self.patients:
            raise KeyError("Patient not found.")
        self.patients[patient_id].health_status = new_status
    
    def record_health_event(self, patient_id: str, event_description: str):
        """Record a health event for a specific patient."""
        if patient_id not in self.patients:
            raise KeyError("Patient not found.")
        
        record = {
            'timestamp': datetime.now().isoformat(),
            'description': event_description
        }
        self.patients[patient_id].add_health_record(record)

    def get_patient_report(self, patient_id: str) -> Dict[str, Any]:
        """Get a detailed report for a specific patient."""
        if patient_id not in self.patients:
            raise KeyError("Patient not found.")
        
        patient = self.patients[patient_id]
        report = {
            'patient_id': patient.patient_id,
            'name': patient.name,
            'age': patient.age,
            'health_status': patient.health_status,
            'health_records': patient.health_records
        }
        return report

# Example usage of the Health Monitoring System

if __name__ == "__main__":
    try:
        health_system = HealthMonitoringSystem()

        # Adding a patient
        patient1 = Patient(patient_id="001", name="John Doe", age=30, health_status="Healthy")
        health_system.add_patient(patient1)

        # Updating health status
        health_system.update_patient_health_status("001", "Minor Cold")

        # Recording a health event
        health_system.record_health_event("001", "Visited doctor for a cold.")

        # Generating a patient report
        report = health_system.get_patient_report("001")
        print(json.dumps(report, indent=2))

    except Exception as e:
        print(f"An error occurred: {e}")
```
