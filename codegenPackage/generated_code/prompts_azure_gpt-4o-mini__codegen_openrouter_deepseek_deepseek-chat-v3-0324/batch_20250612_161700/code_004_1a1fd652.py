"""
Generated Code Metadata:
========================
Original URL: https://appdevistorias.com.br
Prompt: Create a function to generate a customizable inspection report in Word format, similar to the personalized reports offered by BeSoft.
Generated: DETERMINISTIC_1a1fd65204f42b84
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from datetime import datetime
from docx import Document
from docx.shared import Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

def generate_inspection_report(
    output_path: str,
    client_name: str,
    inspection_date: str,
    inspector_name: str,
    findings: list,
    recommendations: list,
    logo_path: str = None,
    template_path: str = None
) -> str:
    """
    Generates a customizable inspection report in Word format.

    Args:
        output_path (str): Path to save the generated report.
        client_name (str): Name of the client/organization.
        inspection_date (str): Date of inspection (format: YYYY-MM-DD).
        inspector_name (str): Name of the inspector.
        findings (list): List of findings (each item is a dict with 'title' and 'description').
        recommendations (list): List of recommendations (each item is a string).
        logo_path (str, optional): Path to company logo. Defaults to None.
        template_path (str, optional): Path to custom template. Defaults to None.

    Returns:
        str: Path to the generated report.

    Raises:
        ValueError: If required arguments are missing or invalid.
        FileNotFoundError: If logo_path or template_path don't exist.
    """
    # Validate inputs
    if not all([output_path, client_name, inspection_date, inspector_name]):
        raise ValueError("Missing required arguments")
    
    if not isinstance(findings, list) or not isinstance(recommendations, list):
        raise ValueError("Findings and recommendations must be lists")
    
    if logo_path and not os.path.exists(logo_path):
        raise FileNotFoundError(f"Logo file not found: {logo_path}")
    
    if template_path and not os.path.exists(template_path):
        raise FileNotFoundError(f"Template file not found: {template_path}")

    try:
        # Create or load document
        if template_path:
            doc = Document(template_path)
        else:
            doc = Document()
        
        # Add header with logo if provided
        if logo_path:
            header = doc.sections[0].header
            header_para = header.paragraphs[0] if header.paragraphs else header.add_paragraph()
            header_para.alignment = WD_ALIGN_PARAGRAPH.LEFT
            run = header_para.add_run()
            run.add_picture(logo_path, width=Inches(1.5))
        
        # Add title
        title = doc.add_heading('INSPECTION REPORT', level=0)
        title.alignment = WD_ALIGN_PARAGRAPH.CENTER
        title.runs[0].font.size = Pt(16)
        title.runs[0].bold = True
        
        # Add metadata table
        metadata = doc.add_table(rows=3, cols=2)
        metadata.alignment = WD_TABLE_ALIGNMENT.CENTER
        metadata.style = 'LightShading-Accent1'
        
        # Set table borders
        tbl = metadata._tbl
        tblBorders = OxmlElement('w:tblBorders')
        tblBorders.set(qn('w:top'), 'single')
        tblBorders.set(qn('w:left'), 'single')
        tblBorders.set(qn('w:bottom'), 'single')
        tblBorders.set(qn('w:right'), 'single')
        tblBorders.set(qn('w:insideH'), 'single')
        tblBorders.set(qn('w:insideV'), 'single')
        tbl.append(tblBorders)
        
        # Populate metadata
        cells = metadata.rows[0].cells
        cells[0].text = "Client:"
        cells[1].text = client_name
        
        cells = metadata.rows[1].cells
        cells[0].text = "Inspection Date:"
        cells[1].text = inspection_date
        
        cells = metadata.rows[2].cells
        cells[0].text = "Inspector:"
        cells[1].text = inspector_name
        
        # Add findings section
        doc.add_heading('Findings', level=1)
        for finding in findings:
            doc.add_heading(finding['title'], level=2)
            doc.add_paragraph(finding['description'])
        
        # Add recommendations section
        doc.add_heading('Recommendations', level=1)
        for idx, recommendation in enumerate(recommendations, 1):
            doc.add_paragraph(f"{idx}. {recommendation}", style='ListNumber')
        
        # Add footer with timestamp
        footer = doc.sections[0].footer
        footer_para = footer.paragraphs[0] if footer.paragraphs else footer.add_paragraph()
        footer_para.text = f"Report generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        footer_para.alignment = WD_ALIGN_PARAGRAPH.CENTER
        
        # Save document
        doc.save(output_path)
        return output_path
    
    except Exception as e:
        raise Exception(f"Error generating report: {str(e)}")
```
