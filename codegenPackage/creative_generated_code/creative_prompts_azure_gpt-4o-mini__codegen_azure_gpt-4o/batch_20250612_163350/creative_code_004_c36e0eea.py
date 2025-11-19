"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://millennium-capital.com
Prompt: Illustrate how to use a library to automate the process of contacting domain owners for potential long-term leases, specifically for domains like Private-Jets.com and EliteBridal.com.
Generated: DETERMINISTIC_c36e0eeab346f5ab
Batch ID: 20250612_163350
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests
import whois
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Function to get WHOIS information for a domain
def get_domain_owner_info(domain):
    try:
        # Fetch WHOIS data
        domain_data = whois.whois(domain)
        return {
            "email": domain_data.email,
            "name": domain_data.name,
            "org": domain_data.org
        }
    except Exception as e:
        print(f"Error fetching WHOIS data for {domain}: {e}")
        return None

# Function to send an email to the domain owner
def send_email(to_email, domain_name):
    try:
        # Email credentials
        sender_email = "your_email@example.com"
        sender_password = "your_email_password"

        # Create the email content
        subject = f"Inquiry about leasing the domain {domain_name}"
        body = f"""
        Dear Domain Owner,

        I hope this message finds you well. I am interested in discussing a potential long-term lease for the domain {domain_name}. 
        Please let me know if this is something you would consider. 

        Feel free to reach out to me at your convenience.

        Best regards,
        [Your Name]
        """

        # Create MIME email object
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Connect to SMTP server and send the email
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()  # Secure the connection
            server.login(sender_email, sender_password)  # Login to the email account
            server.sendmail(sender_email, to_email, msg.as_string())  # Send the email

        print(f"Email successfully sent to {to_email} regarding {domain_name}")
    except Exception as e:
        print(f"Error sending email to {to_email}: {e}")

# Main function to automate contacting domain owners
def automate_contact(domains):
    for domain in domains:
        print(f"Processing domain: {domain}")
        owner_info = get_domain_owner_info(domain)
        
        # Check if WHOIS data contains email
        if owner_info and owner_info['email']:
            print(f"Owner information found for {domain}: {owner_info}")
            send_email(owner_info['email'], domain)
        else:
            print(f"No contact information available for {domain}")

# List of domains to inquire about
domains_to_inquire = ["Private-Jets.com", "EliteBridal.com"]

# Run the automation process
if __name__ == "__main__":
    automate_contact(domains_to_inquire)
```

### Notes:
- Replace `your_email@example.com` and `your_email_password` with your actual email credentials.
- Ensure you have access to the WHOIS library (`pip install python-whois`) and the `requests` library (`pip install requests`).
- Be mindful of WHOIS data privacy regulations and only use this script in compliance with relevant laws.
