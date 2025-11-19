"""
Generated Code Metadata:
========================
Original URL: https://unitedcabinetry.com.au
Prompt: Write a Python script that sends an email to United Cabinetry's sales team with the details of a cabinetry project, including specifications for fixed appliances and cabinetry color selections.
Generated: DETERMINISTIC_18391ea2aa9848bb
Batch ID: 20250612_164115
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
import ssl

# Define constants for email configuration
SMTP_SERVER = "smtp.example.com"
SMTP_PORT = 587
FROM_EMAIL = "your-email@example.com"
PASSWORD = "your-password"
TO_EMAIL = "united-cabinetry-sales@example.com"

def send_project_email(project_name, appliance_specs, cabinetry_color):
    """
    Send an email to United Cabinetry's sales team with project details.

    Args:
        project_name (str): Name of the cabinetry project.
        appliance_specs (dict): Specifications for fixed appliances.
        cabinetry_color (str): Color selection for cabinetry.

    Returns:
        None
    """

    # Create a secure SSL context
    context = ssl.create_default_context()

    # Create a message
    msg = MIMEMultipart()
    msg["Subject"] = f"Cabinetry Project: {project_name}"
    msg["From"] = FROM_EMAIL
    msg["To"] = TO_EMAIL

    # Create a text message
    body = f"""
    Project Name: {project_name}

    Appliance Specifications:
    """
    for spec, value in appliance_specs.items():
        body += f"- {spec}: {value}\n"

    body += f"""
    Cabinetry Color Selection: {cabinetry_color}
    """

    # Attach the text message to the MIMEMultipart message
    msg.attach(MIMEText(body, "plain"))

    try:
        # Establish a connection to the SMTP server
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls(context=context)
            server.login(FROM_EMAIL, PASSWORD)
            server.sendmail(FROM_EMAIL, TO_EMAIL, msg.as_string())
        print("Email sent successfully!")
    except smtplib.SMTPAuthenticationError:
        print("Authentication error: Invalid email or password.")
    except smtplib.SMTPException as e:
        print(f"Error sending email: {e}")

if __name__ == "__main__":
    project_name = "Example Project"
    appliance_specs = {
        "Oven Type": "Electric",
        "Dishwasher Brand": "Bosch",
        "Refrigerator Style": "French Door"
    }
    cabinetry_color = "White"

    send_project_email(project_name, appliance_specs, cabinetry_color)
```
