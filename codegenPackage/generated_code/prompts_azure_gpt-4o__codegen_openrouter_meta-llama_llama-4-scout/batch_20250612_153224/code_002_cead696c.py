"""
Generated Code Metadata:
========================
Original URL: https://naikreatif.com
Prompt: Generate Python code to automate the creation of a restaurant grand opening checklist PDF, inspired by the downloadable checklist mentioned on Naikreatif's site.
Generated: DETERMINISTIC_cead696ccbd6f34c
Batch ID: 20250612_153224
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
from datetime import date

class RestaurantGrandOpeningChecklist:
    def __init__(self, restaurant_name, opening_date):
        self.restaurant_name = restaurant_name
        self.opening_date = opening_date
        self.checklist = []

    def add_checklist_item(self, item, status=False):
        """Add a checklist item with optional status"""
        self.checklist.append({"item": item, "status": status})

    def generate_pdf(self, output_filename):
        """Generate a PDF file with the checklist"""
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=15)
        pdf.cell(200, 10, txt=self.restaurant_name, ln=True, align='C')
        pdf.ln(10)
        pdf.set_font("Arial", size=12)
        pdf.cell(0, 10, txt=f"Grand Opening Checklist - {self.opening_date}", ln=True, align='L')

        pdf.ln(10)
        pdf.set_font("Arial", size=10)
        for i, item in enumerate(self.checklist, start=1):
            status = "Done" if item["status"] else "Pending"
            pdf.cell(0, 10, txt=f"{i}. {item['item']} - {status}", ln=True, align='L')

        pdf.output(output_filename)

def main():
    try:
        restaurant_name = input("Enter restaurant name: ")
        opening_date = input("Enter opening date (YYYY-MM-DD): ")
        checklist = RestaurantGrandOpeningChecklist(restaurant_name, opening_date)

        # Pre-populate checklist items inspired by Naikreatif's site
        checklist.add_checklist_item("Finalize restaurant layout and design")
        checklist.add_checklist_item("Hire and train staff", status=True)
        checklist.add_checklist_item("Source and purchase equipment and supplies")
        checklist.add_checklist_item("Plan marketing and promotion strategies", status=True)
        checklist.add_checklist_item("Obtain necessary licenses and permits")

        output_filename = f"{restaurant_name}_grand_opening_checklist.pdf"
        checklist.generate_pdf(output_filename)
        print(f"PDF generated: {output_filename}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
