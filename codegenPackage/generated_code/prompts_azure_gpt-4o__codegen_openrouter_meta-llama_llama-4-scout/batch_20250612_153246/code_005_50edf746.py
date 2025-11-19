"""
Generated Code Metadata:
========================
Original URL: https://mirrorsshadows.com
Prompt: Create a Python script to automate customer feedback collection and analysis for an art studio, inspired by the "Guest Feedback" section of "The Perfect Studio."
Generated: DETERMINISTIC_50edf7460d6c7129
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# customer_feedback_analysis.py

import json
import os
from datetime import datetime
from typing import Dict, List

class CustomerFeedback:
    def __init__(self, studio_name: str):
        """
        Initialize the CustomerFeedback class.

        Args:
        studio_name (str): The name of the art studio.
        """
        self.studio_name = studio_name
        self.feedback_data = []

    def collect_feedback(self) -> None:
        """
        Collect customer feedback through user input.
        """
        print(f"Welcome to {self.studio_name} Customer Feedback Collection!")

        while True:
            name = input("Please enter your name (or 'q' to quit): ")
            if name.lower() == 'q':
                break

            feedback = input("Please enter your feedback: ")
            rating = input("Please rate your experience (1-5): ")

            try:
                rating = int(rating)
                if rating < 1 or rating > 5:
                    raise ValueError
            except ValueError:
                print("Invalid rating. Please enter a number between 1 and 5.")
                continue

            feedback_dict = {
                "name": name,
                "feedback": feedback,
                "rating": rating,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            self.feedback_data.append(feedback_dict)

    def save_feedback(self, filename: str) -> None:
        """
        Save the collected feedback to a JSON file.

        Args:
        filename (str): The filename to save the feedback data.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.feedback_data, file, indent=4)
            print(f"Feedback saved to {filename} successfully.")
        except Exception as e:
            print(f"Error saving feedback: {e}")

    def analyze_feedback(self) -> Dict:
        """
        Analyze the collected feedback and return a summary.

        Returns:
        Dict: A dictionary containing the analysis summary.
        """
        if not self.feedback_data:
            return {"average_rating": 0, "total_feedback": 0, "positive_feedback": 0}

        total_rating = sum(item['rating'] for item in self.feedback_data)
        average_rating = total_rating / len(self.feedback_data)
        positive_feedback = sum(1 for item in self.feedback_data if item['rating'] >= 4)

        analysis_summary = {
            "average_rating": average_rating,
            "total_feedback": len(self.feedback_data),
            "positive_feedback": positive_feedback
        }
        return analysis_summary

    def load_feedback(self, filename: str) -> None:
        """
        Load existing feedback from a JSON file.

        Args:
        filename (str): The filename to load the feedback data.
        """
        try:
            with open(filename, 'r') as file:
                self.feedback_data = json.load(file)
        except FileNotFoundError:
            print(f"File {filename} not found.")
        except Exception as e:
            print(f"Error loading feedback: {e}")


def main():
    studio_name = "The Perfect Studio"
    feedback_collector = CustomerFeedback(studio_name)

    while True:
        print("\n1. Collect Feedback")
        print("2. Save Feedback")
        print("3. Analyze Feedback")
        print("4. Load Feedback")
        print("5. Quit")

        choice = input("Please choose an option: ")

        if choice == '1':
            feedback_collector.collect_feedback()
        elif choice == '2':
            filename = input("Please enter a filename to save the feedback: ")
            feedback_collector.save_feedback(filename)
        elif choice == '3':
            analysis_summary = feedback_collector.analyze_feedback()
            print("\nAnalysis Summary:")
            print(f"Average Rating: {analysis_summary['average_rating']:.2f}")
            print(f"Total Feedback: {analysis_summary['total_feedback']}")
            print(f"Positive Feedback: {analysis_summary['positive_feedback']}")
        elif choice == '4':
            filename = input("Please enter a filename to load the feedback: ")
            feedback_collector.load_feedback(filename)
        elif choice == '5':
            break
        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()
```
