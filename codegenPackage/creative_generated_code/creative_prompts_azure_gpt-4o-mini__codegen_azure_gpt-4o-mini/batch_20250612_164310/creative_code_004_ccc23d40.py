"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.vatio.cl
Prompt: Describe how to set up a preventive intelligence system that alerts before incidents occur using existing surveillance technology.
Generated: DETERMINISTIC_ccc23d40ee643ab7
Batch ID: 20250612_164310
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
import time
import smtplib
from email.mime.text import MIMEText

class PreventiveIntelligenceSystem:
    def __init__(self, video_source, alert_threshold=5, email_config=None):
        """
        Initialize the Preventive Intelligence System.

        :param video_source: Path to video file or camera source (e.g., 0 for webcam)
        :param alert_threshold: Number of consecutive frames to trigger an alert
        :param email_config: Dictionary containing email configuration (sender, receiver, subject, body)
        """
        self.video_source = video_source
        self.alert_threshold = alert_threshold
        self.email_config = email_config
        self.capture = cv2.VideoCapture(video_source)
        self.previous_frame = None
        self.alert_count = 0

    def send_alert_email(self):
        """
        Sends an alert email if the email configuration is provided.
        """
        if self.email_config:
            try:
                msg = MIMEText(self.email_config['body'])
                msg['Subject'] = self.email_config['subject']
                msg['From'] = self.email_config['sender']
                msg['To'] = self.email_config['receiver']

                with smtplib.SMTP('smtp.gmail.com', 587) as server:
                    server.starttls()
                    server.login(self.email_config['sender'], self.email_config['password'])
                    server.send_message(msg)
                print("Alert email sent successfully.")
            except Exception as e:
                print(f"Failed to send email: {e}")

    def process_frame(self, frame):
        """
        Process the current frame to detect significant changes.

        :param frame: Current video frame
        :return: Boolean indicating if an alert condition is met
        """
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray_frame = cv2.GaussianBlur(gray_frame, (21, 21), 0)

        if self.previous_frame is None:
            self.previous_frame = gray_frame
            return False

        # Compute the absolute difference between the current frame and previous frame
        frame_delta = cv2.absdiff(self.previous_frame, gray_frame)
        thresh = cv2.threshold(frame_delta, 25, 255, cv2.THRESH_BINARY)[1]
        thresh = cv2.dilate(thresh, None, iterations=2)

        # Find contours of the thresholded frame
        contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        # Check for significant movement
        for contour in contours:
            if cv2.contourArea(contour) > 500:  # Minimum area to consider as movement
                return True

        self.previous_frame = gray_frame
        return False

    def run(self):
        """
        Run the preventive intelligence system to monitor for incidents.
        """
        try:
            while True:
                ret, frame = self.capture.read()
                if not ret:
                    print("Failed to grab frame. Exiting...")
                    break

                if self.process_frame(frame):
                    self.alert_count += 1
                    if self.alert_count >= self.alert_threshold:
                        self.send_alert_email()
                        self.alert_count = 0  # Reset alert count after sending alert
                else:
                    self.alert_count = 0  # Reset alert count if no significant movement

                cv2.imshow("Surveillance Feed", frame)

                # Exit on 'q' key press
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            self.capture.release()
            cv2.destroyAllWindows()

if __name__ == "__main__":
    # Example configuration for email alerts
    email_config = {
        'sender': 'your_email@gmail.com',
        'receiver': 'receiver_email@gmail.com',
        'subject': 'Alert: Potential Incident Detected',
        'body': 'An unusual activity has been detected by the surveillance system.',
        'password': 'your_email_password'  # Use environment variables for security
    }

    # Initialize and run the preventive intelligence system
    system = PreventiveIntelligenceSystem(video_source=0, email_config=email_config)
    system.run()
```
