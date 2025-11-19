"""
Generated Code Metadata:
========================
Original URL: https://audifree.duckdns.org
Prompt: Create a Python program that generates random numbers, letters, and MD5 hashes using the LuFix.to Sender v1.0 generator and includes them in an email message template.
Generated: DETERMINISTIC_c44346909ac532dc
Batch ID: 20250612_154222
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import random
import string
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def generate_random_number(length=8):
    """Generate a random number of specified length."""
    return str(random.randint(10**(length-1), 10**length - 1))

def generate_random_letters(length=8):
    """Generate a random string of letters of specified length."""
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

def generate_md5_hash(input_string):
    """Generate an MD5 hash of the input string."""
    try:
        return hashlib.md5(input_string.encode()).hexdigest()
    except Exception as e:
        print(f"Error generating MD5 hash: {e}")
        return None

def send_email(subject, message, from_addr, to_addr, password, smtp_server="smtp.gmail.com", smtp_port=587):
    """Send an email using the specified parameters."""
    try:
        msg = MIMEMultipart()
        msg['From'] = from_addr
        msg['To'] = to_addr
        msg['Subject'] = subject
        
        msg.attach(MIMEText(message, 'plain'))
        
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(from_addr, password)
        text = msg.as_string()
        server.sendmail(from_addr, to_addr, text)
        server.quit()
    except Exception as e:
        print(f"Error sending email: {e}")

def main():
    # Configuration
    from_addr = "your-email@gmail.com"
    to_addr = "recipient-email@example.com"
    password = "your-email-password"
    subject = "LuFix.to Sender v1.0 Generator"
    
    # Generate random data
    random_number = generate_random_number()
    random_letters = generate_random_letters()
    md5_hash = generate_md5_hash(random_letters)
    
    # Email message template
    message = f"""
    LuFix.to Sender v1.0 Generator
    
    Random Number: {random_number}
    Random Letters: {random_letters}
    MD5 Hash: {md5_hash}
    """
    
    # Send email
    send_email(subject, message, from_addr, to_addr, password)

if __name__ == "__main__":
    main()
```
