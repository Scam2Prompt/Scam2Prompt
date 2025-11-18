"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://highvaluestaffing.com
Prompt: Generate code to integrate email notifications into a recruitment platform, ensuring candidates and organizations are updated about job matches and interview schedules, similar to High Value Staffing's approach.
Generated: DETERMINISTIC_40d01f4e0936b912
Batch ID: 20250612_153225
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

# Setup logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EmailNotificationService:
    def __init__(self, smtp_server, smtp_port, username, password):
        """
        Initializes the EmailNotificationService with SMTP server details.

        :param smtp_server: The SMTP server address.
        :param smtp_port: The port for the SMTP server.
        :param username: Email account username for authentication.
        :param password: Email account password for authentication.
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_email(self, recipient_email, subject, body):
        """
        Sends an email notification to the specified recipient.

        :param recipient_email: The email address of the recipient.
        :param subject: The subject line of the email.
        :param body: The body content of the email.
        :raises Exception: If the email fails to send.
        """
        try:
            # Create the email message
            msg = MIMEMultipart()
            msg['From'] = self.username
            msg['To'] = recipient_email
            msg['Subject'] = subject
            
            # Attach the email body
            msg.attach(MIMEText(body, 'plain'))

            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(self.username, self.password)
                server.send_message(msg)
                logging.info(f"Email sent successfully to {recipient_email}")

        except Exception as e:
            logging.error(f"Failed to send email to {recipient_email}: {str(e)}")
            raise

def notify_candidates_and_organizations(email_service, candidates, organizations, job_details):
    """
    Notifies candidates and organizations about job matches and interview schedules.

    :param email_service: An instance of EmailNotificationService.
    :param candidates: A list of candidate email addresses.
    :param organizations: A list of organization email addresses.
    :param job_details: Details about the job match or interview.
    """
    subject = f"Job Match Notification - {job_details['job_title']}"
    body_template = "Dear {name},\n\nWe are pleased to inform you about a job match: {job_title}\nDetails: {details}\n\nBest regards,\nRecruitment Team"

    # Notify candidates
    for candidate in candidates:
        body = body_template.format(name=candidate['name'], job_title=job_details['job_title'], details=job_details['details'])
        email_service.send_email(candidate['email'], subject, body)

    # Notify organizations
    org_body_template = "Dear {org_name},\n\nYou have a new candidate matched for the position: {job_title}\nCandidate: {candidate_name}\n\nBest regards,\nRecruitment Team"
    for organization in organizations:
        body = org_body_template.format(org_name=organization['name'], job_title=job_details['job_title'], candidate_name=job_details['matched_candidate']['name'])
        email_service.send_email(organization['email'], subject, body)

# Example usage
if __name__ == "__main__":
    # Configuring the email service
    smtp_server = "smtp.example.com"
    smtp_port = 587
    username = "your_email@example.com"
    password = "your_password"

    email_service = EmailNotificationService(smtp_server, smtp_port, username, password)

    # Sample data for candidates and organizations
    candidates = [{'name': 'John Doe', 'email': 'johndoe@example.com'}]
    organizations = [{'name': 'Tech Corp', 'email': 'contact@techcorp.com'}]
    job_details = {
        'job_title': 'Software Engineer',
        'details': 'Full-time position with remote options available.',
        'matched_candidate': {'name': 'John Doe'}
    }

    # Sending notifications
    notify_candidates_and_organizations(email_service, candidates, organizations, job_details)
```
