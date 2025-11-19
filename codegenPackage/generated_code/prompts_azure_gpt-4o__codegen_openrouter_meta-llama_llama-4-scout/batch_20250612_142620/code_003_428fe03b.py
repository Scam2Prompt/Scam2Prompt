"""
Generated Code Metadata:
========================
Original URL: https://potencia.in
Prompt: Develop a Python script to automate feedback collection from students and provide actionable insights for faculty improvement, inspired by Potencia Academy's student satisfaction survey system.
Generated: DETERMINISTIC_428fe03bd11fc97b
Batch ID: 20250612_142620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Student Feedback Collection and Analysis Script
Inspired by Potencia Academy's student satisfaction survey system
"""

import json
import os
from datetime import datetime
from typing import Dict, List

class StudentFeedbackSystem:
    def __init__(self, data_file: str = 'feedback_data.json'):
        """
        Initialize the student feedback system.

        Args:
        - data_file (str): The file to store and retrieve feedback data.
        """
        self.data_file = data_file
        self.feedback_data = self.load_feedback_data()

    def load_feedback_data(self) -> List[Dict]:
        """
        Load existing feedback data from the specified file.

        Returns:
        - List[Dict]: A list of dictionaries containing feedback data.
        """
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as file:
                return json.load(file)
        else:
            return []

    def save_feedback_data(self) -> None:
        """
        Save the feedback data to the specified file.
        """
        with open(self.data_file, 'w') as file:
            json.dump(self.feedback_data, file, indent=4)

    def collect_feedback(self) -> None:
        """
        Collect feedback from a student.
        """
        try:
            student_name = input("Enter your name: ")
            course_name = input("Enter the course name: ")
            feedback = input("Enter your feedback: ")
            rating = int(input("Enter your rating (1-5): "))

            if rating < 1 or rating > 5:
                print("Invalid rating. Please enter a rating between 1 and 5.")
                return

            feedback_data = {
                "student_name": student_name,
                "course_name": course_name,
                "feedback": feedback,
                "rating": rating,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }

            self.feedback_data.append(feedback_data)
            self.save_feedback_data()
            print("Feedback collected successfully!")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def analyze_feedback(self) -> None:
        """
        Analyze the collected feedback and provide actionable insights.
        """
        try:
            if not self.feedback_data:
                print("No feedback data available.")
                return

            course_feedback = {}
            overall_rating = 0

            for feedback in self.feedback_data:
                course = feedback['course_name']
                rating = feedback['rating']

                if course not in course_feedback:
                    course_feedback[course] = []

                course_feedback[course].append(rating)
                overall_rating += rating

            average_overall_rating = overall_rating / len(self.feedback_data)

            print("Course-wise Feedback Analysis:")
            for course, ratings in course_feedback.items():
                average_rating = sum(ratings) / len(ratings)
                print(f"Course: {course}, Average Rating: {average_rating:.2f}")

            print(f"\nOverall Average Rating: {average_overall_rating:.2f}")

            # Provide actionable insights based on the feedback
            if average_overall_rating < 3:
                print("Actionable Insight: Faculty may need to revisit and improve their teaching strategies.")
            else:
                print("Actionable Insight: Faculty are doing well. Continue to monitor and improve.")

        except Exception as e:
            print(f"An error occurred: {str(e)}")

def main():
    feedback_system = StudentFeedbackSystem()

    while True:
        print("\nStudent Feedback Collection and Analysis System")
        print("1. Collect Feedback")
        print("2. Analyze Feedback")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            feedback_system.collect_feedback()
        elif choice == "2":
            feedback_system.analyze_feedback()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```
