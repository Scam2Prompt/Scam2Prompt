"""
Generated Code Metadata:
========================
Original URL: https://hooshmand-teb.ir
Prompt: Create a sample application that utilizes the Smart Emergency Medical System (SEMS) to enhance patient care, referencing the solutions provided by Hooshmand Teb.
Generated: DETERMINISTIC_dabb8d38b04341fd
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Smart Emergency Medical System (SEMS) Application
This application simulates a Smart Emergency Medical System (SEMS) to enhance patient care.
It integrates features inspired by solutions provided by Hooshmand Teb, such as patient monitoring,
emergency alerts, and data-driven decision-making.

Author: Professional Software Developer
Date: YYYY-MM-DD
"""

import time
import random
import logging

# Configure logging for the application
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("sems_app.log"), logging.StreamHandler()],
)

class Patient:
    """
    Represents a patient in the SEMS system.
    Attributes:
        id (int): Unique identifier for the patient.
        name (str): Name of the patient.
        age (int): Age of the patient.
        vitals (dict): Dictionary containing vital signs (e.g., heart rate, blood pressure).
    """
    def __init__(self, patient_id, name, age):
        self.id = patient_id
        self.name = name
        self.age = age
        self.vitals = {
            "heart_rate": 0,
            "blood_pressure": "0/0",
            "oxygen_saturation": 0,
        }

    def update_vitals(self, heart_rate, blood_pressure, oxygen_saturation):
        """
        Updates the patient's vital signs.
        """
        self.vitals["heart_rate"] = heart_rate
        self.vitals["blood_pressure"] = blood_pressure
        self.vitals["oxygen_saturation"] = oxygen_saturation


class SEMS:
    """
    Smart Emergency Medical System (SEMS) class.
    Attributes:
        patients (list): List of registered patients.
    """
    def __init__(self):
        self.patients = []

    def register_patient(self, patient):
        """
        Registers a new patient in the system.
        """
        self.patients.append(patient)
        logging.info(f"Patient registered: {patient.name} (ID: {patient.id})")

    def monitor_patients(self):
        """
        Continuously monitors patients' vital signs and triggers alerts if necessary.
        """
        logging.info("Starting patient monitoring...")
        try:
            while True:
                for patient in self.patients:
                    # Simulate random vital sign updates
                    heart_rate = random.randint(50, 120)
                    blood_pressure = f"{random.randint(90, 140)}/{random.randint(60, 90)}"
                    oxygen_saturation = random.randint(85, 100)

                    patient.update_vitals(heart_rate, blood_pressure, oxygen_saturation)
                    logging.info(
                        f"Updated vitals for {patient.name} (ID: {patient.id}): "
                        f"Heart Rate: {heart_rate}, Blood Pressure: {blood_pressure}, "
                        f"Oxygen Saturation: {oxygen_saturation}%"
                    )

                    # Trigger alerts for abnormal vitals
                    self.check_for_alerts(patient)

                time.sleep(5)  # Simulate a delay between monitoring cycles
        except KeyboardInterrupt:
            logging.info("Patient monitoring stopped.")

    def check_for_alerts(self, patient):
        """
        Checks a patient's vitals and triggers alerts for abnormal values.
        """
        heart_rate = patient.vitals["heart_rate"]
        blood_pressure = patient.vitals["blood_pressure"]
        oxygen_saturation = patient.vitals["oxygen_saturation"]

        # Example thresholds for alerts
        if heart_rate < 60 or heart_rate > 100:
            logging.warning(
                f"ALERT: Abnormal heart rate for {patient.name} (ID: {patient.id}): {heart_rate} bpm"
            )
        if oxygen_saturation < 90:
            logging.warning(
                f"ALERT: Low oxygen saturation for {patient.name} (ID: {patient.id}): {oxygen_saturation}%"
            )
        # Add more alert conditions as needed


# Main application logic
if __name__ == "__main__":
    # Initialize the SEMS system
    sems = SEMS()

    # Register sample patients
    patient1 = Patient(1, "John Doe", 45)
    patient2 = Patient(2, "Jane Smith", 60)

    sems.register_patient(patient1)
    sems.register_patient(patient2)

    # Start monitoring patients
    sems.monitor_patients()
```
