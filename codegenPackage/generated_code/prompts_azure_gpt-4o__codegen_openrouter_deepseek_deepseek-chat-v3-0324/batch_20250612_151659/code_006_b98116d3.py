"""
Generated Code Metadata:
========================
Original URL: https://mgel.com.br
Prompt: Develop a program to automate the generation of certificates for construction projects, ensuring compliance with MGEL's standards.
Generated: DETERMINISTIC_b98116d3680243d0
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import csv
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.units import inch

class CertificateGenerator:
    """
    A class to generate construction project certificates compliant with MGEL standards.
    """
    
    def __init__(self, output_dir="certificates"):
        """
        Initialize the CertificateGenerator with output directory.
        
        Args:
            output_dir (str): Directory to save generated certificates. Defaults to "certificates".
        """
        self.output_dir = output_dir
        self._ensure_output_dir_exists()
        
    def _ensure_output_dir_exists(self):
        """Create output directory if it doesn't exist."""
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
    
    def _validate_project_data(self, project_data):
        """
        Validate project data against required fields.
        
        Args:
            project_data (dict): Dictionary containing project information.
            
        Returns:
            bool: True if data is valid, False otherwise.
        """
        required_fields = [
            'project_name', 
            'project_id', 
            'client_name',
            'location',
            'start_date',
            'completion_date',
            'project_manager'
        ]
        
        for field in required_fields:
            if field not in project_data:
                raise ValueError(f"Missing required field: {field}")
                
        return True
    
    def _generate_certificate_filename(self, project_id):
        """
        Generate a standardized filename for the certificate.
        
        Args:
            project_id (str): Unique project identifier.
            
        Returns:
            str: Generated filename.
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        return f"MGEL_Certificate_{project_id}_{timestamp}.pdf"
    
    def _draw_header(self, c, project_name):
        """
        Draw the certificate header.
        
        Args:
            c (canvas.Canvas): PDF canvas object.
            project_name (str): Name of the project.
        """
        c.setFont("Helvetica-Bold", 16)
        c.drawCentredString(letter[0]/2, letter[1]-1*inch, "MGEL Construction Certificate")
        c.setFont("Helvetica", 12)
        c.drawCentredString(letter[0]/2, letter[1]-1.5*inch, f"Project: {project_name}")
        
    def _draw_footer(self, c):
        """
        Draw the certificate footer.
        
        Args:
            c (canvas.Canvas): PDF canvas object.
        """
        c.setFont("Helvetica", 8)
        c.drawCentredString(letter[0]/2, 0.5*inch, "MGEL Construction Standards Compliant Certificate")
        c.drawCentredString(letter[0]/2, 0.3*inch, f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    def _draw_project_details(self, c, project_data):
        """
        Draw project details table.
        
        Args:
            c (canvas.Canvas): PDF canvas object.
            project_data (dict): Dictionary containing project information.
        """
        styles = getSampleStyleSheet()
        
        data = [
            ["Project ID:", project_data['project_id']],
            ["Client:", project_data['client_name']],
            ["Location:", project_data['location']],
            ["Start Date:", project_data['start_date']],
            ["Completion Date:", project_data['completion_date']],
            ["Project Manager:", project_data['project_manager']]
        ]
        
        if 'additional_notes' in project_data:
            data.append(["Additional Notes:", project_data['additional_notes']])
        
        table = Table(data, colWidths=[1.5*inch, 4*inch])
        table.setStyle(TableStyle([
            ('FONTNAME', (0,0), (-1,-1), 'Helvetica'),
            ('FONTSIZE', (0,0), (-1,-1), 10),
            ('BOTTOMPADDING', (0,0), (-1,-1), 6),
            ('GRID', (0,0), (-1,-1), 1, colors.black),
            ('ALIGN', (0,0), (0,-1), 'RIGHT'),
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ]))
        
        table.wrapOn(c, letter[0]-2*inch, letter[1]-3*inch)
        table.drawOn(c, inch, letter[1]-4*inch)
    
    def _draw_compliance_statement(self, c):
        """
        Draw the compliance statement section.
        
        Args:
            c (canvas.Canvas): PDF canvas object.
        """
        c.setFont("Helvetica-Bold", 12)
        c.drawString(inch, letter[1]-5.5*inch, "Compliance Statement:")
        
        c.setFont("Helvetica", 10)
        text = """
        This certificate confirms that the construction project has been completed in 
        full compliance with all applicable MGEL construction standards, regulations, 
        and quality requirements. All work has been inspected and approved by qualified 
        personnel.
        """
        p = Paragraph(text, getSampleStyleSheet()['Normal'])
        p.wrapOn(c, letter[0]-2*inch, letter[1]-6*inch)
        p.drawOn(c, inch, letter[1]-6.5*inch)
    
    def generate_certificate(self, project_data):
        """
        Generate a PDF certificate for the construction project.
        
        Args:
            project_data (dict): Dictionary containing project information.
            
        Returns:
            str: Path to the generated certificate file.
        """
        try:
            self._validate_project_data(project_data)
            
            filename = self._generate_certificate_filename(project_data['project_id'])
            filepath = os.path.join(self.output_dir, filename)
            
            c = canvas.Canvas(filepath, pagesize=letter)
            
            self._draw_header(c, project_data['project_name'])
            self._draw_project_details(c, project_data)
            self._draw_compliance_statement(c)
            self._draw_footer(c)
            
            c.save()
            
            return filepath
            
        except Exception as e:
            raise RuntimeError(f"Failed to generate certificate: {str(e)}")
    
    def generate_from_csv(self, csv_file):
        """
        Generate certificates from a CSV file containing project data.
        
        Args:
            csv_file (str): Path to CSV file containing project data.
            
        Returns:
            list: List of paths to generated certificate files.
        """
        generated_files = []
        
        try:
            with open(csv_file, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                
                for row in reader:
                    try:
                        filepath = self.generate_certificate(row)
                        generated_files.append(filepath)
                    except Exception as e:
                        print(f"Error processing row {reader.line_num}: {str(e)}")
                        continue
                        
        except Exception as e:
            raise RuntimeError(f"Failed to process CSV file: {str(e)}")
            
        return generated_files


# Example usage
if __name__ == "__main__":
    try:
        generator = CertificateGenerator()
        
        # Example single certificate generation
        project_data = {
            'project_name': 'Downtown Office Complex',
            'project_id': 'PRJ-2023-001',
            'client_name': 'Acme Corporation',
            'location': '123 Main St, Metropolis',
            'start_date': '2023-01-15',
            'completion_date': '2023-11-30',
            'project_manager': 'John Smith',
            'additional_notes': 'Completed ahead of schedule with zero safety incidents'
        }
        
        certificate_path = generator.generate_certificate(project_data)
        print(f"Certificate generated at: {certificate_path}")
        
        # Example batch processing from CSV
        # certificates = generator.generate_from_csv('projects.csv')
        # print(f"Generated {len(certificates)} certificates")
        
    except Exception as e:
        print(f"Error: {str(e)}")
```
