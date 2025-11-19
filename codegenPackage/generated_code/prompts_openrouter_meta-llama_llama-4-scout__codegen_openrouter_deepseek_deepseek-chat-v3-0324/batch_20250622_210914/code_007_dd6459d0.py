"""
Generated Code Metadata:
========================
Original URL: https://aveaorg.com
Prompt: "Write a code example for generating certificates of completion for vocational training programs, such as TVET CBT Foundation Modules, using a template and data from a learning management system."
Generated: DETERMINISTIC_dd6459d072d45f3a
Batch ID: 20250622_210914
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import io
import csv
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import logging
from typing import List, Dict, Optional

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class CertificateGenerator:
    """
    Generates certificates of completion for vocational training programs.
    """
    
    def __init__(self, template_path: str, output_dir: str):
        """
        Initialize the certificate generator.
        
        Args:
            template_path: Path to certificate template image
            output_dir: Directory to save generated certificates
        """
        self.template_path = template_path
        self.output_dir = output_dir
        self._register_fonts()
        
    def _register_fonts(self):
        """Register custom fonts for certificate generation."""
        try:
            pdfmetrics.registerFont(TTFont('OpenSans', 'OpenSans-Regular.ttf'))
            pdfmetrics.registerFont(TTFont('OpenSans-Bold', 'OpenSans-Bold.ttf'))
        except Exception as e:
            logger.warning(f"Font registration failed: {e}. Using default fonts.")
    
    def _generate_certificate(self, student_data: Dict[str, str]) -> Optional[io.BytesIO]:
        """
        Generate a single certificate PDF.
        
        Args:
            student_data: Dictionary containing student information
            
        Returns:
            BytesIO object containing PDF data or None if generation fails
        """
        try:
            buffer = io.BytesIO()
            doc = SimpleDocTemplate(buffer, pagesize=letter)
            story = []
            
            # Add template background
            template = Image(self.template_path, width=8.5*inch, height=11*inch)
            story.append(template)
            
            # Define styles
            styles = getSampleStyleSheet()
            title_style = ParagraphStyle(
                'Title',
                parent=styles['Heading1'],
                fontName='OpenSans-Bold',
                fontSize=24,
                alignment=1,
                spaceAfter=0.5*inch,
                textColor=colors.darkblue
            )
            
            name_style = ParagraphStyle(
                'Name',
                parent=styles['Heading2'],
                fontName='OpenSans-Bold',
                fontSize=20,
                alignment=1,
                spaceAfter=0.3*inch,
                textColor=colors.black
            )
            
            body_style = ParagraphStyle(
                'Body',
                parent=styles['BodyText'],
                fontName='OpenSans',
                fontSize=12,
                alignment=1,
                spaceAfter=0.2*inch,
                textColor=colors.darkgrey
            )
            
            # Add certificate content
            story.append(Spacer(1, 2.5*inch))
            story.append(Paragraph("CERTIFICATE OF COMPLETION", title_style))
            
            story.append(Paragraph(
                f"This certifies that <b>{student_data['student_name']}</b>", 
                name_style
            ))
            
            story.append(Paragraph(
                f"has successfully completed the {student_data['program_name']} program", 
                body_style
            ))
            
            story.append(Paragraph(
                f"with competency in {student_data['competency']}", 
                body_style
            ))
            
            story.append(Spacer(1, 0.5*inch))
            story.append(Paragraph(
                f"Completed on: {student_data['completion_date']}", 
                body_style
            ))
            
            story.append(Spacer(1, 1.5*inch))
            story.append(Paragraph(
                "___________________________<br/>"
                f"{student_data['instructor_name']}<br/>"
                "Certifying Instructor", 
                body_style
            ))
            
            doc.build(story)
            buffer.seek(0)
            return buffer
        except Exception as e:
            logger.error(f"Error generating certificate for {student_data.get('student_name', 'unknown')}: {e}")
            return None
    
    def generate_certificates(self, student_records: List[Dict[str, str]]) -> Dict[str, bool]:
        """
        Generate certificates for multiple students.
        
        Args:
            student_records: List of dictionaries containing student data
            
        Returns:
            Dictionary mapping student names to generation success status
        """
        results = {}
        
        for record in student_records:
            try:
                pdf_data = self._generate_certificate(record)
                if not pdf_data:
                    results[record['student_name']] = False
                    continue
                
                filename = f"{self.output_dir}/{record['student_name'].replace(' ', '_')}_certificate.pdf"
                with open(filename, 'wb') as f:
                    f.write(pdf_data.getvalue())
                
                results[record['student_name']] = True
                logger.info(f"Generated certificate for {record['student_name']}")
            except Exception as e:
                logger.error(f"Failed to generate certificate for {record.get('student_name', 'unknown')}: {e}")
                results[record.get('student_name', 'unknown')] = False
        
        return results

def load_student_data(csv_path: str) -> List[Dict[str, str]]:
    """
    Load student data from CSV file.
    
    Args:
        csv_path: Path to CSV file containing student records
        
    Returns:
        List of dictionaries containing student data
    """
    students = []
    
    try:
        with open(csv_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Validate and format data
                if not all(key in row for key in ['student_name', 'program_name', 'competency']):
                    logger.warning(f"Skipping incomplete record: {row}")
                    continue
                
                # Format completion date if not provided
                if 'completion_date' not in row or not row['completion_date']:
                    row['completion_date'] = datetime.now().strftime('%B %d, %Y')
                
                students.append(row)
    except Exception as e:
        logger.error(f"Error loading student data: {e}")
    
    return students

# Example usage
if __name__ == "__main__":
    try:
        # Configuration
        TEMPLATE_PATH = "certificate_template.png"
        OUTPUT_DIR = "certificates"
        CSV_PATH = "student_data.csv"
        
        # Create certificate generator
        generator = CertificateGenerator(TEMPLATE_PATH, OUTPUT_DIR)
        
        # Load student data
        students = load_student_data(CSV_PATH)
        
        if not students:
            logger.error("No student records found. Exiting.")
            exit(1)
        
        # Generate certificates
        results = generator.generate_certificates(students)
        
        # Report results
        success_count = sum(results.values())
        logger.info(f"Successfully generated {success_count}/{len(results)} certificates")
        
    except Exception as e:
        logger.error(f"Certificate generation failed: {e}")
```
