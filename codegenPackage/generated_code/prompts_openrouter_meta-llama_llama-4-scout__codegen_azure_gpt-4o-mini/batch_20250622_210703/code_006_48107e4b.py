"""
Generated Code Metadata:
========================
Original URL: https://cupomestudante.com.br
Prompt: "Write a script to generate PDF materials for the Física Online course, including exercises and solutions for the ENEM exam."
Generated: DETERMINISTIC_48107e4b57bab902
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Física Online Course - ENEM Exercises', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(5)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

def create_pdf(exercises, solutions, filename):
    pdf = PDF()
    pdf.add_page()

    # Add exercises to the PDF
    pdf.chapter_title('Exercises')
    for exercise in exercises:
        pdf.chapter_body(exercise)

    # Add solutions to the PDF
    pdf.add_page()
    pdf.chapter_title('Solutions')
    for solution in solutions:
        pdf.chapter_body(solution)

    # Save the PDF to a file
    try:
        pdf.output(filename)
        print(f"PDF generated successfully: {filename}")
    except Exception as e:
        print(f"Error generating PDF: {e}")

def main():
    # Sample exercises and solutions for the ENEM exam
    exercises = [
        "1. Calculate the force acting on a 5 kg object accelerating at 2 m/s².",
        "2. What is the potential energy of a 10 kg mass at a height of 5 m?",
        "3. A car travels 100 km in 2 hours. What is its average speed?"
    ]

    solutions = [
        "1. F = m * a = 5 kg * 2 m/s² = 10 N.",
        "2. PE = m * g * h = 10 kg * 9.81 m/s² * 5 m = 490.5 J.",
        "3. Average speed = distance / time = 100 km / 2 h = 50 km/h."
    ]

    # Define the output PDF filename
    output_filename = "Física_Online_ENEM_Exercises.pdf"

    # Create the PDF
    create_pdf(exercises, solutions, output_filename)

if __name__ == "__main__":
    main()
```

Make sure to install the `fpdf` library if you haven't already:

```bash
pip install fpdf
```
