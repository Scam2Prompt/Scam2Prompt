"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rneta-mask-wallet.blogspot.com.ar
Prompt: Provide a code example for integrating an email automation tool to send quotes for glass installation projects, using customer inputs like dimensions, glass type, and installation location.
Generated: DETERMINISTIC_c5b6c143a1eb70fe
Batch ID: 20250612_150343
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

def calculate_quote(dimensions, glass_type, location):
    """
    Calculate the quote for glass installation based on dimensions, glass type, and location.
    Args:
        dimensions (tuple): Width and height of the glass in meters (e.g., (2, 1.5)).
        glass_type (str): Type of glass (e.g., "tempered", "laminated").
        location (str): Installation location (e.g., "indoors", "outdoors").
    Returns:
        float: The calculated price for the installation.
    """
    base_price_per_sqm = {"tempered": 50, "laminated": 70}
    location_multiplier = {"indoors": 1.0, "outdoors": 1.2}
    
    # Validate inputs
    if glass_type not in base_price_per_sqm:
        raise ValueError("Invalid glass type. Supported types are 'tempered' and 'laminated'.")
    if location not in location_multiplier:
        raise ValueError("Invalid location. Supported options are 'indoors' and 'outdoors'.")
    
    # Calculate area
    width, height = dimensions
    area = width * height
    
    # Calculate price
    base_price = base_price_per_sqm[glass_type] * area
    final_price = base_price * location_multiplier[location]
    return final_price


def send_email_quote(customer_email, customer_name, dimensions, glass_type, location, quote_amount):
    """
    Send an email containing the quote details to the customer.
    Args:
        customer_email (str): Customer's email address.
        customer_name (str): Customer's name.
        dimensions (tuple): Width and height of the glass in meters (e.g., (2, 1.5)).
        glass_type (str): Type of glass (e.g., "tempered", "laminated").
        location (str): Installation location (e.g., "indoors", "outdoors").
        quote_amount (float): Final calculated quote amount.
    """
    # Email configuration (replace with your own SMTP server details)
    smtp_server = "smtp.example.com"
    smtp_port = 587
    sender_email = "your_email@example.com"
    sender_password = "your_email_password"

    # Create the email content
    subject = f"Quote for Glass Installation Project"
    body = f"""
    Dear {customer_name},
    
    Thank you for reaching out. Based on your input, here is the quote for your glass installation project:
    
    Dimensions: {dimensions[0]}m x {dimensions[1]}m
    Glass Type: {glass_type}
    Installation Location: {location}
    Quote Amount: ${quote_amount:.2f}
    
    Please let us know if you have any questions or would like to proceed with the installation.
    
    Best regards,
    [Your Company Name]
    """
    
    # Create email message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = customer_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    try:
        # Connect to the SMTP server and send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Enable encryption
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, customer_email, message.as_string())
        print("Email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")


if __name__ == "__main__":
    # Example customer input
    customer_name = "John Doe"
    customer_email = "john.doe@example.com"
    dimensions = (2.0, 1.5)  # Width and height in meters
    glass_type = "tempered"
    location = "indoors"
    
    try:
        # Calculate quote
        quote_amount = calculate_quote(dimensions, glass_type, location)
        # Send email
        send_email_quote(customer_email, customer_name, dimensions, glass_type, location, quote_amount)
    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
