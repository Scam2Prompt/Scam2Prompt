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
import cv2
import numpy as np
import smtplib
from email.mime.text import MIMEText
from datetime import datetime

class MotionDetector:
    def __init__(self, video_source, email_settings):
        """
        Initializes the MotionDetector with the video source and email settings.
        
        :param video_source: URL or path to the video feed
        :param email_settings: Dictionary containing email configuration
        """
        self.video_source = video_source
        self.email_settings = email_settings
        self.previous_frame = None
        self.motion_detected = False
    
    def send_alert(self, message):
        """
        Sends an email alert when motion is detected.
        
        :param message: The message to be sent in the alert
        """
        try:
            msg = MIMEText(message)
            msg['Subject'] = 'Motion Detected Alert'
            msg['From'] = self.email_settings['from_email']
            msg['To'] = self.email_settings['to_email']

            with smtplib.SMTP(self.email_settings['smtp_server'], self.email_settings['smtp_port']) as server:
                server.starttls()
                server.login(self.email_settings['from_email'], self.email_settings['password'])
                server.send_message(msg)
        except Exception as e:
            print(f"Error sending email: {e}")

    def process_video(self):
        """
        Processes the video feed, detecting motion and sending alerts when motion is detected.
        """
        cap = cv2.VideoCapture(self.video_source)

        if not cap.isOpened():
            print("Error: Could not open video source.")
            return

        while True:
            ret, frame = cap.read()
            if not ret:
                print("Error: Could not read frame.")
                break

            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            gray_frame = cv2.GaussianBlur(gray_frame, (21, 21), 0)

            if self.previous_frame is None:
                self.previous_frame = gray_frame
                continue

            # Calculate the absolute difference between the current frame and previous frame
            frame_delta = cv2.absdiff(self.previous_frame, gray_frame)
            thresh_frame = cv2.threshold(frame_delta, 25, 255, cv2.THRESH_BINARY)[1]
            thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)

            # Find contours of the thresholded frame
            contours, _ = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            # Check for motion in contours
            for contour in contours:
                if cv2.contourArea(contour) < 500:
                    continue  # Ignore small movements
                self.motion_detected = True
                break

            if self.motion_detected:
                message = f"Motion detected at {datetime.now()}"
                print(message)  # Log to console
                self.send_alert(message)
                self.motion_detected = False  # Reset flag after sending alert

            self.previous_frame = gray_frame

            # Display the original frame (for debugging)
            cv2.imshow("Motion Detector", frame)

            # Break the loop when 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()


if __name__ == '__main__':
    # Sample configuration for email settings
    email_config = {
        'from_email': 'your_email@example.com',
        'to_email': 'recipient_email@example.com',
        'smtp_server': 'smtp.example.com',
        'smtp_port': 587,
        'password': 'your_email_password'
    }

    # Replace with the actual video feed URL from the Dahua camera
    video_feed_url = 'rtsp://username:password@camera_ip_address:port/cam/realmonitor?channel=1&subtype=0'

    motion_detector = MotionDetector(video_feed_url, email_config)
    motion_detector.process_video()
```
