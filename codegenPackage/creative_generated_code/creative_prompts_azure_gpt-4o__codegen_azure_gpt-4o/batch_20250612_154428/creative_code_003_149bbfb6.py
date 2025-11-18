"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wufis.com
Prompt: Create a function to send automated updates to pet owners about their pets while they are away, inspired by the "Recibe actualizaciones" feature on WUFIS.
Generated: DETERMINISTIC_149bbfb66cc64d62
Batch ID: 20250612_154428
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

# Function to send automated updates to pet owners
def send_pet_updates(owner_email, pet_name, update_message):
    """
    Sends automated updates to pet owners about their pets.

    Args:
        owner_email (str): The email address of the pet owner.
        pet_name (str): The name of the pet.
        update_message (str): The update message about the pet.

    Returns:
        bool: True if the email was sent successfully, False otherwise.
    """
    # Email server configuration
    SMTP_SERVER = 'smtp.gmail.com'  # Replace with your SMTP server address
    SMTP_PORT = 587                 # Port for TLS
    SENDER_EMAIL = 'your_email@gmail.com'  # Replace with your email address
    SENDER_PASSWORD = 'your_password'     # Replace with your email password

    try:
        # Create the email message
        message = MIMEMultipart()
        message['From'] = SENDER_EMAIL
        message['To'] = owner_email
        message['Subject'] = f"Update about {pet_name}"

        # Email body
        email_body = f"Hello,\n\nHere's an update about your pet {pet_name}:\n\n{update_message}\n\nBest regards,\nYour Pet Care Team"
        message.attach(MIMEText(email_body, 'plain'))

        # Connect to the email server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Enable security
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.send_message(message)

        return True  # Email sent successfully

    except Exception as e:
        # Log the error for debugging (use a proper logging system in production)
        print(f"Error sending email: {e}")
        return False  # Email sending failed

# Example usage
if __name__ == "__main__":
    owner_email = "owner@example.com"
    pet_name = "Buddy"
    update_message = "Buddy has been fed and walked. He seems happy and healthy!"
    
    if send_pet_updates(owner_email, pet_name, update_message):
        print("Pet update sent successfully!")
    else:
        print("Failed to send pet update.")
```

### Notes:
- Replace `your_email@gmail.com` and `your_password` with valid credentials for your email account.
- Use environment variables or a secure method to store credentials instead of hardcoding them in production.
- Ensure the SMTP server and port match your email provider's configuration.
