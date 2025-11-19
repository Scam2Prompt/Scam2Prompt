"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://freejobsindubai.com
Prompt: Develop a sample resume tailored for a Waiter position in Dubai, incorporating key skills and experiences highlighted on FreeJobsInDubai.com.
Generated: DETERMINISTIC_3b08bd6dfdb566dc
Batch ID: 20250612_162220
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from fpdf import FPDF

# Define a class for creating the resume PDF
class ResumePDF(FPDF):
    def header(self):
        # Add a header for the resume
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Resume - Waiter Position', 0, 1, 'C')
        self.ln(10)

    def footer(self):
        # Add a footer with page number
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def add_section_title(self, title):
        # Add section title with formatting
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(5)

    def add_paragraph(self, text):
        # Add a paragraph with formatting
        self.set_font('Arial', '', 10)
        self.multi_cell(0, 10, text)
        self.ln(5)

    def add_bullet_list(self, items):
        # Add a bulleted list
        self.set_font('Arial', '', 10)
        for item in items:
            self.cell(5, 10, u'\u2022', 0, 0, 'L')  # Bullet point
            self.cell(0, 10, item, 0, 1, 'L')
        self.ln(5)

# Generate the resume content
def generate_resume():
    # Initialize the PDF
    pdf = ResumePDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # Add personal information
    pdf.add_section_title("Personal Information")
    pdf.add_paragraph("Name: John Doe\nEmail: john.doe@example.com\nPhone: +971 50 123 4567\nLocation: Dubai, UAE")

    # Add professional summary
    pdf.add_section_title("Professional Summary")
    pdf.add_paragraph("Experienced waiter with over 5 years in the hospitality industry, delivering exceptional customer service in high-paced environments. Skilled at managing tables, taking orders accurately, and ensuring guests have a memorable dining experience.")

    # Add key skills
    pdf.add_section_title("Key Skills")
    pdf.add_bullet_list([
        "Excellent customer service and communication skills",
        "Ability to work in a fast-paced environment under pressure",
        "Proficiency in handling POS systems and cash transactions",
        "Knowledge of food safety and hygiene practices",
        "Strong teamwork and multitasking abilities"
    ])

    # Add work experience
    pdf.add_section_title("Work Experience")
    pdf.add_paragraph("Waiter | Dubai Marina Restaurant | Dubai, UAE | Jan 2020 - Present")
    pdf.add_bullet_list([
        "Greeted guests and provided menus, ensuring prompt attention to their needs.",
        "Recommended menu specials and upsold beverages, increasing monthly sales by 15%.",
        "Collaborated with kitchen staff to ensure timely food delivery and order accuracy.",
        "Maintained cleanliness of tables and dining areas in adherence to hygiene standards.",
        "Resolved guest complaints professionally, achieving high customer satisfaction rates."
    ])

    pdf.add_paragraph("Waiter | Palm Jumeirah Hotel | Dubai, UAE | Mar 2017 - Dec 2019")
    pdf.add_bullet_list([
        "Served food and beverages to guests in a luxury dining environment.",
        "Assisted in training new staff, improving team productivity and service quality.",
        "Managed high-volume shifts during peak hours with efficiency and professionalism.",
        "Ensured compliance with health and safety regulations at all times."
    ])

    # Add education
    pdf.add_section_title("Education")
    pdf.add_paragraph("Diploma in Hospitality Management | Dubai College of Hospitality | Dubai, UAE | Graduated: 2016")

    # Add certifications
    pdf.add_section_title("Certifications")
    pdf.add_bullet_list([
        "Food Safety and Hygiene Certification (Dubai Municipality)",
        "Advanced Customer Service Training"
    ])

    # Add languages
    pdf.add_section_title("Languages")
    pdf.add_bullet_list([
        "English (Fluent)",
        "Arabic (Intermediate)"
    ])

    # Save the PDF to a file
    try:
        pdf.output("Waiter_Resume_John_Doe.pdf")
        print("Resume generated successfully: Waiter_Resume_John_Doe.pdf")
    except Exception as e:
        print(f"Error generating resume: {e}")

# Call the function to generate the resume
generate_resume()
```
