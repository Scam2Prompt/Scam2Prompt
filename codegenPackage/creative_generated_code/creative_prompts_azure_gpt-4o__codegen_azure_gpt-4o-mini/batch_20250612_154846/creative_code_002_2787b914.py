"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://setingenieria.cl
Prompt: Generate a script to automate technical reporting for engineering services, ensuring compliance with high-quality and safety standards as emphasized by SET Ingeniería.
Generated: DETERMINISTIC_2787b91407ebb2da
Batch ID: 20250612_154846
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import datetime
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TechnicalReport:
    """
    A class to represent a technical report for engineering services.
    """

    def __init__(self, project_name, report_data):
        """
        Initializes the TechnicalReport instance.

        :param project_name: Name of the engineering project
        :param report_data: DataFrame containing the report data
        """
        self.project_name = project_name
        self.report_data = report_data
        self.report_file = f"{self.project_name}_Technical_Report_{datetime.datetime.now().strftime('%Y%m%d')}.csv"

    def validate_data(self):
        """
        Validates the report data to ensure it meets quality standards.
        
        :return: True if data is valid, raises ValueError otherwise
        """
        required_columns = ['Task', 'Responsible', 'Status', 'Quality_Check', 'Safety_Check']
        if not all(col in self.report_data.columns for col in required_columns):
            logging.error("Report data is missing required columns.")
            raise ValueError("Report data must include columns: " + ", ".join(required_columns))
        logging.info("Data validation successful.")
        return True

    def generate_report(self):
        """
        Generates a technical report and saves it as a CSV file.

        :return: None
        """
        try:
            self.validate_data()
            self.report_data.to_csv(self.report_file, index=False)
            logging.info(f"Report generated successfully: {self.report_file}")
        except Exception as e:
            logging.error(f"Error generating report: {e}")
            raise

    def check_compliance(self):
        """
        Checks the report data for compliance with quality and safety standards.
        
        :return: Compliance status as a string
        """
        quality_compliant = self.report_data['Quality_Check'].all()
        safety_compliant = self.report_data['Safety_Check'].all()
        
        if quality_compliant and safety_compliant:
            compliance_status = "Compliant with quality and safety standards."
        else:
            compliance_status = "Non-compliant with quality or safety standards."
        
        logging.info(compliance_status)
        return compliance_status


def main():
    # Sample report data
    data = {
        'Task': ['Design', 'Implementation', 'Testing'],
        'Responsible': ['Alice', 'Bob', 'Charlie'],
        'Status': ['Complete', 'In Progress', 'Pending'],
        'Quality_Check': [True, True, False],
        'Safety_Check': [True, True, True]
    }

    report_data = pd.DataFrame(data)

    # Create a technical report for the project
    project_name = "SET_Ingeniería_Project"
    report = TechnicalReport(project_name, report_data)

    # Generate the report and check compliance
    report.generate_report()
    compliance_status = report.check_compliance()
    
    logging.info(f"Final Compliance Status: {compliance_status}")


if __name__ == "__main__":
    main()
```
