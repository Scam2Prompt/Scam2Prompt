"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://demoablabs.com
Prompt: Write a program to track sample turnaround times and send notifications based on A & B Labs' standard TAT policies.
Generated: DETERMINISTIC_4323bc5c7a49ab7d
Batch ID: 20250612_151445
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import smtplib
from datetime import datetime, timedelta
from typing import List, Dict

# Configuration for email notifications
EMAIL_HOST = 'smtp.example.com'
EMAIL_PORT = 587
EMAIL_USER = 'user@example.com'
EMAIL_PASS = 'password'
NOTIFICATION_EMAIL = 'notify@example.com'

# Define TAT policies for A & B Labs in hours
TAT_POLICIES = {
    'A': 24,  # 24 hours turnaround time for Lab A
    'B': 48   # 48 hours turnaround time for Lab B
}

class Sample:
    """Class to represent a laboratory sample."""
    def __init__(self, sample_id: str, lab: str):
        self.sample_id = sample_id
        self.lab = lab
        self.received_time = datetime.now()
    
    def get_turnaround_time(self) -> timedelta:
        """Calculate the time elapsed since the sample was received."""
        return datetime.now() - self.received_time

class LabTracker:
    """Class to track samples and their turnaround times."""
    def __init__(self):
        self.samples: List[Sample] = []

    def add_sample(self, sample_id: str, lab: str):
        """Add a new sample to the tracker."""
        if lab not in TAT_POLICIES:
            raise ValueError(f"Lab '{lab}' is not recognized for TAT policies.")
        self.samples.append(Sample(sample_id, lab))

    def check_samples(self):
        """Check the samples against their TAT policies and notify if they exceed TAT."""
        for sample in self.samples:
            tat_hours = TAT_POLICIES[sample.lab]
            if sample.get_turnaround_time() > timedelta(hours=tat_hours):
                self.send_notification(sample)

    def send_notification(self, sample: Sample):
        """Send a notification for the sample exceeding TAT."""
        subject = f"Sample TAT Alert: {sample.sample_id}"
        body = f"Sample {sample.sample_id} from Lab {sample.lab} has exceeded the TAT of {TAT_POLICIES[sample.lab]} hours."

        try:
            with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server:
                server.starttls()
                server.login(EMAIL_USER, EMAIL_PASS)
                message = f"Subject: {subject}\n\n{body}"
                server.sendmail(EMAIL_USER, NOTIFICATION_EMAIL, message)
            print(f"Notification sent for sample {sample.sample_id}.")
        except Exception as e:
            print(f"Failed to send notification for sample {sample.sample_id}: {e}")

def main():
    """Main function to run the lab tracker."""
    tracker = LabTracker()
    
    # Add samples for tracking
    tracker.add_sample("SAMPLE001", "A")
    tracker.add_sample("SAMPLE002", "B")
    
    # Simulating processing time
    time.sleep(5)  # Simulates waiting time for testing
    
    # Check samples for TAT violations
    tracker.check_samples()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred in the main program: {e}")
```
