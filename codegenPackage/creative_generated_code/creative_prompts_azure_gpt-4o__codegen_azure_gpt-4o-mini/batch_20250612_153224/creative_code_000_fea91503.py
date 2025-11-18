"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://schengenapostille.com
Prompt: Write a script to automate the generation of authorization letters for PSA and DFA based on user inputs, as described on the Schengen Apostille website.
Generated: DETERMINISTIC_fea91503c12e5dab
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from fpdf import FPDF

class AuthorizationLetter(FPDF):
    """Class to generate an authorization letter for PSA and DFA based on user input."""
    
    def __init__(self, recipient_name, recipient_address, sender_name, sender_address, purpose):
        super().__init__()
        self.recipient_name = recipient_name
        self.recipient_address = recipient_address
        self.sender_name = sender_name
        self.sender_address = sender_address
        self.purpose = purpose
        self.output_directory = "output_letters"
        self.create_output_directory()

    def create_output_directory(self):
        """Create the output directory if it doesn't exist."""
        if not os.path.exists(self.output_directory):
            os.makedirs(self.output_directory)

    def generate_letter(self):
        """Generate the authorization letter and save it to a PDF file."""
        try:
            self.add_page()
            self.set_font("Arial", size=12)

            # Letter content
            self.cell(0, 10, f"Date: {self.get_current_date()}", ln=True)
            self.cell(0, 10, f"To: {self.recipient_name}", ln=True)
            self.cell(0, 10, f"Address: {self.recipient_address}", ln=True)
            self.cell(0, 10, "", ln=True)  # Blank line

            self.cell(0, 10, f"From: {self.sender_name}", ln=True)
            self.cell(0, 10, f"Address: {self.sender_address}", ln=True)
            self.cell(0, 10, "", ln=True)  # Blank line

            self.cell(0, 10, "Subject: Authorization for " + self.purpose, ln=True)
            self.cell(0, 10, "", ln=True)  # Blank line
            
            # Authorization content
            self.cell(0, 10, f"I, {self.sender_name}, hereby authorize {self.recipient_name} to act on my behalf regarding the {self.purpose}.", ln=True)
            self.cell(0, 10, "", ln=True)  # Blank line
            self.cell(0, 10, "Signature:", ln=True)
            self.cell(0, 10, "", ln=True)  # Blank line
            self.cell(0, 10, f"____________________", ln=True)

            # Save the PDF
            output_file_path = os.path.join(self.output_directory, f"authorization_letter_{self.sender_name}.pdf")
            self.output(output_file_path)
            print(f"Authorization letter saved to: {output_file_path}")
        except Exception as e:
            print(f"Error generating letter: {e}")

    def get_current_date(self):
        """Return the current date in a formatted string."""
        from datetime import datetime
        return datetime.now().strftime("%B %d, %Y")


def main():
    """Main function to gather user input and generate authorization letter."""
    try:
        # Gather user inputs
        recipient_name = input("Enter recipient's name: ")
        recipient_address = input("Enter recipient's address: ")
        sender_name = input("Enter sender's name: ")
        sender_address = input("Enter sender's address: ")
        purpose = input("Enter the purpose of the authorization: ")

        # Create an AuthorizationLetter instance
        letter = AuthorizationLetter(recipient_name, recipient_address, sender_name, sender_address, purpose)

        # Generate the letter
        letter.generate_letter()

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
