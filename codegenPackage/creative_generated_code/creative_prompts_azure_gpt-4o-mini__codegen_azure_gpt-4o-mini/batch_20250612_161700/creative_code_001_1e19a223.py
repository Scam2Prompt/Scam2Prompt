"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://beta.metis-lab.com
Prompt: Write a code snippet that simulates a participatory approach for museum events, inspired by the methodologies outlined in Mêtis's resources.
Generated: DETERMINISTIC_1e19a2238bebe2e0
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from typing import List, Dict, Any

class MuseumEvent:
    def __init__(self, title: str, description: str, participants: List[str]):
        """
        Initialize a museum event with its title, description, and participants.
        
        :param title: The title of the event.
        :param description: A brief description of the event.
        :param participants: A list of participants involved in the event.
        """
        self.title = title
        self.description = description
        self.participants = participants
        self.feedbacks = []

    def collect_feedback(self, participant: str, feedback: str) -> None:
        """
        Collect feedback from a participant. Ensures that the participant is part of the event.
        
        :param participant: The name of the participant providing feedback.
        :param feedback: The feedback provided by the participant.
        :raises ValueError: If the participant is not registered for the event.
        """
        if participant not in self.participants:
            raise ValueError(f"{participant} is not a participant in this event.")
        self.feedbacks.append({'participant': participant, 'feedback': feedback})

    def summarize_feedback(self) -> Dict[str, Any]:
        """
        Summarizes the feedback collected from participants and provides an overall sentiment analysis.
        
        :return: A summary of feedback comments and a basic sentiment analysis.
        """
        feedback_count = len(self.feedbacks)
        positive_count = sum(1 for f in self.feedbacks if "good" in f['feedback'].lower() or "great" in f['feedback'].lower())
        sentiment = "Positive" if positive_count > feedback_count / 2 else "Neutral/Negative" if feedback_count > 0 else "No Feedback"
        
        return {
            'total_feedback': feedback_count,
            'positive_feedback': positive_count,
            'sentiment': sentiment,
            'detailed_feedback': self.feedbacks
        }

def simulate_event():
    """
    Simulates the creation of a museum event and collects feedback from participants.
    """
    event_title = "Cultural Heritage Exhibition"
    event_description = "An interactive exhibition showcasing local cultural heritage."
    participants = ["Alice", "Bob", "Charlie"]

    # Create a museum event
    event = MuseumEvent(event_title, event_description, participants)

    # Simulate feedback collection
    feedback_samples = [
        "It was a great experience!",
        "I found it to be very informative.",
        "The event was okay, not the best.",
        "Good organization and lovely exhibits.",
        "I did not enjoy the event."
    ]

    for participant in participants:
        feedback = random.choice(feedback_samples)
        try:
            event.collect_feedback(participant, feedback)
        except ValueError as e:
            print(e)

    # Summarize the feedback
    summary = event.summarize_feedback()
    print("Feedback Summary:", summary)

if __name__ == "__main__":
    simulate_event()
```
