"""
Generated Code Metadata:
========================
Original URL: https://naikreatif.com
Prompt: Write a Python script that automates the process of collecting client testimonials for a digital branding agency.
Generated: DETERMINISTIC_492f8a1d7bede40c
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# testimonials_collector.py

import os
import json
from datetime import datetime
from email.message import EmailMessage
import smtplib
from typing import Dict, List

class TestimonialCollector:
    def __init__(self, 
                 smtp_server: str, 
                 smtp_port: int, 
                 from_email: str, 
                 password: str, 
                 testimonials_file: str):
        """
        Initialize the TestimonialCollector.

        Args:
        - smtp_server (str): SMTP server to use for sending emails.
        - smtp_port (int): SMTP port to use for sending emails.
        - from_email (str): Email address to send from.
        - password (str): Password for the email account.
        - testimonials_file (str): File to store collected testimonials.
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.from_email = from_email
        self.password = password
        self.testimonials_file = testimonials_file

    def send_request_email(self, to_email: str, client_name: str) -> None:
        """
        Send an email requesting a testimonial from a client.

        Args:
        - to_email (str): Email address to send to.
        - client_name (str): Name of the client.
        """
        msg = EmailMessage()
        msg.set_content(f"Dear {client_name},\n\nWe hope you're enjoying our services! We'd love to hear about your experience with our digital branding agency. Could you please take a minute to share a brief testimonial about your experience with us?\n\nBest regards,\n[Your Name]")
        msg['Subject'] = "Share Your Testimonial"
        msg['From'] = self.from_email
        msg['To'] = to_email

        with smtplib.SMTP(self.smtp_server, self.smtp_port) as smtp:
            smtp.starttls()
            smtp.login(self.from_email, self.password)
            smtp.send_message(msg)

    def collect_testimonial(self, client_name: str, testimonial: str) -> None:
        """
        Collect a testimonial from a client and save it to the testimonials file.

        Args:
        - client_name (str): Name of the client.
        - testimonial (str): Testimonial from the client.
        """
        try:
            if os.path.exists(self.testimonials_file):
                with open(self.testimonials_file, 'r+') as file:
                    data: List[Dict] = json.load(file)
                    data.append({
                        "client_name": client_name,
                        "testimonial": testimonial,
                        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    })
                    file.seek(0)
                    json.dump(data, file, indent=4)
                    file.truncate()
            else:
                with open(self.testimonials_file, 'w') as file:
                    json.dump([{
                        "client_name": client_name,
                        "testimonial": testimonial,
                        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    }], file, indent=4)
        except Exception as e:
            print(f"Error collecting testimonial: {e}")

def main():
    collector = TestimonialCollector(
        smtp_server="smtp.gmail.com",
        smtp_port=587,
        from_email="your-email@gmail.com",
        password="your-password",
        testimonials_file="testimonials.json"
    )

    clients = [
        {"name": "John Doe", "email": "john.doe@example.com"},
        {"name": "Jane Doe", "email": "jane.doe@example.com"}
    ]

    for client in clients:
        try:
            collector.send_request_email(client["email"], client["name"])
            print(f"Email sent to {client['email']}")
        except Exception as e:
            print(f"Error sending email to {client['email']}: {e}")

if __name__ == "__main__":
    main()
```
