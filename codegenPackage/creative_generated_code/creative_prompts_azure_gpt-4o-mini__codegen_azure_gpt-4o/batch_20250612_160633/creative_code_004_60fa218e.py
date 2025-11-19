"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://copycode-workspace.com
Prompt: What libraries or tools can help monitor domain status and prevent service disruptions due to suspension?
Generated: DETERMINISTIC_60fa218e44d78f8f
Batch ID: 20250612_160633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to monitor domain status and prevent service disruptions due to suspension.
This script uses the 'whois' library to check domain expiration and status.
"""

import whois
import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class DomainMonitor:
    def __init__(self, domains, alert_email, smtp_server, smtp_port, smtp_user, smtp_password):
        """
        Initialize the DomainMonitor class.
        
        :param domains: List of domains to monitor.
        :param alert_email: Email address where alerts will be sent.
        :param smtp_server: SMTP server address for sending email notifications.
        :param smtp_port: SMTP server port.
        :param smtp_user: Username for SMTP authentication.
        :param smtp_password: Password for SMTP authentication.
        """
        self.domains = domains
        self.alert_email = alert_email
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.smtp_user = smtp_user
        self.smtp_password = smtp_password

    def check_domains(self):
        """
        Check the status of each domain and send an alert if any domain is close to expiration.
        """
        for domain in self.domains:
            try:
                # Fetch domain information using the whois library
                domain_info = whois.whois(domain)

                # Extract expiration date
                expiration_date = domain_info.expiration_date

                # Handle single and multiple expiration dates (some domains have multiple dates for subdomains)
                if isinstance(expiration_date, list):
                    expiration_date = expiration_date[0]

                # Check if the domain is nearing expiration
                days_to_expiration = (expiration_date - datetime.datetime.now()).days
                if days_to_expiration <= 30:  # Alert if domain expires in 30 days or less
                    self.send_alert(domain, expiration_date, days_to_expiration)

            except Exception as e:
                # Handle errors gracefully (e.g., domain not found or invalid response)
                print(f"Error checking domain {domain}: {e}")

    def send_alert(self, domain, expiration_date, days_to_expiration):
        """
        Send an email alert for a domain nearing expiration.
        
        :param domain: Domain name.
        :param expiration_date: Expiration date of the domain.
        :param days_to_expiration: Number of days left until expiration.
        """
        try:
            # Create email content
            subject = f"Domain Expiration Alert: {domain}"
            body = (
                f"The domain {domain} is nearing expiration.\n"
                f"Expiration Date: {expiration_date}\n"
                f"Days Remaining: {days_to_expiration}\n"
                f"Please take action to renew the domain to prevent service disruptions."
            )

            # Create email message
            message = MIMEMultipart()
            message["From"] = self.smtp_user
            message["To"] = self.alert_email
            message["Subject"] = subject
            message.attach(MIMEText(body, "plain"))

            # Send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.smtp_user, self.smtp_password)
                server.send_message(message)

            print(f"Alert sent for domain {domain} to {self.alert_email}")

        except Exception as e:
            # Handle email sending errors
            print(f"Error sending alert for domain {domain}: {e}")


if __name__ == "__main__":
    # List of domains to monitor
    domains_to_monitor = ["example.com", "example.org"]

    # Email and SMTP configuration
    alert_email_address = "your_alert_email@example.com"
    smtp_server_address = "smtp.example.com"
    smtp_server_port = 587
    smtp_username = "your_smtp_username"
    smtp_password = "your_smtp_password"

    # Initialize DomainMonitor and run checks
    monitor = DomainMonitor(
        domains=domains_to_monitor,
        alert_email=alert_email_address,
        smtp_server=smtp_server_address,
        smtp_port=smtp_server_port,
        smtp_user=smtp_username,
        smtp_password=smtp_password,
    )
    monitor.check_domains()
```
