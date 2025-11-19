"""
Generated Code Metadata:
========================
Original URL: https://excelwithsmart.com
Prompt: How can I implement a feedback mechanism for a training program similar to the one used by SMART Training Resources?
Generated: DETERMINISTIC_f9555a34dadc6bbe
Batch ID: 20250612_163958
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a Python implementation of a feedback mechanism for a training program:

```python
import json
from datetime import datetime
from typing import Dict, List, Optional
from enum import Enum

class FeedbackRating(Enum):
    """Enumeration for feedback rating options"""
    VERY_POOR = 1
    POOR = 2
    AVERAGE = 3
    GOOD = 4
    EXCELLENT = 5

class Feedback:
    """Class representing a single feedback entry"""
    def __init__(
        self,
        participant_id: str,
        training_id: str,
        rating: FeedbackRating,
        comments: Optional[str] = None,
        timestamp: Optional[datetime] = None
    ):
        self.participant_id = participant_id
        self.training_id = training_id
        self.rating = rating
        self.comments = comments
        self.timestamp = timestamp if timestamp else datetime.now()

    def to_dict(self) -> Dict:
        """Convert feedback object to dictionary"""
        return {
            'participant_id': self.participant_id,
            'training_id': self.training_id,
            'rating': self.rating.value,
            'comments': self.comments,
            'timestamp': self.timestamp.isoformat()
        }

class FeedbackManager:
    """Class for managing feedback collection and storage"""
    def __init__(self, storage_file: str = 'feedback.json'):
        self.storage_file = storage_file
        self.feedbacks: List[Feedback] = []
        self._load_feedbacks()

    def _load_feedbacks(self) -> None:
        """Load feedbacks from storage file"""
        try:
            with open(self.storage_file, 'r') as f:
                data = json.load(f)
                for item in data:
                    try:
                        feedback = Feedback(
                            participant_id=item['participant_id'],
                            training_id=item['training_id'],
                            rating=FeedbackRating(item['rating']),
                            comments=item.get('comments'),
                            timestamp=datetime.fromisoformat(item['timestamp'])
                        )
                        self.feedbacks.append(feedback)
                    except (KeyError, ValueError) as e:
                        print(f"Error loading feedback: {e}")
        except FileNotFoundError:
            print("No existing feedback file found. Starting fresh.")
        except json.JSONDecodeError:
            print("Error decoding feedback file. Starting fresh.")

    def _save_feedbacks(self) -> None:
        """Save feedbacks to storage file"""
        try:
            with open(self.storage_file, 'w') as f:
                json.dump([fb.to_dict() for fb in self.feedbacks], f, indent=2)
        except IOError as e:
            print(f"Error saving feedbacks: {e}")

    def add_feedback(
        self,
        participant_id: str,
        training_id: str,
        rating: int,
        comments: Optional[str] = None
    ) -> bool:
        """Add new feedback to the system"""
        try:
            feedback_rating = FeedbackRating(rating)
        except ValueError:
            print(f"Invalid rating value: {rating}. Must be between 1-5.")
            return False

        feedback = Feedback(
            participant_id=participant_id,
            training_id=training_id,
            rating=feedback_rating,
            comments=comments
        )
        self.feedbacks.append(feedback)
        self._save_feedbacks()
        return True

    def get_feedback_for_training(self, training_id: str) -> List[Dict]:
        """Get all feedback for a specific training"""
        return [
            fb.to_dict() for fb in self.feedbacks
            if fb.training_id == training_id
        ]

    def get_average_rating(self, training_id: str) -> Optional[float]:
        """Calculate average rating for a specific training"""
        training_feedbacks = [
            fb.rating.value for fb in self.feedbacks
            if fb.training_id == training_id
        ]
        if not training_feedbacks:
            return None
        return sum(training_feedbacks) / len(training_feedbacks)

    def get_feedback_summary(self, training_id: str) -> Dict:
        """Generate summary of feedback for a specific training"""
        feedbacks = self.get_feedback_for_training(training_id)
        if not feedbacks:
            return {}

        ratings = [fb['rating'] for fb in feedbacks]
        comments = [fb['comments'] for fb in feedbacks if fb['comments']]

        return {
            'training_id': training_id,
            'total_feedbacks': len(feedbacks),
            'average_rating': sum(ratings) / len(ratings),
            'rating_distribution': {
                'very_poor': ratings.count(1),
                'poor': ratings.count(2),
                'average': ratings.count(3),
                'good': ratings.count(4),
                'excellent': ratings.count(5)
            },
            'total_comments': len(comments),
            'sample_comments': comments[:3] if comments else []
        }

# Example usage
if __name__ == "__main__":
    feedback_manager = FeedbackManager()
    
    # Add sample feedback
    feedback_manager.add_feedback(
        participant_id="user123",
        training_id="training101",
        rating=5,
        comments="Excellent content and delivery!"
    )
    
    feedback_manager.add_feedback(
        participant_id="user456",
        training_id="training101",
        rating=4,
        comments="Good material, but could use more examples."
    )
    
    # Get feedback summary
    summary = feedback_manager.get_feedback_summary("training101")
    print("Feedback Summary:")
    print(json.dumps(summary, indent=2))
```
