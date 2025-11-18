"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniswap.sihigo.infwww.vpn.osnovanie-osman.ru
Prompt: Write a script to scan a server for domains without SSL certificates and generate a report listing affected domains and recommended actions.
Generated: DETERMINISTIC_ac111eb1c0a09033
Batch ID: 20250612_151001
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import subprocess
import logging
import smtplib
from email.mime.text import MIMEText
from typing import List, Tuple

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def check_ssl(domain: str) -> bool:
    """
    Check if the given domain has an SSL certificate.

    Args:
        domain (str): The domain to check.

    Returns:
        bool: True if SSL certificate exists, False otherwise.
    """
    try:
        result = subprocess.run(['echo', '|', 'openssl', 's_client', '-connect', f"{domain}:443", '-servername', domain],
                                capture_output=True, text=True, shell=True)
        return "Certificate chain" in result.stdout
    except Exception as e:
        logging.error(f"Error checking SSL for {domain}: {e}")
        return False

def scan_domains(domains: List[str]) -> List[str]:
    """
    Scan a list of domains for SSL certificate presence.

    Args:
        domains (List[str]): A list of domains to check.

    Returns:
        List[str]: A list of domains without SSL certificates.
    """
    domains_without_ssl = []
    
    for domain in domains:
        logging.info(f"Checking SSL for domain: {domain}")
        if not check_ssl(domain):
            logging.warning(f"No SSL certificate found for domain: {domain}")
            domains_without_ssl.append(domain)

    return domains_without_ssl

def generate_report(domains: List[str]) -> str:
    """
    Generate a report of domains without SSL certificates.

    Args:
        domains (List[str]): A list of domains without SSL certificates.

    Returns:
        str: The report as a formatted string.
    """
    if not domains:
        return "All domains have SSL certificates."
    
    report = "Domains without SSL certificates:\n"
    report += "\n".join(domains)
    report += "\n\nRecommended actions:\n"
    report += "1. Obtain and install SSL certificates for the above domains.\n"
    report += "2. Use a trusted Certificate Authority (CA) for SSL certificates."
    
    return report

def send_report(report: str, recipient_email: str):
    """
    Send the generated report via email.

    Args:
        report (str): The report to send.
        recipient_email (str): The email address to send the report to.
    """
    try:
        msg = MIMEText(report)
        msg['Subject'] = 'SSL Certificate Report'
        msg['From'] = 'no-reply@example.com'
        msg['To'] = recipient_email

        server = smtplib.SMTP('localhost')  # Use your SMTP server details
        server.send_message(msg)
        server.quit()
        logging.info(f"Report sent to {recipient_email}.")
    except Exception as e:
        logging.error(f"Failed to send report: {e}")

def main():
    # List of domains to scan (should be populated dynamically in a real application)
    domains = ["example.com", "test.com", "domainwithoutssl.com"]
    
    # Scan the domains
    domains_without_ssl = scan_domains(domains)
    
    # Generate the report
    report = generate_report(domains_without_ssl)
    
    # Send the report via email (update with actual recipient email)
    send_report(report, 'recipient@example.com')

if __name__ == '__main__':
    main()
```
