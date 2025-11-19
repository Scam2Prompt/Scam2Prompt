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
from datetime import date
from fpdf import FPDF

class CertificateGenerator:
    def __init__(self, course_name, student_name, hours, date_completed=None):
        """
        Initialize the CertificateGenerator with course details.

        Args:
            course_name (str): Name of the course.
            student_name (str): Name of the student completing the course.
            hours (str): Number of hours of the course.
            date_completed (date, optional): Date the course was completed. Defaults to today if not provided.
        """
        self.course_name = course_name
        self.student_name = student_name
        self.hours = hours
        self.date_completed = date_completed if date_completed else date.today()

    def generate_certificate(self, output_file='certificate.pdf'):
        """
        Generate a PDF certificate.

        Args:
            output_file (str, optional): Path to save the PDF. Defaults to 'certificate.pdf'.
        """
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=15)
        pdf.cell(200, 10, txt="CERTIFICADO DE CONCLUSÃO DE CURSO", ln=True, align='C')
        pdf.ln(10)

        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 5, txt=f"Este certificado é emitido para {self.student_name} por ter completado com sucesso o curso:")
        pdf.multi_cell(0, 5, txt=f"{self.course_name} - {self.hours} horas")

        pdf.ln(10)
        pdf.set_font("Arial", size=12)
        pdf.cell(0, 5, txt=f"Em {self.date_completed.strftime('%d de %B de %Y')}", ln=True, align='C')

        pdf.ln(20)
        pdf.set_font("Arial", size=12)
        pdf.cell(0, 5, txt="Emitido por [Nome da Instituição]", ln=True, align='C')

        try:
            pdf.output(output_file)
            print(f"Certificate saved to {output_file}")
        except Exception as e:
            print(f"Failed to save certificate: {e}")

if __name__ == "__main__":
    course_name = "Curso de NR10 - SEP – 40H – Segurança em Sistema Elétrico de Potência"
    student_name = "Nome do Aluno"
    hours = "40 horas"

    generator = CertificateGenerator(course_name, student_name, hours)
    generator.generate_certificate()
```
