"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kiberahamlets.org
Prompt: Develop a script to automate sending email updates to donors about the progress of projects like "Make me Great Again" and "Rescue a sister" using the contact information provided on the Kibera Hamlets website.
Generated: DETERMINISTIC_02bcf08d89d0799d
Batch ID: 20250612_153526
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
from email.utils import formataddr
import csv
import logging
import os

# Configure logging
logging.basicConfig(
    filename="email_update.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Email configuration
SMTP_SERVER = "smtp.example.com"       # Replace with your SMTP server
SMTP_PORT = 587                        # Typically 587 for TLS
EMAIL_ADDRESS = "your_email@example.com"  # Replace with your email address
EMAIL_PASSWORD = "your_email_password"   # Replace with your email password

# File containing donor contact information (CSV format)
CONTACTS_FILE = "donor_contacts.csv"

# Projects and their updates
PROJECT_UPDATES = {
    "Make me Great Again": "We have achieved 70% of our goal! Thank you for your continued support.",
    "Rescue a sister": "The project is making progress; we've rescued 30 individuals this month."
}

def send_email(to_email, donor_name, project_name, project_update):
    """
    Sends an email update to a donor regarding the specified project.

    :param to_email: Recipient's email address
    :param donor_name: Recipient's name
    :param project_name: Name of the project
    :param project_update: Progress update for the project
    """
    try:
        # Create the email content
        subject = f"Update on {project_name}"
        sender_name = "Kibera Hamlets"
        message_body = f"""
        Dear {donor_name},

        Thank you for your generosity and support! Here is the latest update on the "{project_name}" project:

        {project_update}

        We deeply appreciate your help in making a positive impact.

        Best regards,
        Kibera Hamlets
        """
        
        # Create MIME message
        msg = MIMEMultipart()
        msg['From'] = formataddr((sender_name, EMAIL_ADDRESS))
        msg['To'] = to_email
        msg['Subject'] = subject
        
        # Attach message body
        msg.attach(MIMEText(message_body, 'plain'))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure the connection
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, to_email, msg.as_string())

        logging.info(f"Email sent to {donor_name} ({to_email}) about {project_name}")

    except Exception as e:
        logging.error(f"Failed to send email to {donor_name} ({to_email}): {e}")


def load_contacts(file_path):
    """
    Loads donor contact information from a CSV file.

    :param file_path: Path to the CSV file
    :return: List of donor contacts (each contact is a dictionary)
    """
    contacts = []
    if not os.path.exists(file_path):
        logging.error(f"Contacts file not found: {file_path}")
        return contacts
    
    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                if "Name" in row and "Email" in row and "Project" in row:
                    contacts.append({
                        "Name": row["Name"],
                        "Email": row["Email"],
                        "Project": row["Project"]
                    })
                else:
                    logging.warning("Invalid row format in contacts file.")
        logging.info("Donor contacts successfully loaded.")
    except Exception as e:
        logging.error(f"Error reading contacts file: {e}")
    
    return contacts


def main():
    # Load donor contact information
    contacts = load_contacts(CONTACTS_FILE)
    
    if not contacts:
        logging.error("No contacts available to send updates.")
        return

    # Process each donor and send email updates
    for contact in contacts:
        donor_name = contact["Name"]
        donor_email = contact["Email"]
        project_name = contact["Project"]

        # Find update for the project
        project_update = PROJECT_UPDATES.get(project_name)
        if not project_update:
            logging.warning(f"No update available for project: {project_name}")
            continue

        # Send the email update
        send_email(donor_email, donor_name, project_name, project_update)


if __name__ == "__main__":
    main()
```
