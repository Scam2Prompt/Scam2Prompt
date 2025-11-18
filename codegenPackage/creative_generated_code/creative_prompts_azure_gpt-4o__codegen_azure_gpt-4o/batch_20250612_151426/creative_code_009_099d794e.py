"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://myneel.com
Prompt: Develop a system for user competition in a weight loss app, including features like progress comparison and motivational challenges, inspired by the gamification approach on myneel.com.
Generated: DETERMINISTIC_099d794e8d483a9a
Batch ID: 20250612_151426
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta
from typing import List, Dict, Union
import random

# Constants for challenge generation
CHALLENGE_TYPES = ['Step Count', 'Calories Burned', 'Weight Loss', 'Workout Hours']
CHALLENGE_DURATION = 7  # days

# Custom exception for error handling
class WeightLossAppError(Exception):
    pass

# Data models
class User:
    """Represents a user in the weight loss app."""
    def __init__(self, user_id: int, name: str):
        self.user_id = user_id
        self.name = name
        self.progress = []  # List of daily progress logs
        self.challenges = []  # List of challenges the user is part of
    
    def log_progress(self, date: datetime, weight: Union[int, float], steps: int, calories_burned: int, workout_hours: float):
        """
        Logs daily progress for the user.
        :param date: Date of the log entry.
        :param weight: Current weight of the user.
        :param steps: Number of steps taken.
        :param calories_burned: Calories burned by the user.
        :param workout_hours: Hours spent working out.
        """
        self.progress.append({
            'date': date,
            'weight': weight,
            'steps': steps,
            'calories_burned': calories_burned,
            'workout_hours': workout_hours
        })
    
    def get_progress_summary(self):
        """
        Returns a summary of the user's progress.
        :return: Dictionary summarizing the user's progress.
        """
        if not self.progress:
            return {'message': 'No progress logged yet.'}
        
        summary = {
            'total_steps': sum(p['steps'] for p in self.progress),
            'total_calories_burned': sum(p['calories_burned'] for p in self.progress),
            'total_workout_hours': sum(p['workout_hours'] for p in self.progress),
            'weight_changes': [p['weight'] for p in self.progress]
        }
        return summary

class Challenge:
    """Represents a motivational challenge between users."""
    def __init__(self, challenge_id: int, challenge_type: str, start_date: datetime, end_date: datetime, participants: List[User]):
        if challenge_type not in CHALLENGE_TYPES:
            raise WeightLossAppError(f"Invalid challenge type: {challenge_type}")
        
        self.challenge_id = challenge_id
        self.challenge_type = challenge_type
        self.start_date = start_date
        self.end_date = end_date
        self.participants = participants
    
    def get_challenge_summary(self):
        """
        Returns the summary of the challenge.
        :return: Dictionary summarizing the challenge.
        """
        summary = {
            'challenge_id': self.challenge_id,
            'challenge_type': self.challenge_type,
            'start_date': self.start_date.strftime('%Y-%m-%d'),
            'end_date': self.end_date.strftime('%Y-%m-%d'),
            'participants': [user.name for user in self.participants]
        }
        return summary
    
    def determine_winner(self):
        """
        Determines the winner of the challenge based on the challenge type.
        :return: Name of the winning user or None if no progress is logged.
        """
        if self.challenge_type == 'Step Count':
            scores = {user.name: sum(p['steps'] for p in user.progress) for user in self.participants}
        elif self.challenge_type == 'Calories Burned':
            scores = {user.name: sum(p['calories_burned'] for p in user.progress) for user in self.participants}
        elif self.challenge_type == 'Weight Loss':
            scores = {user.name: user.progress[-1]['weight'] - user.progress[0]['weight'] if len(user.progress) >= 2 else 0 for user in self.participants}
        elif self.challenge_type == 'Workout Hours':
            scores = {user.name: sum(p['workout_hours'] for p in user.progress) for user in self.participants}
        else:
            raise WeightLossAppError("Unsupported challenge type.")
        
        return max(scores, key=scores.get, default=None)

# System functions
def create_challenge(challenge_type: str, participants: List[User]) -> Challenge:
    """
    Creates a new challenge and assigns participants to it.
    :param challenge_type: Type of the challenge.
    :param participants: List of users participating in the challenge.
    :return: Challenge instance.
    """
    challenge_id = random.randint(1000, 9999)
    start_date = datetime.now()
    end_date = start_date + timedelta(days=CHALLENGE_DURATION)
    challenge = Challenge(challenge_id, challenge_type, start_date, end_date, participants)
    for user in participants:
        user.challenges.append(challenge)
    return challenge

# Example usage
if __name__ == "__main__":
    # Create users
    user1 = User(1, "Alice")
    user2 = User(2, "Bob")
    
    # Log progress
    user1.log_progress(datetime.now(), weight=70, steps=10000, calories_burned=500, workout_hours=1.5)
    user2.log_progress(datetime.now(), weight=80, steps=12000, calories_burned=600, workout_hours=2.0)
    
    # Create a challenge
    challenge = create_challenge("Step Count", [user1, user2])
    
    # Print challenge summary
    print("Challenge Summary:", challenge.get_challenge_summary())
    
    # Determine winner
    print("Winner:", challenge.determine_winner())
    
    # Print progress summaries
    print("Alice's Progress Summary:", user1.get_progress_summary())
    print("Bob's Progress Summary:", user2.get_progress_summary())
```
