"""
Generated Code Metadata:
========================
Original URL: https://hooshmand-teb.ir
Prompt: "Write a Python code snippet to implement an IoT-based patient monitoring system using H-IOT and SEMS."
Generated: DETERMINISTIC_9e4cc875577a0322
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import time
import random
import logging
from datetime import datetime

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Patient:
    """Represents a patient with a unique ID and vital signs."""
    def __init__(self, patient_id):
        self.patient_id = patient_id
        self.vital_signs = {
            'heart_rate': None,
            'blood_pressure': None,
            'oxygen_level': None,
            'temperature': None
        }

    def update_vital_signs(self, heart_rate, blood_pressure, oxygen_level, temperature):
        """Updates the patient's vital signs."""
        self.vital_signs['heart_rate'] = heart_rate
        self.vital_signs['blood_pressure'] = blood_pressure
        self.vital_signs['oxygen_level'] = oxygen_level
        self.vital_signs['temperature'] = temperature

class HIoTDevice:
    """Simulates an H-IOT device that collects vital signs from a patient."""
    def __init__(self, patient):
        self.patient = patient

    def collect_vital_signs(self):
        """Simulates collecting vital signs from the patient."""
        heart_rate = random.randint(60, 100)
        blood_pressure = f"{random.randint(90, 140)}/{random.randint(60, 90)}"
        oxygen_level = random.randint(80, 100)
        temperature = round(random.uniform(36.5, 37.5), 2)
        self.patient.update_vital_signs(heart_rate, blood_pressure, oxygen_level, temperature)

class SEMS:
    """Simulates a SEMS (Sensor-Enabled Monitoring System) that receives data from H-IOT devices."""
    def __init__(self):
        self.patients = {}

    def add_patient(self, patient_id):
        """Adds a patient to the SEMS."""
        self.patients[patient_id] = Patient(patient_id)

    def update_patient_vital_signs(self, patient_id):
        """Updates a patient's vital signs using an H-IOT device."""
        if patient_id in self.patients:
            patient = self.patients[patient_id]
            h_iot_device = HIoTDevice(patient)
            h_iot_device.collect_vital_signs()
            logging.info(f"Updated vital signs for patient {patient_id}: {patient.vital_signs}")
        else:
            logging.error(f"Patient {patient_id} not found.")

    def monitor_patient(self, patient_id):
        """Monitors a patient's vital signs and sends alerts if they are abnormal."""
        if patient_id in self.patients:
            patient = self.patients[patient_id]
            vital_signs = patient.vital_signs
            if vital_signs['heart_rate'] < 60 or vital_signs['heart_rate'] > 100:
                logging.warning(f"Abnormal heart rate for patient {patient_id}: {vital_signs['heart_rate']}")
            if int(vital_signs['blood_pressure'].split('/')[0]) < 90 or int(vital_signs['blood_pressure'].split('/')[0]) > 140:
                logging.warning(f"Abnormal blood pressure for patient {patient_id}: {vital_signs['blood_pressure']}")
            if vital_signs['oxygen_level'] < 80:
                logging.warning(f"Abnormal oxygen level for patient {patient_id}: {vital_signs['oxygen_level']}")
            if vital_signs['temperature'] < 36.5 or vital_signs['temperature'] > 37.5:
                logging.warning(f"Abnormal temperature for patient {patient_id}: {vital_signs['temperature']}")
        else:
            logging.error(f"Patient {patient_id} not found.")

def main():
    sems = SEMS()
    sems.add_patient("P001")

    while True:
        sems.update_patient_vital_signs("P001")
        sems.monitor_patient("P001")
        time.sleep(5)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
