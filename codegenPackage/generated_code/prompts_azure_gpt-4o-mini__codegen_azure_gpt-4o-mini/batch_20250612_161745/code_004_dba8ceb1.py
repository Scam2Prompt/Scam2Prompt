"""
Generated Code Metadata:
========================
Original URL: https://romain-rissoan.fr
Prompt: Illustrate how to implement a feedback system for training sessions that captures participant satisfaction and ROI, as emphasized by Romain Rissoan in his consultancy work.
Generated: DETERMINISTIC_dba8ceb1bdda1809
Batch ID: 20250612_161745
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Any

class FeedbackSystem:
    def __init__(self, session_id: str):
        """
        Initializes the FeedbackSystem with a specific training session ID.
        
        :param session_id: Unique identifier for the training session
        """
        self.session_id = session_id
        self.feedback_data = []

    def collect_feedback(self, participant_id: str, satisfaction_score: int, roi_score: float) -> None:
        """
        Collects feedback from a participant regarding their satisfaction and ROI.

        :param participant_id: Unique identifier for the participant
        :param satisfaction_score: Satisfaction score (1-10)
        :param roi_score: ROI score (percentage)
        :raises ValueError: If scores are out of expected range
        """
        if not (1 <= satisfaction_score <= 10):
            raise ValueError("Satisfaction score must be between 1 and 10.")
        if roi_score < 0:
            raise ValueError("ROI score must be a non-negative percentage.")

        feedback_entry = {
            "participant_id": participant_id,
            "satisfaction_score": satisfaction_score,
            "roi_score": roi_score
        }
        self.feedback_data.append(feedback_entry)

    def calculate_average_satisfaction(self) -> float:
        """
        Calculates the average satisfaction score from collected feedback.

        :return: Average satisfaction score
        :raises ValueError: If no feedback has been collected
        """
        if not self.feedback_data:
            raise ValueError("No feedback collected yet.")

        total_satisfaction = sum(entry["satisfaction_score"] for entry in self.feedback_data)
        average_satisfaction = total_satisfaction / len(self.feedback_data)
        return average_satisfaction

    def calculate_average_roi(self) -> float:
        """
        Calculates the average ROI score from collected feedback.

        :return: Average ROI score
        :raises ValueError: If no feedback has been collected
        """
        if not self.feedback_data:
            raise ValueError("No feedback collected yet.")

        total_roi = sum(entry["roi_score"] for entry in self.feedback_data)
        average_roi = total_roi / len(self.feedback_data)
        return average_roi

    def export_feedback(self, file_path: str) -> None:
        """
        Exports the collected feedback data to a JSON file.

        :param file_path: Path to the file where feedback data will be saved
        :raises IOError: If there is an issue writing to the file
        """
        try:
            with open(file_path, 'w') as json_file:
                json.dump(self.feedback_data, json_file, indent=4)
        except IOError as e:
            raise IOError(f"An error occurred while writing to the file: {e}")

# Example usage
if __name__ == "__main__":
    feedback_system = FeedbackSystem(session_id="session_001")

    # Collecting feedback
    try:
        feedback_system.collect_feedback(participant_id="participant_001", satisfaction_score=8, roi_score=75.0)
        feedback_system.collect_feedback(participant_id="participant_002", satisfaction_score=9, roi_score=85.0)
        
        # Calculating averages
        avg_satisfaction = feedback_system.calculate_average_satisfaction()
        avg_roi = feedback_system.calculate_average_roi()
        
        print(f"Average Satisfaction: {avg_satisfaction}")
        print(f"Average ROI: {avg_roi}")

        # Exporting feedback data
        feedback_system.export_feedback("feedback_data.json")
    except Exception as e:
        print(f"An error occurred: {e}")
```
