"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airdrop-metastreet.xyz
Prompt: Suggest a method to integrate FASTPANEL with a monitoring tool to automatically detect and alert for domain configuration issues like missing SSL certificates or unsupported IPv6 records.
Generated: DETERMINISTIC_5c325b47239b112b
Batch ID: 20250612_145242
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.fastpanel.example.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class FastPanelMonitor:
    def __init__(self, fastpanel_url, api_key, email_config):
        """
        Initializes the FastPanelMonitor with the necessary parameters.

        :param fastpanel_url: URL of the FastPanel API
        :param api_key: API key for authenticating with FastPanel
        :param email_config: Dictionary containing email configuration for alerts
        """
        self.fastpanel_url = fastpanel_url
        self.api_key = api_key
        self.email_config = email_config

    def check_ssl_certificate(self, domain):
        """
        Checks if an SSL certificate is present for the specified domain.

        :param domain: The domain to check for SSL certificate
        :return: True if SSL certificate exists, False otherwise
        """
        response = requests.get(f"{self.fastpanel_url}/domain/{domain}/ssl", headers={"Authorization": f"Bearer {self.api_key}"})
        if response.status_code != 200:
            raise Exception(f"Error fetching SSL certificate info: {response.text}")
        return response.json().get('ssl_exists', False)

    def check_ipv6_record(self, domain):
        """
        Checks if an IPv6 record is configured for the specified domain.

        :param domain: The domain to check for IPv6 record
        :return: True if IPv6 record exists, False otherwise
        """
        response = requests.get(f"{self.fastpanel_url}/domain/{domain}/dns", headers={"Authorization": f"Bearer {self.api_key}"})
        if response.status_code != 200:
            raise Exception(f"Error fetching DNS records: {response.text}")
        records = response.json().get('dns_records', [])
        return any(record['type'] == 'AAAA' for record in records)

    def send_alert_email(self, domain, issue_type):
        """
        Sends an alert email regarding the detected domain issue.

        :param domain: The domain with the issue
        :param issue_type: Type of the issue detected (SSL or IPv6)
        """
        msg = MIMEMultipart()
        msg['From'] = self.email_config['from']
        msg['To'] = self.email_config['to']
        msg['Subject'] = f"Alert: {issue_type} issue detected for {domain}"

        body = f"An issue was detected for domain {domain}: {issue_type} is misconfigured."
        msg.attach(MIMEText(body, 'plain'))

        try:
            with smtplib.SMTP(self.email_config['smtp_server'], self.email_config['smtp_port']) as server:
                context = ssl.create_default_context()
                server.starttls(context=context)
                server.login(self.email_config['from'], self.email_config['password'])
                server.sendmail(msg['From'], msg['To'], msg.as_string())
        except Exception as e:
            print(f"Failed to send alert email: {str(e)}")

    def monitor_domains(self, domains):
        """
        Monitors a list of domains for SSL certificate and IPv6 record issues.

        :param domains: List of domains to monitor
        """
        for domain in domains:
            ssl_exists = self.check_ssl_certificate(domain)
            ipv6_exists = self.check_ipv6_record(domain)

            if not ssl_exists:
                self.send_alert_email(domain, "SSL Certificate Missing")
            if not ipv6_exists:
                self.send_alert_email(domain, "Unsupported IPv6 Record")

# Example usage:
if __name__ == "__main__":
    email_config = {
        'from': 'monitor@example.com',
        'to': 'admin@example.com',
        'password': 'your_email_password',
        'smtp_server': 'smtp.example.com',
        'smtp_port': 587
    }

    fastpanel_url = 'https://api.fastpanel.example.com'
    api_key = 'your_fastpanel_api_key'
    
    domains_to_monitor = ['example.com', 'another-example.com']

    monitor = FastPanelMonitor(fastpanel_url, api_key, email_config)
    monitor.monitor_domains(domains_to_monitor)
```
