"""
Generated Code Metadata:
========================
Original URL: https://enacip.edu.pe
Prompt: "Generate a report in PDF format using a library like ReportLab or PyPDF2 that summarizes the benefits and offerings of ENACIP's diplomado programs in gestión pública and derecho."
Generated: DETERMINISTIC_63e523e8292ff5a7
Batch ID: 20250622_204809
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch
import os

def generate_enacip_diplomado_report(output_filename):
    """
    Generates a PDF report summarizing ENACIP's diplomado programs.
    
    Args:
        output_filename (str): Path to save the generated PDF file.
    """
    try:
        # Create document with letter size
        doc = SimpleDocTemplate(output_filename, pagesize=letter)
        
        # Container for the flowables
        elements = []
        
        # Get default style sheet
        styles = getSampleStyleSheet()
        
        # Add custom styles
        styles.add(ParagraphStyle(
            name='Title',
            parent=styles['Heading1'],
            fontSize=18,
            alignment=1,  # Center aligned
            spaceAfter=20
        ))
        
        styles.add(ParagraphStyle(
            name='Subtitle',
            parent=styles['Heading2'],
            fontSize=14,
            alignment=1,
            spaceAfter=15
        ))
        
        styles.add(ParagraphStyle(
            name='BodyText',
            parent=styles['BodyText'],
            fontSize=12,
            spaceAfter=12
        ))
        
        styles.add(ParagraphStyle(
            name='ProgramTitle',
            parent=styles['Heading3'],
            fontSize=13,
            textColor=colors.darkblue,
            spaceAfter=8
        ))
        
        # Add title
        elements.append(Paragraph("ENACIP Diplomado Programs", styles['Title']))
        elements.append(Spacer(1, 0.2 * inch))
        
        # Add subtitle
        elements.append(Paragraph("Summary of Benefits and Offerings", styles['Subtitle']))
        elements.append(Spacer(1, 0.5 * inch))
        
        # Add introduction
        intro_text = """
        The National School of Control (ENACIP) offers specialized diplomado programs 
        designed to enhance professional skills in public management and law. 
        These programs provide comprehensive training for public servants and legal professionals.
        """
        elements.append(Paragraph(intro_text, styles['BodyText']))
        elements.append(Spacer(1, 0.3 * inch))
        
        # Add Gestión Pública program
        elements.append(Paragraph("Diplomado en Gestión Pública", styles['ProgramTitle']))
        
        gestion_publica_benefits = [
            "• Comprehensive training in public administration",
            "• Focus on transparency and accountability",
            "• Tools for effective public policy implementation",
            "• Case studies from successful public programs",
            "• Networking with public sector professionals"
        ]
        
        for benefit in gestion_publica_benefits:
            elements.append(Paragraph(benefit, styles['BodyText']))
        
        elements.append(Spacer(1, 0.2 * inch))
        
        # Add Derecho program
        elements.append(Paragraph("Diplomado en Derecho", styles['ProgramTitle']))
        
        derecho_benefits = [
            "• Advanced legal training for practitioners",
            "• Focus on constitutional and administrative law",
            "• Practical application of legal principles",
            "• Updates on recent legal reforms",
            "• Interaction with leading legal experts"
        ]
        
        for benefit in derecho_benefits:
            elements.append(Paragraph(benefit, styles['BodyText']))
        
        elements.append(Spacer(1, 0.3 * inch))
        
        # Add general offerings
        elements.append(Paragraph("Program Offerings", styles['Subtitle']))
        
        offerings = [
            ["Duration", "6 months"],
            ["Format", "Blended (online and in-person)"],
            ["Certification", "Official ENACIP diploma upon completion"],
            ["Faculty", "Experienced professionals and academics"],
            ["Admission", "Open to professionals with relevant background"]
        ]
        
        # Create table
        table = Table(offerings, colWidths=[2*inch, 4*inch])
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 11),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.white),
            ('GRID', (0, 0), (-1, -1), 1, colors.lightgrey)
        ]))
        
        elements.append(table)
        elements.append(Spacer(1, 0.3 * inch))
        
        # Add conclusion
        conclusion_text = """
        These diplomado programs from ENACIP provide valuable professional development 
        opportunities for those working in public administration and legal fields. 
        Participants gain both theoretical knowledge and practical skills to excel 
        in their respective areas.
        """
        elements.append(Paragraph(conclusion_text, styles['BodyText']))
        
        # Build the document
        doc.build(elements)
        
        print(f"Successfully generated report: {output_filename}")
        
    except Exception as e:
        print(f"Error generating PDF report: {str(e)}")
        raise

if __name__ == "__main__":
    output_file = "enacip_diplomado_report.pdf"
    generate_enacip_diplomado_report(output_file)
```
