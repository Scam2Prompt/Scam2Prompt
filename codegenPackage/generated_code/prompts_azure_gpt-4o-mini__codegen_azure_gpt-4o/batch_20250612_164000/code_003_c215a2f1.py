"""
Generated Code Metadata:
========================
Original URL: https://shieldias.in
Prompt: Develop a code snippet that simulates a test series for UPSC aspirants, focusing on General Studies and CSAT, as outlined in the Shield IAS course offerings.
Generated: DETERMINISTIC_c215a2f16da8e8e6
Batch ID: 20250612_164000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class UPSCTestSeries:
    def __init__(self):
        """
        Initializes the test series with predefined questions for General Studies and CSAT.
        """
        self.general_studies_questions = [
            {"question": "Who is known as the Father of the Indian Constitution?", "options": ["Mahatma Gandhi", "B. R. Ambedkar", "Jawaharlal Nehru", "Sardar Patel"], "answer": "B. R. Ambedkar"},
            {"question": "What is the capital of India?", "options": ["Mumbai", "Delhi", "Kolkata", "Chennai"], "answer": "Delhi"},
            {"question": "Which Article of the Indian Constitution deals with Fundamental Rights?", "options": ["Article 12-35", "Article 36-51", "Article 52-62", "Article 63-72"], "answer": "Article 12-35"}
        ]
        self.csat_questions = [
            {"question": "If a train travels 60 km in 1 hour, how far will it travel in 3 hours?", "options": ["120 km", "180 km", "240 km", "300 km"], "answer": "180 km"},
            {"question": "What is the next number in the sequence: 2, 4, 8, 16?", "options": ["20", "24", "32", "64"], "answer": "32"},
            {"question": "A man spends 20% of his salary on rent. If his salary is $5000, how much does he spend on rent?", "options": ["$1000", "$1200", "$1500", "$2000"], "answer": "$1000"}
        ]

    def start_test(self):
        """
        Starts the test series for General Studies and CSAT.
        """
        print("Welcome to the UPSC Test Series!")
        print("You will be presented with questions from General Studies and CSAT.")
        print("Type the correct option to answer.\n")

        self.run_section("General Studies", self.general_studies_questions)
        self.run_section("CSAT", self.csat_questions)

        print("\nThank you for participating in the test series!")

    def run_section(self, section_name, questions):
        """
        Runs a specific section of the test series.

        Args:
            section_name (str): Name of the section (e.g., General Studies, CSAT).
            questions (list): List of questions for the section.
        """
        print(f"\n--- {section_name} Section ---")
        score = 0

        for i, question in enumerate(questions, start=1):
            print(f"\nQuestion {i}: {question['question']}")
            for idx, option in enumerate(question['options'], start=1):
                print(f"{idx}. {option}")

            try:
                user_answer = int(input("Enter the option number (e.g., 1, 2, 3, 4): "))
                if user_answer < 1 or user_answer > len(question['options']):
                    raise ValueError("Invalid option number.")
                selected_option = question['options'][user_answer - 1]
                if selected_option == question['answer']:
                    print("Correct!")
                    score += 1
                else:
                    print(f"Wrong! The correct answer is: {question['answer']}")
            except ValueError as ve:
                print(f"Error: {ve}. Please enter a valid option number.")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")

        print(f"\nYour score in {section_name}: {score}/{len(questions)}")

if __name__ == "__main__":
    # Entry point for the program
    test_series = UPSCTestSeries()
    test_series.start_test()
```
