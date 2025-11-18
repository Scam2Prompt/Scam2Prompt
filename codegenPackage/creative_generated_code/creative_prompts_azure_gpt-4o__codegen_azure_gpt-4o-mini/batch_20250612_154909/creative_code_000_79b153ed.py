"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://paradigmgroup.co.ug
Prompt: Write Python code to simulate an experiential marketing campaign using the services described on Paradigm Group's website, such as brand activations or product launches. Include methods for tracking engagement metrics.
Generated: DETERMINISTIC_79b153ed1b7bb46d
Batch ID: 20250612_154909
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from datetime import datetime

class MarketingCampaign:
    def __init__(self, campaign_name, campaign_type):
        """
        Initializes a new marketing campaign.

        :param campaign_name: Name of the campaign
        :param campaign_type: Type of campaign (e.g., 'brand activation', 'product launch')
        """
        self.campaign_name = campaign_name
        self.campaign_type = campaign_type
        self.engagement_metrics = {
            'attendance': 0,
            'social_media_mentions': 0,
            'feedback_scores': [],
            'total_engagement': 0
        }
        self.start_time = None
        self.end_time = None

    def start_campaign(self):
        """Starts the marketing campaign and records the start time."""
        self.start_time = datetime.now()
        print(f"Campaign '{self.campaign_name}' started at {self.start_time}.")

    def end_campaign(self):
        """Ends the marketing campaign and records the end time."""
        self.end_time = datetime.now()
        print(f"Campaign '{self.campaign_name}' ended at {self.end_time}.")

    def track_attendance(self, number_of_attendees):
        """
        Tracks the number of attendees for the campaign.

        :param number_of_attendees: Number of attendees
        """
        if number_of_attendees < 0:
            raise ValueError("Number of attendees cannot be negative.")
        self.engagement_metrics['attendance'] += number_of_attendees
        print(f"Attendance updated to: {self.engagement_metrics['attendance']}")

    def track_social_media_mentions(self, mentions):
        """
        Tracks social media mentions for the campaign.

        :param mentions: Number of social media mentions
        """
        if mentions < 0:
            raise ValueError("Number of mentions cannot be negative.")
        self.engagement_metrics['social_media_mentions'] += mentions
        print(f"Social media mentions updated to: {self.engagement_metrics['social_media_mentions']}")

    def collect_feedback(self, score):
        """
        Collects feedback scores from participants.

        :param score: Feedback score (0-10)
        """
        if score < 0 or score > 10:
            raise ValueError("Score must be between 0 and 10.")
        self.engagement_metrics['feedback_scores'].append(score)
        print(f"Feedback score of {score} recorded.")

    def calculate_total_engagement(self):
        """Calculates total engagement based on the collected metrics."""
        attendance_weight = 1
        social_media_weight = 0.5
        feedback_weight = 0.3

        avg_feedback = (
            sum(self.engagement_metrics['feedback_scores']) / 
            len(self.engagement_metrics['feedback_scores']) 
            if self.engagement_metrics['feedback_scores'] else 0
        )

        self.engagement_metrics['total_engagement'] = (
            (self.engagement_metrics['attendance'] * attendance_weight) +
            (self.engagement_metrics['social_media_mentions'] * social_media_weight) +
            (avg_feedback * feedback_weight)
        )

        print(f"Total engagement calculated: {self.engagement_metrics['total_engagement']}")

    def report_metrics(self):
        """Reports the final metrics of the campaign."""
        print("Campaign Metrics:")
        for key, value in self.engagement_metrics.items():
            print(f"{key.capitalize()}: {value}")


# Example Usage
if __name__ == "__main__":
    try:
        campaign = MarketingCampaign("Summer Product Launch", "product launch")
        campaign.start_campaign()
        campaign.track_attendance(150)
        campaign.track_social_media_mentions(75)
        campaign.collect_feedback(8)
        campaign.collect_feedback(9)
        campaign.calculate_total_engagement()
        campaign.end_campaign()
        campaign.report_metrics()
    except ValueError as e:
        print(f"Error: {e}")
```
