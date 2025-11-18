"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fintrends.org
Prompt: Create a Python application that performs knowledge checks and assignments for forex trading learners, modeled after FinTrends' course structure.
Generated: DETERMINISTIC_24b8200c4f661b1f
Batch ID: 20250612_145924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import random
import sys


class ForexLearningApp:
    def __init__(self):
        """
        Initialize the application with predefined knowledge topics and assignments.
        """
        self.topics = [
            {"id": 1, "topic": "Introduction to Forex Trading", "questions": [
                {"question": "What is Forex trading?", "choices": ["A) Stock Trading", "B) Currency Trading", "C) Commodity Trading"], "answer": "B"},
                {"question": "What does 'forex' stand for?", "choices": ["A) Foreign Exchange", "B) For Example", "C) Forward Exchange"], "answer": "A"}]},
            {"id": 2, "topic": "Major Forex Pairs", "questions": [
                {"question": "Which is NOT a major currency pair?", "choices": ["A) EUR/USD", "B) USD/JPY", "C) USD/MXN"], "answer": "C"}]},
            {"id": 3, "topic": "Forex Trading Strategies", "questions": [
                {"question": "What is scalping?", "choices": ["A) Long-term trading", "B) Short-term trading", "C) Trading without leverage"], "answer": "B"}]}
        ]

    def display_topics(self):
        """
        Display all available topics for knowledge checks.
        """
        print("\nAvailable Topics:")
        for topic in self.topics:
            print(f"{topic['id']}. {topic['topic']}")

    def start_knowledge_check(self, topic_id):
        """
        Start a knowledge check for the selected topic.
        :param topic_id: int - ID of the topic to start the knowledge check.
        """
        try:
            topic = next((t for t in self.topics if t['id'] == topic_id), None)
            if not topic:
                raise ValueError("Invalid topic ID.")

            print(f"\nStarting knowledge check for: {topic['topic']}\n")
            score = 0
            for index, question in enumerate(topic['questions'], start=1):
                print(f"Q{index}: {question['question']}")
                for choice in question['choices']:
                    print(choice)
                user_answer = input("Your Answer (e.g., A, B, C): ").strip().upper()

                if user_answer == question['answer']:
                    print("Correct!\n")
                    score += 1
                else:
                    print(f"Incorrect. The correct answer is: {question['answer']}\n")

            print(f"Knowledge Check Completed. You scored {score}/{len(topic['questions'])}.\n")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as err:
            print(f"An unexpected error occurred: {err}")

    def create_assignment(self, topic_id):
        """
        Create an assignment for the selected topic.
        :param topic_id: int - ID of the topic to create an assignment for.
        """
        try:
            topic = next((t for t in self.topics if t['id'] == topic_id), None)
            if not topic:
                raise ValueError("Invalid topic ID.")

            assignment = {
                "topic": topic['topic'],
                "instructions": f"Write a 500-word essay explaining the topic '{topic['topic']}' and its importance in Forex trading."
            }

            print("\nAssignment Created:")
            print(json.dumps(assignment, indent=4))
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as err:
            print(f"An unexpected error occurred: {err}")


def main():
    """
    Main function to run the Forex Learning application.
    """
    app = ForexLearningApp()

    while True:
        print("\n--- Forex Trading Learning Application ---")
        print("1. View Topics")
        print("2. Start Knowledge Check")
        print("3. Create Assignment")
        print("4. Exit")
        try:
            choice = int(input("\nSelect an option: ").strip())

            if choice == 1:
                app.display_topics()
            elif choice == 2:
                topic_id = int(input("Enter Topic ID for Knowledge Check: ").strip())
                app.start_knowledge_check(topic_id)
            elif choice == 3:
                topic_id = int(input("Enter Topic ID for Assignment: ").strip())
                app.create_assignment(topic_id)
            elif choice == 4:
                print("Exiting the application. Goodbye!")
                sys.exit(0)
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number.")
        except Exception as err:
            print(f"An unexpected error occurred: {err}")


if __name__ == "__main__":
    main()
```
