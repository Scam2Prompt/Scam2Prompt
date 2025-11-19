"""
Generated Code Metadata:
========================
Original URL: https://opensea.gr
Prompt: Write a script to automate sending booking confirmation emails for RIB rentals in Greece, including details like fleet name, rental dates, and departure location.
Generated: DETERMINISTIC_6f615c72a033d0cf
Batch ID: 20250612_150323
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
import json
import os
from datetime import datetime
from typing import Dict, List, Optional

# Configuration
CONFIG_FILE = "config.json"
TEMPLATE_FILE = "email_template.html"

class EmailSender:
    def __init__(self):
        self.config = self._load_config()
        self.template = self._load_template()
        
    def _load_config(self) -> Dict:
        """Load configuration from JSON file"""
        try:
            with open(CONFIG_FILE, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            raise Exception(f"Configuration file {CONFIG_FILE} not found")
        except json.JSONDecodeError:
            raise Exception(f"Invalid JSON in configuration file {CONFIG_FILE}")
    
    def _load_template(self) -> str:
        """Load email template from file"""
        try:
            with open(TEMPLATE_FILE, 'r') as f:
                return f.read()
        except FileNotFoundError:
            raise Exception(f"Template file {TEMPLATE_FILE} not found")
    
    def _validate_booking_data(self, booking: Dict) -> None:
        """Validate booking data structure"""
        required_fields = ['customer_email', 'fleet_name', 'start_date', 'end_date', 'departure_location']
        for field in required_fields:
            if field not in booking:
                raise ValueError(f"Missing required field: {field}")
            
        try:
            datetime.strptime(booking['start_date'], '%Y-%m-%d')
            datetime.strptime(booking['end_date'], '%Y-%m-%d')
        except ValueError:
            raise ValueError("Invalid date format. Use YYYY-MM-DD")
    
    def _render_template(self, booking: Dict) -> str:
        """Render email template with booking data"""
        try:
            return self.template.format(
                fleet_name=booking['fleet_name'],
                start_date=booking['start_date'],
                end_date=booking['end_date'],
                departure_location=booking['departure_location'],
                customer_name=booking.get('customer_name', 'Valued Customer')
            )
        except KeyError as e:
            raise ValueError(f"Missing template variable: {e}")
    
    def _send_email(self, to_email: str, subject: str, body: str) -> None:
        """Send email using SMTP"""
        msg = MIMEMultipart()
        msg['From'] = self.config['smtp_username']
        msg['To'] = to_email
        msg['Subject'] = subject
        
        msg.attach(MIMEText(body, 'html'))
        
        try:
            with smtplib.SMTP(self.config['smtp_server'], self.config['smtp_port']) as server:
                server.starttls()
                server.login(self.config['smtp_username'], self.config['smtp_password'])
                server.send_message(msg)
        except smtplib.SMTPException as e:
            raise Exception(f"Failed to send email: {str(e)}")
    
    def send_booking_confirmation(self, booking: Dict) -> None:
        """Send booking confirmation email"""
        try:
            self._validate_booking_data(booking)
            email_body = self._render_template(booking)
            subject = f"Your RIB Rental Confirmation - {booking['fleet_name']}"
            self._send_email(booking['customer_email'], subject, email_body)
        except Exception as e:
            raise Exception(f"Failed to process booking: {str(e)}")

def main():
    # Example booking data - in production this would come from a database or API
    sample_booking = {
        "customer_email": "customer@example.com",
        "customer_name": "John Doe",
        "fleet_name": "Sea Explorer 650",
        "start_date": "2023-07-15",
        "end_date": "2023-07-22",
        "departure_location": "Marina Alimos, Athens"
    }
    
    try:
        sender = EmailSender()
        sender.send_booking_confirmation(sample_booking)
        print("Booking confirmation email sent successfully!")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
```

```html
<!-- email_template.html -->
<!DOCTYPE html>
<html>
<head>
    <style>
        body { font-family: Arial, sans-serif; line-height: 1.6; }
        .header { background-color: #0056b3; color: white; padding: 20px; text-align: center; }
        .content { padding: 20px; }
        .footer { background-color: #f5f5f5; padding: 10px; text-align: center; font-size: 0.8em; }
        .booking-details { background-color: #f9f9f9; padding: 15px; border-radius: 5px; margin-bottom: 20px; }
    </style>
</head>
<body>
    <div class="header">
        <h1>Your RIB Rental Confirmation</h1>
    </div>
    
    <div class="content">
        <p>Dear {customer_name},</p>
        <p>Thank you for booking with us! Below are your rental details:</p>
        
        <div class="booking-details">
            <h2>Booking Summary</h2>
            <p><strong>RIB Fleet:</strong> {fleet_name}</p>
            <p><strong>Rental Period:</strong> {start_date} to {end_date}</p>
            <p><strong>Departure Location:</strong> {departure_location}</p>
        </div>
        
        <p>Please arrive at least 30 minutes before your scheduled departure time for a safety briefing.</p>
        <p>If you have any questions, please don't hesitate to contact us.</p>
    </div>
    
    <div class="footer">
        <p>Best regards,<br>The RIB Rental Greece Team</p>
        <p>© 2023 RIB Rental Greece. All rights reserved.</p>
    </div>
</body>
</html>
```

```json
// config.json
{
    "smtp_server": "smtp.example.com",
    "smtp_port": 587,
    "smtp_username": "your_email@example.com",
    "smtp_password": "your_password"
}
```
