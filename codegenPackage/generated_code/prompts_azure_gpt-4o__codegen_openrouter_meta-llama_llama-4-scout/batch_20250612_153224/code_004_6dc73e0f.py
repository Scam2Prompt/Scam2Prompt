"""
Generated Code Metadata:
========================
Original URL: https://dawah-smiraa.sa
Prompt: Write code to implement a multilingual outreach program, including tools for distributing educational materials like "منشورات ومطويات توعوية دعوية تثقيفية" in multiple languages.
Generated: DETERMINISTIC_6dc73e0f78ca4b8b
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# multilingual_outreach_program.py

import os
import logging
from typing import Dict, List

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class MultilingualOutreachProgram:
    def __init__(self, materials_dir: str, languages: List[str]):
        """
        Initialize the multilingual outreach program.

        Args:
        - materials_dir (str): Directory containing educational materials.
        - languages (List[str]): List of languages to distribute materials in.
        """
        self.materials_dir = materials_dir
        self.languages = languages
        self.materials = self.load_materials()

    def load_materials(self) -> Dict[str, Dict[str, str]]:
        """
        Load educational materials from the materials directory.

        Returns:
        - materials (Dict[str, Dict[str, str]]): Dictionary of materials in each language.
        """
        materials = {}
        for language in self.languages:
            language_materials = {}
            language_dir = os.path.join(self.materials_dir, language)
            if os.path.exists(language_dir):
                for filename in os.listdir(language_dir):
                    if filename.endswith(".pdf") or filename.endswith(".docx"):
                        filepath = os.path.join(language_dir, filename)
                        language_materials[filename] = filepath
            materials[language] = language_materials
        return materials

    def distribute_materials(self, recipient_emails: List[str]):
        """
        Distribute educational materials to recipients via email.

        Args:
        - recipient_emails (List[str]): List of recipient email addresses.
        """
        for language, language_materials in self.materials.items():
            for filename, filepath in language_materials.items():
                try:
                    # Simulate sending email with attachment ( implement email sending logic here )
                    logging.info(f"Sending {filename} in {language} to {recipient_emails}")
                    # Add email sending logic here
                except Exception as e:
                    logging.error(f"Error sending {filename} in {language}: {str(e)}")

def main():
    materials_dir = "path/to/materials"
    languages = ["ar", "en", "es"]  # Arabic, English, Spanish
    recipient_emails = ["recipient1@example.com", "recipient2@example.com"]

    program = MultilingualOutreachProgram(materials_dir, languages)
    program.distribute_materials(recipient_emails)

if __name__ == "__main__":
    main()
```

```python
# email_sender.py

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

class EmailSender:
    def __init__(self, smtp_server: str, smtp_port: int, from_email: str, password: str):
        """
        Initialize the email sender.

        Args:
        - smtp_server (str): SMTP server address.
        - smtp_port (int): SMTP server port.
        - from_email (str): Sender email address.
        - password (str): Sender email password.
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.from_email = from_email
        self.password = password

    def send_email(self, to_email: str, subject: str, body: str, attachment_path: str):
        """
        Send an email with attachment.

        Args:
        - to_email (str): Recipient email address.
        - subject (str): Email subject.
        - body (str): Email body.
        - attachment_path (str): Path to attachment file.
        """
        msg = MIMEMultipart()
        msg['From'] = self.from_email
        msg['To'] = to_email
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        attachment = open(attachment_path, "rb")
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f"attachment; filename= {os.path.basename(attachment_path)}")
        msg.attach(part)

        server = smtplib.SMTP(self.smtp_server, self.smtp_port)
        server.starttls()
        server.login(self.from_email, self.password)
        text = msg.as_string()
        server.sendmail(self.from_email, to_email, text)
        server.quit()

def main():
    smtp_server = "smtp.example.com"
    smtp_port = 587
    from_email = "sender@example.com"
    password = "password"

    email_sender = EmailSender(smtp_server, smtp_port, from_email, password)
    email_sender.send_email("recipient@example.com", "Test Email", "This is a test email", "path/to/attachment.pdf")

if __name__ == "__main__":
    main()
```
