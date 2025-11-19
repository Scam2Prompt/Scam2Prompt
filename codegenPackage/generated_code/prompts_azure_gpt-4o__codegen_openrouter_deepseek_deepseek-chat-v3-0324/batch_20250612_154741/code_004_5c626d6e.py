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
import json
from datetime import datetime
from typing import Dict, List, Optional, Union
import PyPDF2
import docx

class MedicalRecordParser:
    """
    A class to parse and organize medical records for guardianship cases.
    Supports PDF and DOCX file formats.
    """
    
    def __init__(self, output_dir: str = "organized_records"):
        """
        Initialize the parser with an output directory.
        
        Args:
            output_dir (str): Directory to store organized records. Defaults to "organized_records".
        """
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)
        
    def parse_file(self, file_path: str) -> Dict[str, Union[str, List[str]]]:
        """
        Parse a medical record file and extract relevant information.
        
        Args:
            file_path (str): Path to the medical record file.
            
        Returns:
            Dict: Parsed record containing metadata and content.
            
        Raises:
            ValueError: If file format is not supported.
            FileNotFoundError: If file does not exist.
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
            
        file_ext = os.path.splitext(file_path)[1].lower()
        
        if file_ext == '.pdf':
            return self._parse_pdf(file_path)
        elif file_ext == '.docx':
            return self._parse_docx(file_path)
        else:
            raise ValueError(f"Unsupported file format: {file_ext}")
    
    def _parse_pdf(self, file_path: str) -> Dict[str, Union[str, List[str]]]:
        """
        Parse a PDF medical record.
        
        Args:
            file_path (str): Path to the PDF file.
            
        Returns:
            Dict: Parsed PDF content.
        """
        content = []
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                content.append(page.extract_text())
                
        return self._extract_metadata(file_path, content)
    
    def _parse_docx(self, file_path: str) -> Dict[str, Union[str, List[str]]]:
        """
        Parse a DOCX medical record.
        
        Args:
            file_path (str): Path to the DOCX file.
            
        Returns:
            Dict: Parsed DOCX content.
        """
        doc = docx.Document(file_path)
        content = [paragraph.text for paragraph in doc.paragraphs if paragraph.text.strip()]
        
        return self._extract_metadata(file_path, content)
    
    def _extract_metadata(self, file_path: str, content: List[str]) -> Dict[str, Union[str, List[str]]]:
        """
        Extract metadata from file content.
        
        Args:
            file_path (str): Path to the file.
            content (List[str]): Extracted content from the file.
            
        Returns:
            Dict: Record with metadata and content.
        """
        filename = os.path.basename(file_path)
        record_type = self._determine_record_type(filename, content)
        
        return {
            "filename": filename,
            "record_type": record_type,
            "date_processed": datetime.now().isoformat(),
            "content": content
        }
    
    def _determine_record_type(self, filename: str, content: List[str]) -> str:
        """
        Determine the type of medical record based on filename and content.
        
        Args:
            filename (str): Name of the file.
            content (List[str]): Content of the file.
            
        Returns:
            str: Type of record (e.g., "IEP", "Diagnosis", "Psych Report").
        """
        filename_lower = filename.lower()
        content_str = " ".join(content).lower()
        
        if 'iep' in filename_lower or 'iep' in content_str:
            return "IEP"
        elif 'diagnosis' in filename_lower or 'diagnosis' in content_str:
            return "Diagnosis"
        elif 'psych' in filename_lower or 'psych' in content_str or 'psychological' in content_str:
            return "Psych Report"
        elif 'school' in filename_lower or 'school' in content_str:
            return "School Record"
        else:
            return "Medical Record"
    
    def organize_records(self, files: List[str]) -> Dict[str, List[Dict[str, Union[str, List[str]]]]]:
        """
        Organize multiple medical records by type.
        
        Args:
            files (List[str]): List of file paths to process.
            
        Returns:
            Dict: Organized records grouped by type.
        """
        organized = {}
        
        for file_path in files:
            try:
                record = self.parse_file(file_path)
                record_type = record["record_type"]
                
                if record_type not in organized:
                    organized[record_type] = []
                organized[record_type].append(record)
                
                # Save individual record
                self._save_record(record)
                
            except Exception as e:
                print(f"Error processing {file_path}: {str(e)}")
                continue
                
        # Save organized collection
        self._save_organized(organized)
        return organized
    
    def _save_record(self, record: Dict[str, Union[str, List[str]]]) -> None:
        """
        Save an individual record to a JSON file.
        
        Args:
            record (Dict): Record to save.
        """
        filename = record["filename"]
        base_name = os.path.splitext(filename)[0]
        output_path = os.path.join(self.output_dir, f"{base_name}.json")
        
        with open(output_path, 'w') as f:
            json.dump(record, f, indent=2)
    
    def _save_organized(self, organized: Dict[str, List[Dict[str, Union[str, List[str]]]]]) -> None:
        """
        Save organized records to a master JSON file.
        
        Args:
            organized (Dict): Organized records to save.
        """
        output_path = os.path.join(self.output_dir, "organized_records.json")
        
        with open(output_path, 'w') as f:
            json.dump(organized, f, indent=2)
    
    def generate_guardianship_report(self, organized_records: Dict[str, List[Dict[str, Union[str, List[str]]]]]) -> str:
        """
        Generate a summary report suitable for guardianship submission.
        
        Args:
            organized_records (Dict): Organized records to include in report.
            
        Returns:
            str: Generated report in markdown format.
        """
        report = "# Guardianship Case Medical Records Report\n\n"
        report += f"Generated on: {datetime.now().strftime('%Y-%m-%d')}\n\n"
        
        for record_type, records in organized_records.items():
            report += f"## {record_type} Records\n\n"
            report += f"Count: {len(records)}\n\n"
            
            for record in records:
                report += f"### {record['filename']}\n"
                report += f"Processed: {record['date_processed']}\n\n"
                
                # Add first 3 lines of content as preview
                preview = "\n".join(record['content'][:3])
                report += f"Preview:\n```\n{preview}\n```\n\n"
        
        # Save report
        report_path = os.path.join(self.output_dir, "guardianship_report.md")
        with open(report_path, 'w') as f:
            f.write(report)
            
        return report


# Example usage
if __name__ == "__main__":
    parser = MedicalRecordParser()
    
    # Example files (replace with actual paths)
    sample_files = [
        "sample_iep.pdf",
        "diagnosis_report.docx",
        "psych_eval.pdf"
    ]
    
    # Process files
    organized = parser.organize_records(sample_files)
    
    # Generate report
    report = parser.generate_guardianship_report(organized)
    print("Report generated successfully.")
```
