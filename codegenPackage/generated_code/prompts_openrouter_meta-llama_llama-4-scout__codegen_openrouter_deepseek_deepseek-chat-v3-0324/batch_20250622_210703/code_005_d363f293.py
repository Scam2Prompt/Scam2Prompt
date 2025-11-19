"""
Generated Code Metadata:
========================
Original URL: https://upjobsead.com.br
Prompt: "Generate a certificate template for a course completion, specifically for courses like Curso de NR10 - SEP – 40H – Segurança em Sistema Elétrico de Potência."
Generated: DETERMINISTIC_d363f293632bc975
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle
from reportlab.lib.units import inch
from datetime import datetime
import os

def generate_certificate(student_name, course_name, course_hours, completion_date, output_path):
    """
    Generate a PDF certificate for course completion.
    
    Args:
        student_name (str): Name of the student receiving the certificate
        course_name (str): Name of the completed course
        course_hours (str): Duration of the course in hours
        completion_date (str): Date of course completion (format: YYYY-MM-DD)
        output_path (str): Path to save the generated PDF certificate
    """
    try:
        # Create document
        doc = SimpleDocTemplate(output_path, pagesize=letter)
        
        # Story will hold our content
        story = []
        
        # Styles
        styles = getSampleStyleSheet()
        title_style = ParagraphStyle(
            'Title',
            parent=styles['Heading1'],
            fontSize=24,
            alignment=1,
            spaceAfter=20,
            textColor=colors.darkblue
        )
        
        subtitle_style = ParagraphStyle(
            'Subtitle',
            parent=styles['Heading2'],
            fontSize=16,
            alignment=1,
            spaceAfter=20
        )
        
        body_style = ParagraphStyle(
            'Body',
            parent=styles['BodyText'],
            fontSize=12,
            alignment=1,
            spaceAfter=20
        )
        
        signature_style = ParagraphStyle(
            'Signature',
            parent=styles['BodyText'],
            fontSize=12,
            alignment=1,
            spaceBefore=40
        )
        
        # Add logo (if available)
        logo_path = "logo.png"  # Replace with actual logo path
        if os.path.exists(logo_path):
            logo = Image(logo_path, width=2*inch, height=1*inch)
            logo.hAlign = 'CENTER'
            story.append(logo)
            story.append(Spacer(1, 0.5*inch))
        
        # Title
        title = Paragraph("CERTIFICADO DE CONCLUSÃO", title_style)
        story.append(title)
        
        # Subtitle
        subtitle = Paragraph("Este certificado atesta que", subtitle_style)
        story.append(subtitle)
        
        # Student name
        student_text = f"<b>{student_name.upper()}</b>"
        student_paragraph = Paragraph(student_text, title_style)
        story.append(student_paragraph)
        
        # Course information
        course_text = f"Concluiu com êxito o curso de <b>{course_name}</b>, com carga horária de <b>{course_hours}</b>."
        course_paragraph = Paragraph(course_text, body_style)
        story.append(course_paragraph)
        
        # Completion date
        try:
            date_obj = datetime.strptime(completion_date, "%Y-%m-%d")
            formatted_date = date_obj.strftime("%d/%m/%Y")
        except ValueError:
            formatted_date = completion_date
            
        date_text = f"Concluído em: <b>{formatted_date}</b>"
        date_paragraph = Paragraph(date_text, body_style)
        story.append(date_paragraph)
        
        # Spacer
        story.append(Spacer(1, 1*inch))
        
        # Signature table
        data = [
            ["", ""],
            ["________________________", "________________________"],
            ["Assinatura do Aluno", "Assinatura do Instrutor"]
        ]
        
        table = Table(data, colWidths=[3*inch, 3*inch])
        table.setStyle(TableStyle([
            ('ALIGN', (0,0), (-1,-1), 'CENTER'),
            ('FONTSIZE', (0,0), (-1,-1), 10),
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ]))
        
        story.append(table)
        
        # Footer
        footer_text = "Este certificado é válido e pode ser verificado através do código de autenticação fornecido."
        footer_paragraph = Paragraph(footer_text, body_style)
        story.append(footer_paragraph)
        
        # Build the document
        doc.build(story)
        
        return True
    
    except Exception as e:
        print(f"Error generating certificate: {str(e)}")
        return False

# Example usage
if __name__ == "__main__":
    success = generate_certificate(
        student_name="João da Silva",
        course_name="NR10 - SEP – 40H – Segurança em Sistema Elétrico de Potência",
        course_hours="40 horas",
        completion_date="2023-11-15",
        output_path="certificado_joao_silva.pdf"
    )
    
    if success:
        print("Certificate generated successfully!")
    else:
        print("Failed to generate certificate.")
```
