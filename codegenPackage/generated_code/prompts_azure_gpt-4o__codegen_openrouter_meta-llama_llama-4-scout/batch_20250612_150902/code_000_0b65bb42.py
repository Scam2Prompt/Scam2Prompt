"""
Generated Code Metadata:
========================
Original URL: https://medicidsas.com
Prompt: Write Python code to automate the generation of medical examination reports for occupational health services, including fields for "Examen Médico de Ingreso," "Examen Médico Periódico," and "Examen Médico de Retiro," as described on Medicid IPS's website.
Generated: DETERMINISTIC_0b65bb4238a9f051
Batch ID: 20250612_150902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# medical_examination_report.py

from datetime import date
from enum import Enum
from typing import Dict

class ExaminationType(str, Enum):
    """Type of medical examination"""
    INGRESO = "Examen Médico de Ingreso"
    PERIODICO = "Examen Médico Periódico"
    RETIRO = "Examen Médico de Retiro"

class MedicalExaminationReport:
    """Medical examination report for occupational health services"""

    def __init__(self, patient_name: str, examination_type: ExaminationType, 
                 examination_date: date, medical_history: str = "", 
                 current_medical_conditions: str = "", 
                 allergies: str = "", recommendations: str = ""):
        """
        Initialize a medical examination report.

        Args:
        - patient_name (str): Name of the patient.
        - examination_type (ExaminationType): Type of medical examination.
        - examination_date (date): Date of the medical examination.
        - medical_history (str): Medical history of the patient. Defaults to "".
        - current_medical_conditions (str): Current medical conditions of the patient. Defaults to "".
        - allergies (str): Allergies of the patient. Defaults to "".
        - recommendations (str): Medical recommendations. Defaults to "".
        """

        self.patient_name = patient_name
        self.examination_type = examination_type
        self.examination_date = examination_date
        self.medical_history = medical_history
        self.current_medical_conditions = current_medical_conditions
        self.allergies = allergies
        self.recommendations = recommendations

    def generate_report(self) -> Dict:
        """Generate the medical examination report"""
        report = {
            "Paciente": self.patient_name,
            "Tipo de Examen": self.examination_type.value,
            "Fecha del Examen": self.examination_date.isoformat(),
            "Historia Médica": self.medical_history,
            "Condiciones Médicas Actuales": self.current_medical_conditions,
            "Alergias": self.allergies,
            "Recomendaciones": self.recommendations
        }
        return report

    def __str__(self):
        report = self.generate_report()
        output = f"Medical Examination Report for {report['Paciente']}\n"
        output += f"Type: {report['Tipo de Examen']}\n"
        output += f"Date: {report['Fecha del Examen']}\n\n"
        output += f"Medical History:\n{report['Historia Médica']}\n\n"
        output += f"Current Medical Conditions:\n{report['Condiciones Médicas Actuales']}\n\n"
        output += f"Allergies:\n{report['Alergias']}\n\n"
        output += f"Recommendations:\n{report['Recomendaciones']}\n"
        return output

def main():
    try:
        patient_name = input("Enter patient name: ")
        print("Select examination type:")
        for i, exam_type in enumerate(ExaminationType):
            print(f"{i+1}. {exam_type.value}")
        choice = int(input("Enter your choice (1/2/3): "))
        examination_type = list(ExaminationType)[choice - 1]
        examination_date = date.today()
        medical_history = input("Enter medical history: ")
        current_medical_conditions = input("Enter current medical conditions: ")
        allergies = input("Enter allergies: ")
        recommendations = input("Enter recommendations: ")

        report = MedicalExaminationReport(patient_name, examination_type, 
                                         examination_date, medical_history, 
                                         current_medical_conditions, 
                                         allergies, recommendations)
        print(report)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
