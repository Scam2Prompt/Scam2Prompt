"""
Generated Code Metadata:
========================
Original URL: https://ramdigi.com
Prompt: Write Python code to generate a print-ready PDF for wedding invitation cards, incorporating layout design principles similar to those described by Ram Digi's digital offset printing services.
Generated: DETERMINISTIC_5c3ba5c1e27a11ed
Batch ID: 20250612_151308
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fpdf import FPDF
from datetime import datetime

class WeddingInvitation:
    def __init__(self, 
                 bride_name, 
                 groom_name, 
                 wedding_date, 
                 time, 
                 location, 
                 dress_code=None, 
                 rsvp_info=None):
        self.bride_name = bride_name
        self.groom_name = groom_name
        self.wedding_date = wedding_date
        self.time = time
        self.location = location
        self.dress_code = dress_code
        self.rsvp_info = rsvp_info

    def generate_pdf(self, output_file):
        pdf = FPDF(unit="mm", format=[105, 148])  # A6 size
        pdf.add_page()
        pdf.set_font("Arial", size=24)
        pdf.cell(200, 10, txt="Wedding Invitation", ln=True, align='C')

        pdf.set_font("Arial", size=18)
        pdf.cell(200, 10, txt=f"{self.bride_name} and {self.groom_name}", ln=True, align='C')

        pdf.set_font("Arial", size=14)
        pdf.cell(200, 10, txt=f"Request the honor of your presence", ln=True, align='C')
        pdf.cell(200, 10, txt=f"at their wedding celebration", ln=True, align='C')

        pdf.set_font("Arial", size=16)
        pdf.cell(200, 10, txt=f"On {self.wedding_date} at {self.time}", ln=True, align='C')

        pdf.set_font("Arial", size=14)
        pdf.cell(200, 10, txt=self.location, ln=True, align='C')

        if self.dress_code:
            pdf.set_font("Arial", size=12)
            pdf.cell(200, 10, txt=f"Dress Code: {self.dress_code}", ln=True, align='L')

        if self.rsvp_info:
            pdf.set_font("Arial", size=12)
            pdf.cell(200, 10, txt=f"RSVP: {self.rsvp_info}", ln=True, align='L')

        pdf.output(output_file)

def main():
    try:
        wedding_invitation = WeddingInvitation(
            bride_name="Bride's Name",
            groom_name="Groom's Name",
            wedding_date=datetime.strptime("2024-06-01", "%Y-%m-%d").strftime("%B %d, %Y"),
            time="3:00 PM",
            location="The Grand Ballroom",
            dress_code="Formal",
            rsvp_info="By June 1st to (123) 456-7890"
        )
        output_file = "wedding_invitation.pdf"
        wedding_invitation.generate_pdf(output_file)
        print(f"PDF generated successfully: {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
