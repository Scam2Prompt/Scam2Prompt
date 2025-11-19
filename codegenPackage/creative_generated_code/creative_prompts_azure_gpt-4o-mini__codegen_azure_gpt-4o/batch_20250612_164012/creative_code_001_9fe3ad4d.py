"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zk.fest.co
Prompt: Write a Python script that automates the process of contacting sellers for domain names available for sale, such as Fest.co.
Generated: DETERMINISTIC_9fe3ad4de61877b8
Batch ID: 20250612_164012
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
import re

# Configuration variables
SMTP_SERVER = "smtp.gmail.com"  # SMTP server (example: Gmail SMTP)
SMTP_PORT = 587  # Port for TLS
EMAIL_ADDRESS = "your_email@gmail.com"  # Your email address
EMAIL_PASSWORD = "your_email_password"  # Your email password (use app-specific password for security)
CSV_FILE = "domain_sellers.csv"  # Path to the CSV file containing seller information
SUBJECT = "Inquiry About Your Domain for Sale"  # Email subject

# Function to validate email format
def is_valid_email(email):
    """
    Validates the format of an email address using regex.
    
    Args:
        email (str): Email address to validate
    
    Returns:
        bool: True if valid, False otherwise
    """
    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(email_regex, email) is not None

# Function to send email
def send_email(seller_email, seller_name, domain_name):
    """
    Sends an email to the seller regarding a domain for sale.
    
    Args:
        seller_email (str): Seller's email address
        seller_name (str): Seller's name
        domain_name (str): Domain name for sale
    """
    try:
        # Create the email's content
        message = MIMEMultipart()
        message["From"] = EMAIL_ADDRESS
        message["To"] = seller_email
        message["Subject"] = SUBJECT
        
        # Personalized email body
        body = f"""
        Hi {seller_name},
        
        I came across your domain "{domain_name}" listed for sale and would like to inquire further about its availability and pricing. 
        Please let me know the details or feel free to reach out for further discussion.
        
        Best regards,
        [Your Name]
        """
        message.attach(MIMEText(body, "plain"))
        
        # Connect to the SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade the connection to secure TLS
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)  # Login with email credentials
            server.sendmail(EMAIL_ADDRESS, seller_email, message.as_string())  # Send the email
            
        print(f"Email successfully sent to {seller_email}")
    
    except Exception as e:
        print(f"Failed to send email to {seller_email}. Error: {e}")

# Function to process the CSV file and contact sellers
def contact_sellers(csv_file):
    """
    Reads seller information from a CSV file and contacts each seller via email.
    
    Args:
        csv_file (str): Path to CSV file containing seller information
    """
    try:
        with open(csv_file, mode="r") as file:
            reader = csv.DictReader(file)  # Read CSV file as a dictionary
            for row in reader:
                seller_name = row.get("Name")
                seller_email = row.get("Email")
                domain_name = row.get("Domain")
                
                # Validate email format
                if not seller_email or not is_valid_email(seller_email):
                    print(f"Invalid email address for {seller_name}. Skipping...")
                    continue
                
                # Send email to seller
                send_email(seller_email, seller_name, domain_name)
    
    except FileNotFoundError:
        print(f"Error: File '{csv_file}' not found.")
    except Exception as e:
        print(f"An error occurred while processing the CSV file. Error: {e}")

# Main entry point
if __name__ == "__main__":
    print("Starting the domain seller contact automation script...")
    contact_sellers(CSV_FILE)
    print("Script completed.")
```

### Notes:
- Replace `your_email@gmail.com` and `your_email_password` with your actual credentials. For security, consider using environment variables or a more secure method to store credentials.
- The CSV file `domain_sellers.csv` should contain columns: `Name`, `Email`, and `Domain`.
- Make sure to install the necessary dependencies, and ensure email access is properly configured for your SMTP server.
