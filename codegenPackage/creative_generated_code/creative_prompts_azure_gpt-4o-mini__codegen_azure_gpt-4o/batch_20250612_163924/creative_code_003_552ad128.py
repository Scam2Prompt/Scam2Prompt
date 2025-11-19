"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://passandbrazzz.blogspot.com
Prompt: Develop a script that sends a message to the seller of a commercial property, referencing the store of lighting for sale in São Paulo.
Generated: DETERMINISTIC_552ad12857160f28
Batch ID: 20250612_163924
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

def send_message_to_seller(seller_email, property_address, store_name, store_location, seller_name):
    """
    Sends a message to the seller of a commercial property regarding a store of lighting for sale.
    
    Parameters:
        seller_email (str): Email address of the seller
        property_address (str): Address of the commercial property
        store_name (str): Name of the store for sale
        store_location (str): Location of the store (e.g., city, state)
        seller_name (str): Name of the property seller
    
    Returns:
        bool: True if the email was sent successfully, False otherwise
    """
    
    # SMTP server configuration
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = "your_email@gmail.com"  # Replace with your email address
    sender_password = "your_password"  # Replace with your email password; use environment variables for security
    
    try:
        # Create the email content
        subject = "Inquiry About Your Commercial Property in São Paulo"
        body = f"""
        Dear {seller_name},
        
        I am reaching out regarding your commercial property located at {property_address}.
        I wanted to inform you that there is a store for sale specializing in lighting products in São Paulo ({store_name}).
        If you're interested in collaborating or exploring business opportunities, please let me know.
        
        Best regards,
        [Your Name]
        """
        
        # Create the email message
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = seller_email
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))
        
        # Connect to the SMTP server and send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Secure the connection
            server.login(sender_email, sender_password)  # Login to the email account
            server.sendmail(sender_email, seller_email, message.as_string())  # Send the email
        
        print("Email sent successfully.")
        return True
    
    except smtplib.SMTPException as e:
        print(f"Failed to send email: {e}")
        return False

# Example usage
seller_email = "seller@example.com"
property_address = "123 Commercial St, São Paulo"
store_name = "Bright Lights Store"
store_location = "São Paulo"
seller_name = "John Doe"

send_message_to_seller(seller_email, property_address, store_name, store_location, seller_name)
```
