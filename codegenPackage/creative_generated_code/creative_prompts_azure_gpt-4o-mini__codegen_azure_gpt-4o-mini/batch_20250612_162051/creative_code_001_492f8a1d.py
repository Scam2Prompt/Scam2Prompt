"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://naikreatif.com
Prompt: Write a Python script that automates the process of collecting client testimonials for a digital branding agency.
Generated: DETERMINISTIC_492f8a1d7bede40c
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pathlib import Path
from typing import List, Dict, Any

# Constants for email configuration
EMAIL_SENDER = "your_email@example.com"
EMAIL_PASSWORD = "your_password"
EMAIL_SMTP_SERVER = "smtp.example.com"
EMAIL_SMTP_PORT = 587

# File to store testimonials
TESTIMONIALS_FILE = 'testimonials.json'

def load_testimonials() -> List[Dict[str, Any]]:
    """Load testimonials from a JSON file."""
    if not os.path.exists(TESTIMONIALS_FILE):
        return []
    with open(TESTIMONIALS_FILE, 'r') as file:
        return json.load(file)

def save_testimonials(testimonials: List[Dict[str, Any]]) -> None:
    """Save testimonials to a JSON file."""
    with open(TESTIMONIALS_FILE, 'w') as file:
        json.dump(testimonials, file, indent=4)

def send_email(recipient: str, subject: str, body: str) -> None:
    """Send an email to the recipient."""
    msg = MIMEMultipart()
    msg['From'] = EMAIL_SENDER
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        with smtplib.SMTP(EMAIL_SMTP_SERVER, EMAIL_SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.send_message(msg)
    except Exception as e:
        print(f"Error sending email: {e}")

def collect_testimonial(client_name: str, testimonial_text: str) -> None:
    """Collect and store a client's testimonial."""
    testimonials = load_testimonials()
    testimonial = {
        "client_name": client_name,
        "testimonial": testimonial_text
    }
    testimonials.append(testimonial)
    save_testimonials(testimonials)

def main() -> None:
    """Main function to automate the process of collecting testimonials."""
    # Create a directory for testimonials if it doesn't exist
    Path(TESTIMONIALS_FILE).parent.mkdir(parents=True, exist_ok=True)

    # Prompt user for client's name and testimonial
    client_name = input("Enter the client's name: ")
    testimonial_text = input("Enter the testimonial: ")

    # Collect the testimonial
    collect_testimonial(client_name, testimonial_text)

    # Send a thank you email to the client
    email_subject = "Thank You for Your Testimonial!"
    email_body = f"Dear {client_name},\n\nThank you for providing your testimonial! We appreciate your feedback.\n\nBest regards,\nDigital Branding Agency"
    send_email(client_name, email_subject, email_body)

if __name__ == "__main__":
    main()
```
