"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://indologicalindia.com
Prompt: Write Python code to create a donation form for "Indological India" that collects donor information (name, email, phone number, donation amount) and sends it to their email address (indologicalindia@gmail.com).
Generated: DETERMINISTIC_9a1cfd39b7577161
Batch ID: 20250612_154752
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
import re

def send_email(name, email, phone, donation_amount):
    """
    Sends donor information via email to the Indological India organization's email address.
    """
    # Indological India's email address
    recipient_email = "indologicalindia@gmail.com"
    
    # Sender email credentials (update with real credentials)
    sender_email = "your-email@example.com"  # Replace with actual email address
    sender_password = "your-email-password"  # Replace with actual password

    try:
        # Create the email content
        subject = "New Donation Received"
        body = f"""
        Donor Information:
        -------------------
        Name: {name}
        Email: {email}
        Phone: {phone}
        Donation Amount: ₹{donation_amount}
        """

        # Constructing the email
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server and send email
        with smtplib.SMTP("smtp.gmail.com", 587) as server:  # Using Gmail's SMTP server
            server.starttls()  # Secure the connection
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, msg.as_string())

        print("Email sent successfully!")

    except Exception as e:
        print(f"Failed to send email: {e}")

def validate_input(name, email, phone, donation_amount):
    """
    Validates donor input data.
    Returns True if all inputs are valid, otherwise False.
    """
    # Name validation: non-empty and alphabetic
    if not name or not name.isalpha():
        print("Invalid name. Please enter a valid name (alphabetic characters only).")
        return False

    # Email validation: basic regex match for email format
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if not re.match(email_regex, email):
        print("Invalid email. Please enter a valid email address.")
        return False

    # Phone validation: must be numeric and 10 digits
    if not phone.isdigit() or len(phone) != 10:
        print("Invalid phone number. Please enter a valid 10-digit phone number.")
        return False

    # Donation amount validation: positive number
    try:
        donation_amount = float(donation_amount)
        if donation_amount <= 0:
            print("Invalid donation amount. Please enter a positive number.")
            return False
    except ValueError:
        print("Invalid donation amount. Please enter a numeric value.")
        return False

    return True

def donation_form():
    """
    Collects donor information and processes the donation.
    """
    print("Welcome to Indological India's Donation Form!")
    print("Please provide the following details:")

    # Collect donor information
    name = input("Name: ").strip()
    email = input("Email: ").strip()
    phone = input("Phone Number (10 digits): ").strip()
    donation_amount = input("Donation Amount (₹): ").strip()

    # Validate input
    if validate_input(name, email, phone, donation_amount):
        # Send email if input is valid
        send_email(name, email, phone, donation_amount)
    else:
        print("Donation process aborted due to invalid input.")

if __name__ == "__main__":
    donation_form()
```
