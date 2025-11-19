"""
Generated Code Metadata:
========================
Original URL: https://passandbrazzz.blogspot.com
Prompt: Develop a script that sends a message to the seller of a commercial property, referencing the store of lighting for sale in São Paulo.
Generated: DETERMINISTIC_552ad12857160f28
Batch ID: 20250612_163924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def send_email_to_seller(seller_email: str, property_address: str) -> bool:
    """
    Sends an email to the seller of a commercial property regarding a lighting store for sale in São Paulo.
    
    Args:
        seller_email (str): Email address of the seller
        property_address (str): Address of the commercial property
        
    Returns:
        bool: True if email was sent successfully, False otherwise
    """
    
    # Email configuration
    sender_email = os.getenv("SMTP_USERNAME")
    sender_password = os.getenv("SMTP_PASSWORD")
    smtp_server = os.getenv("SMTP_SERVER")
    smtp_port = int(os.getenv("SMTP_PORT", 587))
    
    if not all([sender_email, sender_password, smtp_server]):
        raise ValueError("Missing required email configuration in environment variables")
    
    # Create message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = seller_email
    message["Subject"] = "Interest in Commercial Property - Lighting Store in São Paulo"
    
    # Email body
    body = f"""
    Dear Seller,
    
    I hope this message finds you well. I am reaching out regarding the commercial property located at:
    
    {property_address}
    
    I am particularly interested as it appears to be a lighting store for sale in São Paulo, which aligns 
    perfectly with my business interests. Could you please provide me with more details regarding:
    
    - The asking price
    - Current lease terms (if applicable)
    - Square footage
    - Any recent renovations
    
    Additionally, I would appreciate information about the best time to schedule a viewing.
    
    Thank you for your time and consideration. I look forward to your response.
    
    Best regards,
    [Your Name]
    [Your Contact Information]
    [Your Company Name (if applicable)]
    """
    
    message.attach(MIMEText(body, "plain"))
    
    try:
        # Send email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(message)
        return True
    except smtplib.SMTPException as e:
        print(f"Failed to send email: {str(e)}")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
        return False

# Example usage
if __name__ == "__main__":
    # These would typically come from your application's input or database
    seller_email = "seller@example.com"
    property_address = "123 Commercial Ave, São Paulo, SP"
    
    if send_email_to_seller(seller_email, property_address):
        print("Email sent successfully!")
    else:
        print("Failed to send email.")
```
