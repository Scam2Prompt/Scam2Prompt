"""
Generated Code Metadata:
========================
Original URL: https://fdixchange.com
Prompt: "Generate a sample invoice template in PSD format with a specific font style and layout."
Generated: DETERMINISTIC_2e9fdb6f090cc781
Batch ID: 20250622_205436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, Frame
from reportlab.lib.units import inch
from reportlab.lib import colors

def generate_invoice_pdf(output_path):
    """
    Generates a sample invoice PDF with specific styling and layout.
    
    Args:
        output_path (str): Path to save the generated PDF.
    """
    try:
        # Create a canvas with letter size
        c = canvas.Canvas(output_path, pagesize=letter)
        width, height = letter
        
        # Set font and colors
        c.setFont("Helvetica-Bold", 16)
        c.setFillColor(colors.darkblue)
        
        # Draw header
        c.drawString(1 * inch, height - 1 * inch, "INVOICE")
        
        # Draw company info
        c.setFont("Helvetica", 12)
        c.setFillColor(colors.black)
        c.drawString(1 * inch, height - 1.5 * inch, "Your Company Name")
        c.drawString(1 * inch, height - 1.75 * inch, "123 Business Street")
        c.drawString(1 * inch, height - 2 * inch, "City, State ZIP")
        
        # Client info section
        c.setFont("Helvetica-Bold", 12)
        c.drawString(1 * inch, height - 3 * inch, "BILL TO:")
        c.setFont("Helvetica", 12)
        c.drawString(1 * inch, height - 3.25 * inch, "Client Name")
        c.drawString(1 * inch, height - 3.5 * inch, "Client Address")
        c.drawString(1 * inch, height - 3.75 * inch, "City, State ZIP")
        
        # Invoice details
        c.setFont("Helvetica-Bold", 12)
        c.drawString(4 * inch, height - 3 * inch, "INVOICE #:")
        c.drawString(4 * inch, height - 3.25 * inch, "DATE:")
        c.drawString(4 * inch, height - 3.5 * inch, "DUE DATE:")
        
        c.setFont("Helvetica", 12)
        c.drawString(5.5 * inch, height - 3 * inch, "INV-001")
        c.drawString(5.5 * inch, height - 3.25 * inch, "01/01/2023")
        c.drawString(5.5 * inch, height - 3.5 * inch, "01/15/2023")
        
        # Table header
        c.setFont("Helvetica-Bold", 12)
        c.drawString(1 * inch, height - 4.5 * inch, "DESCRIPTION")
        c.drawString(4 * inch, height - 4.5 * inch, "QTY")
        c.drawString(5 * inch, height - 4.5 * inch, "RATE")
        c.drawString(6 * inch, height - 4.5 * inch, "AMOUNT")
        
        # Draw line
        c.line(1 * inch, height - 4.6 * inch, 7 * inch, height - 4.6 * inch)
        
        # Sample items
        items = [
            ("Product 1", 2, 50.00),
            ("Service 1", 1, 100.00),
            ("Product 2", 3, 25.00)
        ]
        
        y_position = height - 5 * inch
        for desc, qty, rate in items:
            c.setFont("Helvetica", 10)
            c.drawString(1 * inch, y_position, desc)
            c.drawString(4 * inch, y_position, str(qty))
            c.drawString(5 * inch, y_position, f"${rate:.2f}")
            amount = qty * rate
            c.drawString(6 * inch, y_position, f"${amount:.2f}")
            y_position -= 0.25 * inch
        
        # Total section
        c.setFont("Helvetica-Bold", 12)
        c.drawString(5 * inch, y_position - 0.5 * inch, "TOTAL:")
        total = sum(qty * rate for desc, qty, rate in items)
        c.drawString(6 * inch, y_position - 0.5 * inch, f"${total:.2f}")
        
        # Footer note
        styles = getSampleStyleSheet()
        note = Paragraph(
            "Thank you for your business! Payment due within 15 days.",
            styles["Normal"]
        )
        frame = Frame(1 * inch, 0.5 * inch, 6 * inch, 0.5 * inch)
        frame.addFromList([note], c)
        
        # Save the PDF
        c.save()
        print(f"Invoice generated successfully at {output_path}")
        
    except Exception as e:
        print(f"Error generating invoice: {str(e)}")

# Example usage
if __name__ == "__main__":
    generate_invoice_pdf("sample_invoice.pdf")
```
