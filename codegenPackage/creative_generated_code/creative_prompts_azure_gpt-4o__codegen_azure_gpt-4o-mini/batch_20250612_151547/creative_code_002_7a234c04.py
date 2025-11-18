"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tpcontact.co.za
Prompt: Create a script that sends automated email reminders to South African applicants about their UK visa application progress, using the contact information format provided on ContactTP.co.za.
Generated: DETERMINISTIC_7a234c0467c19ea5
Batch ID: 20250612_151547
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
import logging
from typing import List, Dict

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def send_email(to_email: str, subject: str, body: str) -> None:
    """
    Sends an email using the SMTP protocol.

    Args:
        to_email (str): Recipient's email address.
        subject (str): Subject of the email.
        body (str): Content of the email.

    Raises:
        Exception: Raises an exception if sending the email fails.
    """
    try:
        # Email configuration
        from_email = "your_email@example.com"
        password = "your_email_password"  # Use environment variables in production

        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject
        
        # Attach the body to the email
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP('smtp.example.com', 587) as server:
            server.starttls()  # Upgrade the connection to secure
            server.login(from_email, password)
            server.send_message(msg)
        
        logging.info(f"Email sent to {to_email}")

    except Exception as e:
        logging.error(f"Failed to send email to {to_email}: {str(e)}")
        raise

def create_email_body(applicant_info: Dict[str, str]) -> str:
    """
    Creates the email body for the applicant.

    Args:
        applicant_info (Dict[str, str]): Dictionary containing applicant information.

    Returns:
        str: Formatted email body.
    """
    return (f"Dear {applicant_info['name']},\n\n"
            f"We are writing to inform you about the status of your UK visa application.\n"
            f"Your application reference number is {applicant_info['application_id']}.\n"
            f"Current status: {applicant_info['status']}\n\n"
            "Thank you for your patience.\n\n"
            "Best regards,\n"
            "Visa Application Team")

def main(applicants: List[Dict[str, str]]) -> None:
    """
    Main function to send email reminders to applicants.

    Args:
        applicants (List[Dict[str, str]]): List of applicants with their details.
    """
    for applicant in applicants:
        try:
            email_body = create_email_body(applicant)
            send_email(applicant['email'], "UK Visa Application Status Update", email_body)
        except Exception as e:
            logging.error(f"Error processing applicant {applicant['name']}: {str(e)}")

if __name__ == "__main__":
    # Example list of applicants
    applicants_list = [
        {
            'name': 'John Doe',
            'email': 'john.doe@example.com',
            'application_id': 'UK123456',
            'status': 'Under review'
        },
        {
            'name': 'Jane Smith',
            'email': 'jane.smith@example.com',
            'application_id': 'UK654321',
            'status': 'Approved'
        }
    ]
    
    main(applicants_list)
```

**Note:** Make sure to replace `"your_email@example.com"`, `"your_email_password"`, and `'smtp.example.com'` with the actual email and SMTP server details. In a production environment, consider using environment variables or a secure vault for sensitive information like passwords.
