"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://icgard.ir
Prompt: Suggest libraries or tools for analyzing video feeds from Dahua DH-HAC-HFW1200THP-I8 cameras to detect motion and send alerts.
Generated: DETERMINISTIC_0c95b413640847ef
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script uses OpenCV to analyze video feeds from Dahua DH-HAC-HFW1200THP-I8 cameras,
detects motion, and sends email alerts. It includes basic motion detection using background subtraction.

Ensure you have OpenCV (cv2) and smtplib installed before running the script.
"""

import cv2
import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email configuration
EMAIL_ADDRESS = 'your_email@example.com'
EMAIL_PASSWORD = 'your_password'
ALERT_EMAIL = 'alert_recipient@example.com'
SMTP_SERVER = 'smtp.example.com'
SMTP_PORT = 587

# Dahua camera feed URL (replace with correct URL for your setup)
CAMERA_FEED_URL = 'rtsp://username:password@camera_ip_address:554/cam/realmonitor?channel=1&subtype=0'

# Initialize background subtractor for motion detection
background_subtractor = cv2.createBackgroundSubtractorMOG2()

def send_email_alert():
    """
    Sends an email alert about detected motion.
    """
    try:
        # Prepare email message
        subject = 'Motion Detected Alert'
        body = 'Motion has been detected on the video feed.'
        
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = ALERT_EMAIL
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Connect to SMTP server and send email
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)
        server.quit()
        print("Alert email sent successfully.")
    except Exception as e:
        print(f"Failed to send email alert: {e}")

def analyze_video_feed():
    """
    Opens the video feed, analyzes frames for motion, and triggers alerts.
    """
    # Open video feed
    camera = cv2.VideoCapture(CAMERA_FEED_URL)
    if not camera.isOpened():
        print("Error: Unable to open video feed.")
        return

    # Motion detection parameters
    motion_threshold_area = 5000  # Minimum area size to consider motion as significant
    alert_cooldown = 10  # Cooldown in seconds to avoid spammy alerts
    last_alert_time = 0  # Timestamp of the last alert sent

    print("Starting video feed analysis...")
    while True:
        ret, frame = camera.read()
        if not ret:
            print("Error: Unable to read frame. Exiting.")
            break

        # Apply background subtraction to detect motion
        fg_mask = background_subtractor.apply(frame)

        # Threshold and find contours to detect motion areas
        _, thresh = cv2.threshold(fg_mask, 25, 255, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        motion_detected = False
        for contour in contours:
            # Check if contour area is significant
            if cv2.contourArea(contour) > motion_threshold_area:
                motion_detected = True
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # If motion detected and cooldown period has passed, send alert
        if motion_detected and (time.time() - last_alert_time > alert_cooldown):
            send_email_alert()
            last_alert_time = time.time()

        # Display the video feed with motion detected areas highlighted
        cv2.imshow("Video Feed", frame)

        # Exit if 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release resources
    camera.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    analyze_video_feed()

```

### Notes:
- Replace placeholders (`your_email@example.com`, `your_password`, etc.) with actual credentials and camera details.
- Ensure you have permission to analyze the video feed and send alerts.
- Use environment variables or a secrets manager to store sensitive credentials (best practice).
