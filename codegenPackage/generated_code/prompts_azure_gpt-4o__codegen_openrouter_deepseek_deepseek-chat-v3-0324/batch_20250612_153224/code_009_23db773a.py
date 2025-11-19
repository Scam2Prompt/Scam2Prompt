"""
Generated Code Metadata:
========================
Original URL: https://munasimkullakita.org
Prompt: Create a script to automate the generation of educational materials for prevention programs targeting violence and exploitation, as described in Fundación Munasim Kullakita's initiatives.
Generated: DETERMINISTIC_23db773a26aac9a7
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script to automate the generation of educational materials for prevention programs
targeting violence and exploitation, as per Fundación Munasim Kullakita's initiatives.
"""

import os
import json
import datetime
from fpdf import FPDF
from docx import Document
from typing import Dict, List, Optional
from pathlib import Path

class EducationalMaterialGenerator:
    """
    A class to generate educational materials in various formats (PDF, DOCX, TXT).
    """
    
    def __init__(self, output_dir: str = "output_materials"):
        """
        Initialize the generator with output directory.
        
        Args:
            output_dir (str): Directory to save generated materials. Defaults to "output_materials".
        """
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        
    def _validate_content(self, content: Dict) -> bool:
        """
        Validate the content dictionary structure.
        
        Args:
            content (Dict): Content to validate
            
        Returns:
            bool: True if valid, False otherwise
        """
        required_fields = {'title', 'target_audience', 'modules'}
        if not all(field in content for field in required_fields):
            return False
        if not isinstance(content['modules'], list):
            return False
        return True
    
    def generate_pdf(self, content: Dict, filename: Optional[str] = None) -> str:
        """
        Generate a PDF document from the provided content.
        
        Args:
            content (Dict): Dictionary containing material content
            filename (Optional[str]): Output filename. If None, generates from title.
            
        Returns:
            str: Path to generated PDF file
            
        Raises:
            ValueError: If content is invalid
        """
        if not self._validate_content(content):
            raise ValueError("Invalid content structure")
            
        if filename is None:
            filename = f"{content['title'].replace(' ', '_')}.pdf"
        output_path = self.output_dir / filename
        
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        
        # Title
        pdf.set_font("Arial", 'B', 16)
        pdf.cell(200, 10, txt=content['title'], ln=1, align='C')
        pdf.ln(10)
        
        # Metadata
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt=f"Target Audience: {content['target_audience']}", ln=1)
        pdf.cell(200, 10, txt=f"Generated on: {datetime.datetime.now().strftime('%Y-%m-%d')}", ln=1)
        pdf.ln(10)
        
        # Modules
        pdf.set_font("Arial", 'B', 14)
        pdf.cell(200, 10, txt="Modules:", ln=1)
        pdf.set_font("Arial", size=12)
        
        for i, module in enumerate(content['modules'], 1):
            pdf.ln(5)
            pdf.set_font("Arial", 'B', 12)
            pdf.cell(200, 10, txt=f"Module {i}: {module['title']}", ln=1)
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 10, txt=module['content'])
            pdf.ln(5)
        
        pdf.output(output_path)
        return str(output_path)
    
    def generate_docx(self, content: Dict, filename: Optional[str] = None) -> str:
        """
        Generate a DOCX document from the provided content.
        
        Args:
            content (Dict): Dictionary containing material content
            filename (Optional[str]): Output filename. If None, generates from title.
            
        Returns:
            str: Path to generated DOCX file
            
        Raises:
            ValueError: If content is invalid
        """
        if not self._validate_content(content):
            raise ValueError("Invalid content structure")
            
        if filename is None:
            filename = f"{content['title'].replace(' ', '_')}.docx"
        output_path = self.output_dir / filename
        
        doc = Document()
        
        # Title
        doc.add_heading(content['title'], level=0)
        
        # Metadata
        doc.add_paragraph(f"Target Audience: {content['target_audience']}")
        doc.add_paragraph(f"Generated on: {datetime.datetime.now().strftime('%Y-%m-%d')}")
        doc.add_paragraph()
        
        # Modules
        doc.add_heading("Modules", level=1)
        
        for i, module in enumerate(content['modules'], 1):
            doc.add_heading(f"Module {i}: {module['title']}", level=2)
            doc.add_paragraph(module['content'])
            doc.add_paragraph()
        
        doc.save(output_path)
        return str(output_path)
    
    def generate_txt(self, content: Dict, filename: Optional[str] = None) -> str:
        """
        Generate a plain text document from the provided content.
        
        Args:
            content (Dict): Dictionary containing material content
            filename (Optional[str]): Output filename. If None, generates from title.
            
        Returns:
            str: Path to generated TXT file
            
        Raises:
            ValueError: If content is invalid
        """
        if not self._validate_content(content):
            raise ValueError("Invalid content structure")
            
        if filename is None:
            filename = f"{content['title'].replace(' ', '_')}.txt"
        output_path = self.output_dir / filename
        
        with open(output_path, 'w', encoding='utf-8') as f:
            # Title
            f.write(f"{content['title']}\n")
            f.write("=" * len(content['title']) + "\n\n")
            
            # Metadata
            f.write(f"Target Audience: {content['target_audience']}\n")
            f.write(f"Generated on: {datetime.datetime.now().strftime('%Y-%m-%d')}\n\n")
            
            # Modules
            f.write("MODULES:\n")
            f.write("--------\n")
            
            for i, module in enumerate(content['modules'], 1):
                f.write(f"\nModule {i}: {module['title']}\n")
                f.write("-" * (len(module['title']) + 10) + "\n")
                f.write(f"{module['content']}\n")
        
        return str(output_path)
    
    def generate_all_formats(self, content: Dict, base_filename: Optional[str] = None) -> Dict[str, str]:
        """
        Generate materials in all available formats (PDF, DOCX, TXT).
        
        Args:
            content (Dict): Dictionary containing material content
            base_filename (Optional[str]): Base filename without extension
            
        Returns:
            Dict[str, str]: Dictionary mapping format to file path
            
        Raises:
            ValueError: If content is invalid
        """
        if base_filename is None:
            base_filename = content['title'].replace(' ', '_')
            
        return {
            'pdf': self.generate_pdf(content, f"{base_filename}.pdf"),
            'docx': self.generate_docx(content, f"{base_filename}.docx"),
            'txt': self.generate_txt(content, f"{base_filename}.txt")
        }

