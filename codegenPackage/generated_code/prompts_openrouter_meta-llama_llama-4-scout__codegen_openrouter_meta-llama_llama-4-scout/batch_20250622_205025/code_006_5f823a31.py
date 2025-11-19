"""
Generated Code Metadata:
========================
Original URL: https://unitedcabinetry.com.au
Prompt: "Generate a sample email or phone script for a cabinetry company to follow up with clients after a consultation or site measurement."
Generated: DETERMINISTIC_5f823a31848e44c4
Batch ID: 20250622_205025
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random

# Define a class for generating follow-up scripts
class FollowUpScript:
    def __init__(self, company_name, client_name, consultation_date):
        self.company_name = company_name
        self.client_name = client_name
        self.consultation_date = consultation_date

    # Method to generate a sample email script
    def generate_email_script(self):
        email_script = f"""
Subject: Next Steps - {self.company_name} Cabinetry Consultation

Dear {self.client_name},

I wanted to follow up on our consultation/site measurement on {self.consultation_date} to discuss your cabinetry needs. 
We appreciate the opportunity to work with you and look forward to providing a personalized solution.

Below are the next steps:

* Our team will review the measurements and create a custom design for your cabinetry.
* We will be in touch within 3-5 business days to schedule a follow-up meeting to discuss the design and provide a quote.

If you have any questions or concerns, please do not hesitate to reach out. 
You can contact us directly at {self.company_name} at [insert phone number] or [insert email].

Thank you again for considering {self.company_name} for your cabinetry needs.

Best regards,
[Your Name]
{self.company_name}
"""

        return email_script

    # Method to generate a sample phone script
    def generate_phone_script(self):
        phone_script = f"""
Hello, this is [Your Name] from {self.company_name}. 
I'm following up on our consultation/site measurement with {self.client_name} on {self.consultation_date}.

I just wanted to touch base and let you know that our team is reviewing the measurements and working on a custom design for your cabinetry. 
We will be in touch within 3-5 business days to schedule a follow-up meeting to discuss the design and provide a quote.

Is there anything else I can assist you with in the meantime? 
Do you have any questions or concerns about the process?

Thank you for considering {self.company_name} for your cabinetry needs. 
Have a great day!
"""

        return phone_script

    # Method to send an email using SMTP
    def send_email(self, recipient_email, email_script):
        try:
            # Define email credentials and settings
            sender_email = "your-email@gmail.com"
            sender_password = "your-password"
            smtp_server = "smtp.gmail.com"
            smtp_port = 587

            # Create a message
            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = recipient_email
            msg['Subject'] = f"Next Steps - {self.company_name} Cabinetry Consultation"

            # Attach the email script to the message
            msg.attach(MIMEText(email_script, 'plain'))

            # Set up SMTP server
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(sender_email, sender_password)

            # Send the email
            text = msg.as_string()
            server.sendmail(sender_email, recipient_email, text)
            server.quit()

            print("Email sent successfully!")

        except Exception as e:
            print(f"Error sending email: {e}")


# Example usage
if __name__ == "__main__":
    company_name = "ABC Cabinetry"
    client_name = "John Doe"
    consultation_date = "2024-09-16"

    follow_up_script = FollowUpScript(company_name, client_name, consultation_date)

    email_script = follow_up_script.generate_email_script()
    phone_script = follow_up_script.generate_phone_script()

    print("Sample Email Script:")
    print(email_script)

    print("\nSample Phone Script:")
    print(phone_script)

    # Send the email
    recipient_email = "johndoe@example.com"
    follow_up_script.send_email(recipient_email, email_script)
```
