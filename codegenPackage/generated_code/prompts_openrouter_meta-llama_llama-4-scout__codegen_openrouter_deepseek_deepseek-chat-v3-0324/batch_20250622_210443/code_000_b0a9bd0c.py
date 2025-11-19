"""
Generated Code Metadata:
========================
Original URL: https://appdevistorias.com.br
Prompt: "Write a Python code snippet to generate a property inspection report with unlimited photos and customizable documents, similar to the App Vistoria application by BeSoft."
Generated: DETERMINISTIC_b0a9bd0cae94b7c4
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import datetime
import uuid
from typing import List, Dict, Optional
from dataclasses import dataclass
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch
from PIL import Image as PILImage


@dataclass
class Photo:
    file_path: str
    caption: str = ""
    width: float = 4.0  # inches
    height: float = 3.0  # inches


@dataclass
class Section:
    title: str
    content: str
    photos: List[Photo] = None


@dataclass
class PropertyInspectionReport:
    property_address: str
    inspector_name: str
    inspection_date: datetime.date
    sections: List[Section]
    logo_path: Optional[str] = None
    client_name: Optional[str] = None
    report_id: Optional[str] = None

    def __post_init__(self):
        if self.report_id is None:
            self.report_id = str(uuid.uuid4())[:8]
        if self.sections is None:
            self.sections = []
        for section in self.sections:
            if section.photos is None:
                section.photos = []


class ReportGenerator:
    @staticmethod
    def generate_pdf_report(report: PropertyInspectionReport, output_path: str) -> str:
        """
        Generates a PDF inspection report with photos and custom sections.
        
        Args:
            report: PropertyInspectionReport object containing all report data
            output_path: Directory where the PDF will be saved
            
        Returns:
            Path to the generated PDF file
            
        Raises:
            FileNotFoundError: If logo file or photos are not found
            ValueError: If output directory is invalid
        """
        if not os.path.exists(output_path):
            raise ValueError(f"Output directory does not exist: {output_path}")

        filename = f"Property_Inspection_Report_{report.report_id}.pdf"
        full_path = os.path.join(output_path, filename)
        
        doc = SimpleDocTemplate(
            full_path,
            pagesize=letter,
            rightMargin=72,
            leftMargin=72,
            topMargin=72,
            bottomMargin=18
        )
        
        styles = getSampleStyleSheet()
        styles.add(ParagraphStyle(name='SectionTitle', fontSize=14, leading=16, spaceAfter=12))
        styles.add(ParagraphStyle(name='Caption', fontSize=8, leading=10, spaceBefore=6))
        
        elements = []
        
        # Add header
        if report.logo_path:
            if not os.path.exists(report.logo_path):
                raise FileNotFoundError(f"Logo file not found: {report.logo_path}")
            logo = Image(report.logo_path, width=2*inch, height=1*inch)
            elements.append(logo)
            elements.append(Spacer(1, 12))
        
        elements.append(Paragraph(f"<b>Property Inspection Report</b>", styles['Title']))
        elements.append(Spacer(1, 12))
        
        # Add metadata
        meta_data = [
            [f"<b>Report ID:</b> {report.report_id}"],
            [f"<b>Property Address:</b> {report.property_address}"],
            [f"<b>Inspector:</b> {report.inspector_name}"],
            [f"<b>Date:</b> {report.inspection_date.strftime('%Y-%m-%d')}"]
        ]
        
        if report.client_name:
            meta_data.append([f"<b>Client:</b> {report.client_name}"])
        
        meta_table = Table(meta_data)
        meta_table.setStyle(TableStyle([
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('LEFTPADDING', (0, 0), (-1, -1), 0),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ]))
        elements.append(meta_table)
        elements.append(Spacer(1, 24))
        
        # Add sections
        for section in report.sections:
            elements.append(Paragraph(f"<b>{section.title}</b>", styles['SectionTitle']))
            elements.append(Paragraph(section.content, styles['BodyText']))
            elements.append(Spacer(1, 12))
            
            # Add photos if they exist
            if section.photos:
                for photo in section.photos:
                    if not os.path.exists(photo.file_path):
                        raise FileNotFoundError(f"Photo file not found: {photo.file_path}")
                    
                    # Resize image while maintaining aspect ratio
                    img = PILImage.open(photo.file_path)
                    img.thumbnail((photo.width * 300, photo.height * 300))  # 300 DPI
                    temp_path = f"temp_{os.path.basename(photo.file_path)}"
                    img.save(temp_path)
                    
                    reportlab_img = Image(temp_path, width=photo.width*inch, height=photo.height*inch)
                    elements.append(reportlab_img)
                    
                    if photo.caption:
                        elements.append(Paragraph(f"<i>{photo.caption}</i>", styles['Caption']))
                    
                    elements.append(Spacer(1, 12))
                    os.remove(temp_path)
            
            elements.append(Spacer(1, 24))
        
        doc.build(elements)
        return full_path


# Example usage
if __name__ == "__main__":
    try:
        # Create sample report
        sample_report = PropertyInspectionReport(
            property_address="123 Main St, Anytown, USA",
            inspector_name="John Doe",
            inspection_date=datetime.date.today(),
            client_name="ABC Properties",
            logo_path="logo.png",  # Replace with actual logo path
            sections=[
                Section(
                    title="Exterior Inspection",
                    content="The exterior of the property shows normal wear and tear. No major issues found.",
                    photos=[
                        Photo(
                            file_path="exterior1.jpg",  # Replace with actual photo path
                            caption="Front view of the property",
                            width=5.0,
                            height=3.75
                        ),
                        Photo(
                            file_path="exterior2.jpg",  # Replace with actual photo path
                            caption="Side view showing landscaping"
                        )
                    ]
                ),
                Section(
                    title="Interior Inspection",
                    content="The interior is in good condition with minor cosmetic issues noted.",
                    photos=[
                        Photo(
                            file_path="living_room.jpg",  # Replace with actual photo path
                            caption="Living room showing flooring condition"
                        )
                    ]
                )
            ]
        )
        
        # Generate PDF
        output_dir = "reports"
        os.makedirs(output_dir, exist_ok=True)
        pdf_path = ReportGenerator.generate_pdf_report(sample_report, output_dir)
        print(f"Report generated successfully: {pdf_path}")
    
    except Exception as e:
        print(f"Error generating report: {str(e)}")
```
