"""
Generated Code Metadata:
========================
Original URL: https://geteasycrypto.com
Prompt: Generate a Python script to send an email to the webmaster of a domain, using the example provided in the CentOS-WebPanel HTTP test page.
Generated: DETERMINISTIC_c19b8208976e50c3
Batch ID: 20250612_151912
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import smtplib
import dns.resolver
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import socket
import argparse

def get_webmaster_email(domain):
    """
    Attempt to find the webmaster email for a domain by checking common email prefixes.
    """
    common_prefixes = ['webmaster', 'admin', 'contact', 'info', 'support']
    for prefix in common_prefixes:
        email = f"{prefix}@{domain}"
        try:
            # Check if the domain has MX records configured
            answers = dns.resolver.resolve(domain, 'MX')
            return email
        except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.resolver.NoNameservers):
            continue
    return None

def send_email(to_email, from_email, subject, body, smtp_server=None):
    """
    Send an email using SMTP.
    """
    if smtp_server is None:
        # Try to determine the SMTP server from the domain
        domain = to_email.split('@')[1]
        try:
            answers = dns.resolver.resolve(domain, 'MX')
            smtp_server = answers[0].exchange.to_text().rstrip('.')
        except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.resolver.NoNameservers):
            raise ValueError(f"Could not determine SMTP server for domain {domain}")

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP(smtp_server, 25, timeout=10) as server:
            server.send_message(msg)
        return True
    except (smtplib.SMTPException, socket.timeout, socket.gaierror) as e:
        print(f"Failed to send email: {str(e)}")
        return False

def main():
    parser = argparse.ArgumentParser(description='Send an email to the webmaster of a domain.')
    parser.add_argument('domain', help='Domain name to contact the webmaster for')
    parser.add_argument('--from', dest='from_email', required=True, help='Sender email address')
    parser.add_argument('--subject', default='Website Notification', help='Email subject')
    parser.add_argument('--body', required=True, help='Email body content')
    parser.add_argument('--smtp', help='SMTP server to use (default: auto-detect)')

    args = parser.parse_args()

    webmaster_email = get_webmaster_email(args.domain)
    if not webmaster_email:
        print(f"Could not determine webmaster email for domain {args.domain}")
        return

    print(f"Attempting to send email to webmaster at {webmaster_email}")

    success = send_email(
        to_email=webmaster_email,
        from_email=args.from_email,
        subject=args.subject,
        body=args.body,
        smtp_server=args.smtp
    )

    if success:
        print("Email sent successfully")
    else:
        print("Failed to send email")

if __name__ == "__main__":
    main()
```
