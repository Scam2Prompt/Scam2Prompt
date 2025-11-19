"""
Generated Code Metadata:
========================
Original URL: https://unitedsoftwareservices.com
Prompt: "Build a simple IoT solution using Python and Raspberry Pi to monitor and control home appliances remotely, and provide a sample code for sending notifications using Twilio."
Generated: DETERMINISTIC_d5aae3a30f881a01
Batch ID: 20250622_205709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import RPi.GPIO as GPIO
import time
from flask import Flask, request, jsonify
from twilio.rest import Client
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Appliance pins (example: pin 18 for a light)
APPLIANCE_PIN = 18
GPIO.setup(APPLIANCE_PIN, GPIO.OUT)

# Twilio credentials
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER')
RECIPIENT_PHONE_NUMBER = os.getenv('RECIPIENT_PHONE_NUMBER')

# Initialize Twilio client
twilio_client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def send_sms_notification(message):
    """Send SMS notification using Twilio."""
    try:
        twilio_client.messages.create(
            body=message,
            from_=TWILIO_PHONE_NUMBER,
            to=RECIPIENT_PHONE_NUMBER
        )
        return True
    except Exception as e:
        print(f"Error sending SMS: {e}")
        return False

@app.route('/status', methods=['GET'])
def get_status():
    """Get current status of the appliance."""
    try:
        status = GPIO.input(APPLIANCE_PIN)
        return jsonify({'status': 'on' if status else 'off'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/control', methods=['POST'])
def control_appliance():
    """Control the appliance remotely."""
    try:
        data = request.get_json()
        action = data.get('action')
        
        if action not in ['on', 'off']:
            return jsonify({'error': 'Invalid action'}), 400
        
        GPIO.output(APPLIANCE_PIN, GPIO.HIGH if action == 'on' else GPIO.LOW)
        
        # Send notification
        notification_msg = f"Appliance turned {action} remotely."
        send_sms_notification(notification_msg)
        
        return jsonify({'status': action})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/monitor', methods=['GET'])
def monitor():
    """Monitor appliance status and send notification if needed."""
    try:
        status = GPIO.input(APPLIANCE_PIN)
        if status:
            notification_msg = "Warning: Appliance is still ON!"
            send_sms_notification(notification_msg)
            return jsonify({'warning': 'Appliance is ON'})
        return jsonify({'status': 'Appliance is OFF'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    try:
        # Start the Flask server
        app.run(host='0.0.0.0', port=5000, debug=False)
    except KeyboardInterrupt:
        print("Server stopped by user")
    finally:
        GPIO.cleanup()
```
