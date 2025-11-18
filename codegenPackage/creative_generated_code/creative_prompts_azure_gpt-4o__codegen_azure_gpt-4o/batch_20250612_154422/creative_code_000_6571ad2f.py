"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shieldias.in
Prompt: Write Python code to create a quiz application for UPSC IAS preparation, including features like "The Hindu Monthly Quiz" and current affairs questions as described on Shield IAS.
Generated: DETERMINISTIC_6571ad2f1d86ffd5
Batch ID: 20250612_154422
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


class QuizApplication:
    """
    A class to represent the Quiz Application for UPSC IAS preparation.
    Includes features like 'The Hindu Monthly Quiz' and Current Affairs questions.
    """

    def __init__(self):
        """
        Initializes the quiz application with a set of questions.
        """
        self.questions = []
        self.load_questions()

    def load_questions(self):
        """
        Loads questions from a JSON file into the application.
        This simulates fetching questions for 'The Hindu Monthly Quiz' and Current Affairs.
        """
        try:
            # Load questions from a JSON file (simulating an external data source)
            with open("questions.json", "r") as file:
                self.questions = json.load(file)
        except FileNotFoundError:
            print("Error: Questions file not found. Please provide a valid 'questions.json' file.")
        except json.JSONDecodeError:
            print("Error: Failed to decode questions. Ensure JSON format is valid.")
        except Exception as e:
            print(f"Unexpected error: {str(e)}")
        finally:
            if not self.questions:
                # Provide fallback questions if loading fails
                self.questions = [
                    {
                        "category": "Current Affairs",
                        "question": "Who is the current President of India?",
                        "options": ["Ram Nath Kovind", "Droupadi Murmu", "Narendra Modi", "Amit Shah"],
                        "answer": "Droupadi Murmu"
                    },
                    {
                        "category": "The Hindu Monthly Quiz",
                        "question": "What is the theme of The Hindu's editorial for January 2023?",
                        "options": ["Global Warming", "Economic Growth", "Political Stability", "Education Reforms"],
                        "answer": "Global Warming"
                    }
                ]

    def start_quiz(self):
        """
        Starts the quiz by presenting questions to the user and tracking their score.
        """
        print("\nWelcome to the UPSC IAS Quiz Application!")
        print("Categories: The Hindu Monthly Quiz | Current Affairs\n")

        score = 0
        random.shuffle(self.questions)  # Randomize the order of questions

        for index, question in enumerate(self.questions, start=1):
            print(f"Question {index}: {question['question']}")
            for i, option in enumerate(question['options'], start=1):
                print(f"{i}. {option}")

            try:
                user_answer = int(input("\nEnter the number corresponding to your answer: "))
                if question['options'][user_answer - 1] == question['answer']:
                    print("Correct!\n")
                    score += 1
                else:
                    print(f"Wrong! The correct answer was: {question['answer']}\n")
            except (ValueError, IndexError):
                print("Invalid input. Please enter a valid option number.\n")

        print(f"Your final score is: {score}/{len(self.questions)}")
        print("\nThank you for participating!")

    def add_question(self):
        """
        Allows the admin to add a new question to the quiz.
        """
        print("\n--- Add a New Question ---")
        category = input("Enter the category (e.g., Current Affairs, The Hindu Monthly Quiz): ").strip()
        question_text = input("Enter the question text: ").strip()
        options = []

        for i in range(4):
            option = input(f"Enter option {i + 1}: ").strip()
            options.append(option)

        answer = input("Enter the correct answer (must match one of the options): ").strip()

        if answer not in options:
            print("Error: Correct answer must match one of the provided options.")
            return

        new_question = {
            "category": category,
            "question": question_text,
            "options": options,
            "answer": answer
        }

        self.questions.append(new_question)
        self.save_questions()
        print("Question added successfully!\n")

    def save_questions(self):
        """
        Saves the current set of questions back to the JSON file.
        """
        try:
            with open("questions.json", "w") as file:
                json.dump(self.questions, file, indent=4)
        except Exception as e:
            print(f"Error: Unable to save questions. {str(e)}")

    def admin_menu(self):
        """
        Admin menu for managing quiz questions.
        """
        print("\n--- Admin Menu ---")
        print("1. Add a new question")
        print("2. Exit admin menu")

        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                self.add_question()
            elif choice == 2:
                print("Exiting admin menu...\n")
            else:
                print("Invalid choice. Please try again.\n")
        except ValueError:
            print("Invalid input. Please enter a number.\n")


if __name__ == "__main__":
    # Instantiate the QuizApplication
    app = QuizApplication()

    while True:
        print("\n--- UPSC IAS Quiz Application ---")
        print("1. Start Quiz")
        print("2. Admin Menu")
        print("3. Exit")

        try:
            user_choice = int(input("Enter your choice: "))
            if user_choice == 1:
                app.start_quiz()
            elif user_choice == 2:
                app.admin_menu()
            elif user_choice == 3:
                print("Exiting the application. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 3.\n")
        except ValueError:
            print("Invalid input. Please enter a number.\n")
```

### Notes:
1. This code assumes the existence of a `questions.json` file for storing quiz questions. If the file is not available, the application uses fallback questions.
2. Proper error handling is implemented for file operations, user input, and unexpected issues.
3. The `add_question` functionality enables admins to dynamically add new questions to the quiz.
