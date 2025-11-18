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

Here's the Python code for parsing and organizing medical records into a structured format suitable for submission in guardianship cases:

```python
import os
import json
import re
from datetime import datetime

class MedicalRecordsOrganizer:
    """
    A class to parse and organize medical records into a structured format suitable for submission.
    """

    def __init__(self, input_dir, output_file):
        """
        Initializes the organizer with the input directory and output file path.

        :param input_dir: Path to the directory containing medical records (text or PDF files).
        :param output_file: Path to the output JSON file where organized records will be stored.
        """
        self.input_dir = input_dir
        self.output_file = output_file

    @staticmethod
    def _extract_date(text):
        """
        Extracts a date from the given text if present.

        :param text: Text content to search for a date.
        :return: Extracted date as a string (YYYY-MM-DD) or None if no date is found.
        """
        date_pattern = r'\b\d{4}-\d{2}-\d{2}\b'  # Matches dates in YYYY-MM-DD format
        match = re.search(date_pattern, text)
        return match.group(0) if match else None

    @staticmethod
    def _sanitize_text(text):
        """
        Sanitizes text by removing sensitive information.

        :param text: Original text content.
        :return: Sanitized text.
        """
        # Example: Removing SSNs (Social Security Numbers)
        ssn_pattern = r'\b\d{3}-\d{2}-\d{4}\b'
        sanitized_text = re.sub(ssn_pattern, '[REDACTED]', text)
        return sanitized_text

    def _parse_file(self, file_path):
        """
        Parses an individual medical record file.

        :param file_path: Path to the file being parsed.
        :return: Dictionary containing parsed information.
        """
        try:
            with open(file_path, 'r') as file:
                content = file.read()
                sanitized_content = self._sanitize_text(content)

                # Extract metadata
                record_date = self._extract_date(content)
                record = {
                    'file_name': os.path.basename(file_path),
                    'date': record_date,
                    'content': sanitized_content
                }
                return record
        except Exception as e:
            print(f"Error parsing file {file_path}: {e}")
            return None

    def organize_records(self):
        """
        Organizes medical records into a structured JSON format.

        :return: None
        """
        records = []
        try:
            # Iterate over files in the input directory
            for file_name in os.listdir(self.input_dir):
                file_path = os.path.join(self.input_dir, file_name)

                # Process only text files for simplicity (could be extended for PDFs, etc.)
                if os.path.isfile(file_path) and file_name.endswith('.txt'):
                    record = self._parse_file(file_path)
                    if record:
                        records.append(record)

            # Write organized records to the output JSON file
            with open(self.output_file, 'w') as output_file:
                json.dump(records, output_file, indent=4)

            print(f"Organized records saved to {self.output_file}")
        except Exception as e:
            print(f"Error organizing records: {e}")

# Example usage
if __name__ == "__main__":
    input_directory = './medical_records'  # Path to medical records directory
    output_json_file = './organized_records.json'  # Path to the output JSON file

    organizer = MedicalRecordsOrganizer(input_directory, output_json_file)
    organizer.organize_records()
```

### Key Features:
1. The code reads all `.txt` files from the specified directory, sanitizes sensitive data, attempts to extract dates, and organizes content into a structured format.
2. Errors during file reading or processing are handled gracefully with exception handling.
3. Outputs records in a JSON format, making it suitable for submission or further processing.

Ensure the directory and files exist before running the script, and adjust paths as necessary.
