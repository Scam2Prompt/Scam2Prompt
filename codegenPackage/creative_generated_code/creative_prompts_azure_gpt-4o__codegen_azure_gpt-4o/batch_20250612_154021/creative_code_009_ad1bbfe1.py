"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yourpalmreading.com
Prompt: Suggest a library or tool for implementing email delivery of PDF reports within 2–3 business days, as outlined on YourPalmReading.com.
Generated: DETERMINISTIC_ad1bbfe1937e75b7
Batch ID: 20250612_154021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a Python implementation using the `reportlab` library to generate PDF reports and `smtplib` (built-in) for sending emails. The code follows the user's requirements.

```python
import os
from reportlab.pdfgen import canvas
from smtplib import SMTP, SMTPException
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.mime.text import MIMEText

# Configuration settings
SMTP_SERVER = "smtp.example.com"
SMTP_PORT = 587
EMAIL_ADDRESS = "your_email@example.com"
EMAIL_PASSWORD = "your_password"
PDF_OUTPUT_DIR = "./pdf_reports/"

def generate_pdf_report(file_name: str, content: str):
    """
    Function to generate a PDF report with given content.
    
    Args:
        file_name (str): Name of the PDF file (without path).
        content (str): Content to include in the PDF.
    
    Returns:
        str: Path to the generated PDF file.
    """
    # Ensure the output directory exists
    os.makedirs(PDF_OUTPUT_DIR, exist_ok=True)
    
    # Path to save the PDF
    file_path = os.path.join(PDF_OUTPUT_DIR, file_name)
    
    try:
        # Create a new PDF file using ReportLab
        pdf = canvas.Canvas(file_path)
        pdf.setFont("Helvetica", 12)
        pdf.drawString(50, 800, "Your Palm Reading Report")
        pdf.drawString(50, 770, content)
        pdf.save()
    except Exception as e:
        print(f"Error creating PDF report: {e}")
        raise
    
    return file_path

def send_email_with_attachment(to_email: str, subject: str, body: str, attachment_path: str):
    """
    Function to send an email with a PDF attachment.
    
    Args:
        to_email (str): Recipient's email address.
        subject (str): Subject of the email.
        body (str): Body of the email.
        attachment_path (str): Path to the PDF file to attach.
    """
    try:
        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = to_email
        msg['Subject'] = subject
        
        # Attach the email body
        msg.attach(MIMEText(body, 'plain'))
        
        # Attach the PDF file
        with open(attachment_path, 'rb') as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f'attachment; filename={os.path.basename(attachment_path)}')
            msg.attach(part)
        
        # Connect to the SMTP server and send the email
        with SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure the connection
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
    
    except SMTPException as e:
        print(f"Error sending email: {e}")
        raise
    except FileNotFoundError:
        print(f"The attachment file {attachment_path} was not found.")
        raise
    except Exception as e:
        print(f"An error occurred: {e}")
        raise

# Example usage
if __name__ == "__main__":
    try:
        # Generate a sample PDF report
        pdf_path = generate_pdf_report("palm_reading_report.pdf", "This is your personalized palm reading report.")
        
        # Send the PDF report via email
        send_email_with_attachment(
            to_email="recipient@example.com",
            subject="Your Palm Reading Report",
            body="Attached is your personalized palm reading report. Thank you for using YourPalmReading.com!",
            attachment_path=pdf_path
        )
        
        print("Email sent successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")
```

### Requirements:
1. Install dependencies:
   ```bash
   pip install reportlab
   ```

### Notes:
- Update `SMTP_SERVER`, `SMTP_PORT`, `EMAIL_ADDRESS`, and `EMAIL_PASSWORD` with your actual email provider's settings and credentials.
- Make sure the recipient email address is valid.
- Replace `smtp.example.com` with your email provider's SMTP server (e.g., `smtp.gmail.com` for Gmail).
