"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://potencia.in
Prompt: Write Python code to simulate a periodic test system for JEE/NEET preparation, incorporating difficulty levels and performance tracking, as described in Potencia Academy's approach.
Generated: DETERMINISTIC_35a65c5734d3f36f
Batch ID: 20250612_142620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import random
import json

class PeriodicTestSystem:
    def __init__(self):
        """
        Initializes the test system with predefined difficulty levels and an empty performance tracker.
        """
        self.difficulty_levels = ["Easy", "Medium", "Hard"]
        self.performance_tracker = {}  # Stores user performance data in a dictionary

    def generate_question(self, difficulty):
        """
        Generates a random question based on the difficulty level.
        For simplicity, we simulate questions with random numbers.

        Args:
            difficulty (str): The difficulty level of the question (Easy, Medium, Hard).

        Returns:
            dict: A dictionary containing the question and its correct answer.
        """
        # Simulate question generation logic
        if difficulty == "Easy":
            question = f"What is {random.randint(1, 10)} + {random.randint(1, 10)}?"
            answer = eval(question.split(" ")[2] + "+" + question.split(" ")[4])
        elif difficulty == "Medium":
            question = f"What is {random.randint(10, 50)} * {random.randint(1, 10)}?"
            answer = eval(question.split(" ")[2] + "*" + question.split(" ")[4])
        elif difficulty == "Hard":
            question = f"What is {random.randint(50, 100)} / {random.randint(2, 10)} (round to nearest integer)?"
            answer = round(eval(question.split(" ")[2] + "/" + question.split(" ")[4]))
        else:
            raise ValueError(f"Invalid difficulty level: {difficulty}")
        
        return {"question": question, "answer": answer}

    def conduct_test(self, participant_name):
        """
        Simulates a test for a participant. Generates questions based on difficulty levels
        and tracks performance.

        Args:
            participant_name (str): Name of the participant.
        """
        if participant_name not in self.performance_tracker:
            self.performance_tracker[participant_name] = {"Easy": 0, "Medium": 0, "Hard": 0}

        print(f"Conducting test for {participant_name}...")
        for difficulty in self.difficulty_levels:
            print(f"\nDifficulty Level: {difficulty}")
            question_data = self.generate_question(difficulty)
            print("Question:", question_data["question"])
            
            while True:
                try:
                    user_answer = int(input("Your answer: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid integer.")
            
            if user_answer == question_data["answer"]:
                print("Correct!")
                self.performance_tracker[participant_name][difficulty] += 1
            else:
                print(f"Incorrect! The correct answer was {question_data['answer']}.")

    def display_performance(self):
        """
        Displays the performance of all participants stored in the tracker.
        """
        print("\nPerformance Report:")
        for participant, scores in self.performance_tracker.items():
            print(f"\nParticipant: {participant}")
            for difficulty, score in scores.items():
                print(f"  {difficulty}: {score} correct answers")

    def save_to_file(self, filename="performance_data.json"):
        """
        Saves the performance tracker data to a JSON file.

        Args:
            filename (str): Name of the file where data will be saved.
        """
        try:
            with open(filename, "w") as file:
                json.dump(self.performance_tracker, file, indent=4)
            print(f"\nPerformance data saved to {filename}")
        except Exception as e:
            print(f"Error saving data to file: {e}")

def main():
    """
    Main function to run the test system.
    """
    test_system = PeriodicTestSystem()
    while True:
        print("\n--- Periodic Test System ---")
        print("1. Conduct Test")
        print("2. Display Performance")
        print("3. Save Performance to File")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid choice. Please enter a number from 1 to 4.")
            continue

        if choice == 1:
            participant_name = input("Enter participant's name: ").strip()
            test_system.conduct_test(participant_name)
        elif choice == 2:
            test_system.display_performance()
        elif choice == 3:
            test_system.save_to_file()
        elif choice == 4:
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()
```
