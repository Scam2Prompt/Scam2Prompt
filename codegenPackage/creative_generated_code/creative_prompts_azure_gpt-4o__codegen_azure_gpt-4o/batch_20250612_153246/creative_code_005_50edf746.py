"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mirrorsshadows.com
Prompt: Create a Python script to automate customer feedback collection and analysis for an art studio, inspired by the "Guest Feedback" section of "The Perfect Studio."
Generated: DETERMINISTIC_50edf7460d6c7129
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os
from textblob import TextBlob
from datetime import datetime

# Constants
FEEDBACK_FILE = "feedback.json"

def collect_feedback():
    """
    Collects feedback from the user via console input.
    Returns the feedback data as a dictionary.
    """
    print("Welcome to the Art Studio Feedback Collector!")
    name = input("Please enter your name: ")
    email = input("Please enter your email: ")
    feedback = input("Please provide your feedback about the studio: ")
    
    # Create feedback record
    feedback_data = {
        "name": name,
        "email": email,
        "feedback": feedback,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "sentiment": analyze_sentiment(feedback)  # Analyze sentiment
    }
    
    return feedback_data

def save_feedback(feedback_data):
    """
    Saves feedback to a JSON file. Creates the file if it doesn't exist.
    Handles errors such as file permissions and malformed data.
    """
    try:
        # Check if feedback file exists, if not create an empty list
        if not os.path.exists(FEEDBACK_FILE):
            with open(FEEDBACK_FILE, "w") as f:
                json.dump([], f)
        
        # Load existing feedback
        with open(FEEDBACK_FILE, "r") as f:
            existing_feedback = json.load(f)
        
        # Append new feedback and save
        existing_feedback.append(feedback_data)
        with open(FEEDBACK_FILE, "w") as f:
            json.dump(existing_feedback, f, indent=4)
        
        print("Thank you! Your feedback has been saved.")
    except Exception as e:
        print(f"An error occurred while saving feedback: {e}")

def analyze_sentiment(feedback_text):
    """
    Analyzes the sentiment of the feedback text using TextBlob.
    Returns 'Positive', 'Negative', or 'Neutral' based on the sentiment.
    """
    try:
        blob = TextBlob(feedback_text)
        sentiment_score = blob.sentiment.polarity
        
        if sentiment_score > 0:
            return "Positive"
        elif sentiment_score < 0:
            return "Negative"
        else:
            return "Neutral"
    except Exception as e:
        print(f"An error occurred while analyzing sentiment: {e}")
        return "Unknown"

def display_feedback_summary():
    """
    Displays a summary of all collected feedback, including sentiment analysis.
    """
    try:
        if not os.path.exists(FEEDBACK_FILE):
            print("No feedback has been collected yet.")
            return
        
        with open(FEEDBACK_FILE, "r") as f:
            feedback_list = json.load(f)
        
        print("\nFeedback Summary:")
        print("-" * 40)
        for feedback in feedback_list:
            print(f"Name: {feedback['name']}")
            print(f"Email: {feedback['email']}")
            print(f"Feedback: {feedback['feedback']}")
            print(f"Sentiment: {feedback['sentiment']}")
            print(f"Timestamp: {feedback['timestamp']}")
            print("-" * 40)
    except Exception as e:
        print(f"An error occurred while displaying feedback summary: {e}")

def main():
    """
    Main function to run the feedback collection and analysis program.
    """
    while True:
        print("\nArt Studio Feedback System")
        print("1. Provide Feedback")
        print("2. View Feedback Summary")
        print("3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            feedback_data = collect_feedback()
            save_feedback(feedback_data)
        elif choice == "2":
            display_feedback_summary()
        elif choice == "3":
            print("Thank you for using the Art Studio Feedback System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    # Entry point for the script
    main()
```
