"""
Generated Code Metadata:
========================
Original URL: https://opsec.finance
Prompt: "Write a code snippet to automate the reporting of potential security incidents in a financial system."
Generated: DETERMINISTIC_94e178ba6358afbd
Batch ID: 20250622_211650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# security_incident_reporter.py

import logging
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import json

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class SecurityIncidentReporter:
    def __init__(self, config):
        """
        Initialize the SecurityIncidentReporter with configuration.

        :param config: A dictionary containing reporter configuration.
            - 'smtp_server' (str): SMTP server to use for sending emails.
            - 'smtp_port' (int): SMTP server port.
            - 'from_email' (str): Email address to send from.
            - 'to_emails' (list[str]): List of email addresses to send to.
            - 'incident_threshold' (int): Threshold for incident severity.
        """
        self.config = config

    def report_incident(self, incident_data):
        """
        Report a potential security incident.

        :param incident_data: A dictionary containing incident data.
            - 'severity' (int): Severity of the incident (1-10).
            - 'description' (str): Description of the incident.
            - 'timestamp' (str): Timestamp of the incident.
        """
        try:
            # Check if incident severity meets the threshold
            if incident_data['severity'] >= self.config['incident_threshold']:
                # Create email message
                msg = MIMEMultipart()
                msg['From'] = self.config['from_email']
                msg['To'] = ', '.join(self.config['to_emails'])
                msg['Subject'] = 'Potential Security Incident Report'

                # Create email body
                email_body = f"""
                Severity: {incident_data['severity']}
                Description: {incident_data['description']}
                Timestamp: {incident_data['timestamp']}
                """
                msg.attach(MIMEText(email_body, 'plain'))

                # Send email using SMTP server
                server = smtplib.SMTP(self.config['smtp_server'], self.config['smtp_port'])
                server.starttls()
                server.login(self.config['from_email'], 'password')  # Replace with actual password or authentication method
                text = msg.as_string()
                server.sendmail(self.config['from_email'], self.config['to_emails'], text)
                server.quit()

                logger.info('Security incident report sent successfully.')
            else:
                logger.info('Incident severity does not meet the threshold.')
        except Exception as e:
            logger.error(f'Error reporting security incident: {str(e)}')

def load_config(config_file):
    """
    Load reporter configuration from a JSON file.

    :param config_file: Path to the configuration file.
    :return: A dictionary containing reporter configuration.
    """
    try:
        with open(config_file, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        logger.error(f'Configuration file not found: {config_file}')
        return {}
    except json.JSONDecodeError as e:
        logger.error(f'Error parsing configuration file: {str(e)}')
        return {}

def main():
    # Load configuration from file
    config = load_config('config.json')

    # Create a SecurityIncidentReporter instance
    reporter = SecurityIncidentReporter(config)

    # Example incident data
    incident_data = {
        'severity': 5,
        'description': 'Unusual login activity detected.',
        'timestamp': '2023-03-01 12:00:00'
    }

    # Report the incident
    reporter.report_incident(incident_data)

if __name__ == '__main__':
    main()
```

**config.json**
```json
{
    "smtp_server": "smtp.example.com",
    "smtp_port": 587,
    "from_email": "security@example.com",
    "to_emails": ["security_team@example.com"],
    "incident_threshold": 3
}
```
