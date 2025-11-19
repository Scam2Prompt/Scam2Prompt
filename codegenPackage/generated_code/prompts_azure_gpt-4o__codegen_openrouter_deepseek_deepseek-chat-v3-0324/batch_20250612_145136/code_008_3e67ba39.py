"""
Generated Code Metadata:
========================
Original URL: https://meghbd.com
Prompt: Create a Python script to monitor uptime for websites hosted on a server, ensuring 99.9% uptime as promised in the hosting features of the Megh iTech website.
Generated: DETERMINISTIC_3e67ba39653db91b
Batch ID: 20250612_145136
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import requests
import time
import logging
from datetime import datetime, timedelta
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import json
import os

# Configuration
CONFIG_FILE = 'monitor_config.json'
LOG_FILE = 'uptime_monitor.log'
CHECK_INTERVAL = 300  # 5 minutes in seconds
MAX_RETRIES = 3
RETRY_DELAY = 10  # seconds

# Email configuration (to be loaded from config)
EMAIL_CONFIG = {
    'smtp_server': '',
    'smtp_port': 587,
    'sender_email': '',
    'sender_password': '',
    'receiver_email': '',
    'subject_prefix': '[Uptime Monitor]'
}

# Initialize logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

class UptimeMonitor:
    def __init__(self):
        self.websites = []
        self.uptime_stats = {}
        self.load_config()
        self.validate_config()
        
    def load_config(self):
        """Load configuration from JSON file"""
        try:
            if not os.path.exists(CONFIG_FILE):
                raise FileNotFoundError(f"Config file {CONFIG_FILE} not found")
            
            with open(CONFIG_FILE, 'r') as f:
                config = json.load(f)
                
            self.websites = config.get('websites', [])
            self.uptime_stats = {site: {'up': 0, 'down': 0} for site in self.websites}
            
            # Update email config
            email_config = config.get('email', {})
            for key in EMAIL_CONFIG:
                if key in email_config:
                    EMAIL_CONFIG[key] = email_config[key]
                    
        except Exception as e:
            logger.error(f"Error loading config: {str(e)}")
            raise

    def validate_config(self):
        """Validate the loaded configuration"""
        if not self.websites:
            raise ValueError("No websites configured for monitoring")
            
        if not all([isinstance(site, str) for site in self.websites]):
            raise ValueError("Website URLs must be strings")
            
        required_email_fields = ['smtp_server', 'sender_email', 'sender_password', 'receiver_email']
        for field in required_email_fields:
            if not EMAIL_CONFIG.get(field):
                raise ValueError(f"Missing required email configuration: {field}")

    def check_website(self, url):
        """Check if a website is up and running"""
        for attempt in range(MAX_RETRIES):
            try:
                response = requests.get(
                    url,
                    timeout=10,
                    headers={'User-Agent': 'UptimeMonitor/1.0'},
                    allow_redirects=True
                )
                if response.status_code < 400:
                    return True
                else:
                    logger.warning(f"Website {url} returned status code {response.status_code}")
                    time.sleep(RETRY_DELAY)
            except requests.RequestException as e:
                logger.warning(f"Attempt {attempt + 1} failed for {url}: {str(e)}")
                time.sleep(RETRY_DELAY)
                
        return False

    def update_stats(self, url, is_up):
        """Update uptime statistics"""
        if is_up:
            self.uptime_stats[url]['up'] += 1
        else:
            self.uptime_stats[url]['down'] += 1

    def calculate_uptime(self, url):
        """Calculate uptime percentage for a website"""
        stats = self.uptime_stats.get(url, {'up': 0, 'down': 0})
        total = stats['up'] + stats['down']
        if total == 0:
            return 100.0
        return (stats['up'] / total) * 100

    def send_alert(self, url, is_up):
        """Send email alert for website status change"""
        status = "UP" if is_up else "DOWN"
        subject = f"{EMAIL_CONFIG['subject_prefix']} Website {status}: {url}"
        
        uptime_percent = self.calculate_uptime(url)
        body = f"""
        Website: {url}
        Status: {status}
        Current Uptime: {uptime_percent:.2f}%
        Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        """
        
        msg = MIMEMultipart()
        msg['From'] = EMAIL_CONFIG['sender_email']
        msg['To'] = EMAIL_CONFIG['receiver_email']
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        
        try:
            with smtplib.SMTP(EMAIL_CONFIG['smtp_server'], EMAIL_CONFIG['smtp_port']) as server:
                server.starttls()
                server.login(EMAIL_CONFIG['sender_email'], EMAIL_CONFIG['sender_password'])
                server.send_message(msg)
            logger.info(f"Alert sent for {url} (Status: {status})")
        except Exception as e:
            logger.error(f"Failed to send alert email: {str(e)}")

    def generate_report(self):
        """Generate uptime report for all websites"""
        report = []
        for url in self.websites:
            uptime = self.calculate_uptime(url)
            report.append({
                'website': url,
                'uptime_percentage': uptime,
                'meets_sla': uptime >= 99.9,
                'checks': self.uptime_stats[url]
            })
        return report

    def log_report(self):
        """Log the current uptime report"""
        report = self.generate_report()
        logger.info("Current Uptime Report:")
        for entry in report:
            status = "PASS" if entry['meets_sla'] else "FAIL"
            logger.info(
                f"{entry['website']}: {entry['uptime_percentage']:.2f}% "
                f"(Checks: {entry['checks']['up']} up, {entry['checks']['down']} down) - {status}"
            )

    def run(self):
        """Main monitoring loop"""
        logger.info("Starting uptime monitor")
        last_status = {url: True for url in self.websites}
        
        try:
            while True:
                for url in self.websites:
                    try:
                        is_up = self.check_website(url)
                        self.update_stats(url, is_up)
                        
                        # Send alert if status changed
                        if last_status.get(url) != is_up:
                            self.send_alert(url, is_up)
                            last_status[url] = is_up
                            
                        # Log if uptime drops below 99.9%
                        uptime = self.calculate_uptime(url)
                        if uptime < 99.9:
                            logger.warning(
                                f"Uptime for {url} is below 99.9%: {uptime:.2f}%"
                            )
                            
                    except Exception as e:
                        logger.error(f"Error monitoring {url}: {str(e)}")
                
                self.log_report()
                time.sleep(CHECK_INTERVAL)
                
        except KeyboardInterrupt:
            logger.info("Monitoring stopped by user")
        except Exception as e:
            logger.error(f"Fatal error in monitoring loop: {str(e)}")
        finally:
            # Final report
            logger.info("Final Uptime Report:")
            self.log_report()

if __name__ == "__main__":
    try:
        monitor = UptimeMonitor()
        monitor.run()
    except Exception as e:
        logger.error(f"Failed to start monitor: {str(e)}")
```
