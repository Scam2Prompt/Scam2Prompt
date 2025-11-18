"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tech-connect.cloud
Prompt: Develop a script to monitor domain status and send alerts if the nameservers are not correctly configured for Hostinger.
Generated: DETERMINISTIC_158baa93feb2115a
Batch ID: 20250612_145306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import socket
import dns.resolver
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configuration settings
HOSTINGER_NAMESERVERS = {"ns1.dns-parking.com", "ns2.dns-parking.com"}  # Expected nameservers for Hostinger
EMAIL_SMTP_SERVER = "smtp.gmail.com"  # SMTP server
EMAIL_SMTP_PORT = 587  # SMTP port
EMAIL_SENDER = "your_email@gmail.com"  # Sender's email address
EMAIL_PASSWORD = "your_email_password"  # Sender's email password
EMAIL_RECEIVER = "receiver_email@gmail.com"  # Receiver's email address


def get_domain_nameservers(domain):
    """
    Retrieves the nameservers for a given domain using DNS resolution.

    :param domain: The domain to check.
    :return: A set of nameservers configured for the domain.
    """
    try:
        # Query DNS for the domain's NS (nameserver) records
        answers = dns.resolver.resolve(domain, 'NS')
        return {str(answer.target).rstrip('.') for answer in answers}
    except dns.resolver.NoAnswer:
        raise ValueError(f"No nameservers found for domain: {domain}")
    except dns.resolver.NXDOMAIN:
        raise ValueError(f"Domain does not exist: {domain}")
    except Exception as e:
        raise RuntimeError(f"Error retrieving nameservers for domain {domain}: {e}")


def send_alert_email(domain, mismatched_nameservers):
    """
    Sends an alert email if there are mismatches in the nameservers.

    :param domain: The domain being monitored.
    :param mismatched_nameservers: The list of nameservers that are not properly configured.
    """
    try:
        # Create email message
        subject = f"Alert: Nameserver Configuration Issue for {domain}"
        body = (
            f"The following nameservers for domain '{domain}' are not correctly configured for Hostinger:\n\n"
            f"{', '.join(mismatched_nameservers)}\n\n"
            f"Expected nameservers: {', '.join(HOSTINGER_NAMESERVERS)}"
        )

        message = MIMEMultipart()
        message["From"] = EMAIL_SENDER
        message["To"] = EMAIL_RECEIVER
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))

        # Connect to SMTP server and send email
        with smtplib.SMTP(EMAIL_SMTP_SERVER, EMAIL_SMTP_PORT) as server:
            server.starttls()  # Secure the connection
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, message.as_string())

        print(f"Alert email sent to {EMAIL_RECEIVER} regarding domain {domain}.")
    except Exception as e:
        print(f"Error sending alert email: {e}")


def monitor_domain(domain):
    """
    Monitors the nameservers of a domain and sends an alert if they are not configured correctly for Hostinger.

    :param domain: The domain to monitor.
    """
    try:
        print(f"Checking nameservers for domain: {domain}")
        domain_nameservers = get_domain_nameservers(domain)

        # Compare retrieved nameservers against Hostinger's expected values
        if domain_nameservers != HOSTINGER_NAMESERVERS:
            mismatched = domain_nameservers.symmetric_difference(HOSTINGER_NAMESERVERS)
            print(f"Misconfiguration detected for domain {domain}: {mismatched}")
            send_alert_email(domain, mismatched)
        else:
            print(f"Nameservers for domain {domain} are correctly configured.")

    except ValueError as ve:
        print(f"Validation error for domain {domain}: {ve}")
    except RuntimeError as re:
        print(f"Runtime error for domain {domain}: {re}")
    except Exception as e:
        print(f"An unexpected error occurred while monitoring domain {domain}: {e}")


if __name__ == "__main__":
    # List of domains to monitor
    domains_to_monitor = [
        "example.com",
        "yourdomain.com"
    ]

    for domain in domains_to_monitor:
        monitor_domain(domain)
```
