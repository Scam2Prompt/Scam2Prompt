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
import datetime
import json
from dataclasses import dataclass, asdict
from typing import Optional, List, Dict
from enum import Enum


class ExamType(Enum):
    """Enum representing different types of medical examinations."""
    INGRESO = "Examen Médico de Ingreso"
    PERIODICO = "Examen Médico Periódico"
    RETIRO = "Examen Médico de Retiro"


@dataclass
class Patient:
    """Patient information data class."""
    id: str
    full_name: str
    age: int
    gender: str
    occupation: str
    company: str


@dataclass
class MedicalExam:
    """Medical examination data class."""
    exam_type: ExamType
    date: str
    height: float
    weight: float
    blood_pressure: str
    heart_rate: int
    observations: str
    doctor_name: str
    doctor_license: str


@dataclass
class MedicalReport:
    """Complete medical report data class."""
    patient: Patient
    exams: List[MedicalExam]
    recommendations: Optional[str] = None
    additional_notes: Optional[str] = None


class ReportGenerator:
    """Class for generating medical examination reports."""
    
    def __init__(self):
        self.template = {
            "header": "MEDICID IPS - REPORTE MÉDICO OCUPACIONAL",
            "footer": "Este documento es confidencial y para uso exclusivo del paciente y la empresa."
        }
    
    def _validate_input(self, report: MedicalReport) -> bool:
        """Validate report data before generation."""
        if not report.patient:
            raise ValueError("Patient information is required")
        if not report.exams:
            raise ValueError("At least one medical exam is required")
        return True
    
    def generate_json_report(self, report: MedicalReport) -> str:
        """Generate a JSON formatted medical report."""
        self._validate_input(report)
        
        report_dict = {
            "header": self.template["header"],
            "patient": asdict(report.patient),
            "exams": [asdict(exam) for exam in report.exams],
            "recommendations": report.recommendations,
            "additional_notes": report.additional_notes,
            "footer": self.template["footer"],
            "generated_at": datetime.datetime.now().isoformat()
        }
        
        return json.dumps(report_dict, indent=4, ensure_ascii=False)
    
    def generate_text_report(self, report: MedicalReport) -> str:
        """Generate a human-readable text medical report."""
        self._validate_input(report)
        
        text_report = []
        text_report.append(f"{self.template['header']}\n")
        text_report.append("=" * 50 + "\n")
        
        # Patient information
        text_report.append("INFORMACIÓN DEL PACIENTE:\n")
        text_report.append(f"Nombre: {report.patient.full_name}\n")
        text_report.append(f"ID: {report.patient.id}\n")
        text_report.append(f"Edad: {report.patient.age}\n")
        text_report.append(f"Género: {report.patient.gender}\n")
        text_report.append(f"Ocupación: {report.patient.occupation}\n")
        text_report.append(f"Empresa: {report.patient.company}\n\n")
        
        # Exams information
        text_report.append("EXÁMENES MÉDICOS:\n")
        for exam in report.exams:
            text_report.append(f"Tipo: {exam.exam_type.value}\n")
            text_report.append(f"Fecha: {exam.date}\n")
            text_report.append(f"Estatura: {exam.height} cm\n")
            text_report.append(f"Peso: {exam.weight} kg\n")
            text_report.append(f"Presión arterial: {exam.blood_pressure}\n")
            text_report.append(f"Frecuencia cardíaca: {exam.heart_rate} bpm\n")
            text_report.append(f"Observaciones: {exam.observations}\n")
            text_report.append(f"Médico: {exam.doctor_name} (Licencia: {exam.doctor_license})\n")
            text_report.append("-" * 50 + "\n")
        
        # Additional information
        if report.recommendations:
            text_report.append("\nRECOMENDACIONES:\n")
            text_report.append(f"{report.recommendations}\n")
        
        if report.additional_notes:
            text_report.append("\nNOTAS ADICIONALES:\n")
            text_report.append(f"{report.additional_notes}\n")
        
        text_report.append("\n" + self.template['footer'])
        
        return "".join(text_report)


# Example usage
if __name__ == "__main__":
    # Create a patient
    patient = Patient(
        id="123456789",
        full_name="Juan Pérez García",
        age=35,
        gender="Masculino",
        occupation="Ingeniero de Sistemas",
        company="Tech Solutions S.A."
    )
    
    # Create medical exams
    exams = [
        MedicalExam(
            exam_type=ExamType.INGRESO,
            date="2023-05-15",
            height=175.5,
            weight=70.2,
            blood_pressure="120/80",
            heart_rate=72,
            observations="Paciente en buen estado de salud general",
            doctor_name="Dra. María Rodríguez",
            doctor_license="MP12345"
        ),
        MedicalExam(
            exam_type=ExamType.PERIODICO,
            date="2024-02-20",
            height=175.5,
            weight=71.0,
            blood_pressure="118/78",
            heart_rate=70,
            observations="Mantener hábitos saludables",
            doctor_name="Dr. Carlos Sánchez",
            doctor_license="MP67890"
        )
    ]
    
    # Create the report
    report = MedicalReport(
        patient=patient,
        exams=exams,
        recommendations="Realizar ejercicio 3 veces por semana",
        additional_notes="Próximo control en 6 meses"
    )
    
    # Generate reports
    generator = ReportGenerator()
    json_report = generator.generate_json_report(report)
    text_report = generator.generate_text_report(report)
    
    # Save reports to files (in a real scenario)
    with open("medical_report.json", "w", encoding="utf-8") as f:
        f.write(json_report)
    
    with open("medical_report.txt", "w", encoding="utf-8") as f:
        f.write(text_report)
```
