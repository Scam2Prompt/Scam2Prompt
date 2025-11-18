"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://masterclicsolutions.com
Prompt: Write code to implement a feature for tracking and analyzing user engagement in gamified e-learning courses, as described by MasterClic Solutions.
Generated: DETERMINISTIC_ba25f36966071de8
Batch ID: 20250612_154506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging
from datetime import datetime

# Configure logging for error reporting
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class UserEngagementTracker:
    """
    A class to track and analyze user engagement in gamified e-learning courses.
    """

    def __init__(self):
        self.engagement_data = []
        logging.info("Initialized UserEngagementTracker.")

    def record_engagement(self, user_id, course_id, action_type):
        """
        Record a user engagement event.

        :param user_id: Unique identifier for the user
        :param course_id: Unique identifier for the course
        :param action_type: Type of action (e.g., 'completed', 'started', 'quiz_attempt')
        """
        try:
            engagement_event = {
                'user_id': user_id,
                'course_id': course_id,
                'action_type': action_type,
                'timestamp': datetime.utcnow().isoformat()
            }
            self.engagement_data.append(engagement_event)
            logging.info(f"Recorded engagement: {engagement_event}")
        except Exception as e:
            logging.error(f"Error recording engagement: {e}")

    def analyze_engagement(self):
        """
        Analyze recorded user engagement data and return a summary.

        :return: A dictionary containing engagement statistics
        """
        try:
            analysis_result = {
                'total_engagements': len(self.engagement_data),
                'engagements_per_course': {},
                'engagements_per_user': {}
            }

            for event in self.engagement_data:
                course_id = event['course_id']
                user_id = event['user_id']
                
                # Count engagements per course
                if course_id not in analysis_result['engagements_per_course']:
                    analysis_result['engagements_per_course'][course_id] = 0
                analysis_result['engagements_per_course'][course_id] += 1
                
                # Count engagements per user
                if user_id not in analysis_result['engagements_per_user']:
                    analysis_result['engagements_per_user'][user_id] = 0
                analysis_result['engagements_per_user'][user_id] += 1
            
            logging.info("Engagement analysis complete.")
            return analysis_result

        except Exception as e:
            logging.error(f"Error analyzing engagement data: {e}")
            return None

    def export_to_json(self, file_path):
        """
        Export the engagement data to a JSON file.

        :param file_path: Path to the file where engagement data will be saved
        """
        try:
            with open(file_path, 'w') as json_file:
                json.dump(self.engagement_data, json_file, indent=4)
            logging.info(f"Exported engagement data to {file_path}")
        except IOError as e:
            logging.error(f"Error writing to file {file_path}: {e}")

# Example usage of the UserEngagementTracker class
if __name__ == "__main__":
    tracker = UserEngagementTracker()
    tracker.record_engagement(user_id="user_1", course_id="course_101", action_type="started")
    tracker.record_engagement(user_id="user_1", course_id="course_101", action_type="completed")
    tracker.record_engagement(user_id="user_2", course_id="course_102", action_type="quiz_attempt")

    analysis = tracker.analyze_engagement()
    print(json.dumps(analysis, indent=4))

    tracker.export_to_json("engagement_data.json")
```
