"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aiiocate-friendtech.app
Prompt: How do I set up alerts for suspected phishing activity on my site using Cloudflare's tools?
Generated: DETERMINISTIC_7595f62546ba7e79
Batch ID: 20250612_162538
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.cloudflare.com/client/v4": {
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
import os
import requests

# Configuration
CLOUDFLARE_API_URL = "https://api.cloudflare.com/client/v4"
CLOUDFLARE_ZONE_ID = os.getenv("CLOUDFLARE_ZONE_ID")  # Your Cloudflare zone ID
CLOUDFLARE_API_KEY = os.getenv("CLOUDFLARE_API_KEY")  # Your Cloudflare API key
CLOUDFLARE_EMAIL = os.getenv("CLOUDFLARE_EMAIL")      # Your Cloudflare account email
ALERT_EMAIL = os.getenv("ALERT_EMAIL")                # Email to send phishing alerts to
PHISHING_DETECTION_LOG = "phishing_detection.log"     # File to log phishing activity

# Email Notification Function
def send_alert(email, message):
    """
    Sends an alert email to the specified recipient.
    :param email: Recipient email address
    :param message: Alert message content
    """
    # This is a placeholder function. Replace with your email-sending setup.
    print(f"Sending alert to {email}:\n{message}")

# Check Suspicious Activity via Cloudflare Firewall Logs
def check_suspicious_activity():
    """
    Checks Cloudflare firewall logs for suspicious requests and alerts if phishing activity is detected.
    """
    try:
        # API request headers for Cloudflare
        headers = {
            "X-Auth-Email": CLOUDFLARE_EMAIL,
            "X-Auth-Key": CLOUDFLARE_API_KEY,
            "Content-Type": "application/json"
        }

        # Endpoint to fetch firewall events (replace with appropriate endpoint)
        url = f"{CLOUDFLARE_API_URL}/zones/{CLOUDFLARE_ZONE_ID}/firewall/events"
        
        # Perform the API request
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the JSON response
        data = response.json()
        firewall_events = data.get("result", [])
        
        # Check for phishing-related events
        phishing_activity_detected = False
        alert_message = "Suspected phishing activity detected:\n\n"

        for event in firewall_events:
            if "phishing" in event.get("rule_description", "").lower():
                phishing_activity_detected = True
                alert_message += f"IP: {event.get('source_ip')}, URL: {event.get('url')}, Action: {event.get('action')}\n"
                
                # Log the phishing event
                with open(PHISHING_DETECTION_LOG, "a") as log_file:
                    log_file.write(f"{event}\n")
        
        # Send alert if phishing activity is detected
        if phishing_activity_detected:
            send_alert(ALERT_EMAIL, alert_message)

    except requests.exceptions.RequestException as e:
        # Log the error and alert the admin
        error_message = f"Error checking Cloudflare logs: {e}"
        with open(PHISHING_DETECTION_LOG, "a") as log_file:
            log_file.write(f"{error_message}\n")
        send_alert(ALERT_EMAIL, error_message)

# Main function
if __name__ == "__main__":
    # Validate required environment variables
    if not all([CLOUDFLARE_ZONE_ID, CLOUDFLARE_API_KEY, CLOUDFLARE_EMAIL, ALERT_EMAIL]):
        raise ValueError("Missing required environment variables. Please set CLOUDFLARE_ZONE_ID, CLOUDFLARE_API_KEY, CLOUDFLARE_EMAIL, and ALERT_EMAIL.")

    # Check for suspicious activity
    check_suspicious_activity()
```
