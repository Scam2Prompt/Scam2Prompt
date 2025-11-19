"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nearfans.com
Prompt: What are the steps to invite NEARFans to invest in my project, and how can I effectively present my proposal?
Generated: DETERMINISTIC_4289cef95de1e8a6
Batch ID: 20250612_155805
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is Python code that outlines the steps to invite NEARFans to invest in your project, including a way to effectively present the proposal. This is a high-level approach using functions and is structured for clarity and maintainability.

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import logging

# Setup logging for error tracking and debugging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("project_investment.log"),
        logging.StreamHandler()
    ]
)


def validate_email(email):
    """
    Validates the email format.
    :param email: The email address to validate.
    :return: True if valid, False otherwise.
    """
    import re
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(email_regex, email))


def create_proposal(project_name, project_details, investment_opportunity):
    """
    Creates an investment proposal as a formatted text.
    :param project_name: Name of the project.
    :param project_details: Description and details about the project.
    :param investment_opportunity: Highlights of the investment opportunity.
    :return: A formatted proposal string.
    """
    proposal = f"""
    Dear NEARFans,

    We are excited to introduce our new project: {project_name}.

    Project Overview:
    {project_details}

    Investment Opportunity:
    {investment_opportunity}

    Why Invest With Us?
    - Proven track record of success
    - Transparent investment terms
    - High potential for returns

    We would love to discuss this opportunity further.
    Please feel free to reach out to us with any questions.

    Best regards,
    [Your Name]
    [Your Contact Information]
    """
    return proposal.strip()


def send_email(to_email, subject, body, from_email, smtp_server, smtp_port, smtp_username, smtp_password):
    """
    Sends an email to the specified recipient.
    :param to_email: Recipient email address.
    :param subject: Email subject.
    :param body: Email body content.
    :param from_email: Sender email address.
    :param smtp_server: SMTP server address.
    :param smtp_port: SMTP server port.
    :param smtp_username: SMTP username.
    :param smtp_password: SMTP password.
    """
    try:
        # Validate recipient email
        if not validate_email(to_email):
            raise ValueError(f"Invalid email address: {to_email}")

        # Create email message
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Connect to SMTP server and send email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Secure the connection
            server.login(smtp_username, smtp_password)
            server.send_message(msg)

        logging.info(f"Email successfully sent to {to_email}")

    except Exception as e:
        logging.error(f"Failed to send email to {to_email}: {e}")


def invite_nearfans_to_invest(email_list, project_name, project_details, investment_opportunity, smtp_config):
    """
    Invites NEARFans to invest in the project by sending them an email.
    :param email_list: List of recipient email addresses.
    :param project_name: Name of the project.
    :param project_details: Description and details about the project.
    :param investment_opportunity: Highlights of the investment opportunity.
    :param smtp_config: Dictionary containing SMTP configuration.
    """
    proposal = create_proposal(project_name, project_details, investment_opportunity)
    subject = f"Exciting Investment Opportunity: {project_name}"

    for email in email_list:
        send_email(
            to_email=email,
            subject=subject,
            body=proposal,
            from_email=smtp_config['from_email'],
            smtp_server=smtp_config['smtp_server'],
            smtp_port=smtp_config['smtp_port'],
            smtp_username=smtp_config['smtp_username'],
            smtp_password=smtp_config['smtp_password']
        )


# Example usage
if __name__ == "__main__":
    # Define project details
    project_name = "NEAR Blockchain Revolution"
    project_details = (
        "NEAR Blockchain Revolution is a cutting-edge decentralized platform aiming to revolutionize digital economies."
    )
    investment_opportunity = (
        "Join us to be a part of a fast-growing industry with the potential for significant returns."
    )

    # List of NEARFans' email addresses
    email_list = ["nearfan1@example.com", "nearfan2@example.com"]

    # SMTP configuration (replace with your credentials)
    smtp_config = {
        'smtp_server': "smtp.example.com",
        'smtp_port': 587,
        'smtp_username': "your-email@example.com",
        'smtp_password': "your-email-password",
        'from_email': "your-email@example.com"
    }

    # Send invitations
    invite_nearfans_to_invest(email_list, project_name, project_details, investment_opportunity, smtp_config)
```

This code is well-structured, adheres to best practices, and includes proper error handling using logging and email validation. Replace placeholders (e.g., SMTP credentials) with real values before running the code.
