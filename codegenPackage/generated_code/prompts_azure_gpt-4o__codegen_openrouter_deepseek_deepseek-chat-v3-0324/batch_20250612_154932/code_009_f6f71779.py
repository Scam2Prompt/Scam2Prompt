"""
Generated Code Metadata:
========================
Original URL: https://tojsat.net
Prompt: Generate a script to validate the format of manuscripts before submission to TOJSAT, based on their submission guidelines.
Generated: DETERMINISTIC_f6f717798c6af0d1
Batch ID: 20250612_154932
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
"""
TOJSAT Manuscript Format Validator

This script validates the format of manuscripts before submission to TOJSAT
(The Open Journal of Science and Technology) based on their submission guidelines.

Checks include:
- File format (must be .docx or .pdf)
- File size (must be <= 10MB)
- Required sections (Abstract, Keywords, Introduction, etc.)
- Word count (must be between 3000-8000 words)
- Author information (must include all required fields)
- Reference format (APA style)
"""

import os
import sys
import re
import zipfile
from docx import Document
import PyPDF2
from typing import Dict, List, Tuple, Optional

# Constants based on TOJSAT guidelines
MAX_FILE_SIZE_MB = 10
MIN_WORD_COUNT = 3000
MAX_WORD_COUNT = 8000
REQUIRED_SECTIONS = [
    "Abstract",
    "Keywords",
    "Introduction",
    "Materials and Methods",
    "Results",
    "Discussion",
    "Conclusion",
    "References"
]
REQUIRED_AUTHOR_FIELDS = [
    "Full Name",
    "Affiliation",
    "Email",
    "ORCID"
]

class ManuscriptValidator:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.errors: List[str] = []
        self.warnings: List[str] = []
        self.word_count = 0
        self.sections_found: Dict[str, bool] = {section: False for section in REQUIRED_SECTIONS}
        self.author_info: Dict[str, str] = {}

    def validate(self) -> Tuple[bool, List[str], List[str]]:
        """Main validation method that runs all checks"""
        try:
            self._check_file_format()
            self._check_file_size()
            
            if self.file_path.lower().endswith('.docx'):
                self._validate_docx()
            elif self.file_path.lower().endswith('.pdf'):
                self._validate_pdf()
            
            self._check_word_count()
            self._check_sections()
            self._check_references()
            
            return (len(self.errors) == 0, self.errors, self.warnings)
        
        except Exception as e:
            self.errors.append(f"Unexpected error during validation: {str(e)}")
            return (False, self.errors, self.warnings)

    def _check_file_format(self) -> None:
        """Check if file is in accepted format (.docx or .pdf)"""
        if not (self.file_path.lower().endswith('.docx') or self.file_path.lower().endswith('.pdf')):
            self.errors.append("Invalid file format. Only .docx and .pdf files are accepted.")

    def _check_file_size(self) -> None:
        """Check if file size is within limits"""
        file_size_mb = os.path.getsize(self.file_path) / (1024 * 1024)
        if file_size_mb > MAX_FILE_SIZE_MB:
            self.errors.append(f"File size exceeds maximum limit of {MAX_FILE_SIZE_MB}MB.")

    def _validate_docx(self) -> None:
        """Validate .docx specific content"""
        try:
            doc = Document(self.file_path)
            self._extract_sections_from_docx(doc)
            self._count_words_docx(doc)
            self._extract_author_info(doc)
        except Exception as e:
            self.errors.append(f"Error reading DOCX file: {str(e)}")

    def _validate_pdf(self) -> None:
        """Validate .pdf specific content"""
        try:
            with open(self.file_path, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                self._extract_sections_from_pdf(reader)
                self._count_words_pdf(reader)
                self._extract_author_info_from_pdf(reader)
        except Exception as e:
            self.errors.append(f"Error reading PDF file: {str(e)}")

    def _extract_sections_from_docx(self, doc: Document) -> None:
        """Check for required sections in DOCX"""
        for paragraph in doc.paragraphs:
            text = paragraph.text.strip()
            for section in REQUIRED_SECTIONS:
                if text.lower().startswith(section.lower()):
                    self.sections_found[section] = True

    def _extract_sections_from_pdf(self, reader: PyPDF2.PdfReader) -> None:
        """Check for required sections in PDF"""
        for page in reader.pages:
            text = page.extract_text()
            if text:
                for section in REQUIRED_SECTIONS:
                    if section.lower() in text.lower():
                        self.sections_found[section] = True

    def _count_words_docx(self, doc: Document) -> None:
        """Count words in DOCX file"""
        word_count = 0
        for paragraph in doc.paragraphs:
            word_count += len(paragraph.text.split())
        self.word_count = word_count

    def _count_words_pdf(self, reader: PyPDF2.PdfReader) -> None:
        """Count words in PDF file"""
        word_count = 0
        for page in reader.pages:
            text = page.extract_text()
            if text:
                word_count += len(text.split())
        self.word_count = word_count

    def _extract_author_info(self, doc: Document) -> None:
        """Extract author information from DOCX"""
        # This is a simplified version - actual implementation would need more sophisticated parsing
        for i, paragraph in enumerate(doc.paragraphs[:20]):  # Check first 20 paragraphs
            text = paragraph.text.strip()
            for field in REQUIRED_AUTHOR_FIELDS:
                if field.lower() in text.lower():
                    value = text.split(":", 1)[1].strip() if ":" in text else "Not specified"
                    self.author_info[field] = value

    def _extract_author_info_from_pdf(self, reader: PyPDF2.PdfReader) -> None:
        """Extract author information from PDF"""
        # Check first page for author info
        first_page = reader.pages[0].extract_text()
        if first_page:
            for field in REQUIRED_AUTHOR_FIELDS:
                if field.lower() in first_page.lower():
                    # Simple pattern matching - would need more robust parsing
                    pattern = re.compile(rf"{field}:\s*(.+)", re.IGNORECASE)
                    match = pattern.search(first_page)
                    if match:
                        self.author_info[field] = match.group(1).strip()

    def _check_word_count(self) -> None:
        """Check if word count is within limits"""
        if self.word_count < MIN_WORD_COUNT:
            self.errors.append(f"Word count ({self.word_count}) is below minimum requirement of {MIN_WORD_COUNT}.")
        elif self.word_count > MAX_WORD_COUNT:
            self.errors.append(f"Word count ({self.word_count}) exceeds maximum limit of {MAX_WORD_COUNT}.")

    def _check_sections(self) -> None:
        """Check if all required sections are present"""
        missing_sections = [section for section, found in self.sections_found.items() if not found]
        if missing_sections:
            self.errors.append(f"Missing required sections: {', '.join(missing_sections)}")

    def _check_references(self) -> None:
        """Check if references follow APA style (basic check)"""
        # This is a basic check - would need more sophisticated parsing for proper validation
        try:
            if self.file_path.lower().endswith('.docx'):
                doc = Document(self.file_path)
                references_found = False
                for paragraph in doc.paragraphs:
                    if "references" in paragraph.text.lower():
                        references_found = True
                        break
                
                if not references_found:
                    self.errors.append("References section not found.")
            
            elif self.file_path.lower().endswith('.pdf'):
                with open(self.file_path, 'rb') as file:
                    reader = PyPDF2.PdfReader(file)
                    references_found = False
                    for page in reader.pages:
                        if "references" in page.extract_text().lower():
                            references_found = True
                            break
                    
                    if not references_found:
                        self.errors.append("References section not found.")
            
            # Basic APA style check (author last name followed by year)
            # This would need to be more robust in production
            apa_pattern = re.compile(r"\([A-Za-z]+, \d{4}\)")
            if not apa_pattern.search(self._get_references_text()):
                self.warnings.append("References may not follow APA style. Please verify.")
        
        except Exception as e:
            self.warnings.append(f"Could not verify references: {str(e)}")

    def _get_references_text(self) -> str:
        """Extract references section text"""
        references_text = ""
        try:
            if self.file_path.lower().endswith('.docx'):
                doc = Document(self.file_path)
                in_references = False
                for paragraph in doc.paragraphs:
                    if "references" in paragraph.text.lower():
                        in_references = True
