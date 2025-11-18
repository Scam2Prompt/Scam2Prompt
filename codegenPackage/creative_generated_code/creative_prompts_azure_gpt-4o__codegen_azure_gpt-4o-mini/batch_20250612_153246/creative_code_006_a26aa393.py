"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://simho.in
Prompt: Write code to generate automated email templates for HR inquiries, using the contact information and service categories listed on the SIMHO website.
Generated: DETERMINISTIC_a26aa39312ab0741
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import List, Dict

# Define the contact information and service categories
CONTACT_INFO = {
    "HR": {
        "email": "hr@simho.com",
        "phone": "123-456-7890",
        "service_categories": ["Recruitment", "Employee Relations", "Training"]
    },
    "IT": {
        "email": "it@simho.com",
        "phone": "098-765-4321",
        "service_categories": ["Technical Support", "Software Installation", "Network Issues"]
    }
}

def create_email_template(service_category: str, contact_info: Dict) -> str:
    """
    Create an automated email template for HR inquiries.

    Args:
        service_category (str): The service category for the inquiry.
        contact_info (Dict): The contact information for the specific department.

    Returns:
        str: The generated email template.
    """
    # Validate service category
    if service_category not in contact_info['service_categories']:
        raise ValueError(f"Invalid service category: {service_category}. "
                         f"Valid options: {contact_info['service_categories']}")

    # Generate the email template
    template = f"""
    Subject: Inquiry about {service_category}

    Dear HR Team,

    I would like to inquire about the {service_category}. 
    Please provide me with the necessary information regarding this matter.

    Thank you!

    Best regards,
    [Your Name]
    
    Contact Information:
    Email: {contact_info['email']}
    Phone: {contact_info['phone']}
    """
    return template.strip()

def send_email(recipient: str, subject: str, body: str) -> None:
    """
    Send an email using SMTP.

    Args:
        recipient (str): The recipient's email address.
        subject (str): The subject of the email.
        body (str): The body of the email.

    Raises:
        Exception: If the email could not be sent.
    """
    # SMTP server configuration
    smtp_server = "smtp.simho.com"
    smtp_port = 587
    smtp_user = "your_email@simho.com"
    smtp_password = "your_password"

    # Create a multipart email
    msg = MIMEMultipart()
    msg['From'] = smtp_user
    msg['To'] = recipient
    msg['Subject'] = subject
    
    # Attach the body to the email
    msg.attach(MIMEText(body, 'plain'))

    # Send the email
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Use TLS for security
            server.login(smtp_user, smtp_password)
            server.send_message(msg)
    except Exception as e:
        raise Exception(f"Failed to send email: {str(e)}")

def main() -> None:
    """
    Main function to generate and send email templates for HR inquiries.
    """
    department = "HR"
    service_category = "Recruitment"
    
    # Ensure the department exists in the contact info
    if department not in CONTACT_INFO:
        raise ValueError(f"Invalid department: {department}. Available options: {list(CONTACT_INFO.keys())}")

    # Get contact info for the specified department
    contact_info = CONTACT_INFO[department]

    # Create and send the email
    email_body = create_email_template(service_category, contact_info)
    try:
        send_email(contact_info['email'], f"Inquiry about {service_category}", email_body)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
