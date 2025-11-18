"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://araform.org
Prompt: Write Python code to generate a PDF report of course enrollment statistics for the vocational courses offered by Araform, categorized by location and course type.
Generated: DETERMINISTIC_9e1a82e66316d339
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import pandas as pd
from fpdf import FPDF

# Function to generate the PDF report
def generate_pdf_report(data, output_file):
    """
    Generates a PDF report of course enrollment statistics.

    Parameters:
    data (dict): Dictionary containing course enrollment statistics.
                 Example format:
                 {
                     "Location 1": {
                         "Course Type A": 50,
                         "Course Type B": 30
                     },
                     "Location 2": {
                         "Course Type A": 70,
                         "Course Type C": 40
                     }
                 }
    output_file (str): Path to save the generated PDF file.

    Returns:
    None
    """
    try:
        # Initialize the PDF object
        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()
        
        # Set font for the PDF
        pdf.set_font("Arial", size=12)
        
        # Add title
        pdf.set_font("Arial", style="B", size=16)
        pdf.cell(200, 10, txt="Araform Course Enrollment Statistics", ln=True, align="C")
        pdf.ln(10)  # Line break
        
        # Add content for each location
        for location, courses in data.items():
            # Add location heading
            pdf.set_font("Arial", style="B", size=14)
            pdf.cell(0, 10, txt=f"Location: {location}", ln=True)
            pdf.ln(5)  # Line break
            
            # Add course statistics
            pdf.set_font("Arial", size=12)
            for course_type, enrollment in courses.items():
                pdf.cell(0, 10, txt=f"{course_type}: {enrollment} students", ln=True)
            
            pdf.ln(10)  # Line break for next location
        
        # Save the PDF to the specified file
        pdf.output(output_file)
        print(f"PDF report successfully saved to {output_file}")
    
    except Exception as e:
        print(f"An error occurred while generating the PDF: {e}")

# Mock data for testing
course_data = {
    "New York": {
        "Plumbing Fundamentals": 45,
        "Electrical Basics": 60,
        "Carpentry 101": 30
    },
    "Los Angeles": {
        "Plumbing Fundamentals": 50,
        "HVAC Systems": 40,
        "Carpentry 101": 35
    },
    "Chicago": {
        "Electrical Basics": 55,
        "HVAC Systems": 45,
        "Carpentry 101": 25
    }
}

# Output file path
output_pdf_path = "course_enrollment_report.pdf"

# Generate the report
generate_pdf_report(course_data, output_pdf_path)
```
