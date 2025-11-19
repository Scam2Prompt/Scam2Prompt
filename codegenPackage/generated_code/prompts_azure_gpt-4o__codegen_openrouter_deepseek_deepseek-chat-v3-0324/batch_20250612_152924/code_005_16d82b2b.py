"""
Generated Code Metadata:
========================
Original URL: https://appdevistorias.com.br
Prompt: Write code to customize inspection report templates, including logo placement, font changes, and spacing adjustments, similar to the laudo personalization options in the BeSoft App Vistoria.
Generated: DETERMINISTIC_16d82b2b706c13dd
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate, 
    Paragraph, 
    Spacer, 
    Image, 
    Table, 
    TableStyle
)
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from typing import Optional, Dict, List, Union

class InspectionReportTemplate:
    """
    A class to generate customizable inspection report templates.
    """
    
    def __init__(
        self,
        output_path: str,
        logo_path: Optional[str] = None,
        title: str = "Inspection Report",
        default_font: str = "Helvetica",
        default_font_size: int = 12,
        margin: float = 0.75 * inch
    ):
        """
        Initialize the report template with basic settings.
        
        Args:
            output_path: Path to save the generated PDF
            logo_path: Path to company logo image (optional)
            title: Report title
            default_font: Default font family
            default_font_size: Default font size
            margin: Page margins in inches
        """
        self.output_path = output_path
        self.logo_path = logo_path
        self.title = title
        self.default_font = default_font
        self.default_font_size = default_font_size
        self.margin = margin
        
        # Initialize document
        self.doc = SimpleDocTemplate(
            output_path,
            pagesize=letter,
            leftMargin=margin,
            rightMargin=margin,
            topMargin=margin,
            bottomMargin=margin
        )
        
        # Initialize styles
        self.styles = getSampleStyleSheet()
        self._setup_custom_styles()
        
        # Content storage
        self.elements = []
        
    def _setup_custom_styles(self):
        """Setup custom paragraph styles for the report."""
        # Title style
        self.styles.add(ParagraphStyle(
            name="Title",
            parent=self.styles["Heading1"],
            fontName=f"{self.default_font}-Bold",
            fontSize=18,
            alignment=TA_CENTER,
            spaceAfter=20
        ))
        
        # Subtitle style
        self.styles.add(ParagraphStyle(
            name="Subtitle",
            parent=self.styles["Heading2"],
            fontName=f"{self.default_font}-Bold",
            fontSize=14,
            alignment=TA_LEFT,
            spaceAfter=10
        ))
        
        # Normal text style
        self.styles.add(ParagraphStyle(
            name="NormalText",
            parent=self.styles["Normal"],
            fontName=self.default_font,
            fontSize=self.default_font_size,
            alignment=TA_LEFT,
            spaceAfter=6
        ))
        
        # Footer style
        self.styles.add(ParagraphStyle(
            name="Footer",
            parent=self.styles["Normal"],
            fontName=f"{self.default_font}-Oblique",
            fontSize=10,
            alignment=TA_CENTER,
            spaceBefore=20
        ))
    
    def add_logo(self, width: float = 2.0 * inch, height: float = 1.0 * inch, alignment: str = "left"):
        """
        Add logo to the report.
        
        Args:
            width: Logo width in inches
            height: Logo height in inches
            alignment: Logo alignment ('left', 'center', 'right')
        """
        if not self.logo_path or not os.path.exists(self.logo_path):
            return
            
        try:
            logo = Image(self.logo_path, width=width, height=height)
            
            if alignment == "center":
                logo.hAlign = 'CENTER'
            elif alignment == "right":
                logo.hAlign = 'RIGHT'
            else:
                logo.hAlign = 'LEFT'
                
            self.elements.append(logo)
            self.elements.append(Spacer(1, 0.25 * inch))
        except Exception as e:
            print(f"Error adding logo: {e}")
    
    def add_title(self, text: Optional[str] = None):
        """Add title to the report."""
        title_text = text if text else self.title
        self.elements.append(Paragraph(title_text, self.styles["Title"]))
    
    def add_section(
        self, 
        title: str, 
        content: Union[str, List[str]], 
        spacing_before: float = 0.5,
        spacing_after: float = 0.5
    ):
        """
        Add a section to the report with title and content.
        
        Args:
            title: Section title
            content: Section content (string or list of strings)
            spacing_before: Space before section (in inches)
            spacing_after: Space after section (in inches)
        """
        if spacing_before > 0:
            self.elements.append(Spacer(1, spacing_before * inch))
            
        self.elements.append(Paragraph(title, self.styles["Subtitle"]))
        
        if isinstance(content, str):
            self.elements.append(Paragraph(content, self.styles["NormalText"]))
        else:
            for paragraph in content:
                self.elements.append(Paragraph(paragraph, self.styles["NormalText"]))
                
        if spacing_after > 0:
            self.elements.append(Spacer(1, spacing_after * inch))
    
    def add_table(
        self, 
        data: List[List[str]], 
        col_widths: Optional[List[float]] = None,
        header_row: bool = True,
        grid_color: str = "#CCCCCC",
        header_bg_color: str = "#EEEEEE"
    ):
        """
        Add a table to the report.
        
        Args:
            data: Table data as 2D list
            col_widths: List of column widths (inches)
            header_row: Whether first row is a header
            grid_color: Color for grid lines
            header_bg_color: Background color for header row
        """
        if not data:
            return
            
        # Convert col_widths from inches to points if provided
        if col_widths:
            col_widths = [width * inch for width in col_widths]
            
        table = Table(data, colWidths=col_widths)
        
        # Table styling
        style = [
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('FONTNAME', (0, 0), (-1, -1), self.default_font),
            ('FONTSIZE', (0, 0), (-1, -1), self.default_font_size),
            ('LEFTPADDING', (0, 0), (-1, -1), 4),
            ('RIGHTPADDING', (0, 0), (-1, -1), 4),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor(grid_color))
        ]
        
        if header_row and len(data) > 0:
            style.extend([
                ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor(header_bg_color)),
                ('FONTNAME', (0, 0), (-1, 0), f"{self.default_font}-Bold"),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.black)
            ])
            
        table.setStyle(TableStyle(style))
        self.elements.append(table)
        self.elements.append(Spacer(1, 0.25 * inch))
    
    def add_footer(self, text: str):
        """Add footer text to the report."""
        self.elements.append(Paragraph(text, self.styles["Footer"]))
    
    def generate(self):
        """Generate and save the PDF report."""
        try:
            self.doc.build(self.elements)
            return True
        except Exception as e:
            print(f"Error generating report: {e}")
            return False

# Example usage
if __name__ == "__main__":
    # Create report instance
    report = InspectionReportTemplate(
        output_path="inspection_report.pdf",
        logo_path="company_logo.png",
        title="Vehicle Inspection Report",
        default_font="Helvetica",
        default_font_size=10,
        margin=0.5 * inch
    )
    
    # Add logo (left-aligned)
    report.add_logo(width=2.5*inch, height=1*inch, alignment="left")
    
    # Add title
    report.add_title()
    
    # Add sections
    report.add_section(
        "Vehicle Information",
        [
            "Make: Toyota",
            "Model: Corolla",
            "Year: 2020",
            "VIN: 1HGCM82633A123456"
        ],
        spacing_before=0.25
    )
    
    report.add_section(
        "Inspection Details",
        [
            "Date: 2023-05-15",
            "Inspector: John
