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
# -*- coding: utf-8 -*-

"""
PDF Generator for Física Online course materials.

This script generates PDF materials for the Física Online course, 
including exercises and solutions for the ENEM exam.

Author: [Your Name]
Date: [Today's Date]
"""

import os
from fpdf import FPDF
from typing import List

class PDFGenerator:
    def __init__(self, output_dir: str):
        """
        Initialize the PDF generator.

        Args:
        output_dir (str): The directory where the generated PDFs will be saved.
        """
        self.output_dir = output_dir
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

    def generate_pdf(self, exercises: List[dict], solutions: List[dict], filename: str):
        """
        Generate a PDF file containing exercises and solutions.

        Args:
        exercises (List[dict]): A list of dictionaries containing exercise information.
        solutions (List[dict]): A list of dictionaries containing solution information.
        filename (str): The name of the output PDF file.
        """
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=15)
        pdf.cell(200, 10, txt="Física Online - ENEM Exam", ln=True, align='C')

        # Add exercises
        pdf.set_font("Arial", size=12)
        for exercise in exercises:
            pdf.add_page()
            pdf.cell(0, 10, txt=exercise['question'], ln=True, align='L')
            pdf.multi_cell(0, 10, txt=exercise['description'])

        # Add solutions
        pdf.set_font("Arial", size=12)
        for solution in solutions:
            pdf.add_page()
            pdf.cell(0, 10, txt=solution['question'], ln=True, align='L')
            pdf.multi_cell(0, 10, txt=solution['description'])

        pdf.output(os.path.join(self.output_dir, filename))

def main():
    try:
        exercises = [
            {'question': 'Exercise 1', 'description': 'This is the description of exercise 1.'},
            {'question': 'Exercise 2', 'description': 'This is the description of exercise 2.'},
        ]

        solutions = [
            {'question': 'Exercise 1 Solution', 'description': 'This is the solution to exercise 1.'},
            {'question': 'Exercise 2 Solution', 'description': 'This is the solution to exercise 2.'},
        ]

        generator = PDFGenerator('./pdfs')
        generator.generate_pdf(exercises, solutions, 'enem_exercises.pdf')

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
