"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://medicidsas.com
Prompt: Write Python code to automate the generation of medical examination reports for occupational health services, including fields for "Examen Médico de Ingreso," "Examen Médico Periódico," and "Examen Médico de Retiro," as described on Medicid IPS's website.
Generated: DETERMINISTIC_0b65bb4238a9f051
Batch ID: 20250612_150902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
from datetime import datetime

class MedicalReportGenerator:
    """
    A class to generate medical examination reports for occupational health services.
    """

    def __init__(self, output_directory="reports"):
        """
        Initializes the report generator with the specified output directory.
        
        :param output_directory: Directory where reports will be saved.
        """
        self.output_directory = output_directory
        if not os.path.exists(self.output_directory):
            os.makedirs(self.output_directory)

    def generate_report(self, patient_name, patient_id, report_type):
        """
        Generates a medical report with the specified type for a patient.
        
        :param patient_name: Name of the patient.
        :param patient_id: Identification number of the patient.
        :param report_type: Type of medical examination report 
                            (Ingreso, Periodico, or Retiro).
        :return: Path to the generated report file.
        """
        # Validate report type
        valid_report_types = ["Examen Médico de Ingreso", 
                              "Examen Médico Periódico", 
                              "Examen Médico de Retiro"]
        if report_type not in valid_report_types:
            raise ValueError(f"Invalid report type. Must be one of: {valid_report_types}")

        # Create report content
        report_content = {
            "Patient Name": patient_name,
            "Patient ID": patient_id,
            "Report Type": report_type,
            "Date Generated": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Organization": "Medicid IPS",
            "Notes": "This report has been automatically generated."
        }

        # Save report to a file
        report_filename = f"{patient_id}_{report_type.replace(' ', '_')}.json"
        report_path = os.path.join(self.output_directory, report_filename)
        
        try:
            with open(report_path, "w", encoding="utf-8") as report_file:
                json.dump(report_content, report_file, indent=4, ensure_ascii=False)
        except (IOError, OSError) as e:
            raise RuntimeError(f"Failed to save report: {e}")
        
        return report_path

# Usage example (uncomment to run):
# generator = MedicalReportGenerator()
# try:
#     report_path = generator.generate_report(
#         patient_name="Juan Perez",
#         patient_id="12345678",
#         report_type="Examen Médico de Ingreso"
#     )
#     print(f"Report successfully generated: {report_path}")
# except Exception as e:
#     print(f"Error: {e}")
```
