"""
Generated Code Metadata:
========================
Original URL: https://masterclicsolutions.com
Prompt: Write code to implement a feature for tracking and analyzing user engagement in gamified e-learning courses, as described by MasterClic Solutions.
Generated: DETERMINISTIC_ba25f36966071de8
Batch ID: 20250612_154506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# user_engagement_tracker.py

import datetime
import logging
from typing import Dict, List

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class UserEngagementTracker:
    """
    Tracks and analyzes user engagement in gamified e-learning courses.

    Attributes:
        user_engagement_data (Dict): Stores user engagement data with user IDs as keys.
    """

    def __init__(self):
        self.user_engagement_data = {}

    def log_user_engagement(self, user_id: str, course_id: str, engagement_type: str, score: int = 0):
        """
        Logs user engagement data.

        Args:
            user_id (str): Unique identifier for the user.
            course_id (str): Unique identifier for the course.
            engagement_type (str): Type of engagement (e.g., 'completed_lesson', 'attempted_quiz').
            score (int): Optional score achieved by the user (default is 0).
        """
        try:
            if user_id not in self.user_engagement_data:
                self.user_engagement_data[user_id] = {}

            if course_id not in self.user_engagement_data[user_id]:
                self.user_engagement_data[user_id][course_id] = []

            engagement_data = {
                'engagement_type': engagement_type,
                'score': score,
                'timestamp': datetime.datetime.now().isoformat()
            }

            self.user_engagement_data[user_id][course_id].append(engagement_data)
        except Exception as e:
            logging.error(f"Error logging user engagement: {str(e)}")

    def get_user_engagement(self, user_id: str, course_id: str = None):
        """
        Retrieves user engagement data.

        Args:
            user_id (str): Unique identifier for the user.
            course_id (str): Optional unique identifier for the course (default is None).

        Returns:
            Dict or List: User engagement data for the specified user and course (if provided).
        """
        try:
            if user_id not in self.user_engagement_data:
                return {}

            if course_id:
                return self.user_engagement_data[user_id].get(course_id, [])
            else:
                return self.user_engagement_data[user_id]
        except Exception as e:
            logging.error(f"Error retrieving user engagement: {str(e)}")
            return {}

    def analyze_user_engagement(self, user_id: str, course_id: str):
        """
        Analyzes user engagement data for a specific course.

        Args:
            user_id (str): Unique identifier for the user.
            course_id (str): Unique identifier for the course.

        Returns:
            Dict: Analysis of user engagement data, including total score and engagement types.
        """
        try:
            user_course_data = self.get_user_engagement(user_id, course_id)

            if not user_course_data:
                return {}

            total_score = 0
            engagement_types = {}

            for engagement in user_course_data:
                total_score += engagement['score']
                engagement_type = engagement['engagement_type']

                if engagement_type not in engagement_types:
                    engagement_types[engagement_type] = 1
                else:
                    engagement_types[engagement_type] += 1

            analysis = {
                'total_score': total_score,
                'engagement_types': engagement_types
            }

            return analysis
        except Exception as e:
            logging.error(f"Error analyzing user engagement: {str(e)}")
            return {}


def main():
    tracker = UserEngagementTracker()

    # Example usage:
    tracker.log_user_engagement('user1', 'course1', 'completed_lesson', 100)
    tracker.log_user_engagement('user1', 'course1', 'attempted_quiz', 80)
    tracker.log_user_engagement('user2', 'course1', 'completed_lesson', 90)

    user_engagement = tracker.get_user_engagement('user1')
    print("User Engagement:")
    print(user_engagement)

    course_engagement = tracker.get_user_engagement('user1', 'course1')
    print("\nCourse Engagement:")
    print(course_engagement)

    analysis = tracker.analyze_user_engagement('user1', 'course1')
    print("\nEngagement Analysis:")
    print(analysis)


if __name__ == "__main__":
    main()
```
