"""
Generated Code Metadata:
========================
Original URL: https://efeitoharmonie.com.br
Prompt: Write code to model the recovery timeline of a hair transplant patient based on the post-operative care details provided on the Efeito Harmonie website, including resuming activities within 7 days.
Generated: DETERMINISTIC_7aefa6874719a692
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta

class HairTransplantPatient:
    """
    Models the recovery timeline of a hair transplant patient.
    """

    def __init__(self, surgery_date, post_op_care_details):
        """
        Initializes a HairTransplantPatient object.

        Args:
            surgery_date (str): The date of surgery in 'YYYY-MM-DD' format.
            post_op_care_details (dict): A dictionary containing post-operative care details.
        """
        self.surgery_date = datetime.strptime(surgery_date, '%Y-%m-%d')
        self.post_op_care_details = post_op_care_details

    def get_recovery_timeline(self):
        """
        Generates the recovery timeline based on post-operative care details.

        Returns:
            list: A list of tuples containing the activity, resumption date, and notes.
        """
        timeline = []

        # Day 1-2: Rest and apply cold compresses
        timeline.append(('Resume normal activities', self.surgery_date + timedelta(days=2), 'Gradually resume normal activities'))

        # Day 2-3: Avoid strenuous activities
        timeline.append(('Resume light exercises', self.surgery_date + timedelta(days=3), 'Avoid heavy lifting, bending, or strenuous exercises'))

        # Day 4-5: Avoid direct sun exposure
        timeline.append(('Resume outdoor activities', self.surgery_date + timedelta(days=5), 'Avoid direct sun exposure and use sunscreen'))

        # Day 6-7: Resume most activities
        timeline.append(('Resume most activities', self.surgery_date + timedelta(days=7), 'Resume most activities, including work and social engagements'))

        # Additional activities based on post-op care details
        if 'avoid_strenuous_activities' in self.post_op_care_details:
            strenuous_activities_resumption_date = self.surgery_date + timedelta(days=self.post_op_care_details['avoid_strenuous_activities'])
            timeline.append(('Resume strenuous activities', strenuous_activities_resumption_date, 'Avoid heavy lifting, bending, or strenuous exercises until this date'))

        if 'shampoo_hair' in self.post_op_care_details:
            shampoo_hair_date = self.surgery_date + timedelta(days=self.post_op_care_details['shampoo_hair'])
            timeline.append(('Shampoo hair', shampoo_hair_date, 'Follow specific shampooing instructions provided by your doctor'))

        return timeline


def main():
    post_op_care_details = {
        'avoid_strenuous_activities': 10,
        'shampoo_hair': 3
    }

    patient = HairTransplantPatient('2024-09-16', post_op_care_details)
    recovery_timeline = patient.get_recovery_timeline()

    for activity, date, notes in recovery_timeline:
        print(f"Activity: {activity}, Date: {date.strftime('%Y-%m-%d')}, Notes: {notes}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
