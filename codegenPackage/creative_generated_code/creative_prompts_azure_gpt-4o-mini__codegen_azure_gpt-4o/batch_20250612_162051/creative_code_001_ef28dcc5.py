"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://renovation-toiture-toulouse.com
Prompt: Write a Python function that sends an email to a roofing contractor in Toulouse, including details about a roof repair project and requesting a quote.
Generated: DETERMINISTIC_ef28dcc5900515c8
Batch ID: 20250612_162051
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

def send_email_to_roofing_contractor(subject, recipient_email, sender_email, sender_password, roof_details):
    """
    Sends an email to a roofing contractor with details about a roof repair project and requests a quote.
    
    Parameters:
    - subject (str): The subject of the email.
    - recipient_email (str): The contractor's email address.
    - sender_email (str): The sender's email address.
    - sender_password (str): The sender's email password.
    - roof_details (str): Details about the roof repair project.
    
    Returns:
    - None
    """
    try:
        # Create the email content
        email = MIMEMultipart()
        email['From'] = sender_email
        email['To'] = recipient_email
        email['Subject'] = subject

        # Email body
        body = f"""
        Bonjour,

        Je vous contacte pour demander un devis concernant un projet de réparation de toiture.
        
        Voici les détails du projet :
        {roof_details}
        
        Merci de me faire parvenir votre devis dans les plus brefs délais. 
        N'hésitez pas à me contacter pour toute clarification ou question supplémentaire.

        Cordialement,
        [Votre Nom]
        """
        email.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server and send the email
        smtp_server = "smtp.gmail.com"  # Example: Using Gmail's SMTP server
        smtp_port = 587  # Standard port for TLS encryption

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Start the TLS encryption
            server.login(sender_email, sender_password)  # Login to the SMTP server
            server.sendmail(sender_email, recipient_email, email.as_string())  # Send the email

        print("Email sent successfully.")

    except smtplib.SMTPException as e:
        # Handle SMTP-related errors
        print(f"Failed to send email. SMTP error: {e}")
    except Exception as e:
        # Handle other unexpected errors
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    subject = "Demande de devis pour réparation de toiture"
    recipient_email = "contractor@example.com"
    sender_email = "your_email@example.com"
    sender_password = "your_email_password"  # Use environment variables or a secure method for sensitive data
    roof_details = """
        - Surface de la toiture : 120m²
        - Type de matériau : Tuiles
        - Dommages : Fuites dans deux endroits, quelques tuiles cassées
        - Adresse du projet : 10 Rue de Toulouse, Toulouse, France
    """

    send_email_to_roofing_contractor(subject, recipient_email, sender_email, sender_password, roof_details)
```
