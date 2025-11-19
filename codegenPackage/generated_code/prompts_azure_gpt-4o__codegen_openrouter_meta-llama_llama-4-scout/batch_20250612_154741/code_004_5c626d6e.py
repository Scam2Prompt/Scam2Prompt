"""
Generated Code Metadata:
========================
Original URL: https://serveutah.com
Prompt: Write code to parse and organize medical records (e.g., school psychologist reports, IEPs, diagnosis papers) into a format suitable for submission in guardianship cases, as recommended on Serve Utah.
Generated: DETERMINISTIC_5c626d6ebd5efb35
Batch ID: 20250612_154741
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import re
from datetime import datetime
from typing import Dict, List

class MedicalRecord:
    def __init__(self, file_path: str):
        """
        Initialize a MedicalRecord object.

        Args:
        file_path (str): The path to the medical record file.
        """
        self.file_path = file_path
        self.record_type = None
        self.date = None
        self.diagnosis = []
        self.medications = []
        self.iep_goals = []

    def parse_record(self):
        """
        Parse the medical record and extract relevant information.
        """
        try:
            with open(self.file_path, 'r') as file:
                content = file.read()
                self.record_type = self._extract_record_type(content)
                self.date = self._extract_date(content)
                self.diagnosis = self._extract_diagnosis(content)
                self.medications = self._extract_medications(content)
                self.iep_goals = self._extract_iep_goals(content)
        except Exception as e:
            print(f"Error parsing record: {e}")

    def _extract_record_type(self, content: str) -> str:
        """
        Extract the record type (e.g., IEP, diagnosis paper).

        Args:
        content (str): The content of the medical record.

        Returns:
        str: The record type.
        """
        # Use regular expressions to match common record types
        record_types = ['IEP', 'diagnosis', 'psychologist report']
        for record_type in record_types:
            if re.search(record_type, content, re.IGNORECASE):
                return record_type
        return 'Unknown'

    def _extract_date(self, content: str) -> str:
        """
        Extract the date of the medical record.

        Args:
        content (str): The content of the medical record.

        Returns:
        str: The date in YYYY-MM-DD format.
        """
        # Use regular expressions to match common date formats
        date_formats = ['\d{1,2}/\d{1,2}/\d{4}', '\d{1,2}-\d{1,2}-\d{4}', '\d{1,2}\.\d{1,2}\.\d{4}']
        for date_format in date_formats:
            match = re.search(date_format, content)
            if match:
                try:
                    date = datetime.strptime(match.group(), '%m/%d/%Y')
                    return date.strftime('%Y-%m-%d')
                except ValueError:
                    pass
        return None

    def _extract_diagnosis(self, content: str) -> List[str]:
        """
        Extract the diagnosis information.

        Args:
        content (str): The content of the medical record.

        Returns:
        List[str]: A list of diagnosis.
        """
        # Use regular expressions to match common diagnosis phrases
        diagnosis_phrases = ['diagnosis:', 'diagnosed with']
        diagnosis = []
        for phrase in diagnosis_phrases:
            match = re.search(phrase + ' (.*)', content, re.IGNORECASE)
            if match:
                diagnosis.append(match.group(1).strip())
        return diagnosis

    def _extract_medications(self, content: str) -> List[str]:
        """
        Extract the medication information.

        Args:
        content (str): The content of the medical record.

        Returns:
        List[str]: A list of medications.
        """
        # Use regular expressions to match common medication phrases
        medication_phrases = ['medication:', 'prescribed']
        medications = []
        for phrase in medication_phrases:
            match = re.search(phrase + ' (.*)', content, re.IGNORECASE)
            if match:
                medications.append(match.group(1).strip())
        return medications

    def _extract_iep_goals(self, content: str) -> List[str]:
        """
        Extract the IEP goals.

        Args:
        content (str): The content of the medical record.

        Returns:
        List[str]: A list of IEP goals.
        """
        # Use regular expressions to match common IEP goal phrases
        iep_goal_phrases = ['IEP goals:', 'annual goals']
        iep_goals = []
        for phrase in iep_goal_phrases:
            match = re.search(phrase + ' (.*)', content, re.IGNORECASE | re.DOTALL)
            if match:
                iep_goals.append(match.group(1).strip())
        return iep_goals

def organize_medical_records(file_paths: List[str]) -> Dict[str, List[MedicalRecord]]:
    """
    Organize medical records by record type.

    Args:
    file_paths (List[str]): A list of file paths to medical records.

    Returns:
    Dict[str, List[MedicalRecord]]: A dictionary of medical records organized by record type.
    """
    organized_records = {}
    for file_path in file_paths:
        record = MedicalRecord(file_path)
        record.parse_record()
        if record.record_type not in organized_records:
            organized_records[record.record_type] = []
        organized_records[record.record_type].append(record)
    return organized_records

def main():
    # Example usage
    file_paths = ['path/to/record1.pdf', 'path/to/record2.pdf']
    organized_records = organize_medical_records(file_paths)
    for record_type, records in organized_records.items():
        print(f"Record Type: {record_type}")
        for record in records:
            print(f"Date: {record.date}")
            print(f"Diagnosis: {record.diagnosis}")
            print(f"Medications: {record.medications}")
            print(f"IEP Goals: {record.iep_goals}")
            print('------------------------')

if __name__ == '__main__':
    main()
```
