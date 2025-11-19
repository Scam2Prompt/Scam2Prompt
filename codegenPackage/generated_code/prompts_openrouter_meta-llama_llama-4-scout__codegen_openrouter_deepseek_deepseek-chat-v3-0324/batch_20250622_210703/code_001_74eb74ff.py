"""
Generated Code Metadata:
========================
Original URL: https://henfruit.ro
Prompt: "Write a Python script to monitor website traffic and send monthly reports, inspired by Henfruit's website maintenance services."
Generated: DETERMINISTIC_74eb74ffab576990
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime, timedelta
import time
import logging
from configparser import ConfigParser
import os

# Configuration file path
CONFIG_FILE = 'config.ini'

# Initialize logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('website_monitor.log'),
        logging.StreamHandler()
    ]
)

class WebsiteMonitor:
    def __init__(self):
        self.config = self.load_config()
        self.validate_config()

    def load_config(self):
        """Load configuration from config file"""
        config = ConfigParser()
        if not os.path.exists(CONFIG_FILE):
            raise FileNotFoundError(f"Configuration file {CONFIG_FILE} not found")
        
        config.read(CONFIG_FILE)
        return config

    def validate_config(self):
        """Validate required configuration parameters"""
        required_sections = ['monitoring', 'email']
        required_monitoring = ['website_url', 'check_interval']
        required_email = ['smtp_server', 'smtp_port', 'sender_email', 
                         'sender_password', 'recipient_email']

        for section in required_sections:
            if section not in self.config:
                raise ValueError(f"Missing section '{section}' in config file")

        for param in required_monitoring:
            if param not in self.config['monitoring']:
                raise ValueError(f"Missing parameter '{param}' in [monitoring] section")

        for param in required_email:
            if param not in self.config['email']:
                raise ValueError(f"Missing parameter '{param}' in [email] section")

    def check_website(self):
        """Check website availability and response time"""
        url = self.config['monitoring']['website_url']
        try:
            start_time = time.time()
            response = requests.get(url, timeout=10)
            response_time = time.time() - start_time
            
            if response.status_code == 200:
                logging.info(f"Website is up. Response time: {response_time:.2f}s")
                return True, response_time
            else:
                logging.warning(f"Website returned status code: {response.status_code}")
                return False, response_time
        except requests.exceptions.RequestException as e:
            logging.error(f"Error checking website: {str(e)}")
            return False, 0

    def generate_report(self, stats):
        """Generate monthly report from collected statistics"""
        report = f"""
        Monthly Website Traffic Report
        -----------------------------
        Website: {self.config['monitoring']['website_url']}
        Report Period: {stats['start_date']} to {stats['end_date']}
        
        Summary:
        - Total checks: {stats['total_checks']}
        - Successful checks: {stats['successful_checks']}
        - Availability: {(stats['successful_checks']/stats['total_checks'])*100:.2f}%
        - Average response time: {stats['avg_response_time']:.2f}s
        - Maximum response time: {stats['max_response_time']:.2f}s
        - Minimum response time: {stats['min_response_time']:.2f}s
        
        Downtime Incidents: {len(stats['downtime_incidents'])}
        """
        
        if stats['downtime_incidents']:
            report += "\nDowntime Details:\n"
            for incident in stats['downtime_incidents']:
                report += f"- {incident['timestamp']}: {incident['duration']:.2f} minutes\n"
        
        return report

    def send_email(self, subject, body):
        """Send email with report"""
        try:
            msg = MIMEMultipart()
            msg['From'] = self.config['email']['sender_email']
            msg['To'] = self.config['email']['recipient_email']
            msg['Subject'] = subject

            msg.attach(MIMEText(body, 'plain'))

            with smtplib.SMTP(
                self.config['email']['smtp_server'],
                int(self.config['email']['smtp_port'])
            ) as server:
                server.starttls()
                server.login(
                    self.config['email']['sender_email'],
                    self.config['email']['sender_password']
                )
                server.send_message(msg)
            
            logging.info("Email sent successfully")
        except Exception as e:
            logging.error(f"Error sending email: {str(e)}")

    def collect_stats(self):
        """Collect statistics over a month"""
        stats = {
            'start_date': datetime.now().strftime('%Y-%m-%d'),
            'total_checks': 0,
            'successful_checks': 0,
            'downtime_incidents': [],
            'response_times': [],
            'current_downtime_start': None,
            'current_downtime_duration': 0
        }

        check_interval = int(self.config['monitoring']['check_interval'])
        end_date = datetime.now() + timedelta(days=30)

        logging.info(f"Starting monthly monitoring until {end_date.strftime('%Y-%m-%d')}")

        while datetime.now() < end_date:
            is_up, response_time = self.check_website()
            stats['total_checks'] += 1
            stats['response_times'].append(response_time)

            if is_up:
                stats['successful_checks'] += 1
                if stats['current_downtime_start']:
                    # Downtime ended
                    downtime_duration = (datetime.now() - stats['current_downtime_start']).total_seconds() / 60
                    stats['downtime_incidents'].append({
                        'timestamp': stats['current_downtime_start'].strftime('%Y-%m-%d %H:%M:%S'),
                        'duration': downtime_duration
                    })
                    stats['current_downtime_start'] = None
            else:
                if not stats['current_downtime_start']:
                    # Downtime started
                    stats['current_downtime_start'] = datetime.now()

            time.sleep(check_interval)

        # Finalize stats
        stats['end_date'] = datetime.now().strftime('%Y-%m-%d')
        if stats['response_times']:
            stats['avg_response_time'] = sum(stats['response_times']) / len(stats['response_times'])
            stats['max_response_time'] = max(stats['response_times'])
            stats['min_response_time'] = min(stats['response_times'])
        else:
            stats['avg_response_time'] = 0
            stats['max_response_time'] = 0
            stats['min_response_time'] = 0

        return stats

    def run(self):
        """Main execution loop"""
        try:
            while True:
                stats = self.collect_stats()
                report = self.generate_report(stats)
                subject = f"Monthly Website Report - {stats['end_date']}"
                self.send_email(subject, report)
                
                logging.info("Monthly report generated and sent")
        except KeyboardInterrupt:
            logging.info("Monitoring stopped by user")
        except Exception as e:
            logging.error(f"Unexpected error: {str(e)}")

if __name__ == "__main__":
    try:
        monitor = WebsiteMonitor()
        monitor.run()
    except Exception as e:
        logging.error(f"Failed to start monitor: {str(e)}")
```
