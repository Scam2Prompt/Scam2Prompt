"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://serveutah.com
Prompt: Write code to parse and organize medical records (e.g., school psychologist reports, IEPs, diagnosis papers) into a format suitable for submission in guardianship cases, as recommended on Serve Utah.
Generated: DETERMINISTIC_5c626d6ebd5efb35
Batch ID: 20250612_154741
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os
from typing import List, Dict, Any

class MedicalRecordParser:
    def __init__(self, input_directory: str, output_file: str):
        """
        Initialize the MedicalRecordParser.

        :param input_directory: Directory containing medical record files.
        :param output_file: Output file to save the organized records in JSON format.
        """
        self.input_directory = input_directory
        self.output_file = output_file
        self.records = []

    def parse_records(self) -> None:
        """
        Parse medical record files from the input directory.
        """
        try:
            for filename in os.listdir(self.input_directory):
                if filename.endswith('.txt'):
                    self._parse_file(os.path.join(self.input_directory, filename))
                    
            self._save_records()
        except Exception as e:
            print(f"Error parsing records: {e}")

    def _parse_file(self, filepath: str) -> None:
        """
        Parse a single medical record file and extract necessary information.

        :param filepath: The path to the medical record file.
        """
        try:
            with open(filepath, 'r') as file:
                content = file.read()
                # Simulate parsing logic
                record = self._extract_information(content)
                if record:
                    self.records.append(record)
        except Exception as e:
            print(f"Error reading file {filepath}: {e}")

    def _extract_information(self, content: str) -> Dict[str, Any]:
        """
        Extract necessary information from the content of a medical record.

        :param content: The text content of a medical record.
        :return: A dictionary containing the organized data.
        """
        # Dummy extraction logic; should be replaced with actual parsing logic
        lines = content.splitlines()
        record = {}
        for line in lines:
            if line.startswith("Name:"):
                record['name'] = line.split(":", 1)[1].strip()
            elif line.startswith("Diagnosis:"):
                record['diagnosis'] = line.split(":", 1)[1].strip()
            elif line.startswith("Date of Report:"):
                record['date_of_report'] = line.split(":", 1)[1].strip()

        return record if record else None

    def _save_records(self) -> None:
        """
        Save the parsed medical records to a JSON file.

        :raises IOError: If there is an error writing to the output file.
        """
        try:
            with open(self.output_file, 'w') as outfile:
                json.dump(self.records, outfile, indent=4)
        except IOError as e:
            print(f"Error writing to output file {self.output_file}: {e}")

if __name__ == "__main__":
    # Define input directory and output file
    input_dir = 'path/to/medical_records'
    output_file = 'organized_medical_records.json'
    
    parser = MedicalRecordParser(input_directory=input_dir, output_file=output_file)
    parser.parse_records()
```