def load_content_from_json(json_file: str) -> Dict:
    """
    Load content from a JSON file.
    
    Args:
        json_file (str): Path to JSON file
        
    Returns:
        Dict: Parsed content
        
    Raises:
        FileNotFoundError: If file doesn't exist
        json.JSONDecodeError: If invalid JSON
    """
    with open(json_file, 'r', encoding='utf-8') as f:
        return json.load(f)

def main():
    """
    Main execution function with example usage.
    """
    try:
        # Example content (in production, this would come from a file or database)
        example_content = {
            "title": "Prevention of Violence and Exploitation",
            "target_audience": "Adolescents (12-18 years)",
            "modules": [
                {
                    "title": "Understanding Violence",
                    "content": "This module covers the different forms of violence and their impact on individuals and communities."
                },
                {
                    "title": "Safe Relationships",
                    "content": "Learn how to establish and maintain healthy relationships while recognizing warning signs."
                },
                {
                    "title": "Community Resources",
                    "content": "Information about local resources and support systems available for those affected by violence."
                }
            ]
        }
        
        # Initialize generator
        generator = EducationalMaterialGenerator()
        
        # Generate all formats
        generated_files = generator.generate_all_formats(example_content)
        
        print("Successfully generated materials:")
        for format_type, filepath in generated_files.items():
            print(f"- {format_type.upper()}: {filepath}")
            
    except Exception as e:
        print(f"Error generating materials: {str(e)}")
        return 1
    
    return 0

if __name__ == "__main__":
    import sys
    sys.exit(main())
```
