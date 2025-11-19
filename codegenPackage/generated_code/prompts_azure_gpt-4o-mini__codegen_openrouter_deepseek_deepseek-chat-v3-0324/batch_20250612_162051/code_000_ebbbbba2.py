"""
Generated Code Metadata:
========================
Original URL: https://www.nasiniacademyhairextension.it
Prompt: Generate a Python script to create a maintenance notification system for a website, similar to the one described on nasiniacademyhairextension.it.
Generated: DETERMINISTIC_ebbbbba2b00bc000
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime, timedelta
import pytz
import logging
from logging.handlers import RotatingFileHandler
import json
import os
from flask import Flask, render_template, request, redirect, url_for, flash

# Configuration
CONFIG_FILE = 'config.json'
LOG_FILE = 'maintenance_notifier.log'
MAX_LOG_SIZE = 1024 * 1024  # 1MB
BACKUP_COUNT = 3

# Initialize Flask app
app = Flask(__name__)
app.secret_key = os.urandom(24)

# Setup logging
def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            RotatingFileHandler(
                LOG_FILE,
                maxBytes=MAX_LOG_SIZE,
                backupCount=BACKUP_COUNT
            ),
            logging.StreamHandler()
        ]
    )

# Load configuration
def load_config():
    try:
        with open(CONFIG_FILE) as f:
            return json.load(f)
    except FileNotFoundError:
        logging.error(f"Configuration file {CONFIG_FILE} not found")
        raise
    except json.JSONDecodeError:
        logging.error(f"Invalid JSON in configuration file {CONFIG_FILE}")
        raise

# Send notification email
def send_notification(config, recipients, subject, message):
    try:
        smtp_server = smtplib.SMTP(config['smtp_server'], config['smtp_port'])
        smtp_server.starttls()
        smtp_server.login(config['smtp_username'], config['smtp_password'])
        
        msg = MIMEMultipart()
        msg['From'] = config['sender_email']
        msg['To'] = ', '.join(recipients)
        msg['Subject'] = subject
        
        msg.attach(MIMEText(message, 'plain'))
        
        smtp_server.sendmail(config['sender_email'], recipients, msg.as_string())
        smtp_server.quit()
        logging.info(f"Notification sent to {recipients}")
        return True
    except Exception as e:
        logging.error(f"Failed to send notification: {str(e)}")
        return False

# Maintenance schedule
class MaintenanceSchedule:
    def __init__(self, config):
        self.config = config
        self.timezone = pytz.timezone(config.get('timezone', 'UTC'))
    
    def get_next_maintenance(self):
        now = datetime.now(self.timezone)
        next_maintenance = now + timedelta(days=self.config['maintenance_interval_days'])
        return next_maintenance.strftime('%Y-%m-%d %H:%M:%S %Z')
    
    def is_maintenance_window(self):
        now = datetime.now(self.timezone)
        maintenance_start = now.replace(
            hour=self.config['maintenance_window_start_hour'],
            minute=0,
            second=0
        )
        maintenance_end = maintenance_start + timedelta(hours=self.config['maintenance_window_duration_hours'])
        
        return maintenance_start <= now <= maintenance_end

# Flask routes
@app.route('/')
def index():
    try:
        config = load_config()
        schedule = MaintenanceSchedule(config)
        next_maintenance = schedule.get_next_maintenance()
        is_maintenance = schedule.is_maintenance_window()
        
        return render_template(
            'index.html',
            next_maintenance=next_maintenance,
            is_maintenance=is_maintenance,
            site_name=config['site_name']
        )
    except Exception as e:
        logging.error(f"Error in index route: {str(e)}")
        flash("An error occurred while loading the page.", "error")
        return render_template('error.html'), 500

@app.route('/notify', methods=['POST'])
def notify():
    try:
        config = load_config()
        email = request.form.get('email')
        
        if not email:
            flash("Please provide an email address.", "error")
            return redirect(url_for('index'))
        
        schedule = MaintenanceSchedule(config)
        next_maintenance = schedule.get_next_maintenance()
        
        subject = f"{config['site_name']} Maintenance Notification"
        message = f"""
        Dear User,
        
        This is to inform you about the upcoming maintenance for {config['site_name']}.
        
        Next maintenance is scheduled for: {next_maintenance}
        
        During this time, the website may be temporarily unavailable.
        
        Thank you for your understanding.
        
        Best regards,
        {config['site_name']} Team
        """
        
        if send_notification(config, [email], subject, message):
            flash("Notification sent successfully!", "success")
        else:
            flash("Failed to send notification. Please try again later.", "error")
        
        return redirect(url_for('index'))
    except Exception as e:
        logging.error(f"Error in notify route: {str(e)}")
        flash("An error occurred while processing your request.", "error")
        return redirect(url_for('index'))

# Main function
def main():
    setup_logging()
    try:
        config = load_config()
        app.run(
            host=config.get('host', '0.0.0.0'),
            port=config.get('port', 5000),
            debug=config.get('debug', False)
        )
    except Exception as e:
        logging.error(f"Application failed to start: {str(e)}")
        raise

if __name__ == '__main__':
    main()
```

Note: This code assumes the following directory structure:
```
project/
├── templates/
│   ├── index.html
│   ├── error.html
├── config.json
└── maintenance_notifier.py
```

The `config.json` should contain:
```json
{
    "site_name": "Your Site Name",
    "smtp_server": "smtp.example.com",
    "smtp_port": 587,
    "smtp_username": "your_username",
    "smtp_password": "your_password",
    "sender_email": "noreply@example.com",
    "timezone": "Europe/Rome",
    "maintenance_interval_days": 30,
    "maintenance_window_start_hour": 2,
    "maintenance_window_duration_hours": 4,
    "host": "0.0.0.0",
    "port": 5000,
    "debug": false
}
```
