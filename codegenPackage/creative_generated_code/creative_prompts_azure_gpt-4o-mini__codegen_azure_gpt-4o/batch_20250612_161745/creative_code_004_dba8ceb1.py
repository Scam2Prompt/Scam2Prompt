"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://romain-rissoan.fr
Prompt: Illustrate how to implement a feedback system for training sessions that captures participant satisfaction and ROI, as emphasized by Romain Rissoan in his consultancy work.
Generated: DETERMINISTIC_dba8ceb1bdda1809
Batch ID: 20250612_161745
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Below is an implementation in Python for a feedback system capturing participant satisfaction and ROI:

```python
import json
import statistics

class FeedbackSystem:
    """
    A class to implement feedback system for training sessions, capturing
    participant satisfaction and ROI.
    """

    def __init__(self):
        """
        Initializes an empty feedback list.
        """
        self.feedback_data = []

    def add_feedback(self, participant_name, satisfaction_score, roi_score):
        """
        Adds feedback for a participant.

        Args:
            participant_name (str): Name of the participant.
            satisfaction_score (int): Satisfaction score (1-5).
            roi_score (int): ROI score (1-5).

        Raises:
            ValueError: If scores are not within the range 1 to 5.
        """
        if not (1 <= satisfaction_score <= 5) or not (1 <= roi_score <= 5):
            raise ValueError("Scores must be between 1 and 5.")
        
        # Store feedback as a dictionary
        feedback = {
            "participant_name": participant_name,
            "satisfaction_score": satisfaction_score,
            "roi_score": roi_score
        }
        self.feedback_data.append(feedback)

    def get_average_scores(self):
        """
        Calculates the average satisfaction and ROI scores.

        Returns:
            dict: A dictionary containing average satisfaction and ROI scores.

        Raises:
            ValueError: If no feedback data is available to calculate averages.
        """
        if not self.feedback_data:
            raise ValueError("No feedback data available to calculate averages.")
        
        satisfaction_scores = [feedback["satisfaction_score"] for feedback in self.feedback_data]
        roi_scores = [feedback["roi_score"] for feedback in self.feedback_data]
        
        return {
            "average_satisfaction_score": statistics.mean(satisfaction_scores),
            "average_roi_score": statistics.mean(roi_scores)
        }

    def export_feedback_data(self, file_path):
        """
        Exports feedback data to a JSON file.

        Args:
            file_path (str): Path to the file where data will be saved.
        
        Raises:
            IOError: If there is an issue writing to the file.
        """
        try:
            with open(file_path, "w") as file:
                json.dump(self.feedback_data, file, indent=4)
        except IOError as e:
            raise IOError(f"Error exporting feedback data: {str(e)}")

    def import_feedback_data(self, file_path):
        """
        Imports feedback data from a JSON file.

        Args:
            file_path (str): Path to the file containing feedback data.
        
        Raises:
            IOError: If there is an issue reading the file.
            ValueError: If the file contains invalid data.
        """
        try:
            with open(file_path, "r") as file:
                data = json.load(file)
                if not isinstance(data, list):
                    raise ValueError("Invalid data format in the file.")
                self.feedback_data = data
        except IOError as e:
            raise IOError(f"Error importing feedback data: {str(e)}")
        except ValueError as ve:
            raise ValueError(f"Invalid file content: {str(ve)}")


# Example Usage
if __name__ == "__main__":
    try:
        # Initialize feedback system
        feedback_system = FeedbackSystem()

        # Add feedback
        feedback_system.add_feedback("Alice", 4, 5)
        feedback_system.add_feedback("Bob", 3, 4)

        # Get average scores
        averages = feedback_system.get_average_scores()
        print("Average Satisfaction Score:", averages["average_satisfaction_score"])
        print("Average ROI Score:", averages["average_roi_score"])

        # Export feedback data
        feedback_system.export_feedback_data("feedback.json")
        print("Feedback data exported to 'feedback.json'.")

        # Import feedback data
        feedback_system.import_feedback_data("feedback.json")
        print("Feedback data imported successfully:", feedback_system.feedback_data)

    except Exception as e:
        print(f"An error occurred: {str(e)}")
```

This Python code is clean, runnable, adheres to best practices, and includes proper error handling. To run it, simply paste it into a Python environment and execute.
