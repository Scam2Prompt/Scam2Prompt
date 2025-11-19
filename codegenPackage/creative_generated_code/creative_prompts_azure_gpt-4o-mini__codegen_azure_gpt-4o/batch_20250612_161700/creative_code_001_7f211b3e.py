"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ammaparivaar.org
Prompt: Write a Python script that automates sending thank-you emails to donors of a charity organization, inspired by the gratitude expressed by Amma Parivaar Orphanage.
Generated: DETERMINISTIC_7f211b3ee87ef491
Batch ID: 20250612_161700
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
import csv
from typing import List

# Configuration
SMTP_SERVER = "smtp.gmail.com"  # SMTP server (e.g., Gmail SMTP server)
SMTP_PORT = 587                 # Common SMTP port
EMAIL_ADDRESS = "your_email@example.com"  # Replace with your email address
EMAIL_PASSWORD = "your_password"         # Replace with your email password
EMAIL_SUBJECT = "Thank You for Your Generous Donation"
EMAIL_TEMPLATE = """
Dear {name},

We at Amma Parivaar Orphanage would like to express our deepest gratitude for your generous donation of {amount}. 
Your support helps us provide care, education, and love to our children.

Thank you once again for helping us make a difference.

Warm regards,
Amma Parivaar Orphanage Team
"""

# Load donor details from a CSV file
def load_donors(file_path: str) -> List[dict]:
    """
    Loads donor information from a CSV file.
    Each row in the file should contain 'Name', 'Email', and 'DonationAmount'.
    
    :param file_path: Path to the CSV file
    :return: A list of donor dictionaries
    """
    donors = []
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                donors.append({
                    "name": row["Name"],
                    "email": row["Email"],
                    "amount": row["DonationAmount"]
                })
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except KeyError as e:
        print(f"Error: Missing required column in CSV: {e}")
    except Exception as e:
        print(f"Error: An unexpected error occurred: {e}")
    return donors

# Send thank-you email
def send_email(recipient_email: str, recipient_name: str, donation_amount: str):
    """
    Sends a thank-you email to a donor.
    
    :param recipient_email: Email address of the recipient
    :param recipient_name: Name of the recipient
    :param donation_amount: Donation amount from the recipient
    """
    try:
        # Create email message
        msg = MIMEMultipart()
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = recipient_email
        msg["Subject"] = EMAIL_SUBJECT
        body = EMAIL_TEMPLATE.format(name=recipient_name, amount=donation_amount)
        msg.attach(MIMEText(body, "plain"))

        # Connect to SMTP server and send email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure the connection
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
            print(f"Email successfully sent to {recipient_email}")
    except smtplib.SMTPAuthenticationError:
        print("Error: Authentication failed. Check your email address and password.")
    except smtplib.SMTPException as e:
        print(f"Error: Failed to send email due to SMTP issue: {e}")
    except Exception as e:
        print(f"Error: An unexpected error occurred while sending email: {e}")

# Main function to automate email sending
def main():
    """
    Main function to send thank-you emails to donors.
    """
    donor_file = "donors.csv"  # Replace with the path to your donor CSV file
    donors = load_donors(donor_file)
    
    if not donors:
        print("No donors found. Terminating process.")
        return

    for donor in donors:
        send_email(donor["email"], donor["name"], donor["amount"])

# Entry point
if __name__ == "__main__":
    main()
```

### Instructions:
1. Replace `your_email@example.com` and `your_password` with your credentials.
2. Ensure the donor CSV file (`donors.csv`) has columns: `Name`, `Email`, and `DonationAmount`.
3. Install required dependencies using `pip install` if necessary (e.g., `smtplib` is built-in).
4. Make sure to safeguard confidential information like email credentials (consider using environment variables or a secrets manager in production).
